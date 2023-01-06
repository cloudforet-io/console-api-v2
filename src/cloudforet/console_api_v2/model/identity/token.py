from cloudforet.console_api_v2.model import BaseAPIModel
from pydantic import Field
from typing import Union


class IssueTokenRequest(BaseAPIModel):
    user_id: Union[str, None] = Field(None)
    user_type: str = Field(...)
    credentials: dict = Field(...)
    time_out: Union[int, None] = Field(None)
    refresh_count: Union[str, None] = Field(None)
    domain_id: Union[str, None] = Field(None)


class RefreshTokenRequest(BaseAPIModel):
    pass


class TokenInfo(BaseAPIModel):
    access_token: Union[str, None] = Field(None)
    refresh_token: Union[str, None] = Field(None)
