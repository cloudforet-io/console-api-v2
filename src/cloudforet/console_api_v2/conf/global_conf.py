TITLE = 'Http API for Cloudforet'
DESCRIPTION = """
You need api key for authorization. 

If you want to issue api key, please read this [documentation](https://cloudforet.io/docs/guides/my-page/access-with-api-cli/) first.

<br>
| Service                              | Description                                                     | OpenAPI JSON                            |
|--------------------------------------|-----------------------------------------------------------------|-----------------------------------------|
| [Identity](/identity/docs)           | Manage users, roles, permissions to each project easily.        | [download](/identity/openapi.json)      |
| [Inventory](/inventory/docs)         | Discover and manage multi-cloud resources.                      | [download](/inventory/openapi.json)     |
| [Notification](/notification/docs)   | Notify events and manage incidents automatically.               | [download](/notification/openapi.json)  |
| [Repository](/repository/docs)       | Register and manage your deployable plugins, schema and policy. | [download](/repository/openapi.json)    |
| [Cost-analysis](/cost-analysis/docs) | Analyze your costs easily and optimize resources.               | [download](/cost-analysis/openapi.json) |
| [Dashboard](/dashboard/docs)         | Set and customize your dashboard and widget.                    | [download](/dashboard/openapi.json)     |
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
