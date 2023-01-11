ROUTER = [
    {
        'path': 'cloudforet.console_api_v2.interface.rest.dashboard.domain_dashboard:router',
        'prefix': '/dashboard/domain-dashboard',
        'tags': ['dashboard > domain-dashboard']
    },
    {
        'path': 'cloudforet.console_api_v2.interface.rest.dashboard.project_dashboard:router',
        'prefix': '/dashboard/project-dashboard',
        'tags': ['dashboard > project-dashboard']
    },
    {
        'path': 'cloudforet.console_api_v2.interface.rest.dashboard.custom_widget:router',
        'prefix': '/dashboard/custom-widget',
        'tags': ['dashboard > custom-widget'],
    },
    {
        'path': 'cloudforet.console_api_v2.interface.rest.identity.domain:router',
        'prefix': '/identity/domain',
        'tags': ['identity > domain'],
    },
    {
        'path': 'cloudforet.console_api_v2.interface.rest.identity.domain_owner:router',
        'prefix': '/identity/domain-owner',
        'tags': ['identity > domain-owner'],
    },
    {
        'path': 'cloudforet.console_api_v2.interface.rest.identity.endpoint:router',
        'prefix': '/identity/endpoint',
        'tags': ['identity > endpoint'],
    },
    {
        'path': 'cloudforet.console_api_v2.interface.rest.identity.provider:router',
        'prefix': '/identity/provider',
        'tags': ['identity > provider'],
    },
    {
        'path': 'cloudforet.console_api_v2.interface.rest.identity.service_account:router',
        'prefix': '/identity/service-account',
        'tags': ['identity > service-account'],
    },
    {
        'path': 'cloudforet.console_api_v2.interface.rest.identity.project_group:router',
        'prefix': '/identity/project-group',
        'tags': ['identity > project-group'],
    },
    {
        'path': 'cloudforet.console_api_v2.interface.rest.identity.project:router',
        'prefix': '/identity/project',
        'tags': ['identity > project'],
    },
    {
        'path': 'cloudforet.console_api_v2.interface.rest.identity.policy:router',
        'prefix': '/identity/policy',
        'tags': ['identity > policy'],
    },
    {
        'path': 'cloudforet.console_api_v2.interface.rest.identity.role:router',
        'prefix': '/identity/role',
        'tags': ['identity > role'],
    },
    {
        'path': 'cloudforet.console_api_v2.interface.rest.identity.role_binding:router',
        'prefix': '/identity/role-biding',
        'tags': ['identity > role-binding'],
    },
    {
        'path': 'cloudforet.console_api_v2.interface.rest.identity.user:router',
        'prefix': '/identity/user',
        'tags': ['identity > user'],
    },
    {
        'path': 'cloudforet.console_api_v2.interface.rest.identity.api_key:router',
        'prefix': '/identity/api-key',
        'tags': ['identity > api-key']
    },
    {
        'path': 'cloudforet.console_api_v2.interface.rest.identity.token:router',
        'prefix': '/identity/token',
        'tags': ['identity > token']
    },
    {
        'path': 'cloudforet.console_api_v2.interface.rest.inventory.region:router',
        'prefix': '/inventory/region',
        'tags': ['inventory > region']
    },
    {
        'path': 'cloudforet.console_api_v2.interface.rest.inventory.cloud_service_type:router',
        'prefix': '/inventory/cloud-service-type',
        'tags': ['inventory > cloud-service-type']
    },
    {
        'path': 'cloudforet.console_api_v2.interface.rest.inventory.cloud_service:router',
        'prefix': '/inventory/cloud-service',
        'tags': ['inventory > cloud-service']
    },
    {
        'path': 'cloudforet.console_api_v2.interface.rest.inventory.change_history:router',
        'prefix': '/inventory/change-history',
        'tags': ['inventory > change-history']
    },
    {
        'path': 'cloudforet.console_api_v2.interface.rest.inventory.note:router',
        'prefix': '/inventory/note',
        'tags': ['inventory > note']
    },
    {
        'path': 'cloudforet.console_api_v2.interface.rest.inventory.resource_group:router',
        'prefix': '/inventory/resource_group',
        'tags': ['inventory > resource_group']
    },
    {
        'path': 'cloudforet.console_api_v2.interface.rest.inventory.collector:router',
        'prefix': '/inventory/collector',
        'tags': ['inventory > collector']
    },
    {
        'path': 'cloudforet.console_api_v2.interface.rest.inventory.job:router',
        'prefix': '/inventory/job',
        'tags': ['inventory > job']
    },
    {
        'path': 'cloudforet.console_api_v2.interface.rest.inventory.job_task:router',
        'prefix': '/inventory/job_task',
        'tags': ['inventory > job-task']
    },
    {
        'path': 'cloudforet.console_api_v2.interface.rest.repository.repository:router',
        'prefix': '/repository/repository',
        'tags': ['repository > repository']
    },
    {
        'path': 'cloudforet.console_api_v2.interface.rest.repository.plugin:router',
        'prefix': '/repository/plugin',
        'tags': ['repository > plugin']
    },
    {
        'path': 'cloudforet.console_api_v2.interface.rest.repository.schema:router',
        'prefix': '/repository/schema',
        'tags': ['repository > schema']
    },
    {
        'path': 'cloudforet.console_api_v2.interface.rest.repository.policy:router',
        'prefix': '/repository/policy',
        'tags': ['repository > policy']
    },
    {
        'path': 'cloudforet.console_api_v2.interface.rest.notification.protocol:router',
        'prefix': '/notification/protocol',
        'tags': ['notification > protocol']
    },
    {
        'path': 'cloudforet.console_api_v2.interface.rest.notification.quota:router',
        'prefix': '/notification/quota',
        'tags': ['notification > quota']
    },
    {
        'path': 'cloudforet.console_api_v2.interface.rest.notification.notification_usage:router',
        'prefix': '/notification/notification-usage',
        'tags': ['notification > notification-usage']
    },
    {
        'path': 'cloudforet.console_api_v2.interface.rest.notification.project_channel:router',
        'prefix': '/notification/project-channel',
        'tags': ['notification > project-channel']
    },
    {
        'path': 'cloudforet.console_api_v2.interface.rest.notification.user_channel:router',
        'prefix': '/notification/user-channel',
        'tags': ['notification > user-channel']
    },
    {
        'path': 'cloudforet.console_api_v2.interface.rest.notification.notification:router',
        'prefix': '/notification/notification',
        'tags': ['notification > notification']
    },
    {
        'path': 'cloudforet.console_api_v2.interface.rest.cost_analysis.data_source:router',
        'prefix': '/cost-analysis/data-source',
        'tags': ['cost-analysis > data-source'],
    },
    {
        'path': 'cloudforet.console_api_v2.interface.rest.cost_analysis.exchange_rate:router',
        'prefix': '/cost-analysis/exchange-rate',
        'tags': ['cost-analysis > exchange-rate'],
    },
    {
        'path': 'cloudforet.console_api_v2.interface.rest.cost_analysis.cost:router',
        'prefix': '/cost-analysis/cost',
        'tags': ['cost-analysis > cost'],
    },
    {
        'path': 'cloudforet.console_api_v2.interface.rest.cost_analysis.data_source_rule:router',
        'prefix': '/cost-analysis/data-source-rule',
        'tags': ['cost-analysis > data-source-rule'],
    },
    {
        'path': 'cloudforet.console_api_v2.interface.rest.cost_analysis.budget:router',
        'prefix': '/cost-analysis/budget',
        'tags': ['cost-analysis > budget'],
    },
    {
        'path': 'cloudforet.console_api_v2.interface.rest.cost_analysis.budget_usage:router',
        'prefix': '/cost-analysis/budget-usage',
        'tags': ['cost-analysis > budget-usage'],
    },
    {
        'path': 'cloudforet.console_api_v2.interface.rest.cost_analysis.public_dashboard:router',
        'prefix': '/cost-analysis/public-dashboard',
        'tags': ['cost-analysis > public-dashboard'],
    },
    {
        'path': 'cloudforet.console_api_v2.interface.rest.cost_analysis.user_dashboard:router',
        'prefix': '/cost-analysis/user-dashboard',
        'tags': ['cost-analysis > user-dashboard'],
    },
    {
        'path': 'cloudforet.console_api_v2.interface.rest.cost_analysis.cost_query_set:router',
        'prefix': '/cost-analysis/cost-query-set',
        'tags': ['cost-analysis > cost-query-set'],
    },
    {
        'path': 'cloudforet.console_api_v2.interface.rest.cost_analysis.custom_widget:router',
        'prefix': '/cost-analysis/custom-widget',
        'tags': ['cost-analysis > custom-widget'],
    },
    {
        'path': 'cloudforet.console_api_v2.interface.rest.cost_analysis.job:router',
        'prefix': '/cost-analysis/job',
        'tags': ['cost-analysis > job'],
    },
    {
        'path': 'cloudforet.console_api_v2.interface.rest.cost_analysis.job_task:router',
        'prefix': '/cost-analysis/job-task',
        'tags': ['cost-analysis > job-task'],
    }
]
