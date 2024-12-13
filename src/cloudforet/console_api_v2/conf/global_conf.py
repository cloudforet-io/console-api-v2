REST_TITLE = "REST API for Cloudforet"
REST_DESCRIPTION = """
You need to issue api key to use API.
<br>
Please read this user [guide](https://cloudforet.io/docs/guides/iam/iam-app/) first.

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
| [Inventory v2](/inventory-v2/docs) | Inventory v2 Service |
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
| [Opsflow](/opsflow/docs) | Opsflow Service |
| [Alert Manager](/alert-manager/docs) | Alert Manager Service |
"""

OPENAPI_JSON_DIRS = [
    "/opt/openapi/cloudforet/api/identity/v2/*.json",
    "/opt/openapi/cloudforet/api/inventory/v1/*.json",
    "/opt/openapi/cloudforet/api/inventory_v2/v1/*.json",
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
    "/opt/openapi/cloudforet/api/opsflow/v1/*.json",
    "/opt/openapi/cloudforet/api/alert_manager/v1/*.json",
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

# Cache Settings
CACHES = {
    "default": {},
    "local": {
        "backend": "spaceone.core.cache.local_cache.LocalCache",
        "max_size": 128,
        "ttl": 300,
    },
}

# Handler Settings
HANDLERS = {
    # "authentication": [{
    #     "backend": "cloudforet.console_api_v2.handler.authentication_handler:ConsoleAPIAuthenticationHandler"
    # }],
}

# This value is intended for overriding the system token
TOKEN = ""

CONNECTORS = {
    "SpaceConnector": {
        "backend": "spaceone.core.connector.space_connector.SpaceConnector",
        "endpoints": {
            "identity": "grpc://identity:50051",
            "inventory": "grpc://inventory:50051",
            "inventory_v2": "grpc://inventory-v2:50051",
            "repository": "grpc://repository:50051",
            "secret": "grpc://secret:50051",
            "plugin": "grpc://plugin:50051",
            "monitoring": "grpc://monitoring:50051",
            "statistics": "grpc://statistics:50051",
            "notification": "grpc://notification:50051",
            "config": "grpc://config:50051",
            "cost_analysis": "grpc://cost-analysis:50051",
            "board": "grpc://board:50051",
            "file_manager": "grpc://file-manager:50051",
            "dashboard": "grpc://dashboard:50051",
            "search": "grpc://search:50051",
            "opsflow": "grpc://opsflow:50051",
            "alert_manager": "grpc://alert-manager:50051",
        },
    },
}

# OpenCost Settings
OPENCOST_PROMETHEUS_HOST = ""
OPENCOST_PROMETHEUS_EXTERNAL_URL = ""

# SAML Settings
CONSOLE_DOMAIN = ""
CONSOLE_API_V2_ENDPOINT = ""
