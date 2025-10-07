from constructs import Construct
from .base import BaseStack


class IotIngestionRulesStack(BaseStack):
    """Real-time ingestion via IoT Rules.

    Key components (AWS): IoT Rule routing to Kinesis/Firehose/Lambda.
    Purpose: Capture telemetry and route to streaming/analytics/storage destinations.
    """

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.template_options.description = (
            "IoT ingestion rules: route device telemetry to streaming/storage (skeleton)"
        )
        # TODO: Define IoT TopicRules targeting Firehose -> S3 (cheaper path) or Kinesis -> analytics.
