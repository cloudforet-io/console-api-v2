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
class DataSource(BaseAPI):
    token: HTTPAuthorizationCredentials = Depends(_AUTH_SCHEME)
    service = 'console-api'
    
    @router.post('/register')
    @exception_handler
    async def register(self, request: Request, body: dict = Body(...)):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'cost_analysis.DataSource.register'
            return proxy_service.dispatch_api(params)

    @router.post('/update')
    @exception_handler
    async def update(self, request: Request):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'cost_analysis.DataSource.update'
            return proxy_service.dispatch_api(params)

    @router.post('/update-plugin')
    @exception_handler
    async def update_plugin(self, request: Request, body: dict = Body(...)):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'cost_analysis.DataSource.update_plugin'
            return proxy_service.dispatch_api(params)

    @router.post('/verify-plugin')
    @exception_handler
    async def verify_plugin(self, request: Request, body: dict = Body(...)):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'cost_analysis.DataSource.verify_plugin'
            return proxy_service.dispatch_api(params)

    @router.post('/enable')
    @exception_handler
    async def enable(self, request: Request, body: dict = Body(...)):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'cost_analysis.DataSource.enable'
            return proxy_service.dispatch_api(params)

    @router.post('/disable')
    @exception_handler
    async def disable(self, request: Request, body: dict = Body(...)):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'cost_analysis.DataSource.disable'
            return proxy_service.dispatch_api(params)

    @router.post('/deregister')
    @exception_handler
    async def deregister(self, request: Request, body: dict = Body(...)):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'cost_analysis.DataSource.deregister'
            return proxy_service.dispatch_api(params)

    @router.post('/sync')
    @exception_handler
    async def sync(self, request: Request, body: dict = Body(...)):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'cost_analysis.DataSource.sync'
            return proxy_service.dispatch_api(params)

    @router.post('/get')
    @exception_handler
    async def get(self, request: Request, body: dict = Body(...)):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'cost_analysis.DataSource.get'
            return proxy_service.dispatch_api(params)

    @router.post('/list')
    @exception_handler
    async def list(self, request: Request, body: dict = Body(...)):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'cost_analysis.DataSource.list'
            return proxy_service.dispatch_api(params)

    @router.post('/stat')
    @exception_handler
    async def stat(self, request: Request, body: dict = Body(...)):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'cost_analysis.DataSource.stat'
            return proxy_service.dispatch_api(params)

