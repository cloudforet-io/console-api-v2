from pydantic import BaseModel, Field
from typing import Union, List
from datetime import datetime
from cloudforet.console_api_v2.model import BaseAPIModel


class CreateServiceRequest(BaseAPIModel):
    cloud_service_id: str = Field(...)
    provider: str = Field(...)
    cloud_service_group: str = Field(...)
    name: Union[str, None] = Field(None)
    ip_addresses: Union[list, None] = Field(None)
    account: Union[str, None] = Field(None)
    instance_type: Union[str, None] = Field(None)
    instance_size: Union[float, None] = Field(None)
    data: dict = Field(...)
    metadata: Union[dict, None] = Field(None)
    reference: Union[dict, None] = Field(None)
    tags: Union[dict, None] = Field(None)
    region_code: Union[str, None] = Field(None)
    project_id: Union[str, None] = Field(None)
    domain_id: Union[str, None] = Field(None)


class UpdateCloudServiceRequest(BaseAPIModel):
    cloud_service_id: Union[str, None] = Field(...)
    name: Union[str, None] = Field(None)
    ip_addresses: Union[list, None] = Field(None)
    account: Union[str, None] = Field(None)
    instance_type: Union[str, None] = Field(None)
    instance_size: Union[float, None] = Field(None)
    data: Union[dict, None] = Field(None)
    metadata: Union[dict, None] = Field(None)
    reference: Union[dict, None] = Field(None)
    tags: Union[dict, None] = Field(None)
    region_code: Union[str, None] = Field(None)
    project_id: Union[str, None] = Field(None)
    release_project: Union[str, None] = Field(None)
    release_region: Union[str, None] = Field(None)
    domain_id: Union[str, None] = Field(None)


class GetCloudServiceRequest(BaseAPIModel):
    cloud_service_id: Union[str, None] = Field(...)
    only: Union[list, None] = Field(None)
    domain_id: Union[str, None] = Field(None)


class CloudServiceQuery(BaseAPIModel):
    cloud_service_id: Union[str, None] = Field(None)
    name: Union[str, None] = Field(None)
    state: Union[str, None] = Field(None)
    ip_address: Union[str, None] = Field(None)
    account: Union[str, None] = Field(None)
    instance_type: Union[str, None] = Field(None)
    cloud_service_type: Union[str, None] = Field(None)
    cloud_service_group: Union[str, None] = Field(None)
    provider: Union[str, None] = Field(None)
    tags: Union[dict, None] = Field(None)
    region_code: Union[str, None] = Field(None)
    project_id: Union[str, None] = Field(None)
    project_group_id: Union[str, None] = Field(None)
    resource_group_id: Union[str, None] = Field(None)
    query: Union[dict, None] = Field(None)
    domain_id: Union[str, None] = Field(None)


class CloudServiceInfo(BaseAPIModel):
    cloud_service_id: Union[str, None] = Field(None)
    name: Union[str, None] = Field(None)
    state: Union[str, None] = Field(None)
    ip_addresses: Union[list, None] = Field(None)
    account: Union[str, None] = Field(None)
    instance_type: Union[str, None] = Field(None)
    instance_size: Union[float, None] = Field(None)
    cloud_service_type: Union[str, None] = Field(None)
    cloud_service_group: Union[str, None] = Field(None)
    provider: Union[str, None] = Field(None)
    data: Union[dict, None] = Field(None)
    metadata: Union[dict, None] = Field(None)
    reference: Union[dict, None] = Field(None)
    tags: Union[dict, None] = Field(None)
    tag_keys: Union[dict, None] = Field(None)
    collection_info: Union[list, None] = Field(None)
    region_code: Union[str, None] = Field(None)
    project_id: Union[str, None] = Field(None)
    domain_id: Union[str, None] = Field(None)
    created_at: Union[datetime, None] = Field(None)
    updated_at: Union[datetime, None] = Field(None)
    deleted_at: Union[datetime, None] = Field(None)


class CloudServicesInfo(BaseModel):
    results: Union[List[CloudServiceInfo], None] = Field(None)
    total_count: Union[int, None] = Field(None)


class CloudServiceStatQuery(BaseAPIModel):
    resource_group_id: str = Field(None)
    query: dict = Field(...)
    domain_id: Union[str, None] = Field(None)


class CloudServiceAnalyzeQuery(BaseAPIModel):
    query: dict = Field(...)
    domain_id: Union[str, None] = Field(None)
