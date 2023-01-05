from pydantic import Field
from typing import Union, List
from datetime import datetime
from cloudforet.console_api_v2.model import BaseAPIModel


class CreateCostRequest(BaseAPIModel):
    pass


class CostRequest(BaseAPIModel):
    pass


class GetCostRequest(BaseAPIModel):
    pass


class CostQuery(BaseAPIModel):
    cost_id: Union[str, None] = Field(None)
    original_currency: Union[str, None] = Field(None)
    provider: Union[str, None] = Field(None)
    region_code: Union[str, None] = Field(None)
    region_key: Union[str, None] = Field(None)
    category: Union[str, None] = Field(None)
    product: Union[str, None] = Field(None)
    account: Union[str, None] = Field(None)
    usage_type: Union[str, None] = Field(None)
    resource_group: Union[str, None] = Field(None)
    resource: Union[str, None] = Field(None)
    service_account_id: Union[str, None] = Field(None)
    project_id: Union[str, None] = Field(None)
    project_group_id: Union[str, None] = Field(None)
    data_source_id: Union[str, None] = Field(None)
    query: Union[dict, None] = Field(None)
    domain_id: Union[str, None] = Field(None)


class CostInfo(BaseAPIModel):
    cost_id: Union[str, None] = Field(None)
    usd_cost: Union[str, None] = Field(None)
    original_currency: Union[str, None] = Field(None)
    original_cost: Union[float, None] = Field(None)
    usage_quantity: Union[float, None] = Field(None)
    provider: Union[str, None] = Field(None)
    region_code: Union[str, None] = Field(None)
    region_key: Union[str, None] = Field(None)
    category: Union[str, None] = Field(None)
    product: Union[str, None] = Field(None)
    account: Union[str, None] = Field(None)
    usage_type: Union[str, None] = Field(None)
    resource_group: Union[str, None] = Field(None)
    resource: Union[str, None] = Field(None)
    tags: Union[dict, None] = Field(None)
    additional_info: Union[dict, None] = Field(None)
    service_account_id: Union[str, None] = Field(None)
    project_id: Union[str, None] = Field(None)
    data_source_id: Union[str, None] = Field(None)
    domain_id: Union[str, None] = Field(None)
    billed_at: Union[datetime, None] = Field(None)
    created_at: Union[datetime, None] = Field(None)


class CostsInfo(BaseAPIModel):
    results: Union[List[CostInfo], None] = Field(None)
    total_count: Union[int, None] = Field(None)


class CostAnalyzeV2Query(BaseAPIModel):
    query: dict = Field(None)
    domain_id: Union[str, None] = Field(None)


class CostAnalyzeInfo(BaseAPIModel):
    results: Union[list, None] = Field(None)
    more: Union[bool, None] = Field(None)


class CostStatQuery(BaseAPIModel):
    pass
