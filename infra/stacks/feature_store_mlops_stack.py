from constructs import Construct
from .base import BaseStack


class FeatureStoreMlopsStack(BaseStack):
    """ML feature governance.

    Key components (AWS): SageMaker Feature Store, Pipelines.
    Purpose: Manage feature definitions/storage for ML training and inference.
    """

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.template_options.description = "Feature Store & MLOps pipelines (skeleton)"
        # TODO: Define Feature Store resources and SageMaker Pipelines.
