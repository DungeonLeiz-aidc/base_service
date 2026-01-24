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
from src.dependencies import get_place_order_service

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
    service: PlaceOrderService = Depends(get_place_order_service),
):
    """
    Endpoint to place a new order.
    
    Orchestrates the process using PlaceOrderService.
    """
    try:
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
        
    except ProductNotFoundError as e:
        logger.warning(f"Order failed: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": str(e), "type": "product_not_found"}]
        )
    except InsufficientStockError as e:
        logger.warning(f"Order failed: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=[{"msg": str(e), "type": "insufficient_stock"}]
        )
    except OrderValidationError as e:
        logger.warning(f"Order failed: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=[{"msg": str(e), "type": "validation_error"}]
        )
    except Exception as e:
        logger.error(f"Unexpected error placing order: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=[{"msg": "An unexpected error occurred while placing the order", "type": "server_error"}]
        )
