from constructs import Construct
from .base import BaseStack


class InteropApisStack(BaseStack):
    """Partner access APIs.

    Key components (AWS): API Gateway, WAF.
    Purpose: Managed and secure external access to data and workflows.
    """

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.template_options.description = "Interop APIs: API Gateway fronted by WAF (skeleton)"
        # TODO: Define REST/HTTP API, WAF web ACL, throttling, usage plans.
