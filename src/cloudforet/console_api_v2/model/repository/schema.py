from pydantic import BaseModel, Field
from typing import Union
from datetime import datetime


# Base Model

class Schema(BaseModel):
    schema_id: Union[str, None] = Field(None)
    name: Union[str, None] = Field(None)
    service_type: Union[str, None] = Field(None)
    schema_dict: Union[dict, None] = Field(..., alias="schema")
    repository_info: Union[dict, None] = Field(None)
    domain_id: Union[str, None] = Field(None)
    project_id: Union[str, None] = Field(None)
    labels: Union[list, None] = Field(None)
    tags: Union[dict, None] = Field(None)
    created_at: Union[datetime, None] = Field(None)


# SchemaInfo model
class SchemaInfo(Schema):
    class Create(BaseModel):
        schema_id: str = Field(...)
        name: str = Field(...)
        service_type: str = Field(...)
        schema_dict: dict = Field(..., alias="schema")
        project_id: Union[str, None] = Field(None)
        labels: Union[list, None] = Field(None)
        tags: Union[dict, None] = Field(None)
        domain_id: Union[str, None] = Field(None)

    class Update(BaseModel):
        name: Union[str, None] = Field(None)
        schema_dict: Union[dict, None] = Field(None, alias="schema")
        labels: Union[list, None] = Field(None)
        tags: Union[dict, None] = Field(None)
        domain_id: Union[str, None] = Field(None)

    class Delete(BaseModel):
        name: Union[str, None] = Field(None)
        domain_id: Union[str, None] = Field(None)

    class Get(BaseModel):
        name: str = Field(...)
        repository_id: Union[str, None] = Field(None)
        only: Union[list, None] = Field(None)
        domain_id: Union[str, None] = Field(None)

    class List(BaseModel):
        repository_id: str = Field(...)
        service_type: Union[str, None] = Field(None)
        project_id: Union[str, None] = Field(None)
        query: Union[dict, None] = Field(None)
        domain_id: Union[str, None] = Field(None)

    class Stat(BaseModel):
        query: dict = Field(...)
        domain_id: Union[str, None] = Field(None)
