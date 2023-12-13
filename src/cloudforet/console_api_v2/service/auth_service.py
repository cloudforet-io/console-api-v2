import base64
import json
import logging

from spaceone.core import config
from spaceone.core.auth.jwt import JWTAuthenticator, JWTUtil
from spaceone.core.error import ERROR_AUTHENTICATE_FAILURE
from spaceone.core.service import *

from cloudforet.console_api_v2.manager.cloudforet_manager import CloudforetManager

_LOGGER = logging.getLogger(__name__)


@event_handler
class AuthService(BaseService):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @transaction
    def basic(self, params: dict) -> None:
        """Basic authentication
        Args:
            params: dict: {
                'user_name': 'str', # required
                'password': 'str'   # required
            }
        Returns:
            None

        """

        service_account_id = params['username']
        token = params['password']

        domain_id = self._extract_domain_id(token)
        self._authenticate(token, domain_id)

    def _authenticate(self, token: str, domain_id: str) -> dict:
        public_key = self._get_public_key(domain_id)
        return JWTAuthenticator(json.loads(public_key)).validate(token)

    def _get_public_key(self, domain_id: str) -> str:
        system_token = config.get_global().get('TOKEN')
        cloudforet_mgr = CloudforetManager(token=system_token)
        _LOGGER.debug(f'[_get_public_key] get jwk from identity service: {domain_id}')
        response = cloudforet_mgr.dispatch_api('identity.Domain.get_public_key', {"domain_id": domain_id})
        return response['public_key']

    @staticmethod
    def _extract_domain_id(token: str) -> str:
        try:
            decoded = JWTUtil.unverified_decode(token)
        except Exception:
            _LOGGER.debug(f'[_extract_domain_id] failed to decode token: {token[:10]}')
            raise ERROR_AUTHENTICATE_FAILURE(message='failed to decode token.')

        if domain_id := decoded.get('did'):
            return domain_id
        else:
            raise ERROR_AUTHENTICATE_FAILURE(message='empty domain_id provided.')
