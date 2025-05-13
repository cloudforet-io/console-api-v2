import logging
from typing import Tuple, Generator

from spaceone.core.connector.space_connector import SpaceConnector
from spaceone.core.manager import BaseManager
from cloudforet.console_api_v2.error import *

_LOGGER = logging.getLogger(__name__)


class CloudforetManager(BaseManager):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._page_size = 1000

    def dispatch_api(self, grpc_method: str, params: dict, token: str = None):
        service, resource, verb = self._parse_grpc_method(grpc_method)
        space_connector = SpaceConnector(service=service, token=token)
        return space_connector.dispatch(f"{resource}.{verb}", params)

    def paginate_api(
        self, grpc_method: str, params: dict, token: str = None, limit: int = 1000
    ) -> Generator[dict, None, None]:
        start = 1
        paged_params = params.copy()
        while True:
            query = paged_params.get("query", {})
            page_info = query.get("page", {})
            page_info["start"] = start
            page_info["limit"] = max(page_info.get("limit", self._page_size), limit)

            paged_params["query"].update({"page": page_info})

            response = self.dispatch_api(grpc_method, paged_params, token)
            results = response.get("results", [])
            yield response

            if len(results) < page_info["limit"]:
                break

            start += page_info["limit"]

    @staticmethod
    def _parse_grpc_method(grpc_method: str) -> Tuple[str, str, str]:
        try:
            service, resource, verb = grpc_method.split(".")
            return service, resource, verb
        except Exception as e:
            raise ERROR_PARSE_GRPC_METHOD(grpc_method=grpc_method, reason=e)

    @classmethod
    def convert_grpc_method_from_url(cls, url: str) -> str:
        try:
            parts = url.strip("/").split("/")
            print(parts)

            if len(parts) != 3:
                raise ValueError("Path must have at least two segments")

            service = parts[0].replace("-", "_")  # snake_case
            r_source = "".join(
                word.capitalize() for word in parts[1].split("-")
            )  # PascalCase
            verb = parts[2].replace("-", "_")

            return ".".join([service, r_source, verb])
        except Exception as e:
            raise ERROR_PARSE_GRPC_METHOD(grpc_method=url, reason=e)
