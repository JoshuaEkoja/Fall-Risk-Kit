from aws_cdk import (
    Environment,
)
from constructs import Construct
from .base import BaseStack


class CoreFoundationStack(BaseStack):
    """Org bootstrap & security baseline.

    Key components (AWS): IAM, CloudTrail, GuardDuty, org tags.
    Purpose: Establish foundational security, logging, and governance.
    """

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.template_options.description = (
            "Core foundation: IAM/CloudTrail/GuardDuty and org-wide tags for security baseline"
        )
        # TODO: Implement
        # - Organization-wide tagging strategy and Tagging policies
        # - CloudTrail trail (org / multi-region)
        # - GuardDuty detector + auto-enable org configuration
        # - Baseline IAM roles/policies (break-glass, admin, read-only)
