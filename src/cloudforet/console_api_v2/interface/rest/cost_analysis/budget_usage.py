import logging
from fastapi import Request, Depends, Body
from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from spaceone.core.fastapi.api import BaseAPI, exception_handler
from cloudforet.console_api_v2.service.common.proxy_service import ProxyService

_LOGGER = logging.getLogger(__name__)
_AUTH_SCHEME = HTTPBearer()

router = InferringRouter()


@cbv(router)
class BudgetUsage(BaseAPI):
    token: HTTPAuthorizationCredentials = Depends(_AUTH_SCHEME)
    service = 'console-api'

    @router.post('/list')
    @exception_handler
    async def list(self, request: Request, body: dict = Body(...)):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'cost_analysis.BudgetUsage.list'
            return proxy_service.dispatch_api(params)

    @router.post('/analyze')
    @exception_handler
    async def analyze(self, request: Request, body: dict = Body(...)):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'cost_analysis.BudgetUsage.analyze'
            return proxy_service.dispatch_api(params)

    @router.post('/stat')
    @exception_handler
    async def stat(self, request: Request, body: dict = Body(...)):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'cost_analysis.BudgetUsage.stat'
            return proxy_service.dispatch_api(params)

