import logging
import json
import os

from fastapi import APIRouter, Request
from fastapi.openapi.docs import get_swagger_ui_html

from spaceone.core import config
from spaceone.core.cache import cacheable
from cloudforet.console_api_v2.error.swagger import *


_LOGGER = logging.getLogger(__name__)

router = APIRouter(include_in_schema=False)


@cacheable(key='openapi-json:{service}', backend='local')
def _get_openapi_json_data(service):
    openapi_json_dir = config.get_global('OPENAPI_JSON_DIR')
    openapi_json_file_path = f"{openapi_json_dir}/{service.replace('-','_')}_openapi.json"
    if not os.path.exists(openapi_json_file_path):
        raise ERROR_SERVICE_NOT_FOUND(service=service)
    with open(openapi_json_file_path, 'r') as f:
        openapi_json_data = json.loads(f.read())
    return openapi_json_data


@cacheable(key='swagger-ui-html:{service}', backend='local')
def _get_swagger_ui_html(request:Request, service):
    return get_swagger_ui_html(
        openapi_url=f'/{service}/openapi.json',
        title=f'{service.title().replace("-", " ")} API' + ' - Swagger UI',
        oauth2_redirect_url=request.app.swagger_ui_oauth2_redirect_url,
        init_oauth=request.app.swagger_ui_init_oauth,
    )


@router.get('/{service}/docs')
async def docs(request: Request, service: str):
    return _get_swagger_ui_html(request, service)


@router.get('/{service}/openapi.json')
async def openapi_json(service: str):
    return _get_openapi_json_data(service)





