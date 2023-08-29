import logging
from fastapi import Request, Depends
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from spaceone.core.fastapi.api import BaseAPI, exception_handler
from cloudforet.console_api_v2.model.resource import *
from cloudforet.console_api_v2.service.resource_service import ResourceService

_LOGGER = logging.getLogger(__name__)
_AUTH_SCHEME = HTTPBearer()

router = InferringRouter(include_in_schema=True)


@cbv(router)
class Resource(BaseAPI):
    token: HTTPAuthorizationCredentials = Depends(_AUTH_SCHEME)
    service = 'console-api'

    @router.post('/list-fields', openapi_extra=ListFieldsRequest.meta(), response_model=FieldsInfo)
    @exception_handler
    async def list_fields(self, request: Request) -> ValuesInfo:
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ResourceService, metadata) as resource_service:
            return resource_service.list_fields(params)

    @router.post('/list-field-values', openapi_extra=ListFieldValuesRequest.meta(), response_model=ValuesInfo)
    @exception_handler
    async def list_field_values(self, request: Request):
        params, metadata = await self.parse_request(request, self.token.credentials)

        with self.locator.get_service(ResourceService, metadata) as resource_service:
            return resource_service.list_field_values(params)
