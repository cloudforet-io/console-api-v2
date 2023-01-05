from cloudforet.console_api_v2.model import BaseAPIModel
from pydantic import Field
from typing import Union, List
from datetime import datetime


class CreateUserRequest(BaseAPIModel):
    pass


class UpdateUserRequest(BaseAPIModel):
    pass


class SetRequiredActionsRequest(BaseAPIModel):
    pass


class UserRequest(BaseAPIModel):
    user_id: str = Field(...)
    domain_id: Union[str, None] = Field(None)


class UserQuery(BaseAPIModel):
    user_id: Union[str, None] = Field(None)
    name: Union[str, None] = Field(None)
    state: Union[str, None] = Field(None)
    email: Union[str, None] = Field(None)
    user_type: Union[str, None] = Field(None)
    backend: Union[str, None] = Field(None)
    query: Union[dict, None] = Field(None)
    domain_id: Union[str, None] = Field(None)


class UserInfo(BaseAPIModel):
    user_id: Union[str, None] = Field(None)
    name: Union[str, None] = Field(None)
    state: Union[str, None] = Field(None)
    email: Union[str, None] = Field(None)
    user_type: Union[str, None] = Field(None)
    backend: Union[str, None] = Field(None)
    required_actions: Union[list, None] = Field(None)
    tags: Union[dict, None] = Field(None)
    domain_id: Union[str, None] = Field(None)
    last_accessed_at: Union[datetime, None] = Field(None)
    created_at: Union[datetime, None] = Field(None)


class UsersInfo(BaseAPIModel):
    results: Union[List[UserInfo]] = Field(None)
    total_count: Union[int, None] = Field(None)
