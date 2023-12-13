import logging

from fastapi import Depends, Header
from fastapi.concurrency import run_in_threadpool
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from spaceone.core.error import *
from spaceone.core.fastapi.api import BaseAPI, exception_handler

from cloudforet.console_api_v2.model.auth.request import *
from cloudforet.console_api_v2.service.auth_service import AuthService

_LOGGER = logging.getLogger(__name__)
_AUTH_SCHEME = HTTPBasic()

router = InferringRouter(include_in_schema=True)

@cbv(router)
class Auth(BaseAPI):
    service = 'console-api'
    resource = "Auth"

    @router.get('/basic')
    @exception_handler
    async def basic(self, http_authorization: HTTPBasicCredentials = Depends(_AUTH_SCHEME)) -> dict:
        if http_authorization is None:
            raise ERROR_REQUIRED_PARAMETER(message="empty token provided.")

        auth_service = AuthService()
        await run_in_threadpool(auth_service.basic, http_authorization.dict())
        return {"status_code": "200"}


