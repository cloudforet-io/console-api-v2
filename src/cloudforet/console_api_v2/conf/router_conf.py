ROUTER = [
    {
        "router_path": "cloudforet.console_api_v2.interface.rest.api:router",
        "router_options": {
            "prefix": "/console-api/api",
            "tags": ["console-api > api"],
        },
    },
    {
        "router_path": "cloudforet.console_api_v2.interface.rest.extension.auth:router",
        "router_options": {
            "prefix": "/console-api/extension/auth",
            "tags": ["console-api > extension > auth"],
        },
    },
    {
        "router_path": "cloudforet.console_api_v2.interface.rest.extension.agent:router",
        "router_options": {
            "prefix": "/console-api/extension/agent",
            "tags": ["console-api > extension > agent"],
        },
    },
    {
        "router_path": "cloudforet.console_api_v2.interface.rest.swagger:router",
    },
    {
        "router_path": "cloudforet.console_api_v2.interface.rest.proxy:router",
    },
]
