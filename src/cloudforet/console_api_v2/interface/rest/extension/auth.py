import logging

from fastapi import Depends, Request
from fastapi.concurrency import run_in_threadpool
from fastapi.responses import RedirectResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from spaceone.core import config
from spaceone.core.error import ERROR_REQUIRED_PARAMETER
from spaceone.core.fastapi.api import BaseAPI, exception_handler

from cloudforet.console_api_v2.manager.cloudforet_manager import CloudforetManager
from cloudforet.console_api_v2.service.auth_service import AuthService
from cloudforet.console_api_v2.service.proxy_service import ProxyService

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
        form_data = await request.form()
        credentials = self._extract_credentials(request, dict(form_data))
        refresh_token = self._issue_token(credentials, domain_id)
        domain_name = self._get_domain_name(domain_id)
        return self._redirect_response(domain_name, refresh_token)

    @staticmethod
    def _extract_credentials(request: Request, form_data: dict) -> dict:
        return {
            "http_host": request.client.host,
            "server_port": request.url.port,
            "script_name": request.url.path,
            "post_data": form_data,
        }

    @staticmethod
    def _issue_token(credentials: dict, domain_id: str) -> str:
        dispatch_params = {
            "grpc_method": "identity.Token.issue",
            "credentials": credentials,
            "auth_type": "EXTERNAL",
            "domain_id": domain_id,
        }

        proxy_service = ProxyService()
        response = proxy_service.dispatch_api(dispatch_params)

        return response.get("refresh_token")

    @staticmethod
    def _get_domain_name(domain_id: str) -> str:
        cloudforet_mgr = CloudforetManager()
        grpc_method = "identity.Domain.get"
        dispatch_params = {"domain_id": domain_id}
        system_token = config.get_global("TOKEN")

        response = cloudforet_mgr.dispatch_api(
            grpc_method, dispatch_params, system_token
        )

        return response.get("name")

    @staticmethod
    def _redirect_response(domain_name: str, refresh_token: str) -> RedirectResponse:
        console_domain: str = config.get_global("CONSOLE_DOMAIN").format(
            domain_name=domain_name
        )
        if refresh_token:
            return RedirectResponse(
                f"{console_domain}/saml?sso_access_token={refresh_token}",
                status_code=302,
            )

        return RedirectResponse(f"{console_domain}", status_code=302)
