from pydantic import BaseModel, Field
from typing import Union
from datetime import datetime


class CloudServiceTag(BaseModel):
    cloud_service_id: Union[str, None] = Field(None)
    key: Union[str, None] = Field(None)
    value: Union[str, None] = Field(None)
    type: Union[str, None] = Field(None)
    provider: Union[str, None] = Field(None)
    project_id: Union[str, None] = Field(None)
    domain_id: Union[str, None] = Field(None)
    created_at: Union[datetime, None] = Field(None)


class CloudServiceTagInfo(CloudServiceTag):
    class List(BaseModel):
        cloud_service_id: str = Field(...)
        key: Union[str, None] = Field(None)
        provider: Union[str, None] = Field(None)
        domain_id: Union[str, None] = Field(None)
        created_at: Union[datetime, None] = Field(None)

        @staticmethod
        def description():
            return '''
# Request Body
## cloud_service_id
- required
            '''

    class Stat(BaseModel):
        cloud_service_id: str = Field(...)
        query: dict = Field(...)
        domain_id: Union[str, None] = Field(None)

        @staticmethod
        def description():
            return '''
# Request Body
## cloud_service_id
- required

## query
- required      
            '''
