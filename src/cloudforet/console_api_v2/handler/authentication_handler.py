import logging
from typing import Union

from spaceone.core import cache
from spaceone.core.handler.authentication_handler import SpaceONEAuthenticationHandler
from spaceone.core.transaction import get_transaction
from spaceone.core.auth.jwt import JWTUtil

_LOOGER = logging.getLogger(__name__)


class ConsoleAPIAuthenticationHandler(SpaceONEAuthenticationHandler):
    def verify(self, params: dict) -> None:
        if token := self._get_token_from_transaction():
            token_info = self._extract_token_info(token)
            if isinstance(token_info, dict):
                self._update_meta(token_info)

    @staticmethod
    def _get_token_from_transaction() -> Union[str, None]:
        transaction = get_transaction()
        token = transaction.meta.get("token")
        return token

    @staticmethod
    @cache.cacheable(key="console-api-v2:authentication:{token}", expire=300)
    def _extract_token_info(token: str):
        try:
            return JWTUtil.unverified_decode(token)
        except Exception as e:
            _LOOGER.error(f"Failed to decode token: {e}, {token}", exc_info=True)
