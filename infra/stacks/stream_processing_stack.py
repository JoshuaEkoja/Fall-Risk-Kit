from constructs import Construct
from .base import BaseStack


class StreamProcessingStack(BaseStack):
    """Streaming transforms and enrichment.

    Key components (AWS): Kinesis Data Streams/Analytics, Lambda.
    Purpose: Real-time enrichment, aggregation, and anomaly detection.
    """

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.template_options.description = (
            "Stream processing: Kinesis streams/analytics and Lambda (skeleton)"
        )
        # TODO: Define Kinesis streams, analytics applications, and Lambda processors.
