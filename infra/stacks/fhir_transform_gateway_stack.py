from constructs import Construct
from .base import BaseStack


class FhirTransformGatewayStack(BaseStack):
    """Translate device telemetry to FHIR resources behind an API gateway.

    Key components (AWS): API Gateway + Lambda.
    Purpose: Interoperability layer to expose FHIR resources to partners.
    """

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.template_options.description = "FHIR transform gateway: API Gateway + Lambda (skeleton)"
        # TODO: Define Lambda function(s) and API Gateway with routes; integrate with Cognito.
