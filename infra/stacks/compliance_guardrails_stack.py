from constructs import Construct
from .base import BaseStack


class ComplianceGuardrailsStack(BaseStack):
    """Continuous compliance and guardrails.

    Key components (AWS): AWS Config, Security Hub, Macie.
    Purpose: Monitor against standards (HIPAA/CIS), enable remediation and visibility.
    """

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.template_options.description = (
            "Compliance guardrails: AWS Config, Security Hub, Macie"
        )
        # TODO: Enable AWS Config recorders/rules, Security Hub standards, and Macie.
