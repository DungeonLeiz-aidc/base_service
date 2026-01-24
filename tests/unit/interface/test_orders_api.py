"""
test_orders_api.py

Unit tests for Orders API routes using FastAPI TestClient.
"""

import pytest
from fastapi.testclient import TestClient
from unittest.mock import AsyncMock, patch
from decimal import Decimal
from datetime import datetime, timezone

from src.main import app
from src.dependencies import get_place_order_service, get_session, get_auth_payload
from src.application.dtos import OrderResponseDTO, OrderItemResponseDTO
from src.domain.exceptions import ProductNotFoundError, InsufficientStockError


@pytest.fixture
def mock_service():
    return AsyncMock()


@pytest.fixture
def client(mock_service):
    # Setup dependency overrides
    app.dependency_overrides[get_place_order_service] = lambda: mock_service
    # Also override session to prevent DB connection
    app.dependency_overrides[get_session] = lambda: AsyncMock()
    # Override auth to allow access in unit tests
    app.dependency_overrides[get_auth_payload] = lambda: {"sub": "test-user", "role": "admin"}
    
    yield TestClient(app)
    
    # Clean up overrides
    app.dependency_overrides.clear()


@pytest.mark.asyncio
async def test_place_order_api_success(client, mock_service):
    """Should return 201 when order is placed successfully."""
    # Arrange
    mock_service.execute.return_value = OrderResponseDTO(
        id=123,
        customer_id=1,
        items=[
            OrderItemResponseDTO(
                product_id=1, product_sku="S1", product_name="N1", 
                quantity=2, unit_price=Decimal("10.00"), subtotal=Decimal("20.00")
            )
        ],
        total_amount=Decimal("20.00"),
        total_items=2,
        status="pending",
        created_at=datetime.now(timezone.utc),
        updated_at=datetime.now(timezone.utc)
    )

    # Act
    response = client.post(
        "/api/v1/orders",
        json={
            "customer_id": 1,
            "items": [{"product_id": 1, "quantity": 2}]
        }
    )

    # Assert
    assert response.status_code == 201
    data = response.json()
    assert data["id"] == 123
    assert data["status"] == "pending"
    mock_service.execute.assert_called_once()


@pytest.mark.asyncio
async def test_place_order_api_product_not_found(client, mock_service):
    """Should return 404 when product is not found."""
    mock_service.execute.side_effect = ProductNotFoundError(product_id=999)

    response = client.post(
        "/api/v1/orders",
        json={
            "customer_id": 1,
            "items": [{"product_id": 999, "quantity": 1}]
        }
    )

    assert response.status_code == 404
    assert "not found" in response.json()["detail"][0]["msg"]


@pytest.mark.asyncio
async def test_place_order_api_insufficient_stock(client, mock_service):
    """Should return 400 when stock is insufficient."""
    mock_service.execute.side_effect = InsufficientStockError(product_id=1, requested=100, available=5)

    response = client.post(
        "/api/v1/orders",
        json={
            "customer_id": 1,
            "items": [{"product_id": 1, "quantity": 100}]
        }
    )

    assert response.status_code == 400
    assert "Insufficient stock" in response.json()["detail"][0]["msg"]
