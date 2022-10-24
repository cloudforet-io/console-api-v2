import logging
from functools import wraps
from fastapi import APIRouter, Request, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from spaceone.core.error import *
from spaceone.core.locator import Locator
_LOGGER = logging.getLogger(__name__)

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# todo class화


async def _parse_request(request: Request):
    try:
        return await request.json()
    except Exception as e:
        _LOGGER.debug(f'JSON Parsing Error: {e}')
        raise ERROR_UNKNOWN(message='JSON Parsing Error: Request body requires JSON format.')


@router.post('/widgets')
# @exception_handler
async def create(request: Request, token: str = Depends(oauth2_scheme)):
    params = await _parse_request(request)

    locator = Locator()
    metadata = {
        'token': token,
        'service': 'dashboard',
        'resource': 'ProjectDashboard',
        'verb': 'create'
    }
    with locator.get_service('ProejctDashboardService', metadata) as domain_dashboard_service:
        return domain_dashboard_service.create(params)


@router.put('/widget/{widget_id}')
async def update(request: Request, token: str = Depends(oauth2_scheme)):
    params = await _parse_request(request)

    locator = Locator()
    metadata = {
        'token': token,
        'service': 'dashboard',
        'resource': 'DomainDashboard',
        'verb': 'update'
    }
    with locator.get_service('DomainDashboardService', metadata) as domain_dashboard_service:
        return domain_dashboard_service.create(params)


@router.delete('/widget/{widget_id}')
async def delete(request: Request, token: str = Depends(oauth2_scheme)):
    params = await _parse_request(request)

    locator = Locator()
    metadata = {
        'token': token,
        'service': 'dashboard',
        'resource': 'DomainDashboard',
        'verb': 'update'
    }
    with locator.get_service('DomainDashboardService', metadata) as domain_dashboard_service:
        return domain_dashboard_service.create(params)


@router.get('/widget/{widget_id}')
async def get(request: Request, token: str = Depends(oauth2_scheme)):
    params = await _parse_request(request)

    locator = Locator()
    metadata = {
        'token': token,
        'service': 'dashboard',
        'resource': 'DomainDashboard',
        'verb': 'update'
    }
    with locator.get_service('DomainDashboardService', metadata) as domain_dashboard_service:
        return domain_dashboard_service.create(params)


@router.get('/widgets')
async def list(request: Request, token: str = Depends(oauth2_scheme)):
    params = await _parse_request(request)

    locator = Locator()
    metadata = {
        'token': token,
        'service': 'dashboard',
        'resource': 'DomainDashboard',
        'verb': 'update'
    }
    with locator.get_service('DomainDashboardService', metadata) as domain_dashboard_service:
        return domain_dashboard_service.create(params)


@router.post('/widgets/search')
async def list(request: Request, token: str = Depends(oauth2_scheme)):
    params = await _parse_request(request)

    locator = Locator()
    metadata = {
        'token': token,
        'service': 'dashboard',
        'resource': 'DomainDashboard',
        'verb': 'update'
    }
    with locator.get_service('DomainDashboardService', metadata) as domain_dashboard_service:
        return domain_dashboard_service.create(params)


@router.post('/widgets/stat')
async def list(request: Request, token: str = Depends(oauth2_scheme)):
    params = await _parse_request(request)

    locator = Locator()
    metadata = {
        'token': token,
        'service': 'dashboard',
        'resource': 'DomainDashboard',
        'verb': 'update'
    }
    with locator.get_service('DomainDashboardService', metadata) as domain_dashboard_service:
        return domain_dashboard_service.create(params)