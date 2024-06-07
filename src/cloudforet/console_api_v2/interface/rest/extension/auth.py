import logging

from fastapi import Depends, Request
from fastapi.concurrency import run_in_threadpool
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from spaceone.core.error import ERROR_REQUIRED_PARAMETER
from spaceone.core.fastapi.api import BaseAPI, exception_handler

from cloudforet.console_api_v2.service.auth_service import AuthService

_LOGGER = logging.getLogger(__name__)
_AUTH_SCHEME = HTTPBasic()

router = InferringRouter(include_in_schema=True)


@cbv(router)
class Auth(BaseAPI):
    service = "console-api"
    resource = "Auth"

    @router.get("/basic")
    @exception_handler
    async def basic(
        self, http_authorization: HTTPBasicCredentials = Depends(_AUTH_SCHEME)
    ) -> dict:
        if http_authorization is None:
            raise ERROR_REQUIRED_PARAMETER(message="empty token provided.")

        auth_service = AuthService()
        await run_in_threadpool(auth_service.basic, http_authorization.dict())
        return {"status_code": "200"}

    @router.post("/saml/{domain_id}")
    @exception_handler
    async def saml(self, request: Request, domain_id: str):
        saml_service: AuthService = AuthService()
        form_data = await request.form()
        params = {"request": request, "form_data": form_data, "domain_id": domain_id}
        response = await run_in_threadpool(saml_service.saml, params)
        return response

    @router.get("/saml/{domain_id}/metadata")
    @exception_handler
    async def saml_sp_metadata(self, domain_id: str):
        saml_service: AuthService = AuthService()
        response = await run_in_threadpool(saml_service.saml_sp_metadata, domain_id)
        return response
