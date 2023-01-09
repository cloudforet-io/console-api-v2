
ROUTER = [
    {
        'sub_api': 'dashboard',
        'path': 'cloudforet.console_api_v2.interface.rest.dashboard.domain_dashboard:router',
        'prefix': '/dashboard/domain-dashboard',
        'tags': ['dashboard > domain-dashboard']
    },
    {
        'sub_api': 'dashboard',
        'path': 'cloudforet.console_api_v2.interface.rest.dashboard.project_dashboard:router',
        'prefix': '/dashboard/project-dashboard',
        'tags': ['dashboard > project-dashboard']
    },
    {
        'sub_api': 'dashboard',
        'path': 'cloudforet.console_api_v2.interface.rest.dashboard.custom_widget:router',
        'prefix': '/dashboard/custom-widget',
        'tags': ['dashboard > custom-widget'],
    },
    {
        'sub_api': 'identity',
        'path': 'cloudforet.console_api_v2.interface.rest.identity.domain:router',
        'prefix': '/identity/domain',
        'tags': ['identity > domain'],
    },
    {
        'sub_api': 'identity',
        'path': 'cloudforet.console_api_v2.interface.rest.identity.domain_owner:router',
        'prefix': '/identity/domain-owner',
        'tags': ['identity > domain-owner'],
    },
    {
        'sub_api': 'identity',
        'path': 'cloudforet.console_api_v2.interface.rest.identity.endpoint:router',
        'prefix': '/identity/endpoint',
        'tags': ['identity > endpoint'],
    },
    {
        'sub_api': 'identity',
        'path': 'cloudforet.console_api_v2.interface.rest.identity.provider:router',
        'prefix': '/identity/provider',
        'tags': ['identity > provider'],
    },
    {
        'sub_api': 'identity',
        'path': 'cloudforet.console_api_v2.interface.rest.identity.service_account:router',
        'prefix': '/identity/service-account',
        'tags': ['identity > service-account'],
    },
    {
        'sub_api': 'identity',
        'path': 'cloudforet.console_api_v2.interface.rest.identity.project_group:router',
        'prefix': '/identity/project-group',
        'tags': ['identity > project-group'],
    },
    {
        'sub_api': 'identity',
        'path': 'cloudforet.console_api_v2.interface.rest.identity.project:router',
        'prefix': '/identity/project',
        'tags': ['identity > project'],
    },
    {
        'sub_api': 'identity',
        'path': 'cloudforet.console_api_v2.interface.rest.identity.policy:router',
        'prefix': '/identity/policy',
        'tags': ['identity > policy'],
    },
    {
        'sub_api': 'identity',
        'path': 'cloudforet.console_api_v2.interface.rest.identity.role:router',
        'prefix': '/identity/role',
        'tags': ['identity > role'],
    },
    {
        'sub_api': 'identity',
        'path': 'cloudforet.console_api_v2.interface.rest.identity.role_binding:router',
        'prefix': '/identity/role-biding',
        'tags': ['identity > role-binding'],
    },
    {
        'sub_api': 'identity',
        'path': 'cloudforet.console_api_v2.interface.rest.identity.user:router',
        'prefix': '/identity/user',
        'tags': ['identity > user'],
    },
    {
        'sub_api': 'identity',
        'path': 'cloudforet.console_api_v2.interface.rest.identity.api_key:router',
        'prefix': '/identity/api-key',
        'tags': ['identity > api-key']
    },
    {
        'sub_api': 'identity',
        'path': 'cloudforet.console_api_v2.interface.rest.identity.token:router',
        'prefix': '/identity/token',
        'tags': ['identity > token']
    },
    {
        'sub_api': 'inventory',
        'path': 'cloudforet.console_api_v2.interface.rest.inventory.region:router',
        'prefix': '/inventory/region',
        'tags': ['inventory > region']
    },
    {
        'sub_api': 'inventory',
        'path': 'cloudforet.console_api_v2.interface.rest.inventory.cloud_service_type:router',
        'prefix': '/inventory/cloud-service-type',
        'tags': ['inventory > cloud-service-type']
    },
    {
        'sub_api': 'inventory',
        'path': 'cloudforet.console_api_v2.interface.rest.inventory.cloud_service:router',
        'prefix': '/inventory/cloud-service',
        'tags': ['inventory > cloud-service']
    },
    {
        'sub_api': 'inventory',
        'path': 'cloudforet.console_api_v2.interface.rest.inventory.cloud_service_tag:router',
        'prefix': '/inventory/cloud-service-tag',
        'tags': ['inventory > cloud-service-tag']
    },
    {
        'sub_api': 'inventory',
        'path': 'cloudforet.console_api_v2.interface.rest.inventory.change_history:router',
        'prefix': '/inventory/change-history',
        'tags': ['inventory > change-history']
    },
    {
        'sub_api': 'inventory',
        'path': 'cloudforet.console_api_v2.interface.rest.inventory.note:router',
        'prefix': '/inventory/note',
        'tags': ['inventory > note']
    },
    {
        'sub_api': 'inventory',
        'path': 'cloudforet.console_api_v2.interface.rest.inventory.resource_group:router',
        'prefix': '/inventory/resource_group',
        'tags': ['inventory > resource_group']
    },
    {
        'sub_api': 'inventory',
        'path': 'cloudforet.console_api_v2.interface.rest.inventory.collector:router',
        'prefix': '/inventory/collector',
        'tags': ['inventory > collector']
    },
    {
        'sub_api': 'inventory',
        'path': 'cloudforet.console_api_v2.interface.rest.inventory.job:router',
        'prefix': '/inventory/job',
        'tags': ['inventory > job']
    },
    {
        'sub_api': 'inventory',
        'path': 'cloudforet.console_api_v2.interface.rest.inventory.job_task:router',
        'prefix': '/inventory/job_task',
        'tags': ['inventory > job-task']
    },
    {
        'sub_api': 'repository',
        'path': 'cloudforet.console_api_v2.interface.rest.repository.repository:router',
        'prefix': '/repository/repository',
        'tags': ['repository > repository']
    },
    {
        'sub_api': 'repository',
        'path': 'cloudforet.console_api_v2.interface.rest.repository.plugin:router',
        'prefix': '/repository/plugin',
        'tags': ['repository > plugin']
    },
    {
        'sub_api': 'repository',
        'path': 'cloudforet.console_api_v2.interface.rest.repository.schema:router',
        'prefix': '/repository/schema',
        'tags': ['repository > schema']
    },
    {
        'sub_api': 'repository',
        'path': 'cloudforet.console_api_v2.interface.rest.repository.policy:router',
        'prefix': '/repository/policy',
        'tags': ['repository > policy']
    },
    {
        'sub_api': 'notification',
        'path': 'cloudforet.console_api_v2.interface.rest.notification.protocol:router',
        'prefix': '/notification/protocol',
        'tags': ['notification > protocol']
    },
    {
        'sub_api': 'notification',
        'path': 'cloudforet.console_api_v2.interface.rest.notification.quota:router',
        'prefix': '/notification/quota',
        'tags': ['notification > quota']
    },
    {
        'sub_api': 'notification',
        'path': 'cloudforet.console_api_v2.interface.rest.notification.notification_usage:router',
        'prefix': '/notification/notification-usage',
        'tags': ['notification > notification-usage']
    },
    {
        'sub_api': 'notification',
        'path': 'cloudforet.console_api_v2.interface.rest.notification.project_channel:router',
        'prefix': '/notification/project-channel',
        'tags': ['notification > project-channel']
    },
    {
        'sub_api': 'notification',
        'path': 'cloudforet.console_api_v2.interface.rest.notification.user_channel:router',
        'prefix': '/notification/user-channel',
        'tags': ['notification > user-channel']
    },
    {
        'sub_api': 'notification',
        'path': 'cloudforet.console_api_v2.interface.rest.notification.notification:router',
        'prefix': '/notification/notification',
        'tags': ['notification > notification']
    },
    {
        'sub_api': 'cost-analysis',
        'path': 'cloudforet.console_api_v2.interface.rest.cost_analysis.data_source:router',
        'prefix': '/cost-analysis/data-source',
        'tags': ['cost-analysis > data-source'],
    },
    {
        'sub_api': 'cost-analysis',
        'path': 'cloudforet.console_api_v2.interface.rest.cost_analysis.exchange_rate:router',
        'prefix': '/cost-analysis/exchange-rate',
        'tags': ['cost-analysis > exchange-rate'],
    },
    {
        'sub_api': 'cost-analysis',
        'path': 'cloudforet.console_api_v2.interface.rest.cost_analysis.cost:router',
        'prefix': '/cost-analysis/cost',
        'tags': ['cost-analysis > cost'],
    },
    {
        'sub_api': 'cost-analysis',
        'path': 'cloudforet.console_api_v2.interface.rest.cost_analysis.data_source_rule:router',
        'prefix': '/cost-analysis/data-source-rule',
        'tags': ['cost-analysis > data-source-rule'],
    },
    {
        'sub_api': 'cost-analysis',
        'path': 'cloudforet.console_api_v2.interface.rest.cost_analysis.budget:router',
        'prefix': '/cost-analysis/budget',
        'tags': ['cost-analysis > budget'],
    },
    {
        'sub_api': 'cost-analysis',
        'path': 'cloudforet.console_api_v2.interface.rest.cost_analysis.budget_usage:router',
        'prefix': '/cost-analysis/budget-usage',
        'tags': ['cost-analysis > budget-usage'],
    },
    {
        'sub_api': 'cost-analysis',
        'path': 'cloudforet.console_api_v2.interface.rest.cost_analysis.public_dashboard:router',
        'prefix': '/cost-analysis/public-dashboard',
        'tags': ['cost-analysis > public-dashboard'],
    },
    {
        'sub_api': 'cost-analysis',
        'path': 'cloudforet.console_api_v2.interface.rest.cost_analysis.user_dashboard:router',
        'prefix': '/cost-analysis/user-dashboard',
        'tags': ['cost-analysis > user-dashboard'],
    },
    {
        'sub_api': 'cost-analysis',
        'path': 'cloudforet.console_api_v2.interface.rest.cost_analysis.cost_query_set:router',
        'prefix': '/cost-analysis/cost-query-set',
        'tags': ['cost-analysis > cost-query-set'],
    },
    {
        'sub_api': 'cost-analysis',
        'path': 'cloudforet.console_api_v2.interface.rest.cost_analysis.custom_widget:router',
        'prefix': '/cost-analysis/custom-widget',
        'tags': ['cost-analysis > custom-widget'],
    },
    {
        'sub_api': 'cost-analysis',
        'path': 'cloudforet.console_api_v2.interface.rest.cost_analysis.job:router',
        'prefix': '/cost-analysis/job',
        'tags': ['cost-analysis > job'],
    },
    {
        'sub_api': 'cost-analysis',
        'path': 'cloudforet.console_api_v2.interface.rest.cost_analysis.job_task:router',
        'prefix': '/cost-analysis/job-task',
        'tags': ['cost-analysis > job-task'],
    }
]
