"""
order.py

Order domain entity and OrderItem value object.
Represents an order with its items and business rules.
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone, timezone
from decimal import Decimal
from enum import Enum
from typing import List, Optional


class OrderStatus(str, Enum):
    """Order status enum."""
    
    PENDING = "pending"  # Order created, waiting for payment
    CONFIRMED = "confirmed"  # Payment confirmed, ready for processing
    PROCESSING = "processing"  # Order is being prepared
    SHIPPED = "shipped"  # Order has been shipped
    DELIVERED = "delivered"  # Order delivered to customer
    CANCELLED = "cancelled"  # Order cancelled
    FAILED = "failed"  # Order failed (payment/stock issues)


@dataclass(frozen=True)
class OrderItem:
    """
    OrderItem value object.
    
    Immutable representation of an item in an order.
    """
    
    product_id: int
    product_sku: str
    product_name: str
    quantity: int
    unit_price: Decimal
    
    def __post_init__(self) -> None:
        """Validate order item invariants."""
        if self.quantity <= 0:
            raise ValueError("Order item quantity must be positive")
        
        if self.unit_price < Decimal("0"):
            raise ValueError("Order item unit price cannot be negative")
    
    @property
    def subtotal(self) -> Decimal:
        """Calculate subtotal for this item (quantity * unit_price)."""
        return self.unit_price * Decimal(self.quantity)


@dataclass
class Order:
    """
    Order domain entity.
    
    Represents a customer order with business rules and state transitions.
    """
    
    id: Optional[int]
    customer_id: int
    items: List[OrderItem]
    status: OrderStatus = OrderStatus.PENDING
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)
    
    def __post_init__(self) -> None:
        """Validate order invariants after initialization."""
        self._validate()
    
    def _validate(self) -> None:
        """
        Validate order business rules.
        
        Raises:
            ValueError: If any business rule is violated.
        """
        if self.customer_id <= 0:
            raise ValueError("Customer ID must be positive")
        
        if not self.items:
            raise ValueError("Order must have at least one item")
        
        if len(self.items) > 50:  # Business rule: max 50 items per order
            raise ValueError("Order cannot have more than 50 items")
    
    @property
    def total_amount(self) -> Decimal:
        """Calculate total amount for the order."""
        return sum(item.subtotal for item in self.items)
    
    @property
    def total_items(self) -> int:
        """Get total number of items in the order."""
        return sum(item.quantity for item in self.items)
    
    def can_transition_to(self, new_status: OrderStatus) -> bool:
        """
        Check if order can transition to new status.
        
        Business rules for status transitions:
        - PENDING -> CONFIRMED, CANCELLED, FAILED
        - CONFIRMED -> PROCESSING, CANCELLED
        - PROCESSING -> SHIPPED, CANCELLED
        - SHIPPED -> DELIVERED
        - DELIVERED, CANCELLED, FAILED -> (no transitions)
        
        Args:
            new_status: Target status.
            
        Returns:
            True if transition is allowed, False otherwise.
        """
        allowed_transitions = {
            OrderStatus.PENDING: {OrderStatus.CONFIRMED, OrderStatus.CANCELLED, OrderStatus.FAILED},
            OrderStatus.CONFIRMED: {OrderStatus.PROCESSING, OrderStatus.CANCELLED},
            OrderStatus.PROCESSING: {OrderStatus.SHIPPED, OrderStatus.CANCELLED},
            OrderStatus.SHIPPED: {OrderStatus.DELIVERED},
            OrderStatus.DELIVERED: set(),
            OrderStatus.CANCELLED: set(),
            OrderStatus.FAILED: set(),
        }
        
        return new_status in allowed_transitions.get(self.status, set())
    
    def confirm(self) -> None:
        """
        Confirm the order (payment successful, stock reserved).
        
        Raises:
            ValueError: If order cannot be confirmed.
        """
        if not self.can_transition_to(OrderStatus.CONFIRMED):
            raise ValueError(
                f"Cannot confirm order with status {self.status.value}"
            )
        
        self.status = OrderStatus.CONFIRMED
        self.updated_at = datetime.now(timezone.utc)
    
    def start_processing(self) -> None:
        """
        Start processing the order (picking, packing).
        
        Raises:
            ValueError: If order cannot be processed.
        """
        if not self.can_transition_to(OrderStatus.PROCESSING):
            raise ValueError(
                f"Cannot process order with status {self.status.value}"
            )
        
        self.status = OrderStatus.PROCESSING
        self.updated_at = datetime.now(timezone.utc)
    
    def ship(self) -> None:
        """
        Mark order as shipped.
        
        Raises:
            ValueError: If order cannot be shipped.
        """
        if not self.can_transition_to(OrderStatus.SHIPPED):
            raise ValueError(
                f"Cannot ship order with status {self.status.value}"
            )
        
        self.status = OrderStatus.SHIPPED
        self.updated_at = datetime.now(timezone.utc)
    
    def deliver(self) -> None:
        """
        Mark order as delivered.
        
        Raises:
            ValueError: If order cannot be delivered.
        """
        if not self.can_transition_to(OrderStatus.DELIVERED):
            raise ValueError(
                f"Cannot deliver order with status {self.status.value}"
            )
        
        self.status = OrderStatus.DELIVERED
        self.updated_at = datetime.now(timezone.utc)
    
    def cancel(self) -> None:
        """
        Cancel the order.
        
        Raises:
            ValueError: If order cannot be cancelled.
        """
        if not self.can_transition_to(OrderStatus.CANCELLED):
            raise ValueError(
                f"Cannot cancel order with status {self.status.value}"
            )
        
        self.status = OrderStatus.CANCELLED
        self.updated_at = datetime.now(timezone.utc)
    
    def mark_as_failed(self) -> None:
        """
        Mark order as failed (payment failed, stock unavailable).
        
        Raises:
            ValueError: If order cannot be marked as failed.
        """
        if not self.can_transition_to(OrderStatus.FAILED):
            raise ValueError(
                f"Cannot fail order with status {self.status.value}"
            )
        
        self.status = OrderStatus.FAILED
        self.updated_at = datetime.now(timezone.utc)
    
    def is_terminal_state(self) -> bool:
        """
        Check if order is in a terminal state (no more transitions possible).
        
        Returns:
            True if order is in DELIVERED, CANCELLED, or FAILED status.
        """
        return self.status in {OrderStatus.DELIVERED, OrderStatus.CANCELLED, OrderStatus.FAILED}
    
    def __repr__(self) -> str:
        """String representation of Order."""
        return (
            f"Order(id={self.id}, customer_id={self.customer_id}, "
            f"items={len(self.items)}, total={self.total_amount}, "
            f"status={self.status.value})"
        )
