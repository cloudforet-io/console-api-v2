import logging
from fastapi import Request, Depends, Body
from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from spaceone.core.fastapi.api import BaseAPI, exception_handler
from cloudforet.console_api_v2.service.common.proxy_service import ProxyService
from cloudforet.console_api_v2.model.inventory.cloud_service import *

_LOGGER = logging.getLogger(__name__)
_AUTH_SCHEME = HTTPBearer()

router = InferringRouter()


@cbv(router)
class CloudService(BaseAPI):
    token: HTTPAuthorizationCredentials = Depends(_AUTH_SCHEME)
    service = 'console-api'

    @router.post('/create', openapi_extra=CreateServiceRequest.meta(), response_model=CloudServiceInfo)
    @exception_handler
    async def create(self, request: Request):
        """
        - **cloud_service_type(required)**

        - **provider(required)**

        - **cloud_service_group(required)**

        - **data(required)**

        - **name**

        - **ip_addresses**

        - **account**

        - **instance_type**

        - **instance_size**

        - **metadata**

        - **reference**

        - **tags**

        - **region_code**

        - **project_id**

        - **domain_id**
        """
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'inventory.CloudService.create'
            return proxy_service.dispatch_api(params)

    @router.post('/update', openapi_extra=UpdateCloudServiceRequest.meta(), response_model=CloudServiceInfo)
    @exception_handler
    async def update(self, request: Request):
        """
        # Request Body
        ## cloud_service_id
        - required
        """
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'inventory.CloudService.update'
            return proxy_service.dispatch_api(params)

    @router.post('/get', openapi_extra=GetCloudServiceRequest.meta(), response_model=CloudServiceInfo)
    @exception_handler
    async def get(self, request: Request):
        """
        # Request Body
        ## cloud_service_id
        - required
        """
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'inventory.CloudService.get'
            return proxy_service.dispatch_api(params)

    @router.post('/list', openapi_extra=CloudServiceQuery.meta(), response_model=CloudServicesInfo)
    @exception_handler
    async def list(self, request: Request):
        """
        ## Description
        Gets a list of all CloudServices. You can use a query to get a filtered list of CloudServices.
        <br>

        | Key                     | Description                                                  | Type   | Required |
        |-------------------------|--------------------------------------------------------------|--------|----------|
        | **cloud_service_id**    | Cloud Service id                                             | string |          |
        | **name**                | Name of your resource from CSP                               | string |          |
        | **state**               | Collected state of cloud service by collector                | string |          |
        | **ip_address**          | One of IP addresses the cloud service has                    | string |          |
        | **account**             | Unique ID to identify your account from CSP                  | string |          |
        | **instance_type**       | Cloud service's Instance type                                | string |          |
        | **cloud_service_type**  | Type of your cloud service from CSP like Instance or Database| string |          |
        | **cloud_service_group** | Name of your cloud service from CSP                          | string |          |
        | **provider**            | CSP code like aws, azure and google_cloud                    | string |          |
        | **region_code**         | Unique region code by each CSP                               | string |          |
        | **project_id**          | Project id                                                   | string |          |
        | **project_group_id**    | Project group id                                             | string |          |
        | **resource_group_id**   | Resource group id                                            | string |          |
        | **query**               | Query option for detail search                               | object |          |
        | **domain_id**           | Unique id by each domain (extracted automatically from token)| string |          |
        """
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'inventory.CloudService.list'
            return proxy_service.dispatch_api(params)

    @router.post('/analyze', openapi_extra=CloudServiceAnalyzeQuery.meta())
    @exception_handler
    async def analyze(self, request: Request):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'inventory.CloudService.analyze'
            return proxy_service.dispatch_api(params)

    @router.post('/stat', openapi_extra=CloudServiceStatQuery.meta())
    @exception_handler
    async def stat(self, request: Request):
        """
        # Request Body
        ## query
        - required
        """
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'inventory.CloudService.stat'
            return proxy_service.dispatch_api(params)
