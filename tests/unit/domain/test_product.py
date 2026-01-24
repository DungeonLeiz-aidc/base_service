"""
test_product.py

Unit tests for Product domain entity.
"""

import pytest
from decimal import Decimal
from src.domain.entities.product import Product


class TestProductCreation:
    """Tests for Product entity creation and validation."""
    
    def test_create_valid_product(self):
        """Should create product with valid data."""
        product = Product(
            id=1,
            sku="LAPTOP-001",
            name="Gaming Laptop",
            description="High-performance gaming laptop",
            price=Decimal("1500.00"),
            stock_quantity=10
        )
        
        assert product.id == 1
        assert product.sku == "LAPTOP-001"
        assert product.name == "Gaming Laptop"
        assert product.price == Decimal("1500.00")
        assert product.stock_quantity == 10
    
    def test_create_product_with_zero_stock(self):
        """Should create product with zero stock."""
        product = Product(
            id=None,
            sku="MOUSE-001",
            name="Gaming Mouse",
            description="RGB Mouse",
            price=Decimal("50.00"),
            stock_quantity=0
        )
        
        assert product.stock_quantity == 0
    
    def test_create_product_without_id(self):
        """Should create product without id (not yet persisted)."""
        product = Product(
            id=None,
            sku="KB-001",
            name="Keyboard",
            description="Mechanical keyboard",
            price=Decimal("100.00"),
            stock_quantity=5
        )
        
        assert product.id is None
    
    def test_raise_error_for_empty_sku(self):
        """Should raise error if SKU is empty."""
        with pytest.raises(ValueError, match="SKU cannot be empty"):
            Product(
                id=1,
                sku="",
                name="Product",
                description="Test",
                price=Decimal("10.00"),
                stock_quantity=5
            )
    
    def test_raise_error_for_empty_name(self):
        """Should raise error if name is empty."""
        with pytest.raises(ValueError, match="Product name cannot be empty"):
            Product(
                id=1,
                sku="SKU-001",
                name="",
                description="Test",
                price=Decimal("10.00"),
                stock_quantity=5
            )
    
    def test_raise_error_for_negative_price(self):
        """Should raise error if price is negative."""
        with pytest.raises(ValueError, match="Price cannot be negative"):
            Product(
                id=1,
                sku="SKU-001",
                name="Product",
                description="Test",
                price=Decimal("-10.00"),
                stock_quantity=5
            )
    
    def test_raise_error_for_negative_stock(self):
        """Should raise error if stock is negative."""
        with pytest.raises(ValueError, match="Stock quantity cannot be negative"):
            Product(
                id=1,
                sku="SKU-001",
                name="Product",
                description="Test",
                price=Decimal("10.00"),
                stock_quantity=-5
            )


class TestProductAvailability:
    """Tests for product availability checks."""
    
    @pytest.fixture
    def product(self):
        """Create a sample product for testing."""
        return Product(
            id=1,
            sku="TEST-001",
            name="Test Product",
            description="Test",
            price=Decimal("100.00"),
            stock_quantity=10
        )
    
    def test_is_available_with_sufficient_stock(self, product):
        """Should return True if stock is sufficient."""
        assert product.is_available(5) is True
        assert product.is_available(10) is True
    
    def test_is_available_with_insufficient_stock(self, product):
        """Should return False if stock is insufficient."""
        assert product.is_available(11) is False
        assert product.is_available(100) is False
    
    def test_is_available_default_quantity(self, product):
        """Should check for quantity 1 by default."""
        assert product.is_available() is True
    
    def test_is_available_with_zero_stock(self):
        """Should return False if product has zero stock."""
        product = Product(
            id=1,
            sku="TEST-002",
            name="Out of Stock",
            description="Test",
            price=Decimal("50.00"),
            stock_quantity=0
        )
        
        assert product.is_available(1) is False


class TestProductPriceCalculation:
    """Tests for price calculation logic."""
    
    @pytest.fixture
    def product(self):
        """Create a sample product for testing."""
        return Product(
            id=1,
            sku="CALC-001",
            name="Calculator Product",
            description="Test",
            price=Decimal("25.50"),
            stock_quantity=100
        )
    
    def test_calculate_total_price(self, product):
        """Should calculate correct total price."""
        assert product.calculate_total_price(1) == Decimal("25.50")
        assert product.calculate_total_price(2) == Decimal("51.00")
        assert product.calculate_total_price(10) == Decimal("255.00")
    
    def test_calculate_total_price_with_zero_quantity(self, product):
        """Should return zero for zero quantity."""
        assert product.calculate_total_price(0) == Decimal("0")
    
    def test_calculate_total_price_raises_error_for_negative(self, product):
        """Should raise error for negative quantity."""
        with pytest.raises(ValueError, match="Quantity cannot be negative"):
            product.calculate_total_price(-1)


class TestProductStockReservation:
    """Tests for stock reservation and release."""
    
    @pytest.fixture
    def product(self):
        """Create a sample product for testing."""
        return Product(
            id=1,
            sku="STOCK-001",
            name="Stock Product",
            description="Test",
            price=Decimal("100.00"),
            stock_quantity=20
        )
    
    def test_reserve_stock_success(self, product):
        """Should decrease stock quantity when reserving."""
        product.reserve_stock(5)
        assert product.stock_quantity == 15
        
        product.reserve_stock(10)
        assert product.stock_quantity == 5
    
    def test_reserve_stock_raises_error_for_insufficient_stock(self, product):
        """Should raise error if trying to reserve more than available."""
        with pytest.raises(ValueError, match="Insufficient stock"):
            product.reserve_stock(21)
    
    def test_reserve_stock_raises_error_for_zero_quantity(self, product):
        """Should raise error for zero quantity."""
        with pytest.raises(ValueError, match="Quantity must be positive"):
            product.reserve_stock(0)
    
    def test_reserve_stock_raises_error_for_negative_quantity(self, product):
        """Should raise error for negative quantity."""
        with pytest.raises(ValueError, match="Quantity must be positive"):
            product.reserve_stock(-5)
    
    def test_release_stock_success(self, product):
        """Should increase stock quantity when releasing."""
        product.release_stock(5)
        assert product.stock_quantity == 25
        
        product.release_stock(10)
        assert product.stock_quantity == 35
    
    def test_release_stock_raises_error_for_zero_quantity(self, product):
        """Should raise error for zero quantity."""
        with pytest.raises(ValueError, match="Quantity must be positive"):
            product.release_stock(0)
    
    def test_release_stock_raises_error_for_negative_quantity(self, product):
        """Should raise error for negative quantity."""
        with pytest.raises(ValueError, match="Quantity must be positive"):
            product.release_stock(-5)
    
    def test_reserve_and_release_stock_workflow(self, product):
        """Should handle reserve and release workflow correctly."""
        initial_stock = product.stock_quantity
        
        # Reserve stock
        product.reserve_stock(10)
        assert product.stock_quantity == initial_stock - 10
        
        # Release stock (e.g., order cancelled)
        product.release_stock(10)
        assert product.stock_quantity == initial_stock


class TestProductPriceUpdate:
    """Tests for product price updates."""
    
    @pytest.fixture
    def product(self):
        """Create a sample product for testing."""
        return Product(
            id=1,
            sku="PRICE-001",
            name="Price Product",
            description="Test",
            price=Decimal("100.00"),
            stock_quantity=10
        )
    
    def test_update_price_success(self, product):
        """Should update price successfully."""
        product.update_price(Decimal("150.00"))
        assert product.price == Decimal("150.00")
    
    def test_update_price_to_zero(self, product):
        """Should allow updating price to zero."""
        product.update_price(Decimal("0"))
        assert product.price == Decimal("0")
    
    def test_update_price_raises_error_for_negative(self, product):
        """Should raise error for negative price."""
        with pytest.raises(ValueError, match="Price cannot be negative"):
            product.update_price(Decimal("-50.00"))


class TestProductRepresentation:
    """Tests for product string representation."""
    
    def test_product_repr(self):
        """Should generate correct string representation."""
        product = Product(
            id=1,
            sku="REPR-001",
            name="Repr Product",
            description="Test product",
            price=Decimal("99.99"),
            stock_quantity=5
        )
        
        repr_str = repr(product)
        assert "Product(id=1" in repr_str
        assert "sku='REPR-001'" in repr_str
        assert "name='Repr Product'" in repr_str
        assert "price=99.99" in repr_str
        assert "stock=5" in repr_str
