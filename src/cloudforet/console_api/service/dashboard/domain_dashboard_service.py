import logging
from spaceone.core.service import *
from cloudforet.console_api.manager.cloudforet_manager import CloudforetManager

_LOGGER = logging.getLogger(__name__)


@authentication_handler
@event_handler
class DomainDashboardService(BaseService):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cf_mgr: CloudforetManager = self.locator.get_manager(CloudforetManager)

    @transaction
    @check_required(['name'])
    def create(self, params):
        """Create domain dashboard
        Args:
            params (dict): {
            }
        Returns:
            domain_dashboard_info(dict)
        """

        return self.cf_mgr.dispatch_api('identity.User.list', {})
