import logging
from spaceone.core.service import *
from cloudforet.console_api_v2.error.resource import *
from cloudforet.console_api_v2.manager.resource_manager import ResourceManager
from cloudforet.console_api_v2.manager.resource_manager.inventory_manager import InventoryManager
from cloudforet.console_api_v2.manager.resource_manager.cost_analysis_manager import CostAnalysisManager

_LOGGER = logging.getLogger(__name__)


_RESOURCE_MANAGER_MAP = {
    'inventory': InventoryManager,
    'cost_analysis': CostAnalysisManager
}


@event_handler
class ResourceService(BaseService):

    @transaction
    @check_required(['service', 'resource'])
    def list_fields(self, params):
        """ list fields of API resource

        Args:
            params (dict): {
                'service': 'str',
                'resource': 'str',
                'resource': 'str',
                'options': 'dict',
                'limit': 'int',
            }

        Returns:
            fields_info (list)
        """

        service = params['service']
        resource = params['resource']
        options = params.get('options', {})
        limit = params.get('limit')

        resource_mgr: ResourceManager = self._get_manager_from_service_name(service)
        return resource_mgr.list_fields(resource, options, limit)

    @transaction
    @check_required(['service', 'resource', 'field'])
    def list_field_values(self, params):
        """ list values of API resource field

        Args:
            params (dict): {
                'service': 'str',
                'resource': 'str',
                'field': 'str',
                'options': 'dict',
                'search': 'str',
                'limit': 'int'
            }

        Returns:
            values_info (list)
        """

        return {
            'results': [],
            'more': False
        }

    def _get_manager_from_service_name(self, service):
        manager = _RESOURCE_MANAGER_MAP.get(service)
        if manager is None:
            raise ERROR_UNSUPPORTED_SERVICE(services=list(_RESOURCE_MANAGER_MAP.keys()))

        return self.locator.get_manager(manager)
