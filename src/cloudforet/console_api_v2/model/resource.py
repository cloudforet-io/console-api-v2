from cloudforet.console_api_v2.model import BaseAPIModel
from pydantic import Field
from typing import Union, List


class ListFieldsRequest(BaseAPIModel):
    service: str = Field(..., description='Service name (identity, inventory, etc.)', examples=['inventory','identity'])
    resource: str = Field(..., description='Resource name')
    options: Union[dict, None] = Field(default=None, description='Additional options for each resource')
    limit: Union[int, None] = Field(None, description='Set the number of returns')

    class Config:
        description = 'List fields of API Resource.'


class FieldInfo(BaseAPIModel):
    key: str = Field(None)
    name: str = Field(None)
    nested: bool = Field(None)


class FieldsInfo(BaseAPIModel):
    results: List[FieldInfo] = Field(None, description='List of fields')
    more: bool = Field(None)


class ListFieldValuesRequest(BaseAPIModel):
    service: str = Field(..., description='Service name (identity, inventory, etc.)')
    resource: str = Field(..., description='Resource name')
    field: str = Field(..., description='field name')
    options: Union[dict, None] = Field(None, description='Additional options for each resource')
    search: Union[str, None] = Field(None, description='search keywords for value')
    limit: Union[int, None] = Field(None, description='Set the number of returns')

    class Config:
        description = 'List values of API resource field'


class ValueInfo(BaseAPIModel):
    key: str = Field(None)
    name: str = Field(None)


class ValuesInfo(BaseAPIModel):
    results: List[ValueInfo] = Field(None)
    more: bool = Field(None)

