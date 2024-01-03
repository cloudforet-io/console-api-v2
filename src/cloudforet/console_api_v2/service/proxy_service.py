import functools
import logging
from functools import wraps

from spaceone.core.service import *
from cloudforet.console_api_v2.manager.cloudforet_manager import CloudforetManager

_LOGGER = logging.getLogger(__name__)


@event_handler
class ProxyService(BaseService):
    resource = "Proxy"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cf_mgr: CloudforetManager = self.locator.get_manager(CloudforetManager)

    @transaction()
    @check_required(['grpc_method'])
    def dispatch_api(self, params):
        grpc_method = params['grpc_method']
        del params['grpc_method']
        return self.cf_mgr.dispatch_api(grpc_method, params)
