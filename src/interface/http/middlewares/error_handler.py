"""
error_handler.py

FastAPI global error handler middleware.
Captures exceptions and transforms them into standardized JSON responses.
"""

from fastapi import Request, status
from fastapi.responses import JSONResponse
from loguru import logger

from src.domain.exceptions import (
    ProductNotFoundError,
    InsufficientStockError,
    OrderValidationError,
    DomainException,
)


async def global_exception_handler(request: Request, exc: Exception):
    """
    Global catch-all exception handler.
    Logs the error with AUDIT | prefix and returns a safe 500 response.
    """
    logger.error(f"AUDIT | FAILED | Uncaught exception: {exc}")
    
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "detail": [{"msg": "Internal server error", "type": "server_error"}]
        },
    )


async def domain_exception_handler(request: Request, exc: DomainException):
    """
    Handler for specialized domain exceptions.
    Maps business invariants violations to specific HTTP status codes with AUDIT logging.
    """
    if isinstance(exc, ProductNotFoundError):
        status_code = status.HTTP_404_NOT_FOUND
        error_type = "product_not_found"
    elif isinstance(exc, InsufficientStockError):
        status_code = status.HTTP_400_BAD_REQUEST
        error_type = "insufficient_stock"
    elif isinstance(exc, OrderValidationError):
        status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        error_type = "order_validation_error"
    else:
        status_code = status.HTTP_400_BAD_REQUEST
        error_type = "domain_error"
        
    logger.warning(f"AUDIT | FAILED | Domain invariant violation: {exc} | Type: {error_type}")
    
    return JSONResponse(
        status_code=status_code,
        content={
            "detail": [{"msg": str(exc), "type": error_type}]
        },
    )
