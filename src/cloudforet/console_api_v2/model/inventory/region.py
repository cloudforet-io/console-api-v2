from pydantic import Field
from typing import Union, List
from datetime import datetime
from cloudforet.console_api_v2.model import BaseAPIModel


class CreateRegionRequest(BaseAPIModel):
    name: Union[str, None] = Field(...)
    region_code: Union[str, None] = Field(...)
    provider: Union[str, None] = Field(...)
    tags: Union[dict, None] = Field(None)
    domain_id: Union[str, None] = Field(None)


class UpdateRegionRequest(BaseAPIModel):
    region_id: Union[str, None] = Field(...)
    name: Union[str, None] = Field(None)
    tags: Union[dict, None] = Field(None)
    domain_id: Union[str, None] = Field(None)


class RegionRequest(BaseAPIModel):
    region_id: Union[str, None] = Field(...)
    domain_id: Union[str, None] = Field(None)


class GetRegionRequest(BaseAPIModel):
    region_id: Union[str, None] = Field(...)
    only: Union[list, None] = Field(None)
    domain_id: Union[str, None] = Field(None)


class RegionQuery(BaseAPIModel):
    region_id: Union[str, None] = Field(None)
    name: Union[str, None] = Field(None)
    region_key: Union[str, None] = Field(None)
    region_code: Union[list, None] = Field(None)
    provider: Union[str, None] = Field(None)
    query: Union[dict, None] = Field(None)
    domain_id: Union[str, None] = Field(None)


class RegionStatQuery(BaseAPIModel):
    query: dict = Field(...)
    domain_id: Union[str, None] = Field(None)


class RegionInfo(BaseAPIModel):
    region_id: Union[str, None] = Field(None)
    name: Union[str, None] = Field(None)
    region_key: Union[str, None] = Field(None)
    region_code: Union[str, None] = Field(None)
    provider: Union[str, None] = Field(None)
    tags: Union[dict, None] = Field(None)
    domain_id: Union[str, None] = Field(None)
    created_at: Union[datetime, None] = Field(None)
    updated_at: Union[datetime, None] = Field(None)


class RegionsInfo(BaseAPIModel):
    results: Union[List[RegionInfo], None] = Field(None)
    total_count: Union[int, None] = Field(None)


class RegionStatInfo(BaseAPIModel):
    results: Union[list, None] = Field(None)
