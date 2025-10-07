from aws_cdk import aws_stepfunctions as sfn
from constructs import Construct
from .base import BaseStack


class EtlOrchestrationStack(BaseStack):
    """Batch/mini-batch ETL orchestration.

    Key components (AWS): Step Functions, Lambda (later).
    Purpose: Automate transformations and data quality pipelines.
    """

    def __init__(self, scope: Construct, construct_id: str, *, state_machine_name: str = "frk-etl", **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.template_options.description = (
            "ETL orchestration: Step Functions state machine (placeholder)"
        )
        definition = sfn.Pass(self, "Start").next(sfn.Pass(self, "Done"))
        self.state_machine = sfn.StateMachine(
            self,
            "StateMachine",
            state_machine_name=state_machine_name,
            definition=definition,
        )
        # TODO: Add Lambda tasks, Glue jobs, and error handling with retries/catchers.
