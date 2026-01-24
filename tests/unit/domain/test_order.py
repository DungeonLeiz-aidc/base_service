"""
test_order.py

Unit tests for Order domain entity and OrderItem value object.
"""

import pytest
from datetime import datetime
from decimal import Decimal
from src.domain.entities.order import Order, OrderItem, OrderStatus


class TestOrderItemCreation:
    """Tests for OrderItem value object creation."""
    
    def test_create_valid_order_item(self):
        """Should create order item with valid data."""
        item = OrderItem(
            product_id=1,
            product_sku="LAPTOP-001",
            product_name="Gaming Laptop",
            quantity=2,
            unit_price=Decimal("1500.00")
        )
        
        assert item.product_id == 1
        assert item.product_sku == "LAPTOP-001"
        assert item.product_name == "Gaming Laptop"
        assert item.quantity == 2
        assert item.unit_price == Decimal("1500.00")
    
    def test_order_item_is_immutable(self):
        """Should not allow modification of order item fields."""
        item = OrderItem(
            product_id=1,
            product_sku="SKU-001",
            product_name="Product",
            quantity=1,
            unit_price=Decimal("100.00")
        )
        
        with pytest.raises(AttributeError):
            item.quantity = 5  # type: ignore
    
    def test_raise_error_for_zero_quantity(self):
        """Should raise error for zero quantity."""
        with pytest.raises(ValueError, match="quantity must be positive"):
            OrderItem(
                product_id=1,
                product_sku="SKU-001",
                product_name="Product",
                quantity=0,
                unit_price=Decimal("100.00")
            )
    
    def test_raise_error_for_negative_quantity(self):
        """Should raise error for negative quantity."""
        with pytest.raises(ValueError, match="quantity must be positive"):
            OrderItem(
                product_id=1,
                product_sku="SKU-001",
                product_name="Product",
                quantity=-1,
                unit_price=Decimal("100.00")
            )
    
    def test_raise_error_for_negative_price(self):
        """Should raise error for negative price."""
        with pytest.raises(ValueError, match="unit price cannot be negative"):
            OrderItem(
                product_id=1,
                product_sku="SKU-001",
                product_name="Product",
                quantity=1,
                unit_price=Decimal("-100.00")
            )
    
    def test_calculate_subtotal(self):
        """Should calculate correct subtotal."""
        item = OrderItem(
            product_id=1,
            product_sku="SKU-001",
            product_name="Product",
            quantity=3,
            unit_price=Decimal("25.50")
        )
        
        assert item.subtotal == Decimal("76.50")


class TestOrderCreation:
    """Tests for Order entity creation."""
    
    @pytest.fixture
    def sample_items(self):
        """Create sample order items."""
        return [
            OrderItem(
                product_id=1,
                product_sku="LAPTOP-001",
                product_name="Gaming Laptop",
                quantity=1,
                unit_price=Decimal("1500.00")
            ),
            OrderItem(
                product_id=2,
                product_sku="MOUSE-001",
                product_name="Gaming Mouse",
                quantity=2,
                unit_price=Decimal("50.00")
            ),
        ]
    
    def test_create_valid_order(self, sample_items):
        """Should create order with valid data."""
        order = Order(
            id=1,
            customer_id=100,
            items=sample_items
        )
        
        assert order.id == 1
        assert order.customer_id == 100
        assert len(order.items) == 2
        assert order.status == OrderStatus.PENDING
        assert isinstance(order.created_at, datetime)
        assert isinstance(order.updated_at, datetime)
    
    def test_create_order_without_id(self, sample_items):
        """Should create order without id (not yet persisted)."""
        order = Order(
            id=None,
            customer_id=100,
            items=sample_items
        )
        
        assert order.id is None
    
    def test_raise_error_for_invalid_customer_id(self, sample_items):
        """Should raise error for invalid customer ID."""
        with pytest.raises(ValueError, match="Customer ID must be positive"):
            Order(
                id=1,
                customer_id=0,
                items=sample_items
            )
        
        with pytest.raises(ValueError, match="Customer ID must be positive"):
            Order(
                id=1,
                customer_id=-1,
                items=sample_items
            )
    
    def test_raise_error_for_empty_items(self):
        """Should raise error for order without items."""
        with pytest.raises(ValueError, match="must have at least one item"):
            Order(
                id=1,
                customer_id=100,
                items=[]
            )
    
    def test_raise_error_for_too_many_items(self):
        """Should raise error for order with more than 50 items."""
        many_items = [
            OrderItem(
                product_id=i,
                product_sku=f"SKU-{i}",
                product_name=f"Product {i}",
                quantity=1,
                unit_price=Decimal("10.00")
            )
            for i in range(51)
        ]
        
        with pytest.raises(ValueError, match="cannot have more than 50 items"):
            Order(
                id=1,
                customer_id=100,
                items=many_items
            )


class TestOrderCalculations:
    """Tests for order calculations."""
    
    @pytest.fixture
    def order(self):
        """Create sample order."""
        return Order(
            id=1,
            customer_id=100,
            items=[
                OrderItem(
                    product_id=1,
                    product_sku="LAPTOP-001",
                    product_name="Laptop",
                    quantity=1,
                    unit_price=Decimal("1000.00")
                ),
                OrderItem(
                    product_id=2,
                    product_sku="MOUSE-001",
                    product_name="Mouse",
                    quantity=2,
                    unit_price=Decimal("25.50")
                ),
                OrderItem(
                    product_id=3,
                    product_sku="KB-001",
                    product_name="Keyboard",
                    quantity=1,
                    unit_price=Decimal("75.00")
                ),
            ]
        )
    
    def test_calculate_total_amount(self, order):
        """Should calculate correct total amount."""
        # 1000 + (2 * 25.50) + 75 = 1126.00
        assert order.total_amount == Decimal("1126.00")
    
    def test_calculate_total_items(self, order):
        """Should calculate total number of items."""
        # 1 + 2 + 1 = 4
        assert order.total_items == 4


class TestOrderStatusTransitions:
    """Tests for order status transitions."""
    
    @pytest.fixture
    def pending_order(self):
        """Create order in PENDING status."""
        return Order(
            id=1,
            customer_id=100,
            items=[
                OrderItem(
                    product_id=1,
                    product_sku="SKU-001",
                    product_name="Product",
                    quantity=1,
                    unit_price=Decimal("100.00")
                )
            ]
        )
    
    def test_confirm_pending_order(self, pending_order):
        """Should confirm pending order."""
        pending_order.confirm()
        assert pending_order.status == OrderStatus.CONFIRMED
    
    def test_cancel_pending_order(self, pending_order):
        """Should cancel pending order."""
        pending_order.cancel()
        assert pending_order.status == OrderStatus.CANCELLED
    
    def test_fail_pending_order(self, pending_order):
        """Should mark pending order as failed."""
        pending_order.mark_as_failed()
        assert pending_order.status == OrderStatus.FAILED
    
    def test_cannot_process_pending_order_directly(self, pending_order):
        """Should not allow processing pending order directly."""
        with pytest.raises(ValueError, match="Cannot process order"):
            pending_order.start_processing()
    
    def test_confirmed_order_transitions(self, pending_order):
        """Should handle confirmed order transitions."""
        pending_order.confirm()
        
        # Can process
        pending_order.start_processing()
        assert pending_order.status == OrderStatus.PROCESSING
    
    def test_processing_order_transitions(self, pending_order):
        """Should handle processing order transitions."""
        pending_order.confirm()
        pending_order.start_processing()
        
        # Can ship
        pending_order.ship()
        assert pending_order.status == OrderStatus.SHIPPED
    
    def test_shipped_order_transitions(self, pending_order):
        """Should handle shipped order transitions."""
        pending_order.confirm()
        pending_order.start_processing()
        pending_order.ship()
        
        # Can deliver
        pending_order.deliver()
        assert pending_order.status == OrderStatus.DELIVERED
    
    def test_cannot_transition_from_delivered(self, pending_order):
        """Should not allow transitions from delivered status."""
        pending_order.confirm()
        pending_order.start_processing()
        pending_order.ship()
        pending_order.deliver()
        
        with pytest.raises(ValueError, match="Cannot cancel order"):
            pending_order.cancel()
    
    def test_cannot_transition_from_cancelled(self, pending_order):
        """Should not allow transitions from cancelled status."""
        pending_order.cancel()
        
        with pytest.raises(ValueError, match="Cannot confirm order"):
            pending_order.confirm()
    
    def test_cannot_transition_from_failed(self, pending_order):
        """Should not allow transitions from failed status."""
        pending_order.mark_as_failed()
        
        with pytest.raises(ValueError, match="Cannot confirm order"):
            pending_order.confirm()
    
    def test_can_cancel_confirmed_order(self, pending_order):
        """Should allow cancelling confirmed order."""
        pending_order.confirm()
        pending_order.cancel()
        assert pending_order.status == OrderStatus.CANCELLED
    
    def test_can_cancel_processing_order(self, pending_order):
        """Should allow cancelling processing order."""
        pending_order.confirm()
        pending_order.start_processing()
        pending_order.cancel()
        assert pending_order.status == OrderStatus.CANCELLED
    
    def test_cannot_cancel_shipped_order(self, pending_order):
        """Should not allow cancelling shipped order."""
        pending_order.confirm()
        pending_order.start_processing()
        pending_order.ship()
        
        with pytest.raises(ValueError, match="Cannot cancel order"):
            pending_order.cancel()


class TestOrderTerminalStates:
    """Tests for terminal state checks."""
    
    @pytest.fixture
    def order(self):
        """Create sample order."""
        return Order(
            id=1,
            customer_id=100,
            items=[
                OrderItem(
                    product_id=1,
                    product_sku="SKU-001",
                    product_name="Product",
                    quantity=1,
                    unit_price=Decimal("100.00")
                )
            ]
        )
    
    def test_pending_is_not_terminal(self, order):
        """Should return False for pending order."""
        assert order.is_terminal_state() is False
    
    def test_confirmed_is_not_terminal(self, order):
        """Should return False for confirmed order."""
        order.confirm()
        assert order.is_terminal_state() is False
    
    def test_processing_is_not_terminal(self, order):
        """Should return False for processing order."""
        order.confirm()
        order.start_processing()
        assert order.is_terminal_state() is False
    
    def test_shipped_is_not_terminal(self, order):
        """Should return False for shipped order."""
        order.confirm()
        order.start_processing()
        order.ship()
        assert order.is_terminal_state() is False
    
    def test_delivered_is_terminal(self, order):
        """Should return True for delivered order."""
        order.confirm()
        order.start_processing()
        order.ship()
        order.deliver()
        assert order.is_terminal_state() is True
    
    def test_cancelled_is_terminal(self, order):
        """Should return True for cancelled order."""
        order.cancel()
        assert order.is_terminal_state() is True
    
    def test_failed_is_terminal(self, order):
        """Should return True for failed order."""
        order.mark_as_failed()
        assert order.is_terminal_state() is True


class TestOrderRepresentation:
    """Tests for order string representation."""
    
    def test_order_repr(self):
        """Should generate correct string representation."""
        order = Order(
            id=123,
            customer_id=456,
            items=[
                OrderItem(
                    product_id=1,
                    product_sku="SKU-001",
                    product_name="Product",
                    quantity=2,
                    unit_price=Decimal("50.00")
                )
            ]
        )
        
        repr_str = repr(order)
        assert "Order(id=123" in repr_str
        assert "customer_id=456" in repr_str
        assert "items=1" in repr_str
        assert "total=100" in repr_str
        assert "status=pending" in repr_str
