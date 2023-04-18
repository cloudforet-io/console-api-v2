import abc
import logging

from spaceone.core.manager import BaseManager

_LOGGER = logging.getLogger(__name__)


class ResourceManager(BaseManager):

    @abc.abstractmethod
    def list_fields(self, resource: str, options: dict, limit: int) -> dict:
        raise NotImplementedError('Method not implemented!')

    @abc.abstractmethod
    def list_field_values(self, resource: str, field: str, options: dict, search: str, limit: int) -> dict:
        raise NotImplementedError('Method not implemented!')

    @staticmethod
    def make_response(results: list, limit: int = None) -> dict:
        more = False
        total_count = len(results)

        if limit and limit > 0:
            results = results[:limit]
            if total_count > len(results):
                more = True

        return {
            'results': results,
            'more': more
        }
