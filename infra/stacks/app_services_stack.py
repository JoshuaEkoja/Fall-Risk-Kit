from constructs import Construct
from .base import BaseStack


class AppServicesStack(BaseStack):
    """Core business services.

    Key components (AWS): Lambda/ECS, DynamoDB, SQS/SNS.
    Purpose: Host core application logic and connect workflows and APIs.
    """

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.template_options.description = "App services: Lambda/ECS, DynamoDB, messaging (skeleton)"
        # TODO: Define compute (Lambda/ECS), DynamoDB tables, and messaging (SQS/SNS) resources.
