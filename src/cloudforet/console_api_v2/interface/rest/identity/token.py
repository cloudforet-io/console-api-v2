import logging
from fastapi import Request, Body, Depends, Header
from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from spaceone.core.fastapi.api import BaseAPI, exception_handler
from cloudforet.console_api_v2.service.common.proxy_service import ProxyService
from cloudforet.console_api_v2.model.identity.token import *

_LOGGER = logging.getLogger(__name__)
_AUTH_SCHEME = HTTPBearer()

router = InferringRouter()


@cbv(router)
class Token(BaseAPI):
    service = 'console-api'

    @router.post('/issue', openapi_extra=IssueTokenRequest.meta(), response_model=TokenInfo)
    @exception_handler
    async def issue(self, request: Request):
        params, metadata = await self.parse_request(request)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'identity.Token.issue'
            return proxy_service.dispatch_api(params)

    @router.post('/refresh', openapi_extra=RefreshTokenRequest.meta())
    @exception_handler
    async def refresh(self, request: Request, refresh_token: str = Header(...)):
        params, metadata = await self.parse_request(request, token=refresh_token)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'identity.Token.refresh'
            return proxy_service.dispatch_api(params)
