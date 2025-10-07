from constructs import Construct
from .base import BaseStack


class CognitoAuthStack(BaseStack):
    """App/user authentication and authorization.

    Key components (AWS): Cognito User Pool and Identity Pool.
    Purpose: Identity management for app users and developers; integrate with APIs.
    """

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.template_options.description = "Cognito auth: User/Identity Pools (skeleton)"
        # TODO: Define Cognito User Pool, app clients, domain, and (optional) Identity Pool.
