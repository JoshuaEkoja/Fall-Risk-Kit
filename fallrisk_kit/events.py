"""Simple in-process event bus.

The EventBus provides publish/subscribe for pipeline stages using asyncio.
"""
import asyncio
from dataclasses import dataclass
from typing import Any, Callable, Dict, List


@dataclass
class Event:
    """Lightweight event container.

    Attributes:
        type: Event type string (e.g., "frk.telemetry.ingested").
        detail: Event payload.
    """

    type: str
    detail: Dict[str, Any]


class EventBus:
    """An asynchronous in-memory event bus.

    Subscribers register handlers per event type. Published events are queued and
    dispatched to all handlers for the matching type.
    """

    def __init__(self):
        self._subs: Dict[str, List[Callable[[Event], Any]]] = {}
        self._queue: "asyncio.Queue[Event]" = asyncio.Queue()

    def subscribe(self, event_type: str, handler: Callable[[Event], Any]):
        """Subscribe a handler to a given event type.

        Args:
            event_type: The event type string.
            handler: Callable that takes an Event; may be sync or async.
        """
        self._subs.setdefault(event_type, []).append(handler)

    async def publish(self, event: Event):
        """Queue an event for dispatch to subscribers.

        Args:
            event: The event to publish.
        """
        await self._queue.put(event)

    async def run(self):
        """Run the event loop to dispatch queued events to subscribers."""
        while True:
            evt = await self._queue.get()
            for handler in self._subs.get(evt.type, []):
                res = handler(evt)
                if asyncio.iscoroutine(res):
                    await res
            self._queue.task_done()
