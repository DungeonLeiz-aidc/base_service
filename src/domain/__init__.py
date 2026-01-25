"""
domain/__init__.py

Core Domain layer containing entities, value objects, and business rules.
This layer is the most stable and has no dependencies on other layers.
"""

from src.domain.entities import Product, Order, OrderItem, OrderStatus
from src.domain.events import OrderPlaced, OrderFailed
from src.domain.exceptions import DomainException

__all__ = ["Product", "Order", "OrderItem", "OrderStatus", "OrderPlaced", "OrderFailed", "DomainException"]
