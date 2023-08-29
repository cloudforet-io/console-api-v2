EXTENSION_SWAGGER_PATH = '/opt/cloudforet/openapi'
TITLE = 'Http API for Cloudforet'
DESCRIPTION = """
You need to issue api key to use Cloudforet API.
<br>
Please read this user [guide](https://cloudforet.io/docs/guides/my-page/access-with-api-cli/) first.

After issuing api key, enter the api key in the [Authorize] button on the right side of the screen.
<br>
<br>
If you're interested in learning more about Cloudforet, please visit our [website](https://cloudforet.io/).
<br>
For a more comprehensive understanding of the Cloudforet API, please visit our [documentation](https://cloudforet-io.github.io/api-doc/).
"""

UVICORN_OPTIONS = {}

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
