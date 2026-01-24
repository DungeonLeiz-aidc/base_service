"""
test_order_service.py

Unit tests for PlaceOrderService.
"""

import pytest
from unittest.mock import AsyncMock, MagicMock
from decimal import Decimal
from datetime import datetime, timezone

from src.application.service.order_service import PlaceOrderService
from src.application.dtos import PlaceOrderRequestDTO, OrderItemDTO
from src.domain.entities import Product, Order, OrderStatus
from src.domain.exceptions import (
    ProductNotFoundError,
    InsufficientStockError,
)


@pytest.fixture
def mock_product_repo():
    return AsyncMock()


@pytest.fixture
def mock_order_repo():
    return AsyncMock()


@pytest.fixture
def mock_inventory_cache():
    return AsyncMock()


@pytest.fixture
def mock_event_publisher():
    return AsyncMock()


@pytest.fixture
def order_service(mock_product_repo, mock_order_repo, mock_inventory_cache, mock_event_publisher):
    return PlaceOrderService(
        product_repository=mock_product_repo,
        order_repository=mock_order_repo,
        inventory_cache=mock_inventory_cache,
        event_publisher=mock_event_publisher,
    )


@pytest.fixture
def sample_product():
    return Product(
        id=1,
        sku="SKU-001",
        name="Test Product",
        description="Description",
        price=Decimal("100.00"),
        stock_quantity=10
    )


@pytest.mark.asyncio
class TestPlaceOrderService:
    """Tests for PlaceOrderService execution logic."""

    async def test_execute_success(
        self, order_service, mock_product_repo, mock_order_repo, 
        mock_inventory_cache, mock_event_publisher, sample_product
    ):
        """Should successfully place an order when all conditions are met."""
        # Arrange
        request = PlaceOrderRequestDTO(
            customer_id=1,
            items=[OrderItemDTO(product_id=1, quantity=2)]
        )
        
        mock_product_repo.get_many_by_ids.return_value = [sample_product]
        mock_inventory_cache.check_and_reserve_stock.return_value = True
        
        # Mock saved order
        saved_order = MagicMock(spec=Order)
        saved_order.id = 123
        saved_order.customer_id = 1
        saved_order.total_amount = Decimal("200.00")
        saved_order.total_items = 2
        saved_order.status = OrderStatus.PENDING
        saved_order.items = []
        saved_order.created_at = datetime.now(timezone.utc)
        saved_order.updated_at = datetime.now(timezone.utc)
        
        mock_order_repo.save.return_value = saved_order

        # Act
        response = await order_service.execute(request)

        # Assert
        assert response.id == 123
        assert response.status == "pending"
        mock_product_repo.get_many_by_ids.assert_called_once_with([1])
        mock_inventory_cache.check_and_reserve_stock.assert_called_once_with(product_id=1, quantity=2)
        mock_order_repo.save.assert_called_once()
        mock_event_publisher.publish.assert_called()

    async def test_raise_product_not_found(self, order_service, mock_product_repo):
        """Should raise ProductNotFoundError if a product does not exist."""
        # Arrange
        request = PlaceOrderRequestDTO(
            customer_id=1,
            items=[OrderItemDTO(product_id=999, quantity=1)]
        )
        mock_product_repo.get_many_by_ids.return_value = []

        # Act & Assert
        with pytest.raises(ProductNotFoundError):
            await order_service.execute(request)

    async def test_raise_insufficient_stock(self, order_service, mock_product_repo, mock_inventory_cache, sample_product):
        """Should raise InsufficientStockError and rollback if stock reservation fails."""
        # Arrange
        request = PlaceOrderRequestDTO(
            customer_id=1,
            items=[OrderItemDTO(product_id=1, quantity=100)]
        )
        mock_product_repo.get_many_by_ids.return_value = [sample_product]
        mock_inventory_cache.check_and_reserve_stock.return_value = False

        # Act & Assert
        with pytest.raises(InsufficientStockError):
            await order_service.execute(request)
        
        # Verify rollback wasn't called because first reservation failed
        mock_inventory_cache.release_stock.assert_not_called()

    async def test_rollback_on_persistence_failure(
        self, order_service, mock_product_repo, mock_inventory_cache, 
        mock_order_repo, sample_product
    ):
        """Should release reserved stock if database persistence fails."""
        # Arrange
        request = PlaceOrderRequestDTO(
            customer_id=1,
            items=[OrderItemDTO(product_id=1, quantity=2)]
        )
        mock_product_repo.get_many_by_ids.return_value = [sample_product]
        mock_inventory_cache.check_and_reserve_stock.return_value = True
        mock_order_repo.save.side_effect = Exception("DB Error")

        # Act & Assert
        with pytest.raises(Exception, match="DB Error"):
            await order_service.execute(request)
        
        # Verify rollback
        mock_inventory_cache.release_stock.assert_called_once_with(1, 2)
