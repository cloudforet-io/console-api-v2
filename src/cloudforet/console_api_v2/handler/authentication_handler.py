import jwt
from spaceone.core import cache
from spaceone.core.error import ERROR_PERMISSION_DENIED
from spaceone.core.handler.authentication_handler import SpaceONEAuthenticationHandler


class ConsoleAPIAuthenticationHandler(SpaceONEAuthenticationHandler):
    def verify(self, params: dict) -> None:
        token = self._get_token()
        token_info = self._extract_token_info(token)

        self._update_meta(token_info)

    @staticmethod
    @cache.cacheable(key="console-api-v2:authentication:{token}", expire=300)
    def _extract_token_info(token: str):
        try:

            decoded_payload = jwt.decode(
                token,
                options={"verify_signature": False},
            )

            token_info = decoded_payload

            return token_info

        except Exception as e:
            raise ERROR_PERMISSION_DENIED()
