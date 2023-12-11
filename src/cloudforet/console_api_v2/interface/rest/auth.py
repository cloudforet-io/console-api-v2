import logging

from fastapi import Depends
from fastapi.concurrency import run_in_threadpool
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from spaceone.core.error import *
from spaceone.core.fastapi.api import BaseAPI, exception_handler

from cloudforet.console_api_v2.model.auth.request import *
from cloudforet.console_api_v2.service.auth_service import AuthService

_LOGGER = logging.getLogger(__name__)
_AUTH_SCHEME = HTTPBearer(auto_error=False)

router = InferringRouter(include_in_schema=True)


@cbv(router)
class Auth(BaseAPI):
    token: HTTPAuthorizationCredentials = Depends(_AUTH_SCHEME)
    service = 'console-api'
    resource = "Auth"

    @router.get('/basic-auth')
    @exception_handler
    async def basic_auth(self, params: AuthBasicAuthRequest = Depends()):
        params.token = params.token or self.token.credentials

        if params.token is None:
            raise ERROR_REQUIRED_PARAMETER(message='empty token provided.')

        auth_service = AuthService()
        await run_in_threadpool(auth_service.basic_auth, params.dict())
        return {"status_code": "200"}


