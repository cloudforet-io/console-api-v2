import logging
from fastapi import Request, Depends, Body
from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from spaceone.core.fastapi.api import BaseAPI, exception_handler
from cloudforet.console_api_v2.service.common.proxy_service import ProxyService
from cloudforet.console_api_v2.model.inventory.cloud_service_type import *

_LOGGER = logging.getLogger(__name__)
_AUTH_SCHEME = HTTPBearer()

router = InferringRouter()


@cbv(router)
class CloudServiceType(BaseAPI):
    token: HTTPAuthorizationCredentials = Depends(_AUTH_SCHEME)
    service = 'console-api'

    @router.post('/create', description=CloudServiceTypeInfo.Create.description())
    @exception_handler
    async def create(self, request: Request, body: CloudServiceTypeInfo.Create):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'inventory.CloudServiceType.create'
            return proxy_service.dispatch_api(params)

    @router.post('/update', description=CloudServiceTypeInfo.Update.description())
    @exception_handler
    async def update(self, request: Request, body: CloudServiceTypeInfo.Update):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'inventory.CloudServiceType.update'
            return proxy_service.dispatch_api(params)

    @router.post('/get', description=CloudServiceTypeInfo.Get.description())
    @exception_handler
    async def get(self, request: Request, body: CloudServiceTypeInfo.Get):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'inventory.CloudServiceType.get'
            return proxy_service.dispatch_api(params)

    @router.post('/list', openapi_extra=CloudServiceTypeQuery.meta(), response_model=CloudServiceTypesInfo)
    @exception_handler
    async def list(self, request: Request):
        """
        ## Description
        Gets a list of all CloudServiceTypes. You can use a query to get a filtered list of CloudServiceTypes.
        <br>

        | Key                        | Description                                                   | Type    | Required |
        |----------------------------|---------------------------------------------------------------|---------|----------|
        | **cloud_service_type_id**  | Cloud service type id                                         | string  |          |
        | **name**                   | Type of your cloud service from CSP like Instance or Database | string  |          |
        | **provider**               | CSP code like aws, azure and google_cloud                     | string  |          |
        | **group**                  | Name of your cloud service from CSP                           | string  |          |
        | **cloud_service_type_key** | {provider}.{group}.{name} format value                        | string  |          |
        | **service_code**           | Standard for classify resources by each CSP                   | string  |          |
        | **is_primary**             | Priority value to show resource within group                  | boolean |          |
        | **is_major**               | Priority value to show resource within group                  | boolean |          |
        | **resource_type**          | Standard for classify resources                               | string  |          |
        | **query**                  | Query option for detail search                                | object  |          |
        | **domain_id**              | Unique id by each domain (extracted automatically from token) | string  |          |
        """
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'inventory.CloudServiceType.list'
            return proxy_service.dispatch_api(params)

    @router.post('/stat', description=CloudServiceTypeInfo.Stat.description())
    @exception_handler
    async def stat(self, request: Request, body: CloudServiceTypeInfo.Stat):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'inventory.CloudServiceType.stat'
            return proxy_service.dispatch_api(params)
