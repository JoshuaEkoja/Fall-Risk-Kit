from constructs import Construct
from .base import BaseStack


class KmsSecretsSsmStack(BaseStack):
    """Central secrets and configuration.

    Key components (AWS): KMS CMKs, Secrets Manager, SSM Parameter Store.
    Purpose: Centralize encryption, secrets, and application parameters.
    """

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.template_options.description = (
            "KMS/Secrets/SSM: central key management, secrets, and parameters"
        )
        # TODO: Define KMS CMKs, Secrets Manager secrets, and SSM parameters.