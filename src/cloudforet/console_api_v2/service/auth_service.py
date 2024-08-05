import json
import logging
from typing import Union

from fastapi import Request, Response
from fastapi.responses import RedirectResponse
from spaceone.core import cache, config
from spaceone.core.auth.jwt import JWTAuthenticator, JWTUtil
from spaceone.core.error import ERROR_AUTHENTICATE_FAILURE
from spaceone.core.service import BaseService, event_handler, transaction

from cloudforet.console_api_v2.manager.cloudforet_manager import CloudforetManager
from cloudforet.console_api_v2.service.proxy_service import ProxyService

_LOGGER = logging.getLogger(__name__)


@event_handler
class AuthService(BaseService):
    resource = "Auth"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @transaction()
    def basic(self, params: dict) -> None:
        """Basic authentication

        Args:
            params: dict: {
                'username': 'str', # required
                'password': 'str'   # required
            }
        Returns:
            None
        """

        service_account_id = params["username"]
        token = params["password"]

        decoded_token_info = self.decode_token(token)

        domain_id = self.extract_domain_id(decoded_token_info)
        client_id = decoded_token_info.get("jti")
        decoded_service_account_id = decoded_token_info["injected_params"][
            "service_account_id"
        ]

        if service_account_id != decoded_service_account_id:
            raise ERROR_AUTHENTICATE_FAILURE(
                message=f"Given service account id {service_account_id} is not matched with {decoded_service_account_id}."
            )

        self._check_app(client_id, domain_id)
        self._authenticate(token, domain_id)

    def saml(self, params: dict) -> RedirectResponse:
        request = params.get("request")
        form_data = params.get("form_data")
        domain_id = params.get("domain_id")

        console_api_v2_endpoint = config.get_global("CONSOLE_API_V2_ENDPOINT")
        credentials = self._extract_credentials(
            request, console_api_v2_endpoint, dict(form_data)
        )
        domain_name = self._get_domain_name(domain_id)

        refresh_token = "unauthorized"
        try:
            refresh_token = self._issue_token(credentials, domain_id)
        except Exception as e:
            _LOGGER.error(f"[saml] failed to issue token: {e}")

        return self._redirect_response(domain_name, refresh_token)

    def saml_sp_metadata(self, domain_id: str) -> Response:
        sp_entity_id = domain_id
        domain_name = self._get_domain_name(domain_id)
        acs_url = self._get_acs_url(domain_name, domain_id)
        metadata_xml = self._generate_sp_metadata(sp_entity_id, acs_url)
        return Response(content=metadata_xml, media_type="application/xml")

    def _authenticate(self, token: str, domain_id: str) -> dict:
        public_key = self._get_public_key(domain_id)
        return JWTAuthenticator(json.loads(public_key)).validate(token)

    @staticmethod
    def _get_public_key(domain_id: str) -> str:
        system_token = config.get_global().get("TOKEN")
        cloudforet_mgr = CloudforetManager()
        _LOGGER.debug(f"[_get_public_key] get jwk from identity service: {domain_id}")
        response = cloudforet_mgr.dispatch_api(
            "identity.Domain.get_public_key",
            {"domain_id": domain_id},
            token=system_token,
        )
        return response["public_key"]

    @staticmethod
    def extract_domain_id(token_info: dict) -> str:
        if domain_id := token_info.get("did"):
            return domain_id
        else:
            raise ERROR_AUTHENTICATE_FAILURE(message="empty domain_id provided.")

    @staticmethod
    def decode_token(token: str) -> dict:
        try:
            decoded = JWTUtil.unverified_decode(token)
        except Exception:
            _LOGGER.debug(f"[_extract_domain_id] failed to decode token: {token[:10]}")
            raise ERROR_AUTHENTICATE_FAILURE(message="failed to decode token.")

        return decoded

    @staticmethod
    @cache.cacheable(
        key="console-api-v2:auth:check-app:{domain_id}:client_id:{client_id}",
        alias="local",
    )
    def _check_app(client_id: str, domain_id: str):
        system_token = config.get_global("TOKEN")

        _LOGGER.debug(f"[_check_app] check app from identity service: {client_id}")

        cloudforet_mgr = CloudforetManager()
        cloudforet_mgr.dispatch_api(
            "identity.App.check",
            {"client_id": client_id, "domain_id": domain_id},
            token=system_token,
        )

    @staticmethod
    def _extract_credentials(
        request: Request, console_api_v2_endpoint: str, form_data: dict
    ) -> dict:
        return {
            "http_host": console_api_v2_endpoint,
            "script_name": request.url.path,
            "post_data": form_data,
            "https": "on",
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

        return RedirectResponse(
            f"{console_domain}/saml?refresh_token={refresh_token}", status_code=302
        )

    @staticmethod
    def _get_acs_url(domain_name: str, domain_id: str) -> str:
        console_api_v2_endpoint = config.get_global("CONSOLE_API_V2_ENDPOINT")
        acs_url = f"https://{console_api_v2_endpoint}/console-api/extension/auth/saml/{domain_id}"

        return acs_url

    @staticmethod
    def _generate_sp_metadata(sp_entity_id: str, acs_url: str) -> str:
        """Generates SP metadata XML.

        Args:
            'sp_entity_id': 'str' (Service Provider Entity ID),
            'acs_url': 'str' (Assertion Consumer Service URL),
            'x509_cert': 'str' (X.509 certificate),

        Returns:
            'metadata_template': 'str' (SP metadata XML)
        """
        metadata_template = f"""
                <?xml version="1.0" encoding="UTF-8"?>
                <md:EntityDescriptor xmlns:md="urn:oasis:names:tc:SAML:2.0:metadata" entityID="{sp_entity_id}">
                    <md:SPSSODescriptor protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:protocol">
                        <md:AssertionConsumerService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" Location="{acs_url}" index="1"/>
                    </md:SPSSODescriptor>
                </md:EntityDescriptor>
                """

        return metadata_template.strip()
