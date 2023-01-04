from pydantic import BaseModel, Field
from typing import Union, List
from datetime import datetime
from cloudforet.console_api_v2.model import BaseAPIModel


class CloudServiceType(BaseModel):
    cloud_service_type_id: Union[str, None] = Field(None)
    name: Union[str, None] = Field(None)
    provider: Union[str, None] = Field(None)
    group: Union[str, None] = Field(None)
    cloud_service_type_key: Union[str, None] = Field(None)
    service_code: Union[str, None] = Field(None)
    is_primary: Union[bool, None] = Field(None)
    is_major: Union[bool, None] = Field(None)
    resource_type: Union[str, None] = Field(None)
    metadata: Union[dict, None] = Field(None)
    labels: Union[list, None] = Field(None)
    tags: Union[dict, None] = Field(None)
    domain_id: Union[str, None] = Field(None)
    created_at: Union[datetime, None] = Field(None)
    updated_at: Union[datetime, None] = Field(None)


class CloudServiceTypeInfo(CloudServiceType):
    class Create(BaseModel):
        name: str = Field(...)
        provider: str = Field(...)
        group: str = Field(...)
        service_code: Union[str, None] = Field(None)
        is_primary: Union[bool, None] = Field(None)
        is_major: Union[bool, None] = Field(None)
        resource_type: Union[str, None] = Field(None)
        metadata: Union[dict, None] = Field(None)
        labels: Union[list, None] = Field(None)
        tags: Union[dict, None] = Field(None)
        domain_id: Union[str, None] = Field(None)

        @staticmethod
        def description():
            return '''
# Request Body
## name
- required

## provider
- required

## group
- required
            '''

    class Update(BaseModel):
        cloud_service_type_id: str = Field(...)
        service_code: Union[str, None] = Field(None)
        is_primary: Union[bool, None] = Field(None)
        is_major: Union[bool, None] = Field(None)
        resource_type: Union[str, None] = Field(None)
        metadata: Union[dict, None] = Field(None)
        labels: Union[list, None] = Field(None)
        tags: Union[dict, None] = Field(None)
        domain_id: Union[str, None] = Field(None)

        @staticmethod
        def description():
            return '''
# Request Body
## cloud_service_type_id
- required      
            '''

    class Delete(BaseModel):
        cloud_service_type_id: str = Field(...)
        domain_id: Union[str, None] = Field(None)

        @staticmethod
        def description():
            return '''
# Request Body
## cloud_service_type_id
- required      
                '''

    class Get(BaseModel):
        cloud_service_type_id: str = Field(...)
        only: Union[list, None] = Field(None)
        domain_id: Union[str, None] = Field(None)

        @staticmethod
        def description():
            return '''
# Request Body
## cloud_service_type_id
- required      
                '''

    class List(BaseModel):
        cloud_service_type_id: Union[str, None] = Field(None)
        name: Union[str, None] = Field(None)
        provider: Union[str, None] = Field(None)
        group: Union[str, None] = Field(None)
        cloud_service_type_key: Union[str, None] = Field(None)
        service_code: Union[str, None] = Field(None)
        is_primary: Union[bool, None] = Field(None)
        is_major: Union[bool, None] = Field(None)
        resource_type: Union[str, None] = Field(None)
        query: Union[dict, None] = Field(None)
        domain_id: Union[str, None] = Field(None)

    class Stat(BaseModel):
        query: dict = Field(...)
        domain_id: Union[str, None] = Field(None)

        @staticmethod
        def description():
            return '''
# Request Body
## query
- required      
            '''


class CloudServiceTypeQuery(BaseAPIModel):
    cloud_service_type_id: Union[str, None] = Field(None)
    name: Union[str, None] = Field(None)
    provider: Union[str, None] = Field(None)
    group: Union[str, None] = Field(None)
    cloud_service_type_key: Union[str, None] = Field(None)
    service_code: Union[str, None] = Field(None)
    is_primary: Union[bool, None] = Field(None)
    is_major: Union[bool, None] = Field(None)
    resource_type: Union[str, None] = Field(None)
    query: Union[dict, None] = Field(None)
    domain_id: Union[str, None] = Field(None)


class CloudServiceTypesInfo(BaseAPIModel):
    results: Union[List[CloudServiceTypeInfo], None] = Field(None)
    total_count: Union[int, None] = Field(None)
