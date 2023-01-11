
ROUTER = [
    {
        'sub_api': 'dashboard',
        'path': 'cloudforet.console_api_v2.interface.rest.dashboard.domain_dashboard:router',
        'prefix': '/domain-dashboard',
        'tags': ['dashboard > domain-dashboard']
    },
    {
        'sub_api': 'dashboard',
        'path': 'cloudforet.console_api_v2.interface.rest.dashboard.project_dashboard:router',
        'prefix': '/project-dashboard',
        'tags': ['dashboard > project-dashboard']
    },
    {
        'sub_api': 'dashboard',
        'path': 'cloudforet.console_api_v2.interface.rest.dashboard.custom_widget:router',
        'prefix': '/custom-widget',
        'tags': ['dashboard > custom-widget'],
    },
    {
        'sub_api': 'identity',
        'path': 'cloudforet.console_api_v2.interface.rest.identity.domain:router',
        'prefix': '/domain',
        'tags': ['identity > domain'],
    },
    {
        'sub_api': 'identity',
        'path': 'cloudforet.console_api_v2.interface.rest.identity.domain_owner:router',
        'prefix': '/domain-owner',
        'tags': ['identity > domain-owner'],
    },
    {
        'sub_api': 'identity',
        'path': 'cloudforet.console_api_v2.interface.rest.identity.endpoint:router',
        'prefix': '/endpoint',
        'tags': ['identity > endpoint'],
    },
    {
        'sub_api': 'identity',
        'path': 'cloudforet.console_api_v2.interface.rest.identity.provider:router',
        'prefix': '/provider',
        'tags': ['identity > provider'],
    },
    {
        'sub_api': 'identity',
        'path': 'cloudforet.console_api_v2.interface.rest.identity.service_account:router',
        'prefix': '/service-account',
        'tags': ['identity > service-account'],
    },
    {
        'sub_api': 'identity',
        'path': 'cloudforet.console_api_v2.interface.rest.identity.project_group:router',
        'prefix': '/project-group',
        'tags': ['identity > project-group'],
    },
    {
        'sub_api': 'identity',
        'path': 'cloudforet.console_api_v2.interface.rest.identity.project:router',
        'prefix': '/project',
        'tags': ['identity > project'],
    },
    {
        'sub_api': 'identity',
        'path': 'cloudforet.console_api_v2.interface.rest.identity.policy:router',
        'prefix': '/policy',
        'tags': ['identity > policy'],
    },
    {
        'sub_api': 'identity',
        'path': 'cloudforet.console_api_v2.interface.rest.identity.role:router',
        'prefix': '/role',
        'tags': ['identity > role'],
    },
    {
        'sub_api': 'identity',
        'path': 'cloudforet.console_api_v2.interface.rest.identity.role_binding:router',
        'prefix': '/role-biding',
        'tags': ['identity > role-binding'],
    },
    {
        'sub_api': 'identity',
        'path': 'cloudforet.console_api_v2.interface.rest.identity.user:router',
        'prefix': '/user',
        'tags': ['identity > user'],
    },
    {
        'sub_api': 'identity',
        'path': 'cloudforet.console_api_v2.interface.rest.identity.api_key:router',
        'prefix': '/api-key',
        'tags': ['identity > api-key']
    },
    {
        'sub_api': 'identity',
        'path': 'cloudforet.console_api_v2.interface.rest.identity.token:router',
        'prefix': '/token',
        'tags': ['identity > token']
    },
    {
        'sub_api': 'inventory',
        'path': 'cloudforet.console_api_v2.interface.rest.inventory.region:router',
        'prefix': '/region',
        'tags': ['inventory > region']
    },
    {
        'sub_api': 'inventory',
        'path': 'cloudforet.console_api_v2.interface.rest.inventory.cloud_service_type:router',
        'prefix': '/cloud-service-type',
        'tags': ['inventory > cloud-service-type']
    },
    {
        'sub_api': 'inventory',
        'path': 'cloudforet.console_api_v2.interface.rest.inventory.cloud_service:router',
        'prefix': '/cloud-service',
        'tags': ['inventory > cloud-service']
    },
    {
        'sub_api': 'inventory',
        'path': 'cloudforet.console_api_v2.interface.rest.inventory.cloud_service_tag:router',
        'prefix': '/cloud-service-tag',
        'tags': ['inventory > cloud-service-tag']
    },
    {
        'sub_api': 'inventory',
        'path': 'cloudforet.console_api_v2.interface.rest.inventory.change_history:router',
        'prefix': '/change-history',
        'tags': ['inventory > change-history']
    },
    {
        'sub_api': 'inventory',
        'path': 'cloudforet.console_api_v2.interface.rest.inventory.note:router',
        'prefix': '/note',
        'tags': ['inventory > note']
    },
    {
        'sub_api': 'inventory',
        'path': 'cloudforet.console_api_v2.interface.rest.inventory.resource_group:router',
        'prefix': '/resource_group',
        'tags': ['inventory > resource_group']
    },
    {
        'sub_api': 'inventory',
        'path': 'cloudforet.console_api_v2.interface.rest.inventory.collector:router',
        'prefix': '/collector',
        'tags': ['inventory > collector']
    },
    {
        'sub_api': 'inventory',
        'path': 'cloudforet.console_api_v2.interface.rest.inventory.job:router',
        'prefix': '/job',
        'tags': ['inventory > job']
    },
    {
        'sub_api': 'inventory',
        'path': 'cloudforet.console_api_v2.interface.rest.inventory.job_task:router',
        'prefix': '/job_task',
        'tags': ['inventory > job-task']
    },
    {
        'sub_api': 'repository',
        'path': 'cloudforet.console_api_v2.interface.rest.repository.repository:router',
        'prefix': '/repository',
        'tags': ['repository > repository']
    },
    {
        'sub_api': 'repository',
        'path': 'cloudforet.console_api_v2.interface.rest.repository.plugin:router',
        'prefix': '/plugin',
        'tags': ['repository > plugin']
    },
    {
        'sub_api': 'repository',
        'path': 'cloudforet.console_api_v2.interface.rest.repository.schema:router',
        'prefix': '/schema',
        'tags': ['repository > schema']
    },
    {
        'sub_api': 'repository',
        'path': 'cloudforet.console_api_v2.interface.rest.repository.policy:router',
        'prefix': '/policy',
        'tags': ['repository > policy']
    },
    {
        'sub_api': 'notification',
        'path': 'cloudforet.console_api_v2.interface.rest.notification.protocol:router',
        'prefix': '/protocol',
        'tags': ['notification > protocol']
    },
    {
        'sub_api': 'notification',
        'path': 'cloudforet.console_api_v2.interface.rest.notification.quota:router',
        'prefix': '/quota',
        'tags': ['notification > quota']
    },
    {
        'sub_api': 'notification',
        'path': 'cloudforet.console_api_v2.interface.rest.notification.notification_usage:router',
        'prefix': '/notification-usage',
        'tags': ['notification > notification-usage']
    },
    {
        'sub_api': 'notification',
        'path': 'cloudforet.console_api_v2.interface.rest.notification.project_channel:router',
        'prefix': '/project-channel',
        'tags': ['notification > project-channel']
    },
    {
        'sub_api': 'notification',
        'path': 'cloudforet.console_api_v2.interface.rest.notification.user_channel:router',
        'prefix': '/user-channel',
        'tags': ['notification > user-channel']
    },
    {
        'sub_api': 'notification',
        'path': 'cloudforet.console_api_v2.interface.rest.notification.notification:router',
        'prefix': '/notification',
        'tags': ['notification > notification']
    },
    {
        'sub_api': 'cost-analysis',
        'path': 'cloudforet.console_api_v2.interface.rest.cost_analysis.data_source:router',
        'prefix': '/data-source',
        'tags': ['cost-analysis > data-source'],
    },
    {
        'sub_api': 'cost-analysis',
        'path': 'cloudforet.console_api_v2.interface.rest.cost_analysis.exchange_rate:router',
        'prefix': '/exchange-rate',
        'tags': ['cost-analysis > exchange-rate'],
    },
    {
        'sub_api': 'cost-analysis',
        'path': 'cloudforet.console_api_v2.interface.rest.cost_analysis.cost:router',
        'prefix': '/cost',
        'tags': ['cost-analysis > cost'],
    },
    {
        'sub_api': 'cost-analysis',
        'path': 'cloudforet.console_api_v2.interface.rest.cost_analysis.data_source_rule:router',
        'prefix': '/data-source-rule',
        'tags': ['cost-analysis > data-source-rule'],
    },
    {
        'sub_api': 'cost-analysis',
        'path': 'cloudforet.console_api_v2.interface.rest.cost_analysis.budget:router',
        'prefix': '/budget',
        'tags': ['cost-analysis > budget'],
    },
    {
        'sub_api': 'cost-analysis',
        'path': 'cloudforet.console_api_v2.interface.rest.cost_analysis.budget_usage:router',
        'prefix': '/budget-usage',
        'tags': ['cost-analysis > budget-usage'],
    },
    {
        'sub_api': 'cost-analysis',
        'path': 'cloudforet.console_api_v2.interface.rest.cost_analysis.public_dashboard:router',
        'prefix': '/public-dashboard',
        'tags': ['cost-analysis > public-dashboard'],
    },
    {
        'sub_api': 'cost-analysis',
        'path': 'cloudforet.console_api_v2.interface.rest.cost_analysis.user_dashboard:router',
        'prefix': '/user-dashboard',
        'tags': ['cost-analysis > user-dashboard'],
    },
    {
        'sub_api': 'cost-analysis',
        'path': 'cloudforet.console_api_v2.interface.rest.cost_analysis.cost_query_set:router',
        'prefix': '/cost-query-set',
        'tags': ['cost-analysis > cost-query-set'],
    },
    {
        'sub_api': 'cost-analysis',
        'path': 'cloudforet.console_api_v2.interface.rest.cost_analysis.custom_widget:router',
        'prefix': '/custom-widget',
        'tags': ['cost-analysis > custom-widget'],
    },
    {
        'sub_api': 'cost-analysis',
        'path': 'cloudforet.console_api_v2.interface.rest.cost_analysis.job:router',
        'prefix': '/job',
        'tags': ['/cost-analysis > job'],
    },
    {
        'sub_api': 'cost-analysis',
        'path': 'cloudforet.console_api_v2.interface.rest.cost_analysis.job_task:router',
        'prefix': '/job-task',
        'tags': ['cost-analysis > job-task'],
    }
]
