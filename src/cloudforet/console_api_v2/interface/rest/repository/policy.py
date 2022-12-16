import logging
from fastapi import Request, Depends, Body
from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from spaceone.core.fastapi.api import BaseAPI, exception_handler
from cloudforet.console_api_v2.service.common.proxy_service import ProxyService

from cloudforet.console_api_v2.model.repository.policy import PolicyInfo
_LOGGER = logging.getLogger(__name__)
_AUTH_SCHEME = HTTPBearer()

router = InferringRouter()


@cbv(router)
class Policy(BaseAPI):
    token: HTTPAuthorizationCredentials = Depends(_AUTH_SCHEME)
    service = 'console-api'

    @router.post('/create')
    @exception_handler
    async def create(self, request: Request, body: PolicyInfo.Create):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'repository.Policy.create'
            return proxy_service.dispatch_api(params)

    @router.post('/update')
    @exception_handler
    async def update(self, request: Request, body: PolicyInfo.Update):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'repository.Policy.update'
            return proxy_service.dispatch_api(params)

    @router.post('/delete')
    @exception_handler
    async def delete(self, request: Request, body: PolicyInfo.Delete):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'repository.Policy.delete'
            return proxy_service.dispatch_api(params)

    @router.post('/get')
    @exception_handler
    async def get(self, request: Request, body: PolicyInfo.Get):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'repository.Policy.get'
            return proxy_service.dispatch_api(params)

    @router.post('/list')
    @exception_handler
    async def list(self, request: Request, body: PolicyInfo.List):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'repository.Policy.list'
            return proxy_service.dispatch_api(params)

    @router.post('/stat')
    @exception_handler
    async def stat(self, request: Request, body: PolicyInfo.Stat):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'repository.Policy.stat'
            return proxy_service.dispatch_api(params)

