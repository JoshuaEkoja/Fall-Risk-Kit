from aws_cdk import aws_logs as logs
from constructs import Construct
from .base import BaseStack


class ObservabilityStack(BaseStack):
    """End-to-end monitoring and tracing.

    Key components (AWS): CloudWatch Logs/Alarms, X-Ray, Synthetics.
    Purpose: Collect, visualize, and alert on infra and app metrics/traces.
    """

    def __init__(self, scope: Construct, construct_id: str, *, log_group_name: str = "/frk/app", **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.template_options.description = (
            "Observability: CloudWatch logs/alarms, X-Ray, Synthetics"
        )
        # Minimal log group as a starting point
        self.app_logs = logs.LogGroup(
            self,
            "AppLogGroup",
            log_group_name=log_group_name,
            retention=logs.RetentionDays.ONE_MONTH,
        )
        # TODO: Add alarms, dashboards, X-Ray groups, and synthetics canaries.
