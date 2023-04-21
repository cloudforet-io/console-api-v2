from cloudforet.console_api_v2.model import BaseAPIModel
from pydantic import Field
from typing import Union, List


class ListFieldsRequest(BaseAPIModel):
    service: str = Field(...)
    resource: str = Field(...)
    options: Union[dict, None] = Field(None)
    limit: Union[int, None] = Field(None)


class FieldInfo(BaseAPIModel):
    key: str = Field(None)
    name: str = Field(None)
    nested: bool = Field(None)


class FieldsInfo(BaseAPIModel):
    results: List[FieldInfo] = Field(None)
    more: bool = Field(None)


class ListFieldValuesRequest(BaseAPIModel):
    service: str = Field(...)
    resource: str = Field(...)
    field: str = Field(...)
    options: Union[dict, None] = Field(None)
    search: Union[str, None] = Field(None)
    limit: Union[int, None] = Field(None)


class ValueInfo(BaseAPIModel):
    key: str = Field(None)
    name: str = Field(None)


class ValuesInfo(BaseAPIModel):
    results: List[ValueInfo] = Field(None)
    more: bool = Field(None)
