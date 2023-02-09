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
class Domain(BaseAPI):
    service = 'console-api'

    @router.post('/get')
    @exception_handler
    async def get(self, request: Request, body: dict = Body(...),
                  token: HTTPAuthorizationCredentials = Depends(_AUTH_SCHEME)):
        params, metadata = await self.parse_request(request, token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'identity.Domain.get'
            return proxy_service.dispatch_api(params)

    @router.post('/stat')
    @exception_handler
    async def stat(self, request: Request, body: dict = Body(...),
                   token: HTTPAuthorizationCredentials = Depends(_AUTH_SCHEME)):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'identity.Domain.stat'
            return proxy_service.dispatch_api(params)
