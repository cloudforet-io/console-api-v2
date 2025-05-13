from typing import Union
from pydantic import BaseModel

__all__ = ["ExcelExportRequest"]


class ExcelSource(BaseModel):
    url: Union[str, None] = None
    param: Union[dict, None] = None
    data: Union[dict, list, None] = None


class ExcelTemplate(BaseModel):
    options: Union[dict, None] = None
    fields: Union[list, None] = None


class ExcelExportRequest(BaseModel):
    source: ExcelSource
    template: ExcelTemplate


class ExcelDownloadRequest(BaseModel):
    key: str
