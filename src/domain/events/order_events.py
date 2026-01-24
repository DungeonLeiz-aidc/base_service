"""
Order events for Domain-Driven Design.
"""

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import List, Dict, Any


@dataclass(frozen=True)
class OrderPlaced:
    """Event fired when a new order is placed."""
    order_id: int
    customer_id: int
    total_amount: Decimal
    items_count: int
    placed_at: datetime
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "event_type": "order.placed",
            "order_id": self.order_id,
            "customer_id": self.customer_id,
            "total_amount": str(self.total_amount),
            "items_count": self.items_count,
            "placed_at": self.placed_at.isoformat(),
        }


@dataclass(frozen=True)
class OrderConfirmed:
    """Event fired when an order is confirmed."""
    order_id: int
    customer_id: int
    confirmed_at: datetime
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "event_type": "order.confirmed",
            "order_id": self.order_id,
            "customer_id": self.customer_id,
            "confirmed_at": self.confirmed_at.isoformat(),
        }


@dataclass(frozen=True)
class OrderFailed:
    """Event fired when an order fails."""
    order_id: int
    customer_id: int
    reason: str
    failed_at: datetime
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "event_type": "order.failed",
            "order_id": self.order_id,
            "customer_id": self.customer_id,
            "reason": self.reason,
            "failed_at": self.failed_at.isoformat(),
        }


@dataclass(frozen=True)
class OrderCancelled:
    """Event fired when an order is cancelled."""
    order_id: int
    customer_id: int
    cancelled_by: str
    reason: str
    cancelled_at: datetime
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "event_type": "order.cancelled",
            "order_id": self.order_id,
            "customer_id": self.customer_id,
            "cancelled_by": self.cancelled_by,
            "reason": self.reason,
            "cancelled_at": self.cancelled_at.isoformat(),
        }


@dataclass(frozen=True)
class OrderShipped:
    """Event fired when an order is shipped."""
    order_id: int
    customer_id: int
    tracking_number: str
    carrier: str
    shipped_at: datetime
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "event_type": "order.shipped",
            "order_id": self.order_id,
            "customer_id": self.customer_id,
            "tracking_number": self.tracking_number,
            "carrier": self.carrier,
            "shipped_at": self.shipped_at.isoformat(),
        }
