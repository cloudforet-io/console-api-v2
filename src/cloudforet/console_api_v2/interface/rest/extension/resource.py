import logging
from fastapi import Request, Depends, Body
from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from spaceone.core.fastapi.api import BaseAPI, exception_handler
from cloudforet.console_api_v2.model.extension.resource import *
from cloudforet.console_api_v2.service.extension.resource_service import ResourceService

_LOGGER = logging.getLogger(__name__)
_AUTH_SCHEME = HTTPBearer()

router = InferringRouter()


@cbv(router)
class Resource(BaseAPI):

    token: HTTPAuthorizationCredentials = Depends(_AUTH_SCHEME)
    service = 'console-api'

    @router.post('/list-fields', openapi_extra=ListFieldsRequest.meta(), response_model=FieldsInfo)
    @exception_handler
    async def list_fields(self, request: Request):
        """
        ## Description
        List fields of API Resource.
        <br>
        | Key               | Description                                                   | Type      | Required|
        |-------------------|---------------------------------------------------------------|-----------|-------|
        |**service**        | Service name (identity, inventory, etc.)                      | string    | True  |
        |**resource**       | Resource name                                                 | string    | True  |
        |**options**        | Additional options for each resource                          | object    |       |
        |**field**          | describe nested fields in specific field                      | string    |       |
        |**limit**          | Set the number of returns                                     | integer   |       |
        """
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ResourceService, metadata) as resource_service:
            return resource_service.list_fields(params)

    @router.post('/list-field-values', openapi_extra=ListFieldValuesRequest.meta(), response_model=ValuesInfo)
    @exception_handler
    async def list_field_values(self, request: Request):
        """
        ## Description
        List values of API resource field
        <br>
        | Key               | Description                                                   | Type      | Required|
        |-------------------|---------------------------------------------------------------|-----------|-------|
        |**service**        | Service name (identity, inventory, etc.)                      | string    | True  |
        |**resource**       | Resource name                                                 | string    | True  |
        |**field**          | field name                                                    | string    | True  |
        |**options**        | Additional options for each resource                          | object    |       |
        |**search**         | search keywords for value                                     | string    |       |
        |**limit**          | Set the number of returns                                     | integer   |       |
        """
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ResourceService, metadata) as resource_service:
            return resource_service.list_field_values(params)
