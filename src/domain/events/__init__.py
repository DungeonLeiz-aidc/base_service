"""
Domain Events for Order Management System.
"""

from .order_events import (
    OrderPlaced,
    OrderConfirmed,
    OrderFailed,
    OrderCancelled,
    OrderShipped,
)

__all__ = [
    "OrderPlaced",
    "OrderConfirmed",
    "OrderFailed",
    "OrderCancelled",
    "OrderShipped",
]
