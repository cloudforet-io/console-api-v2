REST_TITLE = 'Http API for Cloudforet'
REST_DESCRIPTION = """
You need to issue api key to use Cloudforet API.
<br>
Please read this user [guide](https://cloudforet.io/docs/guides/my-page/access-with-api-cli/) first.

After issuing api key, enter the api key in the [Authorize] button on the right side of the screen.
<br>
<br>
If you're interested in learning more about Cloudforet, please visit our [website](https://cloudforet.io/).
<br>
For a more comprehensive understanding of the Cloudforet API, please visit our [documentation](https://cloudforet-io.github.io/api-doc/).
<br>
<br>
## List of Services \n
[Home](/docs)\n
| **Name** | **Description**  |
|---|---|
| [Identity](/identity/docs) | This is a Identity Service | 
| [Inventory](/inventory/docs) | This is a Inventory Service | 
| [Cost Analysis](/cost-analysis/docs) | This is a Board Service |
| [Monitoring](/monitoring/docs) | This is a Monitoring Service | 
| [Notification](/notification/docs) | This is a Notification Service | 
| [Repository](/repository/docs) | This is a Repository Service | 
| [Board](/board/docs) | This is a Board Service | 
| [Config](/config/docs) | This is a Config Service | 
| [Dashboard](/dashboard/docs) | This is a Dashboard Service | 
| [File Manager](/file-manager/docs) | This is a File Manager Service | 
| [Plugin](/plugin/docs) | This is a Plugin Service | 
| [Secret](/secret/docs) | This is a Secret Service | 
| [Statistics](/statistics/docs) | This is a Statistics Service | 
"""

OPENAPI_JSON_DIR = '/opt/cloudforet/openapi'

UVICORN_OPTIONS = {
    'factory': True
}

LOG = {
    'loggers': {
        'cloudforet': {
            'level': 'DEBUG',
            'handlers': ['console']
        }
    }
}


CONNECTORS = {
    'SpaceConnector': {
        'backend': 'spaceone.core.connector.space_connector.SpaceConnector',
        'endpoints': {
            'identity': 'grpc://identity:50051/v1',
            'inventory': 'grpc://inventory:50051/v1',
            'repository': 'grpc://repository:50051/v1',
            'secret': 'grpc://secret:50051/v1',
            'plugin': 'grpc://plugin:50051/v1',
            'monitoring': 'grpc://monitoring:50051/v1',
            'statistics': 'grpc://statistics:50051/v1',
            'notification': 'grpc://notification:50051/v1',
            'config': 'grpc://config:50051/v1',
            'cost_analysis': 'grpc://cost-analysis:50051/v1',
            'board': 'grpc://board:50051/v1',
            'file_manager': 'grpc://file-manager:50051/v1',
            'dashboard': 'grpc://dashboard:50051/v1',
        }
    },
}
