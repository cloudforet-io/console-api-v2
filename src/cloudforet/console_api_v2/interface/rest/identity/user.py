import logging
from fastapi import Request, Depends, Body
from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from spaceone.core.fastapi.api import BaseAPI, exception_handler
from cloudforet.console_api_v2.model.identity.user import *
from cloudforet.console_api_v2.service.common.proxy_service import ProxyService

_LOGGER = logging.getLogger(__name__)
_AUTH_SCHEME = HTTPBearer()

router = InferringRouter()


@cbv(router)
class User(BaseAPI):

    token: HTTPAuthorizationCredentials = Depends(_AUTH_SCHEME)
    service = 'console-api'

    @router.post('/create', openapi_extra=CreateUserRequest.meta(), response_model=UserInfo)
    @exception_handler
    async def create(self, request: Request):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'identity.User.create'
            return proxy_service.dispatch_api(params)

    @router.post('/update', openapi_extra=UpdateUserRequest.meta(), response_model=UserInfo)
    @exception_handler
    async def update(self, request: Request):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'identity.User.update'
            return proxy_service.dispatch_api(params)

    @router.post('/verify-email', openapi_extra=VerifyEmailRequest.meta())
    @exception_handler
    async def verify_email(self, request: Request):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'identity.User.verify_email'
            return proxy_service.dispatch_api(params)

    @router.post('/confirm-email', openapi_extra=ConfirmEmailRequest.meta(), response_model=UserInfo)
    @exception_handler
    async def confirm_email(self, request: Request):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'identity.User.confirm_email'
            return proxy_service.dispatch_api(params)

    @router.post('/delete', openapi_extra=UserRequest.meta())
    @exception_handler
    async def delete(self, request: Request):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'identity.User.delete'
            return proxy_service.dispatch_api(params)

    @router.post('/set-required-actions', openapi_extra=SetRequiredActionsRequest.meta(), response_model=UserInfo)
    @exception_handler
    async def set_required_actions(self, request: Request):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'identity.User.set_required_actions'
            return proxy_service.dispatch_api(params)

    @router.post('/find')
    @exception_handler
    async def find(self, request: Request, body: dict = Body(...)):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'identity.User.find'
            return proxy_service.dispatch_api(params)

    @router.post('/sync', openapi_extra=UserQuery.meta())
    @exception_handler
    async def sync(self, request: Request):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'identity.User.sync'
            return proxy_service.dispatch_api(params)

    @router.post('/list', openapi_extra=UserQuery.meta(), response_model=UsersInfo)
    @exception_handler
    async def list(self, request: Request):
        """
        ## Description
        Get all of your users.

        <br>
        | Key           | Description                                                   | Type   | Required |
        |---------------|---------------------------------------------------------------|--------|----------|
        | **user_id**   | Login id                                                      | string |          |
        | **name**      | Name value                                                    | string |          |
        | **state**     | State of user id                                              | string |          |
        | **email**     | Email value                                                   | string |          |
        | **user_type** | USER(default) and API_USER type exist                         | string |          |
        | **backend**   | LOCAL(default) and EXTERANL type exist                        | string |          |
        | **query**     | Query option for detail search                                | object |          |
        | **domain_id** | Unique id by each domain (extracted automatically from token) | string |          |
        """
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'identity.User.list'
            return proxy_service.dispatch_api(params)

    @router.post('/stat')
    @exception_handler
    async def stat(self, request: Request, body: dict = Body(...)):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'identity.User.stat'
            return proxy_service.dispatch_api(params)


@cbv(router)
class NotAuthenticatedUser(BaseAPI):

    service = 'console-api'

    @router.post('/reset-password', openapi_extra=UserRequest.meta())
    @exception_handler
    async def reset_password(self, request: Request):
        params, metadata = await self.parse_request(request, token=None)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'identity.User.reset_password'
            return proxy_service.dispatch_api(params)
