import glob
import logging
import json
import os

from fastapi import Request, Depends
from fastapi.concurrency import run_in_threadpool
from fastapi_utils.cbv import cbv
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi_utils.inferring_router import InferringRouter
from spaceone.core.cache import cacheable
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


def _add_paths_from_openapi_json():
    openapi_paths = []
    openapi_json_dirs = config.get_global('OPENAPI_JSON_DIRS')

    for openapi_json_dir in openapi_json_dirs:
        openapi_json_files = glob.glob(os.path.join(openapi_json_dir))
        with open(openapi_json_files[0], 'r') as f:
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
            paths.extend(_add_paths_from_openapi_json())
        else:
            paths.append(route.path)

    if path in paths:
        return True
    return False


@cacheable(key='path:{service}:{resource}:{verb}', alias='local')
def _request_path_validator(service, resource, verb, app):
    routes = app.routes
    path = os.path.join('/', service, resource, verb)

    if not _path_exists(path, routes):
        return False

    return True


def _convert_service_resource_verb(service, resource, verb):
    service = service.replace('-','_').lower()

    if resource == 'api-key':
        resource = 'APIKey'
    else:
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
        if not _request_path_validator(service, resource, verb, request.app):
            raise ERROR_UNSUPPORTED_API(reason=f'method: {request.method}, path: {request.url.path}')

        service, resource, verb = _convert_service_resource_verb(service, resource, verb)

        if self.token:
            params, metadata = await self.parse_request(request, self.token.credentials, resource, verb)
        else:
            params, metadata = await self.parse_request(request, None, resource, verb)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = f'{service}.{resource}.{verb}'
            response = await run_in_threadpool(proxy_service.dispatch_api, params)
            return response
