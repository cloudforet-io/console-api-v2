import logging
from fastapi import Request, Depends, Body
from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from spaceone.core.fastapi.api import BaseAPI, exception_handler
from cloudforet.console_api_v2.service.common.proxy_service import ProxyService
from cloudforet.console_api_v2.model.inventory.change_history import *
_LOGGER = logging.getLogger(__name__)
_AUTH_SCHEME = HTTPBearer()

router = InferringRouter()


@cbv(router)
class ChangeHistory(BaseAPI):
    token: HTTPAuthorizationCredentials = Depends(_AUTH_SCHEME)
    service = 'console-api'

    @router.post('/list', description=ChangeHistoryInfo.List.description())
    @exception_handler
    async def list(self, request: Request, body: ChangeHistoryInfo.List):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'inventory.ChangeHistory.list'
            return proxy_service.dispatch_api(params)

    @router.post('/stat')
    @exception_handler
    async def stat(self, request: Request, body: ChangeHistoryInfo.Stat):
        """
        Create an item with all the information

        ---
        ### - name (required)
        - each item must have name
        ### - price (required)
        ### - description (required)
        - a long description

       """
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'inventory.ChangeHistory.stat'
            return proxy_service.dispatch_api(params)
