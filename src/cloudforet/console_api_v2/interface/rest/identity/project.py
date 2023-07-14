import logging
from fastapi import Request, Depends, Body
from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from spaceone.core.fastapi.api import BaseAPI, exception_handler
from cloudforet.console_api_v2.service.common.proxy_service import ProxyService
from cloudforet.console_api_v2.model.identity.project import *
_LOGGER = logging.getLogger(__name__)
_AUTH_SCHEME = HTTPBearer()

router = InferringRouter()


@cbv(router)
class Project(BaseAPI):
    token: HTTPAuthorizationCredentials = Depends(_AUTH_SCHEME)
    service = 'console-api'

    @router.post('/create', openapi_extra=CreateProjectRequest.meta(), response_model=ProjectInfo)
    @exception_handler
    async def create(self, request: Request):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'identity.Project.create'
            return proxy_service.dispatch_api(params)

    @router.post('/update', openapi_extra=UpdateProjectRequest.meta(), response_model=ProjectInfo)
    @exception_handler
    async def update(self, request: Request):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'identity.Project.update'
            return proxy_service.dispatch_api(params)

    @router.post('/update', openapi_extra=UpdateProjectRequest.meta(), response_model=ProjectInfo)
    @exception_handler
    async def update(self, request: Request):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'identity.Project.update'
            return proxy_service.dispatch_api(params)

    @router.post('/member-modify')
    @exception_handler
    async def modify_member(self, request: Request, body: dict = Body(...)):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'identity.Project.modify_member'
            return proxy_service.dispatch_api(params)

    @router.post('/member-list')
    @exception_handler
    async def list_members(self, request: Request, body: dict = Body(...)):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'identity.Project.list_members'
            return proxy_service.dispatch_api(params)

    @router.post('/list', openapi_extra=ProjectQuery.meta(), response_model=ProjectsInfo)
    @exception_handler
    async def list(self, request: Request):
        """
        ## Description
        Get all of your projects.

        <br>
        | Key                  | Description                                                   | Type   | Required |
        |----------------------|---------------------------------------------------------------|--------|----------|
        | **project_id**       | Project id                                                    | string |          |
        | **name**             | Project name                                                  | string |          |
        | **project_group_id** | Project group id                                              | string |          |
        | **query**            | Query option for detail search                                | object |          |
        | **domain_id**        | Unique id by each domain (extracted automatically from token) | string |          |
        """
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'identity.Project.list'
            return proxy_service.dispatch_api(params)

    @router.post('/stat')
    @exception_handler
    async def stat(self, request: Request, body: dict = Body(...)):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'identity.Project.stat'
            return proxy_service.dispatch_api(params)
