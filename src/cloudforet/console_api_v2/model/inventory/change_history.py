from pydantic import BaseModel, Field
from typing import Union
from datetime import datetime


class Record(BaseModel):
    record_id: Union[str, None] = Field(None)
    cloud_service_id: Union[str, None] = Field(None)
    action: Union[str, None] = Field(None)
    diff: Union[list, None] = Field(None)
    diff_count: Union[int, None] = Field(None)
    user_id: Union[str, None] = Field(None)
    collector_id: Union[str, None] = Field(None)
    job_id: Union[str, None] = Field(None)
    updated_by: Union[str, None] = Field(None)
    domain_id: Union[str, None] = Field(None)
    created_at: Union[datetime, None] = Field(None)


class ChangeHistoryInfo(Record):
    class List(BaseModel):
        cloud_service_id: Union[str, None] = Field(...)
        record_id: Union[str, None] = Field(None)
        action: Union[str, None] = Field(None)
        user_id: Union[str, None] = Field(None)
        collector_id: Union[str, None] = Field(None)
        job_id: Union[str, None] = Field(None)
        updated_by: Union[str, None] = Field(None)
        query: Union[str, None] = Field(None)
        domain_id: Union[str, None] = Field(None)

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
