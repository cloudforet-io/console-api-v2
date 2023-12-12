from cloudforet.console_api_v2.model import BaseAPIModel
from pydantic import Field


class AuthBasicAuthRequest(BaseAPIModel):
    http_authorization: str = Field(description='Token for authentication', default="Basic encoded_token")
