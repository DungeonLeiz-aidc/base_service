"""
order_dtos.py

Data Transfer Objects for Order operations.
"""

from dataclasses import dataclass
from decimal import Decimal
from typing import List
from datetime import datetime


@dataclass
class OrderItemDTO:
    """DTO for order item."""
    
    product_id: int
    quantity: int


@dataclass
class PlaceOrderRequestDTO:
    """DTO for placing a new order."""
    
    customer_id: int
    items: List[OrderItemDTO]


@dataclass
class OrderItemResponseDTO:
    """DTO for order item in response."""
    
    product_id: int
    product_sku: str
    product_name: str
    quantity: int
    unit_price: Decimal
    subtotal: Decimal


@dataclass
class OrderResponseDTO:
    """DTO for order response."""
    
    id: int
    customer_id: int
    items: List[OrderItemResponseDTO]
    total_amount: Decimal
    total_items: int
    status: str
    created_at: datetime
    updated_at: datetime
    
    @classmethod
    def from_entity(cls, order):
        """
        Create OrderResponseDTO from Order entity.
        
        Args:
            order: Order entity from domain.
            
        Returns:
            OrderResponseDTO instance.
        """
        return cls(
            id=order.id,
            customer_id=order.customer_id,
            items=[
                OrderItemResponseDTO(
                    product_id=item.product_id,
                    product_sku=item.product_sku,
                    product_name=item.product_name,
                    quantity=item.quantity,
                    unit_price=item.unit_price,
                    subtotal=item.subtotal,
                )
                for item in order.items
            ],
            total_amount=order.total_amount,
            total_items=order.total_items,
            status=order.status.value,
            created_at=order.created_at,
            updated_at=order.updated_at,
        )
