from constructs import Construct
from .base import BaseStack


class FhirHealthlakeStack(BaseStack):
    """FHIR repository and APIs.

    Key components (AWS): Amazon HealthLake datastore.
    Purpose: Host clinical data in FHIR format for secure storage and retrieval.
    """

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.template_options.description = "HealthLake FHIR datastore (skeleton)"
        # TODO: Define HealthLake datastore and access policies.
