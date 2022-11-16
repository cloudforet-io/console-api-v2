import logging
from fastapi import Request, Depends
from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from spaceone.core.fastapi.api import BaseAPI, exception_handler
from cloudforet.console_api_v2.model.dashboard.domain_dashboard import *
from cloudforet.console_api_v2.service.common.proxy_service import ProxyService

_LOGGER = logging.getLogger(__name__)
_AUTH_SCHEME = HTTPBearer()

router = InferringRouter()


@cbv(router)
class DomainDashboard(BaseAPI):

    token: HTTPAuthorizationCredentials = Depends(_AUTH_SCHEME)
    service = 'console-api'

    @router.post(
        '/create',
        description=DomainDashboardInfo.Create.description(),
        responses=DomainDashboardInfo.Create.response()
    )
    @exception_handler
    async def create(self, request: Request, body: DomainDashboardInfo.Create):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'dashboard.DomainDashboard.create'
            return proxy_service.dispatch_api(params)

    @router.post(
        '/update',
        description=DomainDashboardInfo.Update.description(),
        responses=DomainDashboardInfo.Update.response(),
    )
    @exception_handler
    async def update(self, request: Request, body: DomainDashboardInfo.Update):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'dashboard.DomainDashboard.update'
            return proxy_service.dispatch_api(params)

    @router.post(
        '/delete',
        description=DomainDashboardInfo.Delete.description()
    )
    async def delete(self, request: Request, body: DomainDashboardInfo.Delete):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'dashboard.DomainDashboard.delete'
            return proxy_service.dispatch_api(params)

    @router.post(
        '/get',
        description=DomainDashboardInfo.Get.description(),
        responses=DomainDashboardInfo.Get.response()
    )
    async def get(self, request: Request, body: DomainDashboardInfo.Get):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'dashboard.DomainDashboard.get'
            return proxy_service.dispatch_api(params)

    @router.post(
        '/delete_version',
    )
    async def delete_version(self, request: Request, body: DomainDashboardVersionInfo.DeleteVersion):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'dashboard.DomainDashboard.delete_version'
            return proxy_service.dispatch_api(params)

    @router.post(
        '/revert_version',
        description=DomainDashboardVersionInfo.RevertVersion.description(),
        responses=DomainDashboardVersionInfo.RevertVersion.response()
    )
    async def revert_version(self, request: Request, body: DomainDashboardVersionInfo.RevertVersion):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'dashboard.DomainDashboard.revert_version'
            return proxy_service.dispatch_api(params)

    @router.post(
        '/get_version',
        description=DomainDashboardVersionInfo.GetVersion.description(),
        responses=DomainDashboardVersionInfo.GetVersion.response()
    )
    async def get_version(self, request: Request, body: DomainDashboardVersionInfo.GetVersion):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'dashboard.DomainDashboard.get_version'
            return proxy_service.dispatch_api(params)

    @router.post(
        '/list_versions',
        description=DomainDashboardVersionInfo.ListVersions.description(),
        responses=DomainDashboardVersionInfo.ListVersions.response()
    )
    async def list_versions(self, request: Request, body: DomainDashboardVersionInfo.ListVersions):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'dashboard.DomainDashboard.list_versions'
            return proxy_service.dispatch_api(params)

    @router.post(
        '/list',
        description=DomainDashboardInfo.List.description(),
        responses=DomainDashboardInfo.List.response()
    )
    async def list(self, request: Request, body: DomainDashboardInfo.List):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'dashboard.DomainDashboard.list'
            return proxy_service.dispatch_api(params)

    @router.post(
        '/stat',
        description=Stat.description(),
        responses=Stat.response()
    )
    async def stat(self, request: Request, body: Stat):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'dashboard.DomainDashboard.stat'
            return proxy_service.dispatch_api(params)
