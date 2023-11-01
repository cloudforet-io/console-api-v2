import glob
import json
import logging
import os

from fastapi import APIRouter, Request

from spaceone.core import config
from spaceone.core.cache import cacheable
from spaceone.core.fastapi.api import exception_handler

_LOGGER = logging.getLogger(__name__)

router = APIRouter()


def _add_mounted_apis(app, path=None):
    apis = []
    for route in app.routes:
        apis.append({'path': f'{path}{route.path}', 'name': route.name, 'method': route.methods})
    return apis


def _check_openapi_json_files(openapi_json_files, openapi_json_dir):
    if not openapi_json_files or not os.path.exists(openapi_json_files[0]):
        _LOGGER.info(f'[_check_openapi_json_files] openapi.json not found in {openapi_json_dir}')
        return False
    return True


def _add_apis_from_openapi_json():
    apis = []
    openapi_json_dir_list = config.get_global('OPENAPI_JSON_DIRS')

    for openapi_json_dir in openapi_json_dir_list:
        openapi_json_file_list = glob.glob(os.path.join(openapi_json_dir))

        if _check_openapi_json_files(openapi_json_file_list, openapi_json_dir):
            with open(openapi_json_file_list[0], 'r') as f:
                openapi_json = json.loads(f.read())
                for path, value in openapi_json.get('paths').items():
                    if path != 'securitySchemes':
                        name = path.split('/')[-1]
                        method = [next(iter(value))]
                        apis.append({'path': path, 'name': name, 'method': method})
    return apis


@cacheable(key='api-reflection', alias='local')
def _get_apis(request):
    apis = []
    for route in request.app.routes:
        if not hasattr(route, 'methods'):
            apis.append({'path': route.path, 'name': route.name, 'method': []})
            apis.extend(_add_mounted_apis(route.app, route.path))
        elif '/openapi.json' in route.path and len(route.path.split('/')) > 2:
            apis.extend(_add_apis_from_openapi_json())
        else:
            apis.append({'path': route.path, 'name': route.name, 'method': route.methods})
    return {'apis': apis}


@router.get('/reflection')
@exception_handler
async def api_reflection(request: Request):
    response = _get_apis(request)
    return response
