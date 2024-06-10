REST_TITLE = "REST API for Cloudforet"
REST_DESCRIPTION = """
You need to issue api key to use API.
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
| [Identity](/identity/docs) | Identity Service | 
| [Inventory](/inventory/docs) | Inventory Service | 
| [Cost Analysis](/cost-analysis/docs) | Cost Analysis Service |
| [Monitoring](/monitoring/docs) |Monitoring Service | 
| [Notification](/notification/docs) | Notification Service | 
| [Repository](/repository/docs) | Repository Service | 
| [Board](/board/docs) | Board Service | 
| [Config](/config/docs) | Config Service | 
| [Dashboard](/dashboard/docs) | Dashboard Service | 
| [File Manager](/file-manager/docs) | File Manager Service | 
| [Plugin](/plugin/docs) | Plugin Service | 
| [Secret](/secret/docs) | Secret Service | 
| [Statistics](/statistics/docs) | Statistics Service | 
| [Search](/search/docs) | Search Service |
"""

OPENAPI_JSON_DIRS = [
    "/opt/openapi/cloudforet/api/identity/v2/*.json",
    "/opt/openapi/cloudforet/api/inventory/v1/*.json",
    "/opt/openapi/cloudforet/api/cost_analysis/v1/*.json",
    "/opt/openapi/cloudforet/api/monitoring/v1/*.json",
    "/opt/openapi/cloudforet/api/notification/v1/*.json",
    "/opt/openapi/cloudforet/api/repository/v1/*.json",
    "/opt/openapi/cloudforet/api/board/v1/*.json",
    "/opt/openapi/cloudforet/api/config/v1/*.json",
    "/opt/openapi/cloudforet/api/dashboard/v1/*.json",
    "/opt/openapi/cloudforet/api/file_manager/v1/*.json",
    "/opt/openapi/cloudforet/api/plugin/v1/*.json",
    "/opt/openapi/cloudforet/api/secret/v1/*.json",
    "/opt/openapi/cloudforet/api/statistics/v1/*.json",
    "/opt/openapi/cloudforet/api/search/v1/*.json",
]

UVICORN_OPTIONS = {"factory": True}

LOG = {
    "loggers": {"cloudforet": {"level": "DEBUG", "handlers": ["console"]}},
    "filters": {
        "masking": {
            "rules": {"Auth.basic": ["token", "password"], "Proxy.dispatch": ["token"]}
        }
    },
}

# This value is intended for overriding the system token
TOKEN = ""

CONNECTORS = {
    "SpaceConnector": {
        "backend": "spaceone.core.connector.space_connector.SpaceConnector",
        "endpoints": {
            "identity": "grpc://identity:50051/v1",
            "inventory": "grpc://inventory:50051/v1",
            "repository": "grpc://repository:50051/v1",
            "secret": "grpc://secret:50051/v1",
            "plugin": "grpc://plugin:50051/v1",
            "monitoring": "grpc://monitoring:50051/v1",
            "statistics": "grpc://statistics:50051/v1",
            "notification": "grpc://notification:50051/v1",
            "config": "grpc://config:50051/v1",
            "cost_analysis": "grpc://cost-analysis:50051/v1",
            "board": "grpc://board:50051/v1",
            "file_manager": "grpc://file-manager:50051/v1",
            "dashboard": "grpc://dashboard:50051/v1",
            "search": "grpc://search:50051/v1",
        },
    },
}

# OpenCost Settings
OPENCOST_PROMETHEUS_HOST = ""
OPENCOST_PROMETHEUS_EXTERNAL_URL = ""

# SAML Settings
CONSOLE_DOMAIN = ""
CONSOLE_API_V2_ENDPOINT = ""
