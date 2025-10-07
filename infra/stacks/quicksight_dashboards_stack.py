from constructs import Construct
from .base import BaseStack


class QuicksightDashboardsStack(BaseStack):
    """User-facing dashboards.

    Key components (AWS): Amazon QuickSight dashboards.
    Purpose: Visualize operational, financial, and clinical insights.
    """

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.template_options.description = "QuickSight dashboards (skeleton)"
        # TODO: Define QuickSight datasets, analyses, and dashboards (note: CDK support is limited).
