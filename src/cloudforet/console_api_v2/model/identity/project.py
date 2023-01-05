from cloudforet.console_api_v2.model import BaseAPIModel
from pydantic import Field
from typing import Union, List
from datetime import datetime


class CreateProjectRequest(BaseAPIModel):
    pass


class UpdateProjectRequest(BaseAPIModel):
    pass


class ProjectQuery(BaseAPIModel):
    project_id: Union[str, None] = Field(None)
    name: Union[str, None] = Field(None)
    project_group_id: Union[str, None] = Field(None)
    query: Union[dict, None] = Field(None)
    domain_id: Union[str, None] = Field(None)


class ProjectInfo(BaseAPIModel):
    project_id: Union[str, None] = Field(None)
    name: Union[str, None] = Field(None)
    tags: Union[dict, None] = Field(None)
    project_group_info: Union[dict, None] = Field(None)
    domain_id: Union[str, None] = Field(None)
    created_by: Union[str, None] = Field(None)
    created_at: Union[datetime, None] = Field(None)


class ProjectsInfo(BaseAPIModel):
    results: Union[List[ProjectInfo]] = Field(None)
    total_count: Union[int, None] = Field(None)
