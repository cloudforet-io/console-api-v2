from pydantic import BaseModel, Field
from typing import List, Dict, Union, Any
from datetime import datetime
from enum import Enum

# Base Model


class Viewers(str, Enum):
    public = 'PUBLIC'
    private = 'PRIVATE'


class ProjectDashboard(BaseModel):
    project_dashboard_id: Union[str, None] = Field(None)
    project_id: Union[str, None] = Field(None)
    name: Union[str, None] = Field(None)
    viewers: Union[Viewers, None] = Field(None)
    version: Union[int, None] = Field(None)
    layouts: Union[List[Any], None] = Field(None)
    variables_schema: Union[dict, None] = Field(None)
    settings: Union[dict, None] = Field(None)
    labels: Union[List[str], None] = Field(None)
    tags: Union[dict, None] = Field(None)
    user_id: Union[str, None] = Field(None)
    domain_id: Union[str, None] = Field(None)
    created_at: Union[datetime, None] = Field(None)
    updated_at: Union[datetime, None] = Field(None)


class ProjectDashboardVersion(BaseModel):
    project_dashboard_id: Union[str, None] = Field(None)
    version: Union[int, None] = Field(None)
    layouts: Union[List[Any], None] = Field(None)
    variables: Union[dict, None] = Field(None)
    settings: Union[dict, None] = Field(None)
    variables_schema: Union[dict, None] = Field(None)
    domain_id: Union[str, None] = Field(None)
    create_at: Union[datetime, None] = Field(None)


class StatInfo(BaseModel):
    results: Union[List[Any], None] = Field(None)
    total_count: Union[List[int], None] = Field(None)


# Project Dashboard Info model

class ProjectDashboardInfo(ProjectDashboard):
    class Create(BaseModel):
        project_id: str = Field(...)
        name: str = Field(...)
        viewers: Viewers = Field(...)
        layout: Union[List[dict], None] = Field(None)
        variables: Union[dict, None] = Field(None)
        settings: Union[dict, None] = Field(None)
        variables_schema: Union[dict, None] = Field(None)
        labels: Union[List[str], None] = Field(None)
        tags: Union[dict, None] = Field(None)
        domain_id: str = Field(None)

    class Update(BaseModel):
        project_dashboard_id: str = Field(...)
        name: Union[str, None] = Field(None)
        layout: Union[List[dict], None] = Field(None)
        variables: Union[dict, None] = Field(None)
        settings: Union[dict, None] = Field(None)
        variables_schema: Union[dict, None] = Field(None)
        labels: Union[List[str], None] = Field(None)
        tags: Union[dict, None] = Field(None)
        domain_id: str = Field(None)

    class Delete(BaseModel):
        project_dashboard_id: str = Field(...)
        domain_id: str = Field(None)

    class Get(BaseModel):
        project_dashboard_id: str = Field(...)
        only: Union[List[str], None] = Field(None)
        domain_id: str = Field(None)

    class List(BaseModel):
        project_dashboard_id: Union[str, None] = Field(None)
        project_id: Union[str, None] = Field(None)
        name: Union[str, None] = Field(None)
        viewers: Union[Viewers, None] = Field(None)
        user_id: Union[str, None] = Field(None)
        query: Union[dict, None] = Field(None)
        domain_id: str = Field(None)


class ProjectDashboardVersionInfo(ProjectDashboardVersion):
    class DeleteVersion(BaseModel):
        project_dashboard_id: str = Field(...)
        version: int = Field(...)
        domain_id: str = Field(None)

    class RevertVersion(BaseModel):
        project_dashboard_id: str = Field(...)
        version: int = Field(...)
        domain_id: str = Field(None)

    class GetVersion(BaseModel):
        project_dashboard_id: str = Field(...)
        version: int = Field(...)
        domain_id: str = Field(None)

    class ListVersions(BaseModel):
        project_dashboard_id: str = Field(...)
        version: Union[int, None] = Field(None)
        query: Union[dict, None] = Field(None)
        domain_id: str = Field(None)


class Stat(BaseModel):
    query: dict = Field(...)
    domain_id: str = Field(None)

    @staticmethod
    def description():
        desc = """
# Request Body
## query
- required

## domain_id
- required
                                        """
        return desc

    @staticmethod
    def response():
        response_example = {
            "200": {
                "model": StatInfo
            }
        }
        return response_example
