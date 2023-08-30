import logging
import json

from fastapi import Request, Depends
from fastapi_utils.cbv import cbv
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi_utils.inferring_router import InferringRouter
from spaceone.core.fastapi.api import BaseAPI, exception_handler
from spaceone.core import config
from spaceone.core.error import ERROR_UNSUPPORTED_API

from cloudforet.console_api_v2.service.proxy_service import ProxyService

_LOGGER = logging.getLogger(__name__)
_AUTH_SCHEME = HTTPBearer(auto_error=False)

router = InferringRouter(include_in_schema=False)


def _add_mounted_app_paths(app, path=None):
    mounted_app_paths = [f'{path}{route.path}' for route in app.routes if route.method == 'POST']
    return mounted_app_paths


def _add_paths_from_openapi_json(route):
    openapi_paths = []
    extension_swagger_path = config.get_global('EXTENSION_SWAGGER_PATH')
    service_name = route.path.split('/')[1].replace('-', '_')
    with open(f'{extension_swagger_path}/{service_name}_openapi.json', 'r') as f:
        openapi_json = json.loads(f.read())
        for path, value in openapi_json.get('paths').items():
            method = [next(iter(value))]
            if method == ['post']:
                openapi_paths.append(path)
    return openapi_paths


def _path_exists(path, routes):
    paths = []
    
    for route in routes:
        if not hasattr(route, 'methods'):
            paths.extend(_add_mounted_app_paths(route.app, route.path))
        elif '/openapi.json' in route.path and len(route.path.split('/')) > 2:
            paths.extend(_add_paths_from_openapi_json(route))
        else:
            paths.append(route.path)

    if path in paths:
        return True
    return False


def _request_path_validator(request: Request):
    path = request.url.path
    routes = request.app.routes

    if not _path_exists(path, routes):
        raise ERROR_UNSUPPORTED_API(reason=f'method: POST, path: {path}')


def _convert_service_resource_verb(service, resource, verb):
    service = service.lower()
    resource = resource.replace('-', ' ').title().replace(' ', '')
    verb = verb.replace('-', '_').lower()
    return service, resource, verb


@cbv(router)
class Proxy(BaseAPI):
    token: HTTPAuthorizationCredentials = Depends(_AUTH_SCHEME)
    service = 'console-api'

    @router.post('/{service}/{resource}/{verb}')
    @exception_handler
    async def proxy_api(self, request: Request, service, resource, verb):
        _request_path_validator(request)
        service, resource, verb = _convert_service_resource_verb(service, resource, verb)

        if self.token:
            params, metadata = await self.parse_request(request, self.token.credentials, resource, verb)
        else:
            params, metadata = await self.parse_request(request, None, resource, verb)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = f'{service}.{resource}.{verb}'
            return proxy_service.dispatch_api(params)

