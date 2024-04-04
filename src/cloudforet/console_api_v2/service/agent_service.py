import yaml

from cloudforet.console_api_v2.manager.cloudforet_manager import CloudforetManager

from spaceone.core.service import (
    BaseService,
    check_required,
    event_handler,
    transaction,
)
from spaceone.core.error import ERROR_AUTHENTICATE_FAILURE

from cloudforet.console_api_v2.service.auth_service import AuthService


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
        service_account_info = self._get_service_account_info(cloudforet_mgr, params)

        self._validate_token(params["service_account_id"], params["token"])

        params.update(self._validate_and_update_options(service_account_info))
        yaml_config: dict = self._construct_yaml_format(params)

        return yaml.dump(yaml_config, sort_keys=False)

    @staticmethod
    def _get_service_account_info(manager, params: dict) -> dict:
        """Retrieves service account information using the Cloudforet Manager.

        Args:
            manager: The Cloudforet Manager instance used for making API calls.
            params (dict): A dictionary containing 'service_account_id' and 'token'
                           for authentication and identification of the service account.
        Returns:
            dict: The service account information returned from the Cloudforet API.
        """
        return manager.dispatch_api(
            "identity.ServiceAccount.get",
            params={"service_account_id": params["service_account_id"]},
            token=params["token"],
        )

    @staticmethod
    def _validate_token(service_account_id: str, token: str) -> None:
        """Validates the given token against the provided service account ID.

        Args:
            service_account_id (str): The service account ID to validate the token against.
            token (str): The authentication token to be decoded and validated.
        Raises:
            ERROR_AUTHENTICATE_FAILURE: If the decoded token's service account ID does not match the
                                        provided service account ID, indicating an authentication failure.
        """
        decoded_info = AuthService().decode_token(token)
        if service_account_id != decoded_info["injected_params"]["service_account_id"]:
            raise ERROR_AUTHENTICATE_FAILURE(
                message=f"Given service account id {service_account_id} is not matched with {decoded_info['injected_params']['service_account_id']}."
            )

    @staticmethod
    def _validate_and_update_options(service_account_info: dict) -> dict:
        """Validates the presence of required fields in the service account info
        and updates the params dictionary with extracted options.

        Args:
            service_account_info (dict): Dictionary containing the service account info.
        Returns:
            options (dict): Updated options dictionary with keys 'cluster_name',
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

        options = {
            "cluster_name": cluster_name,
            "kube_state_metrics": kube_state_metrics,
            "prometheus_node_exporter": prometheus_node_exporter,
        }

        return options

    @staticmethod
    def _construct_yaml_format(params: dict) -> dict:
        """Constructs a YAML configuration based on service account details
        and Kubernetes service flags.

        Args:
            params (dict): {
                'token' (str): Authentication token,
                'service_account_id' (str): ID of the SpaceONE service account,
                'cluster_name' (str): Name of the cluster,
                'kube_state_metrics' (str): Flag to enable kube-state-metrics ('true' or 'false'),
                'prometheus_node_exporter' (str): Flag to enable prometheus-node-exporter ('true' or 'false'),
           }
        Returns:
            dict: A dictionary representing the YAML configuration.
        """

        token = params.get("token")
        cluster_name = params.get("cluster_name")
        service_account_id = params.get("service_account_id")
        kube_state_metrics = params.get("kube_state_metrics")
        prometheus_node_exporter = params.get("prometheus_node_exporter")

        default_yaml_format = {
            "cluster": {"name": cluster_name},
            "externalServices": {
                "prometheus": {
                    "tenantId": service_account_id,
                    "basicAuth": {
                        "username": service_account_id,
                        "password": token,
                    },
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
