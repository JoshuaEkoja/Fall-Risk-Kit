from constructs import Construct
from .base import BaseStack


class WorkflowsStack(BaseStack):
    """Long-running or multi-step workflows.

    Key components (AWS): Step Functions.
    Purpose: Orchestrate human-in-the-loop and complex processes.
    """

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.template_options.description = "Workflows orchestration via Step Functions (skeleton)"
        # TODO: Define long-running state machines and necessary integrations.
