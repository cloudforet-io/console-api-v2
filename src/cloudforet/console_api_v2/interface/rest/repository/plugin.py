import logging
from fastapi import Request, Depends
from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from spaceone.core.fastapi.api import BaseAPI, exception_handler
from cloudforet.console_api_v2.service.common.proxy_service import ProxyService

from cloudforet.console_api_v2.model.repository.plugin import PluginInfo
_LOGGER = logging.getLogger(__name__)
_AUTH_SCHEME = HTTPBearer()

router = InferringRouter()


@cbv(router)
class Plugin(BaseAPI):
    token: HTTPAuthorizationCredentials = Depends(_AUTH_SCHEME)
    service = 'console-api'

    @router.post('/register')
    @exception_handler
    async def register(self, request: Request, body: PluginInfo.Register):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'repository.Plugin.register'
            return proxy_service.dispatch_api(params)

    @router.post('/update')
    @exception_handler
    async def update(self, request: Request, body: PluginInfo.Update):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'repository.Plugin.update'
            return proxy_service.dispatch_api(params)

    @router.post('/enable')
    @exception_handler
    async def enable(self, request: Request, body: PluginInfo.Enable):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'repository.Plugin.enable'
            return proxy_service.dispatch_api(params)

    @router.post('/disable')
    @exception_handler
    async def disable(self, request: Request):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'repository.Plugin.disable'
            return proxy_service.dispatch_api(params)

    @router.post('/deregister')
    @exception_handler
    async def deregister(self, request: Request, body: PluginInfo.Deregister):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'repository.Plugin.deregister'
            return proxy_service.dispatch_api(params)

    @router.post('/get-versions')
    @exception_handler
    async def get_versions(self, request: Request, body: PluginInfo.GetVersions):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'repository.Plugin.get_versions'
            return proxy_service.dispatch_api(params)

    @router.post('/get')
    @exception_handler
    async def get(self, request: Request, body: PluginInfo.Get):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'repository.Plugin.get'
            return proxy_service.dispatch_api(params)

    @router.post('/list')
    @exception_handler
    async def list(self, request: Request, body: PluginInfo.List):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'repository.Plugin.list'
            return proxy_service.dispatch_api(params)

    @router.post('/stat')
    @exception_handler
    async def stat(self, request: Request, body: PluginInfo.Stat):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'repository.Plugin.stat'
            return proxy_service.dispatch_api(params)

