import logging

from cloudforet.console_api_v2.error.resource import *
from cloudforet.console_api_v2.manager.resource_manager import ResourceManager

_LOGGER = logging.getLogger(__name__)

_FIELDS_MAP = {
    'Cost': [
        {'key': 'product', 'name': 'Product'},
        {'key': 'category', 'name': 'Category'},
        {'key': 'usage_type', 'name': 'Type'},
        {'key': 'account', 'name': 'Account'},
        {'key': 'tags', 'name': 'Tags', 'data_type': 'object', 'sortable': False},
        {'key': 'additional_info', 'name': 'Additional Info', 'data_type': 'object', 'sortable': False},
    ]
}


class CostAnalysisManager(ResourceManager):

    def list_fields(self, resource: str, options: dict, limit: int) -> dict:
        self._check_resource(resource)
        return self.make_response(_FIELDS_MAP[resource], limit)

    def list_field_values(self, resource: str, field: str, options: dict, search: str, limit: int) -> dict:
        return self.make_response([], limit)

    @staticmethod
    def _check_resource(resource: str):
        if resource not in _FIELDS_MAP:
            raise ERROR_UNSUPPORTED_RESOURCE(service='inventory', resource=resource)