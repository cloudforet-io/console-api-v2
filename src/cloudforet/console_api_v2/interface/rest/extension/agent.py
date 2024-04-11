import logging

from fastapi import Request, Depends, Response
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from spaceone.core.fastapi.api import BaseAPI, exception_handler

from cloudforet.console_api_v2.service.agent_service import AgentService

_LOGGER = logging.getLogger(__name__)
_AUTH_SCHEME = HTTPBearer()

router = InferringRouter(include_in_schema=True)


@cbv(router)
class Agent(BaseAPI):
    token: HTTPAuthorizationCredentials = Depends(_AUTH_SCHEME)
    service = "console-api"
    resource = "Agent"

    @router.get("/kubernetes")
    @exception_handler
    async def kubernetes(self, request: Request, service_account_id: str):
        token = self.token.credentials

        agent_service = AgentService()
        params = {"service_account_id": service_account_id, "token": token}
        spaceone_agent = agent_service.kubernetes(params)

        return Response(content=spaceone_agent, media_type="application/x-yaml")
