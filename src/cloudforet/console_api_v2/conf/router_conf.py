SUB_APP = {
    'identity': {
        'path': '/identity',
        'title': 'Identity HTTP APIs',
        'description': '',
        'contact': ''
    },
    'inventory': {
        'path': '/inventory',
        'title': 'Inventory HTTP APIs',
        'description': '',
        'contact': ''
    },
    'notification': {
        'path': '/notification',
        'title': 'Notification HTTP APIs',
        'description': '',
        'contact': ''
    },
    'repository': {
        'path': '/repository',
        'title': 'Repository HTTP APIs',
        'description': '',
        'contact': ''
    },
    'cost-analysis': {
        'path': '/cost-analysis',
        'title': 'Cost Analysis HTTP APIs',
        'description': '',
        'contact': ''
    },
    'dashboard': {
        'path': '/dashboard',
        'title': 'Dashboard HTTP APIs',
        'description': '',
        'contact': ''
    }
}

ROUTER = [
    {
        'sub_app': 'dashboard',
        'router_path': 'cloudforet.console_api_v2.interface.rest.dashboard.domain_dashboard:router',
        'router_options': {
            'prefix': '/domain-dashboard',
            'tags': ['dashboard > domain-dashboard']
        }
    },
    {
        'sub_app': 'dashboard',
        'router_path': 'cloudforet.console_api_v2.interface.rest.dashboard.project_dashboard:router',
        'router_options': {
            'prefix': '/project-dashboard',
            'tags': ['dashboard > project-dashboard']
        }
    },
    {
        'sub_app': 'dashboard',
        'router_path': 'cloudforet.console_api_v2.interface.rest.dashboard.custom_widget:router',
        'router_options': {
            'prefix': '/custom-widget',
            'tags': ['dashboard > custom-widget'],
        }
    },
    {
        'sub_app': 'identity',
        'router_path': 'cloudforet.console_api_v2.interface.rest.identity.domain:router',
        'router_options': {
            'prefix': '/domain',
            'tags': ['identity > domain']
        }
    },
    {
        'sub_app': 'identity',
        'router_path': 'cloudforet.console_api_v2.interface.rest.identity.domain_owner:router',
        'router_options': {
            'prefix': '/domain-owner',
            'tags': ['identity > domain-owner']
        }
    },
    {
        'sub_app': 'identity',
        'router_path': 'cloudforet.console_api_v2.interface.rest.identity.endpoint:router',
        'router_options': {
            'prefix': '/endpoint',
            'tags': ['identity > endpoint'],
        }
    },
    {
        'sub_app': 'identity',
        'router_path': 'cloudforet.console_api_v2.interface.rest.identity.provider:router',
        'router_options': {
            'prefix': '/provider',
            'tags': ['identity > provider']
        }
    },
    {
        'sub_app': 'identity',
        'router_path': 'cloudforet.console_api_v2.interface.rest.identity.service_account:router',
        'router_options': {
            'prefix': '/service-account',
            'tags': ['identity > service-account']
        }
    },
    {
        'sub_app': 'identity',
        'router_path': 'cloudforet.console_api_v2.interface.rest.identity.project_group:router',
        'router_options': {
            'prefix': '/project-group',
            'tags': ['identity > project-group']
        }
    },
    {
        'sub_app': 'identity',
        'router_path': 'cloudforet.console_api_v2.interface.rest.identity.project:router',
        'router_options': {
            'prefix': '/project',
            'tags': ['identity > project']
        }
    },
    {
        'sub_app': 'identity',
        'router_path': 'cloudforet.console_api_v2.interface.rest.identity.policy:router',
        'router_options': {
            'prefix': '/policy',
            'tags': ['identity > policy']
        }
    },
    {
        'sub_app': 'identity',
        'router_path': 'cloudforet.console_api_v2.interface.rest.identity.role:router',
        'router_options': {
            'prefix': '/role',
            'tags': ['identity > role']
        }
    },
    {
        'sub_app': 'identity',
        'router_path': 'cloudforet.console_api_v2.interface.rest.identity.role_binding:router',
        'router_options': {
            'prefix': '/role-biding',
            'tags': ['identity > role-binding'],
        }
    },
    {
        'sub_app': 'identity',
        'router_path': 'cloudforet.console_api_v2.interface.rest.identity.user:router',
        'router_options': {
            'prefix': '/user',
            'tags': ['identity > user'],
        }
    },
    {
        'sub_app': 'identity',
        'router_path': 'cloudforet.console_api_v2.interface.rest.identity.api_key:router',
        'router_options': {
            'prefix': '/api-key',
            'tags': ['identity > api-key']
        }
    },
    {
        'sub_app': 'identity',
        'router_path': 'cloudforet.console_api_v2.interface.rest.identity.token:router',
        'router_options': {
            'prefix': '/token',
            'tags': ['identity > token']
        }
    },
    {
        'sub_app': 'inventory',
        'router_path': 'cloudforet.console_api_v2.interface.rest.inventory.region:router',
        'router_options': {
            'prefix': '/region',
            'tags': ['inventory > region']
        }
    },
    {
        'sub_app': 'inventory',
        'router_path': 'cloudforet.console_api_v2.interface.rest.inventory.cloud_service_type:router',
        'router_options': {
            'prefix': '/cloud-service-type',
            'tags': ['inventory > cloud-service-type']
        }
    },
    {
        'sub_app': 'inventory',
        'router_path': 'cloudforet.console_api_v2.interface.rest.inventory.cloud_service:router',
        'router_options': {
            'prefix': '/cloud-service',
            'tags': ['inventory > cloud-service']
        }
    },
    {
        'sub_app': 'inventory',
        'router_path': 'cloudforet.console_api_v2.interface.rest.inventory.cloud_service_tag:router',
        'router_options': {
            'prefix': '/cloud-service-tag',
            'tags': ['inventory > cloud-service-tag']
        }
    },
    {
        'sub_app': 'inventory',
        'router_path': 'cloudforet.console_api_v2.interface.rest.inventory.change_history:router',
        'router_options': {
            'prefix': '/change-history',
            'tags': ['inventory > change-history']
        }
    },
    {
        'sub_app': 'inventory',
        'router_path': 'cloudforet.console_api_v2.interface.rest.inventory.note:router',
        'router_options': {
            'prefix': '/note',
            'tags': ['inventory > note']
        }
    },
    {
        'sub_app': 'inventory',
        'router_path': 'cloudforet.console_api_v2.interface.rest.inventory.resource_group:router',
        'router_options': {
            'prefix': '/resource_group',
            'tags': ['inventory > resource_group']
        }
    },
    {
        'sub_app': 'inventory',
        'router_path': 'cloudforet.console_api_v2.interface.rest.inventory.collector:router',
        'router_options': {
            'prefix': '/collector',
            'tags': ['inventory > collector']
        }
    },
    {
        'sub_app': 'inventory',
        'router_path': 'cloudforet.console_api_v2.interface.rest.inventory.job:router',
        'router_options': {
            'prefix': '/job',
            'tags': ['inventory > job']
        }
    },
    {
        'sub_app': 'inventory',
        'router_path': 'cloudforet.console_api_v2.interface.rest.inventory.job_task:router',
        'router_options': {
            'prefix': '/job_task',
            'tags': ['inventory > job-task']
        }
    },
    {
        'sub_app': 'repository',
        'router_path': 'cloudforet.console_api_v2.interface.rest.repository.repository:router',
        'router_options': {
            'prefix': '/repository',
            'tags': ['repository > repository']
        }
    },
    {
        'sub_app': 'repository',
        'router_path': 'cloudforet.console_api_v2.interface.rest.repository.plugin:router',
        'router_options': {
            'prefix': '/plugin',
            'tags': ['repository > plugin']
        }
    },
    {
        'sub_app': 'repository',
        'router_path': 'cloudforet.console_api_v2.interface.rest.repository.schema:router',
        'router_options': {
            'prefix': '/schema',
            'tags': ['repository > schema']
        }
    },
    {
        'sub_app': 'repository',
        'router_path': 'cloudforet.console_api_v2.interface.rest.repository.policy:router',
        'router_options': {
            'prefix': '/policy',
            'tags': ['repository > policy']
        }
    },
    {
        'sub_app': 'notification',
        'router_path': 'cloudforet.console_api_v2.interface.rest.notification.protocol:router',
        'router_options': {
            'prefix': '/protocol',
            'tags': ['notification > protocol']
        }
    },
    {
        'sub_app': 'notification',
        'router_path': 'cloudforet.console_api_v2.interface.rest.notification.quota:router',
        'router_options': {
            'prefix': '/quota',
            'tags': ['notification > quota']
        }
    },
    {
        'sub_app': 'notification',
        'router_path': 'cloudforet.console_api_v2.interface.rest.notification.notification_usage:router',
        'router_options': {
            'prefix': '/notification-usage',
            'tags': ['notification > notification-usage']
        }
    },
    {
        'sub_app': 'notification',
        'router_path': 'cloudforet.console_api_v2.interface.rest.notification.project_channel:router',
        'router_options': {
            'prefix': '/project-channel',
            'tags': ['notification > project-channel']
        }
    },
    {
        'sub_app': 'notification',
        'router_path': 'cloudforet.console_api_v2.interface.rest.notification.user_channel:router',
        'router_options': {
            'prefix': '/user-channel',
            'tags': ['notification > user-channel']
        }
    },
    {
        'sub_app': 'notification',
        'router_path': 'cloudforet.console_api_v2.interface.rest.notification.notification:router',
        'router_options': {
            'prefix': '/notification',
            'tags': ['notification > notification']
        }
    },
    {
        'sub_app': 'cost-analysis',
        'router_path': 'cloudforet.console_api_v2.interface.rest.cost_analysis.data_source:router',
        'router_options': {
            'prefix': '/data-source',
            'tags': ['cost-analysis > data-source'],
        }
    },
    {
        'sub_app': 'cost-analysis',
        'router_path': 'cloudforet.console_api_v2.interface.rest.cost_analysis.exchange_rate:router',
        'router_options': {
            'prefix': '/exchange-rate',
            'tags': ['cost-analysis > exchange-rate'],
        }
    },
    {
        'sub_app': 'cost-analysis',
        'router_path': 'cloudforet.console_api_v2.interface.rest.cost_analysis.cost:router',
        'router_options': {
            'prefix': '/cost',
            'tags': ['cost-analysis > cost'],
        }
    },
    {
        'sub_app': 'cost-analysis',
        'router_path': 'cloudforet.console_api_v2.interface.rest.cost_analysis.data_source_rule:router',
        'router_options': {
            'prefix': '/data-source-rule',
            'tags': ['cost-analysis > data-source-rule'],
        }
    },
    {
        'sub_app': 'cost-analysis',
        'router_path': 'cloudforet.console_api_v2.interface.rest.cost_analysis.budget:router',
        'router_options': {
            'prefix': '/budget',
            'tags': ['cost-analysis > budget'],
        }
    },
    {
        'sub_app': 'cost-analysis',
        'router_path': 'cloudforet.console_api_v2.interface.rest.cost_analysis.budget_usage:router',
        'router_options': {
            'prefix': '/budget-usage',
            'tags': ['cost-analysis > budget-usage'],
        }
    },
    {
        'sub_app': 'cost-analysis',
        'router_path': 'cloudforet.console_api_v2.interface.rest.cost_analysis.public_dashboard:router',
        'router_options': {
            'prefix': '/public-dashboard',
            'tags': ['cost-analysis > public-dashboard'],
        }
    },
    {
        'sub_app': 'cost-analysis',
        'router_path': 'cloudforet.console_api_v2.interface.rest.cost_analysis.user_dashboard:router',
        'router_options': {
            'prefix': '/user-dashboard',
            'tags': ['cost-analysis > user-dashboard'],
        }
    },
    {
        'sub_app': 'cost-analysis',
        'router_path': 'cloudforet.console_api_v2.interface.rest.cost_analysis.cost_query_set:router',
        'router_options': {
            'prefix': '/cost-query-set',
            'tags': ['cost-analysis > cost-query-set']
        }
    },
    {
        'sub_app': 'cost-analysis',
        'router_path': 'cloudforet.console_api_v2.interface.rest.cost_analysis.custom_widget:router',
        'router_options': {
            'prefix': '/custom-widget',
            'tags': ['cost-analysis > custom-widget']
        }
    },
    {
        'sub_app': 'cost-analysis',
        'router_path': 'cloudforet.console_api_v2.interface.rest.cost_analysis.job:router',
        'router_options': {
            'prefix': '/job',
            'tags': ['/cost-analysis > job'],
        }
    },
    {
        'sub_app': 'cost-analysis',
        'router_path': 'cloudforet.console_api_v2.interface.rest.cost_analysis.job_task:router',
        'router_options': {
            'prefix': '/job-task',
            'tags': ['cost-analysis > job-task']
        }
    }
]
