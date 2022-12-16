from pydantic import BaseModel, Field
from typing import Union
from datetime import datetime


# Base Model

class Repository(BaseModel):
    repository_id: Union[str, None] = Field(None)
    name: Union[str, None] = Field(None)
    repository_type: Union[str, None] = Field(None)
    endpoint: Union[str, None] = Field(None)
    created_at: Union[datetime, None] = Field(None)


# RepositoryInfo model
class RepositoryInfo(Repository):
    class Register(BaseModel):
        name: str = Field(...)
        repository_type: str = Field(...)
        endpoint: Union[str, None] = Field(None)
        domain_id: Union[str, None] = Field(None)

    class Update(BaseModel):
        repository_id: str = Field(...)
        name: Union[str, None] = Field(None)
        domain_id: Union[str, None] = Field(None)

    class Deregister(BaseModel):
        repository_id: str = Field(...)
        only: Union[list, None] = Field(None)
        domain_id: Union[str, None] = Field(None)

    class Get(BaseModel):
        repository_id: str = Field(...)
        domain_id: Union[str, None] = Field(None)

    class List(BaseModel):
        repository_id: Union[str, None] = Field(None)
        domain_id: Union[str, None] = Field(None)

    class Stat(BaseModel):
        query: dict = Field(...)
        domain_id: Union[str, None] = Field(None)
