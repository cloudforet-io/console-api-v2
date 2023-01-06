import logging
from fastapi import Request, Depends, Body
from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from spaceone.core.fastapi.api import BaseAPI, exception_handler
from cloudforet.console_api_v2.service.common.proxy_service import ProxyService
from cloudforet.console_api_v2.model.inventory.region import *

_LOGGER = logging.getLogger(__name__)
_AUTH_SCHEME = HTTPBearer()

router = InferringRouter()


@cbv(router)
class Region(BaseAPI):
    token: HTTPAuthorizationCredentials = Depends(_AUTH_SCHEME)
    service = 'console-api'

    @router.post('/create', openapi_extra=CreateRegionRequest.meta(), response_model=RegionInfo)
    @exception_handler
    async def create(self, request: Request):
        """
        # Request Body
        ## name
        - required

        ## region_code
        - required

        ## provider
        - required

        """
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'inventory.Region.create'
            return proxy_service.dispatch_api(params)

    @router.post('/update', openapi_extra=UpdateRegionRequest.meta(), response_model=RegionInfo)
    @exception_handler
    async def update(self, request: Request):
        """
        # Request Body
        ## region_id
        - required
        """
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'inventory.Region.update'
            return proxy_service.dispatch_api(params)

    @router.post('/delete', openapi_extra=RegionRequest.meta())
    @exception_handler
    async def delete(self, request: Request):
        """
        # Request Body
        ## region_id
        - required
        """
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'inventory.Region.delete'
            return proxy_service.dispatch_api(params)

    @router.post('/get', openapi_extra=GetRegionRequest.meta(), response_model=RegionInfo)
    @exception_handler
    async def get(self, request: Request):
        """
        # Request Body
        ## region_id
        - required
        """
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'inventory.Region.get'
            return proxy_service.dispatch_api(params)

    @router.post('/list', openapi_extra=RegionQuery.meta(), response_model=RegionsInfo)
    @exception_handler
    async def list(self, request: Request):
        """
        ## Description
        Gets a list of all Regions. You can use a query to get a filtered list of Regions.
        <br>
        | Key               | Description                                                  | Type    | Required|
        |-------------------|--------------------------------------------------------------|---------|---------|
        |**region_id**      | Region id                                                    | string  |         |
        |**name**           | Region name                                                  | string  |         |
        |**region_key**     | {provider}.{region_code} format value                        | string  |         |
        |**region_code**    | Unique region code by each CSP                               | string  |         |
        |**provider**       | CSP code like aws, azure and google_cloud                    | string  |         |
        |**query**          | Query option for detail search                               | object  |         |
        |**domain_id**      | Unique id by each domain (extracted automatically from token)| string  |         |
        """
        
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'inventory.Region.list'
            return proxy_service.dispatch_api(params)

    @router.post('/stat', openapi_extra=RegionStatQuery.meta(), response_model=RegionStatInfo)
    @exception_handler
    async def stat(self, request: Request):
        """
        # Request Body
        ## query
        - required
        """
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ProxyService, metadata) as proxy_service:
            params['grpc_method'] = 'inventory.Region.stat'
            return proxy_service.dispatch_api(params)
