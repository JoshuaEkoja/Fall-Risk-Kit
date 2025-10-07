from constructs import Construct
from .base import BaseStack


class NetworkBaselineStack(BaseStack):
    """Private, secure networking.

    Key components (AWS): VPC, Subnets, NAT, Endpoints, Security Groups.
    Purpose: Standardize network fabric for secure, isolated workloads.
    """

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.template_options.description = (
            "Network baseline: VPC, subnets, NAT, endpoints, and security groups"
        )
        # TODO: Implement VPC with public/private subnets, NAT, and interface/gateway endpoints.
