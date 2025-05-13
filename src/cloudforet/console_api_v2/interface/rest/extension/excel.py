import json
import logging
import inspect
from fastapi import APIRouter, Depends, Request, Query
from fastapi.concurrency import run_in_threadpool
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from starlette.responses import StreamingResponse

from spaceone.core import cache
from spaceone.core.error import ERROR_REQUIRED_PARAMETER, ERROR_CACHE_CONFIGURATION
from spaceone.core.fastapi.api import BaseAPI, exception_handler

from cloudforet.console_api_v2.service.excel_service import ExcelService

_LOGGER = logging.getLogger(__name__)
_AUTH_SCHEME = HTTPBearer(auto_error=False)

router = APIRouter(include_in_schema=True)

SERVICE = "console-api"
RESOURCE = "Excel"


@router.post("/export")
@exception_handler
async def export(
    request: Request, token: HTTPAuthorizationCredentials = Depends(_AUTH_SCHEME)
) -> dict:
    base_api = BaseAPI()
    base_api.service = SERVICE
    verb = inspect.currentframe().f_code.co_name

    if token:
        params, metadata = await base_api.parse_request(
            request, token=token.credentials, resource=RESOURCE, verb=verb
        )
    else:
        params, metadata = await base_api.parse_request(
            request, None, resource=RESOURCE, verb=verb
        )

    excel_service = ExcelService(metadata)

    response = await run_in_threadpool(excel_service.export, params)
    return response


@router.get("/download")
@exception_handler
async def download(key: str = Query(default=None)) -> StreamingResponse:
    base_api = BaseAPI()
    base_api.service = SERVICE

    if not key:
        raise ERROR_REQUIRED_PARAMETER(key="key")

    if not cache.is_set(alias="local"):
        raise ERROR_CACHE_CONFIGURATION(alias="local")

    json_str = cache.get(key=f"console-api:excel:{key}", alias="local")
    json_obj = json.loads(json_str)

    params = json_obj["request_body"]
    metadata = json_obj["auth_info"]

    excel_service = ExcelService(metadata)
    response = await run_in_threadpool(excel_service.download, params)
    return response
