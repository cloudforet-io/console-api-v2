from cloudforet.console_api_v2.model import BaseAPIModel
from pydantic import Field
from typing import Union, List
from datetime import datetime


class CreateUserRequest(BaseAPIModel):
    user_id: Union[str, None] = Field(...)
    password: Union[str, None] = Field(None)
    name: Union[str, None] = Field(None)
    email: Union[str, None] = Field(None)
    user_type: Union[str, None] = Field(None)
    backend: Union[str, None] = Field(...)
    language: Union[str, None] = Field(None)
    timezone: Union[str, None] = Field(None)
    tags: Union[dict, None] = Field(None)
    domain_id: Union[str, None] = Field(None)
    reset_password: Union[bool, None] = Field(None)


class UpdateUserRequest(BaseAPIModel):
    user_id: Union[str, None] = Field(...)
    password: Union[str, None] = Field(None)
    name: Union[str, None] = Field(None)
    email: Union[str, None] = Field(None)
    reset_password: Union[bool, None] = Field(None)
    language: Union[str, None] = Field(None)
    timezone: Union[str, None] = Field(None)
    tags: Union[dict, None] = Field(None)
    domain_id: Union[str, None] = Field(None)


class ConfirmUserRequest(BaseAPIModel):
    user_id: Union[str, None] = Field(...)
    verify_code: Union[str, None] = Field(...)
    domain_id: Union[str, None] = Field(None)


class SetRequiredActionsRequest(BaseAPIModel):
    user_id: Union[str, None] = Field(...)
    actions: Union[list, None] = Field(...)
    domain_id: Union[str, None] = Field(None)


class VerifyEmailRequest(BaseAPIModel):
    user_id: Union[str, None] = Field(...)
    email: Union[str, None] = Field(None)
    force: Union[bool, None] = Field(None)
    domain_id: Union[str, None] = Field(None)


class ConfirmEmailRequest(BaseAPIModel):
    user_id: Union[str, None] = Field(...)
    verify_code: Union[str, None] = Field(...)
    domain_id: Union[str, None] = Field(None)


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
    last_accessed_at: Union[datetime, None] = Field(None)
    created_at: Union[datetime, None] = Field(None)
    domain_id: Union[str, None] = Field(None)
    email_verified: Union[bool, None] = Field(None)


class UsersInfo(BaseAPIModel):
    results: Union[List[UserInfo]] = Field(None)
    total_count: Union[int, None] = Field(None)
