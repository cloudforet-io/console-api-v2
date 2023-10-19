ROUTER = [
    {
        'router_path': 'cloudforet.console_api_v2.interface.rest.api:router',
        'router_options': {
            'prefix': '/console-api/api',
            'tags': ['console-api > api']
        }
    },
    # {
    #     'router_path': 'cloudforet.console_api_v2.interface.rest.resource:router',
    #     'router_options': {
    #         'prefix': '/console-api/resource',
    #         'tags': ['console-api > resource']
    #     }
    # },
    {
        'router_path': 'cloudforet.console_api_v2.interface.rest.swagger:router'
    },
    {
        'router_path': 'cloudforet.console_api_v2.interface.rest.proxy:router',
    }
]


