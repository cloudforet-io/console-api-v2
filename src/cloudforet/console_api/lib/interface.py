from fastapi import Request
from spaceone.core.error import *


async def parse_request(request: Request, logger):
    _LOGGER = logger
    try:
        return await request.json()
    except Exception as e:
        _LOGGER.debug(f'JSON Parsing Error: {e}')
        raise ERROR_UNKNOWN(message='JSON Parsing Error: Request body requires JSON format.')