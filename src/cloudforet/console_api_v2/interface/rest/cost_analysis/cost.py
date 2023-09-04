import logging
from fastapi import Request, Depends, Body
from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from spaceone.core.fastapi.api import BaseAPI, exception_handler
from cloudforet.console_api_v2.service.common.proxy_service import ProxyService
from cloudforet.console_api_v2.model.cost_analysis.cost import *

_LOGGER = logging.getLogger(__name__)
_AUTH_SCHEME = HTTPBearer()

router = InferringRouter()


@cbv(router)
class Cost(BaseAPI):
    token: HTTPAuthorizationCredentials = Depends(_AUTH_SCHEME)
    service = 'console-api'
    
    @router.post('/create', openapi_extra=CreateCostRequest.meta(), response_model=CostInfo)
    @exception_handler
    async def create(self, request: Request):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'cost_analysis.Cost.create'
            return proxy_service.dispatch_api(params)

    @router.post('/delete', openapi_extra=CostQuery.meta(), response_model=CostInfo)
    @exception_handler
    async def delete(self, request: Request):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'cost_analysis.Cost.delete'
            return proxy_service.dispatch_api(params)

    @router.post('/get', openapi_extra=GetCostRequest.meta(), response_model=CostInfo)
    @exception_handler
    async def get(self, request: Request):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'cost_analysis.Cost.get'
            return proxy_service.dispatch_api(params)

    @router.post('/list', openapi_extra=CostQuery.meta(), response_model=CostsInfo)
    @exception_handler
    async def list(self, request: Request):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'cost_analysis.Cost.list'
            return proxy_service.dispatch_api(params)

    @router.post('/analyze', openapi_extra=CostAnalyzeQuery.meta(), response_model=CostAnalyzeInfo)
    @exception_handler
    async def analyze(self, request: Request):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'cost_analysis.Cost.analyze'
            return proxy_service.dispatch_api(params)

    @router.post('/stat', openapi_extra=CostStatQuery.meta())
    @exception_handler
    async def stat(self, request: Request):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'cost_analysis.Cost.stat'
            return proxy_service.dispatch_api(params)

