from aws_cdk import aws_events as events
from constructs import Construct
from .base import BaseStack


class EventsBusStack(BaseStack):
    """Event-driven backbone.

    Key components (AWS): EventBridge event bus, rules, and schedules.
    Purpose: Central nervous system for event routing and fan-out.
    """

    def __init__(self, scope: Construct, construct_id: str, *, bus_name: str = "frk-bus", **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.template_options.description = (
            "EventBridge bus and scaffolding for rules/schedules"
        )
        self.bus = events.EventBus(self, "EventBus", event_bus_name=bus_name)
        # TODO: Add rules and targets as downstream stacks become available.
