import logging

import yaml
from fastapi import Request, Depends, Response
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from spaceone.core.fastapi.api import BaseAPI, exception_handler

from cloudforet.console_api_v2.service.auth_service import AuthService
from cloudforet.console_api_v2.manager.cloudforet_manager import CloudforetManager

_LOGGER = logging.getLogger(__name__)
_AUTH_SCHEME = HTTPBearer()

router = InferringRouter(include_in_schema=True)


@cbv(router)
class Agent(BaseAPI):
    token: HTTPAuthorizationCredentials = Depends(_AUTH_SCHEME)
    service = "service-account"

    @router.get("/kubernetes")
    @exception_handler
    async def kubernetes(self, request: Request, service_account_id: str):
        token = self.token.credentials
        # spaceone clinet sercret 검증
        auth_service = AuthService()
        auth_service.basic({"username": service_account_id, "password": token})
        # service account id 확인
        cloudforet_mgr = CloudforetManager()
        cloudforet_mgr.dispatch_api(
            "identity.ServiceAccount",
            params={"service_account_id": service_account_id},
            token=token,
        )
        # yaml 파일 혹은 response return
        data = {"service_account_id": service_account_id}
        data = yaml.dump(data)

        return Response(content=data, media_type="application/x-yaml")

    def check_service_account(self, service_account_id):
        pass
