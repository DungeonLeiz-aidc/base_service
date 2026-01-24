"""
schemas.py

Pydantic schemas for external API request/response validation.
Defines the external contract for the Order Management System.
"""

from datetime import datetime
from decimal import Decimal
from typing import List, Optional
from pydantic import BaseModel, Field, ConfigDict


class OrderItemRequest(BaseModel):
    """Schema for an item in a place order request."""
    
    product_id: int = Field(..., gt=0, description="The ID of the product")
    quantity: int = Field(..., gt=0, description="Quantity to purchase")


class PlaceOrderRequest(BaseModel):
    """Schema for placing a new order."""
    
    customer_id: int = Field(..., gt=0, description="The ID of the customer placing the order")
    items: List[OrderItemRequest] = Field(..., min_length=1, max_length=50, description="List of items in the order")


class OrderItemResponse(BaseModel):
    """Schema for an item in an order response."""
    
    product_id: int
    product_sku: str
    product_name: str
    quantity: int
    unit_price: Decimal
    subtotal: Decimal
    
    model_config = ConfigDict(from_attributes=True)


class OrderResponse(BaseModel):
    """Schema for order response."""
    
    id: int
    customer_id: int
    items: List[OrderItemResponse]
    total_amount: Decimal
    total_items: int
    status: str
    created_at: datetime
    updated_at: datetime
    
    model_config = ConfigDict(from_attributes=True)


class ProductResponse(BaseModel):
    """Schema for product response."""
    
    id: int
    sku: str
    name: str
    description: str
    price: Decimal
    stock_quantity: int
    
    model_config = ConfigDict(from_attributes=True)


class ErrorDetail(BaseModel):
    """Schema for error details."""
    
    msg: str
    type: str
    loc: Optional[List[str]] = None


class ErrorResponse(BaseModel):
    """General error response schema."""
    
    detail: List[ErrorDetail]
