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
class Collector(BaseAPI):
    token: HTTPAuthorizationCredentials = Depends(_AUTH_SCHEME)
    service = 'console-api'

    @router.post('/create')
    @exception_handler
    async def create(self, request: Request, body: dict = Body(...)):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'inventory.Collector.create'
            return proxy_service.dispatch_api(params)

    @router.post('/update')
    @exception_handler
    async def update(self, request: Request):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'inventory.Collector.update'
            return proxy_service.dispatch_api(params)

    @router.post('/update-plugin')
    @exception_handler
    async def update_plugin(self, request: Request):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'inventory.Collector.update_plugin'
            return proxy_service.dispatch_api(params)

    @router.post('/verify-plugin')
    @exception_handler
    async def verify_plugin(self, request: Request):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'inventory.Collector.verify_plugin'
            return proxy_service.dispatch_api(params)

    @router.post('/get')
    @exception_handler
    async def get(self, request: Request, body: dict = Body(...)):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'inventory.Collector.get'
            return proxy_service.dispatch_api(params)

    @router.post('/add-schedule')
    @exception_handler
    async def add_schedule(self, request: Request, body: dict = Body(...)):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'inventory.Collector.add_schedule'
            return proxy_service.dispatch_api(params)

    @router.post('/update-schedule')
    @exception_handler
    async def update_schedule(self, request: Request, body: dict = Body(...)):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'inventory.Collector.update_schedule'
            return proxy_service.dispatch_api(params)

    @router.post('/delete-schedule')
    @exception_handler
    async def delete_schedule(self, request: Request, body: dict = Body(...)):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'inventory.Collector.delete_schedule'
            return proxy_service.dispatch_api(params)

    @router.post('/list-schedules')
    @exception_handler
    async def list_schedules(self, request: Request, body: dict = Body(...)):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'inventory.Collector.list_schedules'
            return proxy_service.dispatch_api(params)

    @router.post('/get-schedule')
    @exception_handler
    async def get_schedule(self, request: Request, body: dict = Body(...)):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'inventory.Collector.get_schedule'
            return proxy_service.dispatch_api(params)

    @router.post('/collect')
    @exception_handler
    async def list(self, request: Request, body: dict = Body(...)):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'inventory.Collector.list'
            return proxy_service.dispatch_api(params)

    @router.post('/stat')
    @exception_handler
    async def stat(self, request: Request, body: dict = Body(...)):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'inventory.Collector.stat'
            return proxy_service.dispatch_api(params)
