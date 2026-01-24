"""
orders.py

FastAPI routes for Order Management System.
Connects external HTTP requests to internal application services.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from loguru import logger

from src.interface.schemas import PlaceOrderRequest, OrderResponse
from src.application.dtos import PlaceOrderRequestDTO, OrderItemDTO
from src.application.service import PlaceOrderService
from src.domain.exceptions import (
    ProductNotFoundError,
    InsufficientStockError,
    OrderValidationError,
)
from src.dependencies import get_place_order_service, get_auth_payload

router = APIRouter(prefix="/orders", tags=["Orders"])


@router.post(
    "",
    response_model=OrderResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Place a new order",
    description="Creates a new order, reserves inventory in Redis, and persists to PostgreSQL.",
)
async def place_order(
    request: PlaceOrderRequest,
    current_user: dict = Depends(get_auth_payload),
    service: PlaceOrderService = Depends(get_place_order_service),
):
    """
    Endpoint to place a new order.
    
    Orchestrates the process using PlaceOrderService.
    Leverages global exception handlers for domain-specific errors.
    """
    # Map interface schema to application DTO
    dto = PlaceOrderRequestDTO(
        customer_id=request.customer_id,
        items=[
            OrderItemDTO(product_id=item.product_id, quantity=item.quantity)
            for item in request.items
        ]
    )
    
    # Execute use case
    result = await service.execute(dto)
    
    return result
