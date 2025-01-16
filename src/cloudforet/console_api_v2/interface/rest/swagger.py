import logging
import glob
import json
import os

from fastapi import APIRouter, Request, FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.responses import FileResponse

from spaceone.core import config
from spaceone.core.cache import cacheable
from spaceone.core.fastapi.api import exception_handler
from cloudforet.console_api_v2.error.swagger import *

_LOGGER = logging.getLogger(__name__)

app = FastAPI()
router = APIRouter(include_in_schema=False)

SWAGGER_UI_PATH = os.path.join(os.path.dirname(__file__), f"../../static")


@cacheable(key='openapi-json:{service}', alias='local')
def _get_openapi_json_data(service):
    openapi_json_dirs = config.get_global('OPENAPI_JSON_DIRS', [])

    for openapi_json_dir in openapi_json_dirs:
        openapi_json_files = glob.glob(os.path.join(openapi_json_dir))
        for openapi_json_file in openapi_json_files:
            if service.replace('-', '_') in openapi_json_file:
                if not os.path.exists(openapi_json_file):
                    break
                with open(openapi_json_file, 'r') as f:
                    return json.loads(f.read())
    _LOGGER.error(f'[_get_openapi_json_data] in this dirs {openapi_json_dirs} openapi.json not found for {service}')
    raise ERROR_NOT_FOUND(key=service, value='openapi.json')


@cacheable(key='swagger-ui-html:{service}', alias='local')
def _get_swagger_ui_html(request: Request, service):
    return get_swagger_ui_html(
        openapi_url=f'/{service}/openapi.json',
        title=f'{service.title().replace("-", " ")} API' + ' - Swagger UI',
        oauth2_redirect_url=request.app.swagger_ui_oauth2_redirect_url,
        init_oauth=request.app.swagger_ui_init_oauth,
        swagger_css_url="/static/swagger_ui.css",
        swagger_js_url="/static/swagger_ui_bundle.js",
        swagger_favicon_url="/static/favicon.png",
    )


def _get_swagger_ui_files(filename):
    file_path = os.path.join(SWAGGER_UI_PATH, filename)
    if os.path.exists(file_path):
        return FileResponse(file_path)
    _LOGGER.error(f'Swagger UI file not found {filename}')
    raise ERROR_NOT_FOUND(key='file', value=filename)


@router.get('/{service}/docs')
@exception_handler
async def docs(request: Request, service: str):
    return _get_swagger_ui_html(request, service)


@router.get('/{service}/openapi.json')
@exception_handler
async def openapi_json(service: str):
    return _get_openapi_json_data(service)


@router.get("/static/{filename:path}")
async def swagger_ui(filename: str):
    return _get_swagger_ui_files(filename)
