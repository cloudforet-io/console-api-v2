from pydantic import BaseModel, Field
from typing import List, Any, Union
from datetime import datetime
from enum import Enum


# Base Model


class Viewers(str, Enum):
    public = 'PUBLIC'
    private = 'PRIVATE'


class DomainDashboard(BaseModel):
    domain_dashboard_id: Union[str, None] = Field(None)
    name: Union[str, None] = Field(None)
    viewers: Union[Viewers, None] = Field(None)
    version: Union[int, None] = Field(None)
    layouts: Union[List[Any], None] = Field(None)
    variables: Union[dict, None] = Field(None)
    settings: Union[dict, None] = Field(None)
    variables_schema: Union[dict, None] = Field(None)
    labels: Union[List[str], None] = Field(None)
    tags: Union[dict, None] = Field(None)
    user_id: Union[str, None] = Field(None)
    domain_id: Union[str, None] = Field(None)
    created_at: Union[datetime, None] = Field(None)
    updated_at: Union[datetime, None] = Field(None)


class DomainDashboardVersion(BaseModel):
    domain_dashboard_id: Union[str, None] = Field(None)
    version: Union[int, None] = Field(None)
    latest: Union[bool, None] = Field(None)
    layouts: Union[List[Any], None] = Field(None)
    variables: Union[dict, None] = Field(None)
    settings: Union[dict, None] = Field(None)
    variables_schema: Union[dict, None] = Field(None)
    domain_id: Union[str, None] = Field(None)
    created_at: Union[datetime, None] = Field(None)


class StatInfo(BaseModel):
    results: Union[List[Any], None] = Field(None)
    total_count: Union[List[int], None] = Field(None)


# Domain Dashboard Info model


class DomainDashboardInfo(DomainDashboard):
    class Create(BaseModel):
        name: str = Field(...)
        viewers: Viewers = Field(...)
        layouts: Union[List[Any], None] = Field(None)
        variables: Union[dict, None] = Field(None)
        settings: Union[dict, None] = Field(None)
        variables_schema: Union[dict, None] = Field(None)
        labels: Union[List[str], None] = Field(None)
        tags: Union[dict, None] = Field(None)
        domain_id: str = Field(None)

        @staticmethod
        def description():
            desc = """
# Request Body
## name
- required

## viewers
- required

## domain_id
- required
                """
            return desc

        @staticmethod
        def response():
            responses_example = {
                "200": {
                    "model": DomainDashboardInfo
                }
            }
            return responses_example

    class Update(BaseModel):
        domain_dashboard_id: str = Field(...)
        name: Union[str, None] = Field(None)
        layouts: Union[List[Any], None] = Field(None)
        variables: Union[dict, None] = Field(None)
        settings: Union[dict, None] = Field(None)
        variables_schema: Union[dict, None] = Field(None)
        labels: Union[list, None] = Field(None)
        tags: Union[dict, None] = Field(None)
        domain_id: str = Field(None)

        @staticmethod
        def description():
            desc = """
# Request Body
## domain_dashboard_id
- required

## domain_id
- required
                        """
            return desc

        @staticmethod
        def response():
            responses_example = {
                "200": {
                    "model": DomainDashboardInfo
                }
            }
            return responses_example

    class Delete(BaseModel):
        domain_dashboard_id: str = Field(...)
        domain_id: str = Field(None)

        @staticmethod
        def description():
            desc = """
# Request Body
## domain_dashboard_id
- required

## domain_id
- required
                                """
            return desc

    class Get(BaseModel):
        domain_dashboard_id: str = Field(...)
        only: Union[List[str], None] = Field(None)
        domain_id: str = Field(None)

        @staticmethod
        def description():
            desc = """
# Request Body
## domain_dashboard_id
- required

## domain_id
- required
                                """
            return desc

        @staticmethod
        def response():
            response_example = {
                "200": {
                    "model": DomainDashboardInfo
                }
            }
            return response_example

    class List(BaseModel):
        domain_dashboard_id: Union[str, None] = Field(None)
        name: Union[str, None] = Field(None)
        viewers: Union[Viewers, None] = Field(None)
        user_id: Union[str, None] = Field(None)
        query: Union[dict, None] = Field(None)
        domain_id: str = Field(None)

        @staticmethod
        def description():
            desc = """
# Request Body
## domain_id
- required
                                    """
            return desc

        @staticmethod
        def response():
            response_example = {
                "200": {
                    "model": DomainDashboardInfos
                }
            }
            return response_example


# Domain Dashboard Version Info model
class DomainDashboardVersionInfo(DomainDashboardVersion):
    class DeleteVersion(BaseModel):
        domain_dashboard_id: str = Field(...)
        version: int = Field(...)
        domain_id: str = Field(None)

        @staticmethod
        def description():
            desc = """
# Request Body
## domain_dashboard_id
- required

## version
- required

## domain_id
- required
                """
            return desc

    class RevertVersion(BaseModel):
        domain_dashboard_id: str = Field(...)
        version: int = Field(...)
        domain_id: str = Field(None)

        @staticmethod
        def description():
            desc = """
# Request Body
## domain_dashboard_id
- required

## version
- required

## domain_id
- required
                                            """
            return desc

        @staticmethod
        def response():
            response_example = {
                "200": {
                    "model": DomainDashboardInfo
                }
            }
            return response_example

    class GetVersion(BaseModel):
        domain_dashboard_id: str = Field(...)
        version: int = Field(...)
        only: Union[List[str], None] = Field(None)
        domain_id: str = Field(None)

        @staticmethod
        def description():
            desc = """
# Request Body
## domain_dashboard_id
- required

## version
- required

## domain_id
- required
                                    """
            return desc

        @staticmethod
        def response():
            response_example = {
                "200": {
                    "model": DomainDashboardVersionInfo
                }
            }
            return response_example

    class ListVersions(BaseModel):
        domain_dashboard_id: str = Field(...)
        version: Union[List[int], None] = Field(None)
        query: Union[dict, None] = Field(None)
        domain_id: str = Field(None)

        @staticmethod
        def description():
            desc = """
# Request Body
## domain_dashboard_id
- required

## domain_id
- required
                                    """
            return desc

        @staticmethod
        def response():
            response_example = {
                "200": {
                    "model": DomainDashboardVersionInfos
                }
            }
            return response_example


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


# List Results
class DomainDashboardVersionInfos(BaseModel):
    results: Union[List[DomainDashboardVersionInfo], None] = Field(None)
    total_count: Union[int, None] = Field(None)


class DomainDashboardInfos(BaseModel):
    results: Union[List[DomainDashboardInfo], None] = Field(None)
    total_count: Union[int, None] = Field(None)
