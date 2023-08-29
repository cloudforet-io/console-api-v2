import json
import logging
from fastapi import APIRouter, Request
from spaceone.core import config


_LOGGER = logging.getLogger(__name__)

router = APIRouter()


def _add_mounted_apis(app, path=None):
    apis = []
    for route in app.routes:
        apis.append({'path': f'{path}{route.path}', 'name': route.name, 'method': route.methods})
    return apis


def _add_apis_from_openapi_json(route):
    apis = []
    extension_swagger_path = config.get_global('EXTENSION_SWAGGER_PATH')
    service_name = route.path.split('/')[1].replace('-', '_')
    with open(f'{extension_swagger_path}/{service_name}_openapi.json', 'r') as f:
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
            response['apis'].extend(_add_apis_from_openapi_json(route))
        else:
            response['apis'].append({'path': route.path, 'name': route.name, 'method': route.methods})
    return response
