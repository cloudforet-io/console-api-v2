from pydantic import BaseModel, Field
from typing import Union
from datetime import datetime


class Note(BaseModel):
    note_id: Union[str, None] = Field(None)
    record_id: Union[str, None] = Field(None)
    cloud_service_id: Union[str, None] = Field(None)
    note: Union[str, None] = Field(None)
    created_by: Union[str, None] = Field(None)
    domain_id: Union[str, None] = Field(None)
    created_at: Union[datetime, None] = Field(None)


class NoteInfo(Note):
    class Create(BaseModel):
        record_id: str = Field(...)
        note: str = Field(...)
        domain_id: Union[str, None] = Field(None)
        user_id: Union[str, None] = Field(None)

        @staticmethod
        def description():
            return '''
# Request Body
## record_id
- required

## note
- required
            '''

    class Update(BaseModel):
        note_id: Union[str, None] = Field(...)
        note: Union[str, None] = Field(...)
        domain_id: Union[str, None] = Field(None)

        @staticmethod
        def description():
            return '''
# Request Body
## note_id
- required     

## node
- required 
            '''

    class Delete(BaseModel):
        note_id: Union[str, None] = Field(...)
        domain_id: Union[str, None] = Field(None)

        @staticmethod
        def description():
            return '''
# Request Body
## note_id
- required      
                '''

    class Get(BaseModel):
        note_id: Union[str, None] = Field(...)
        only: Union[list, None] = Field(None)
        domain_id: Union[str, None] = Field(None)

        @staticmethod
        def description():
            return '''
# Request Body
## note_id
- required      
                '''

    class List(BaseModel):
        note_id: Union[str, None] = Field(None)
        state: Union[str, None] = Field(None)
        name: Union[str, None] = Field(None)
        ip_addresses: Union[list, None] = Field(None)
        account: Union[str, None] = Field(None)
        instance_type: Union[str, None] = Field(None)
        cloud_service_type: Union[str, None] = Field(None)
        cloud_service_group: Union[str, None] = Field(None)
        provider: Union[str, None] = Field(None)
        region_code: Union[str, None] = Field(None)
        project_id: Union[str, None] = Field(None)
        project_group_id: Union[str, None] = Field(None)
        resource_group_id: Union[str, None] = Field(None)
        query: Union[dict, None] = Field(None)
        domain_id: Union[str, None] = Field(None)

    class Stat(BaseModel):
        resource_group_id: str = Field(None)
        query: dict = Field(...)
        domain_id: Union[str, None] = Field(None)

        @staticmethod
        def description():
            return '''
# Request Body
## query
- required      
            '''
