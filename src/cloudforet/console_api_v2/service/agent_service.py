import yaml

from cloudforet.console_api_v2.manager.cloudforet_manager import CloudforetManager

from spaceone.core.service import (
    BaseService,
    check_required,
    event_handler,
    transaction,
)


@event_handler
class AgentService(BaseService):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @transaction
    @check_required(["service_account_id", "token"])
    def kubernetes(self, params: dict) -> str:
        """Generates a YAML configuration for the SpaceONE Agent setup based on
        the SpaceONE service account info.

        Args:
            params (dict): {
               'service_account_id' (str): ID of the SpaceONE service account,  # required
               'token' (str): Authentication token,                             # required
           }
        Returns:
            yaml (str): YAML configuration as a string.
        """

        cloudforet_mgr = CloudforetManager()
        service_account_id = params.get("service_account_id")
        token = params.get("token")

        service_account_info = cloudforet_mgr.dispatch_api(
            "identity.ServiceAccount.get",
            params={"service_account_id": service_account_id},
            token=token,
        )
        params.update(self._validate_and_get_options(service_account_info))
        yaml_format: dict = self._construct_yaml_format(params)

        return yaml.dump(yaml_format)

    @staticmethod
    def _validate_and_get_options(service_account_info: dict) -> dict:
        """Validates the presence of required fields in the service account info
        and updates the params dictionary with extracted options.

        Args:
            service_account_info (dict): Dictionary containing the service account info.
        Returns:
            params (dict): Updated params dictionary with keys 'cluster_name',
            'kube_state_metrics', and 'prometheus_node_exporter' {
               'service_account_id' (str): ID of the SpaceONE service account,
               'token' (str): Authentication token,
               'cluster_name' (str): Name of the cluster,
               'kube_state_metrics' (str): Flag to enable kube-state-metrics ('true' or 'false'),
               'prometheus_node_exporter' (str): Flag to enable prometheus-node-exporter ('true' or 'false'),
           }
        Raises:
            Exception: If required fields are missing in the 'options' or
            the 'options' field itself is missing.
        """
        options = service_account_info.get("options")
        if not options:
            raise Exception(
                "The 'options' field is required but was not provided or is empty."
            )

        cluster_name = options.get("cluster_name")
        kube_state_metrics = options.get("kube_state_metrics")
        prometheus_node_exporter = options.get("prometheus_node_exporter")
        if not all([cluster_name, kube_state_metrics, prometheus_node_exporter]):
            missing_fields = []
            if "cluster_name" not in options:
                missing_fields.append("cluster_name")
            if "kube_state_metrics" not in options:
                missing_fields.append("kube_state_metrics")
            if "prometheus_node_exporter" not in options:
                missing_fields.append("prometheus_node_exporter")

            raise Exception(f"Missing required fields: {', '.join(missing_fields)}.")

        params = {
            "cluster_name": cluster_name,
            "kube_state_metrics": kube_state_metrics,
            "prometheus_node_exporter": prometheus_node_exporter,
        }

        return params

    @staticmethod
    def _construct_yaml_format(params: dict) -> dict:
        """Constructs a YAML configuration based on service account details
        and Kubernetes service flags.

        Args:
            params (dict): {
               'service_account_id' (str): ID of the SpaceONE service account,
               'cluster_name' (str): Name of the cluster,
               'kube_state_metrics' (str): Flag to enable kube-state-metrics ('true' or 'false'),
               'prometheus_node_exporter' (str): Flag to enable prometheus-node-exporter ('true' or 'false'),
           }
        Returns:
            dict: A dictionary representing the YAML configuration.
        """

        cluster_name = params.get("cluster_name")
        service_account_id = params.get("service_account_id")
        kube_state_metrics = params.get("kube_state_metrics")
        prometheus_node_exporter = params.get("prometheus_node_exporter")

        default_yaml_format = {
            "cluster": {"name": cluster_name},
            "externalServices": {
                "prometheus": {
                    "tenantId": service_account_id,
                },
                "opencost": {
                    "opencost": {
                        "exporter": {
                            "defaultClusterId": cluster_name,
                            "extraEnv": {
                                "PROMETHEUS_HEADER_X_SCOPE_ORGID": service_account_id
                            },
                        }
                    }
                },
            },
        }

        if kube_state_metrics == "true":
            default_yaml_format["kube-state-metrics"] = {"enabled": "false"}
        if prometheus_node_exporter == "true":
            default_yaml_format["prometheus-node-exporter"] = {"enabled": "false"}

        return default_yaml_format
