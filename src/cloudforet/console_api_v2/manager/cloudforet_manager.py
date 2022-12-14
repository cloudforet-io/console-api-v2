import logging

from spaceone.core.connector.space_connector import SpaceConnector
from spaceone.core.manager import BaseManager
from cloudforet.console_api_v2.error import *

_LOGGER = logging.getLogger(__name__)


class CloudforetManager(BaseManager):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.connectors = {}

    def get_connector(self, service):
        if service not in self.connectors:
            self.connectors[service] = self.locator.get_connector('SpaceConnector', service=service)

        return self.connectors[service]

    def dispatch_api(self, grpc_method, params):
        service, resource, verb = self._parse_grpc_method(grpc_method)
        connector: SpaceConnector = self.get_connector(service)

        return connector.dispatch(f'{resource}.{verb}', params)

    @staticmethod
    def _parse_grpc_method(grpc_method):
        try:
            service, resource, verb = grpc_method.split('.')
        except Exception as e:
            raise ERROR_PARSE_GRPC_METHOD(grpc_method=grpc_method, reason=e)

        return service, resource, verb
