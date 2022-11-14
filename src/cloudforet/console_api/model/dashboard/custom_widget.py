from pydantic import BaseModel, Field
from typing import Union, List, Any
from datetime import datetime


# Base Model

class CustomWidget(BaseModel):
    widget_name: Union[str, None] = Field(None)
    title: Union[str, None] = Field(None)
    widget_options: Union[dict, None] = Field(None)
    inherit_options: Union[dict, None] = Field(None)
    labels: Union[List[str], None] = Field(None)
    tags: Union[dict, None] = Field(None)
    user_id: Union[str, None] = Field(None)
    domain_id: Union[str, None] = Field(None)
    created_at: Union[datetime, None] = Field(None)
    updated_at: Union[datetime, None] = Field(None)


class StatInfo(BaseModel):
    results: Union[List[Any], None] = Field(None)
    total_count: Union[List[int], None] = Field(None)


# Custom Widget Info model
class CustomWidgetInfo(CustomWidget):
    class Create(BaseModel):
        widget_name: str = Field(...)
        title: str = Field(...)
        widget_options: dict = Field(...)
        inherit_options: Union[dict, None] = Field(None)
        labels: Union[List[str], None] = Field(None)
        tags: Union[dict, None] = Field(None)
        domain_id: str = Field(...)

    class Update(BaseModel):
        custom_widget_id: str = Field(...)
        title: Union[str, None] = Field(None)
        widget_options: Union[dict, None] = Field(None)
        inherit_options: Union[dict, None] = Field(None)
        labels: Union[List[str], None] = Field(None)
        tags: Union[dict, None] = Field(None)
        domain_id: str = Field(...)

    class Delete(BaseModel):
        custom_widget_id: str = Field(...)
        domain_id: str = Field(...)

    class Get(BaseModel):
        custom_widget_id: str = Field(...)
        only: Union[List[str], None] = Field(None)
        domain_id: str = Field(...)

    class List(BaseModel):
        custom_widget_id: Union[str, None] = Field(None)
        widget_name: Union[str, None] = Field(None)
        title: Union[str, None] = Field(None)
        user_id: Union[str, None] = Field(None)
        query: Union[dict, None] = Field(None)
        domain_id: str = Field(...)


class Stat(BaseModel):
    query: dict = Field(...)
    domain_id: str = Field(...)

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