from pydantic import BaseModel, Field
from typing import Union
from datetime import datetime


# Base Model

class Policy(BaseModel):
    policy_id: Union[str, None] = Field(None)
    name: Union[str, None] = Field(None)
    permissions: Union[list, None] = Field(None)
    labels: Union[list, None] = Field(None)
    tags: Union[dict, None] = Field(None)
    domain_id: Union[str, None] = Field(None)
    project_id: Union[str, None] = Field(None)
    created_at: Union[datetime, None] = Field(None)


# PolicyInfo model
class PolicyInfo(Policy):
    class Create(BaseModel):
        policy_id: str = Field(...)
        name: str = Field(...)
        permissions: list = Field(...)
        labels: Union[list, None] = Field(None)
        tags: Union[dict, None] = Field(None)
        project_id: Union[str, None] = Field(None)
        domain_id: Union[str, None] = Field(None)

    class Update(BaseModel):
        policy_id: str = Field(...)
        name: Union[str, None] = Field(None)
        permissions: list = Field(...)
        labels: Union[list, None] = Field(None)
        tags: Union[dict, None] = Field(None)
        domain_id: Union[str, None] = Field(None)

    class Delete(BaseModel):
        policy_id: Union[str, None] = Field(None)
        domain_id: Union[str, None] = Field(None)

    class Get(BaseModel):
        policy_id: str = Field(...)
        repository_id: Union[str, None] = Field(None)
        only: Union[list, None] = Field(None)
        domain_id: Union[str, None] = Field(None)

    class List(BaseModel):
        repository_id: str = Field(...)
        policy_id: Union[str, None] = Field(None)
        name: Union[str, None] = Field(None)
        query: Union[dict, None] = Field(None)
        domain_id: Union[str, None] = Field(None)

    class Stat(BaseModel):
        repository_id: str = Field(...)
        query: dict = Field(...)
        domain_id: Union[str, None] = Field(None)
