import json
import logging
import os

from fastapi import APIRouter, Request

from spaceone.core import config
from spaceone.core.cache import cacheable


_LOGGER = logging.getLogger(__name__)

router = APIRouter()


def _add_mounted_apis(app, path=None):
    apis = []
    for route in app.routes:
        apis.append({'path': f'{path}{route.path}', 'name': route.name, 'method': route.methods})
    return apis


@cacheable(key='reflection', backend='local')
def _add_apis_from_openapi_json():
    apis = []
    openapi_json_dir = config.get_global('OPENAPI_JSON_DIR')
    openapi_file_name_list = os.listdir(openapi_json_dir)

    for open_api_file_name in openapi_file_name_list:
        with open(f'{openapi_json_dir}/{open_api_file_name}', 'r') as f:
            openapi_json = json.loads(f.read())
            for path, value in openapi_json.get('paths').items():
                if path != 'securitySchemes':
                    name = path.split('/')[-1]
                    method = [next(iter(value))]
                    apis.append({'path': path, 'name': name, 'method': method})
    return apis


@router.get('/reflection')
async def api_reflection(request: Request):
    response = {'apis': []}

    for route in request.app.routes:
        if not hasattr(route, 'methods'):
            response['apis'].append({'path': route.path, 'name': route.name, 'method': []})
            response['apis'].extend(_add_mounted_apis(route.app, route.path))
        elif '/openapi.json' in route.path and len(route.path.split('/')) > 2:
            response['apis'].extend(_add_apis_from_openapi_json())
        else:
            response['apis'].append({'path': route.path, 'name': route.name, 'method': route.methods})
    return response
