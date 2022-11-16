import logging
from fastapi import Request, Depends
from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from spaceone.core.fastapi.api import BaseAPI, exception_handler
from cloudforet.console_api_v2.model.dashboard.project_dashboard import *
from cloudforet.console_api_v2.service.common.proxy_service import ProxyService

_LOGGER = logging.getLogger(__name__)
_AUTH_SCHEME = HTTPBearer()

router = InferringRouter()


@cbv(router)
class ProjectDashboard(BaseAPI):
    token: HTTPAuthorizationCredentials = Depends(_AUTH_SCHEME)
    service = 'console-api'

    @router.post(
        '/create',
    )
    @exception_handler
    async def create(self, request: Request, body: ProjectDashboardInfo.Create):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'dashboard.ProjectDashboard.create'
            return proxy_service.dispatch_api(params)

    @router.post(
        '/update'
    )
    @exception_handler
    async def update(self, request: Request, body: ProjectDashboardInfo.Update):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'dashboard.ProjectDashboard.update'
            return proxy_service.dispatch_api(params)

    @router.post(
        '/delete'
    )
    @exception_handler
    async def delete(self, request: Request, body: ProjectDashboardInfo.Delete):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'dashboard.ProjectDashboard.delete'
            return proxy_service.dispatch_api(params)

    @router.post(
        '/get'
    )
    @exception_handler
    async def get(self, request: Request, body: ProjectDashboardInfo.Get):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'dashboard.ProjectDashboard.get'
            return proxy_service.dispatch_api(params)

    @router.post(
        '/delete_version'
    )
    @exception_handler
    async def delete_version(self, request: Request, body: ProjectDashboardVersionInfo.DeleteVersion):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'dashboard.ProjectDashboard.delete_version'
            return proxy_service.dispatch_api(params)

    @router.post(
        '/revert_version'
    )
    @exception_handler
    async def revert_version(self, request: Request, body: ProjectDashboardVersionInfo.RevertVersion):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'dashboard.ProjectDashboard.revert_version'
            return proxy_service.dispatch_api(params)

    @router.post(
        '/get_version'
    )
    @exception_handler
    async def get_version(self, request: Request, body: ProjectDashboardVersionInfo.RevertVersion):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'dashboard.ProjectDashboard.get_version'
            return proxy_service.dispatch_api(params)

    @router.post(
        '/list_versions'
    )
    @exception_handler
    async def list_versions(self, request: Request, body: ProjectDashboardVersionInfo.ListVersions):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'dashboard.ProjectDashboard.list_versions'
            return proxy_service.dispatch_api(params)

    @router.post(
        '/list'
    )
    @exception_handler
    async def list(self, request: Request, body: ProjectDashboardInfo.List):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'dashboard.ProjectDashboard.list'
            return proxy_service.dispatch_api(params)

    @router.post(
        '/stat'
    )
    @exception_handler
    async def stat(self, request: Request, body: Stat):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'dashboard.ProjectDashboard.stat'
            return proxy_service.dispatch_api(params)

