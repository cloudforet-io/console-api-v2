from cloudforet.console_api_v2.model import BaseAPIModel
from pydantic import Field


class AuthBasicAuthRequest(BaseAPIModel):
    token: str = Field(default=None, description='Token for authentication')
