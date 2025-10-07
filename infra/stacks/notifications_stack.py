from constructs import Construct
from .base import BaseStack


class NotificationsStack(BaseStack):
    """Alerts and fan-out messaging.

    Key components (AWS): SNS, SQS, Chatbot.
    Purpose: Ensure critical events reach users/systems across channels.
    """

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.template_options.description = "Notifications: SNS topics, SQS queues, Chatbot (skeleton)"
        # TODO: Define SNS topics, SQS queues/subscriptions, and Chatbot integrations.
