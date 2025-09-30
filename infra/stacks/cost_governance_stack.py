from constructs import Construct
from .base import BaseStack


class CostGovernanceStack(BaseStack):
    """Cost visibility and governance.

    Key components (AWS): Cost & Usage Reports (CUR), Athena views.
    Purpose: Tag-based cost allocation, reporting, and financial telemetry.
    """

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.template_options.description = (
            "Cost governance: CUR delivery and Athena reporting views"
        )
        # TODO: Configure CUR delivery to S3 and Athena workgroup/views.
