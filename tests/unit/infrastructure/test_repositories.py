"""
test_repositories.py

Unit tests for Repositories using SQLite in-memory for testing SQLAlchemy logic.
"""

import pytest
import pytest_asyncio
from decimal import Decimal
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base

from src.infrastructure.models.product_model import ProductModel, Base as ProductBase
from src.infrastructure.models.order_model import OrderModel, OrderItemModel, Base as OrderBase
from src.infrastructure.repositories.product_repository import ProductRepository
from src.infrastructure.repositories.order_repository import OrderRepository
from src.domain.entities import Product, Order, OrderItem, OrderStatus

# Use a combined base or separate ones for testing
Base = declarative_base()

@pytest_asyncio.fixture
async def test_session():
    """Create a clean in-memory SQLite database for each test."""
    engine = create_async_engine("sqlite+aiosqlite:///:memory:", echo=False)
    
    # In SQLite, we might need to create tables from both bases if they are different
    async with engine.begin() as conn:
        await conn.run_sync(ProductBase.metadata.create_all)
        await conn.run_sync(OrderBase.metadata.create_all)
    
    Session = async_sessionmaker(engine, expire_on_commit=False)
    async with Session() as session:
        yield session
    
    await engine.dispose()


@pytest.mark.asyncio
class TestProductRepository:
    """Tests for ProductRepository implementation."""

    async def test_save_and_get_product(self, test_session):
        repo = ProductRepository(test_session)
        product = Product(
            id=None,
            sku="TEST-SKU",
            name="Test Product",
            description="Desc",
            price=Decimal("10.50"),
            stock_quantity=100
        )
        
        # Save
        saved_product = await repo.save(product)
        await test_session.commit()
        
        assert saved_product.id is not None
        assert saved_product.sku == "TEST-SKU"
        
        # Get by ID
        found_product = await repo.get_by_id(saved_product.id)
        assert found_product.sku == "TEST-SKU"
        assert found_product.price == Decimal("10.50")

    async def test_get_by_sku(self, test_session):
        repo = ProductRepository(test_session)
        model = ProductModel(sku="SKU-1", name="N", price=1.0, stock_quantity=1)
        test_session.add(model)
        await test_session.commit()
        
        product = await repo.get_by_sku("SKU-1")
        assert product is not None
        assert product.sku == "SKU-1"

    async def test_update_stock(self, test_session):
        repo = ProductRepository(test_session)
        model = ProductModel(sku="SKU-2", name="N", price=1.0, stock_quantity=10)
        test_session.add(model)
        await test_session.commit()
        
        await repo.update_stock(model.id, -5)
        await test_session.commit()
        
        updated = await repo.get_by_id(model.id)
        assert updated.stock_quantity == 5


@pytest.mark.asyncio
class TestOrderRepository:
    """Tests for OrderRepository implementation."""

    async def test_save_and_get_order(self, test_session):
        # Need products first? No, OrderModel items don't strictly require foreign keys to products table in this schema
        repo = OrderRepository(test_session)
        order = Order(
            id=None,
            customer_id=1,
            items=[
                OrderItem(product_id=1, product_sku="S1", product_name="N1", quantity=2, unit_price=Decimal("5.00"))
            ],
            status=OrderStatus.PENDING
        )
        
        saved_order = await repo.save(order)
        await test_session.commit()
        
        assert saved_order.id is not None
        assert len(saved_order.items) == 1
        
        # Get by ID
        found_order = await repo.get_by_id(saved_order.id)
        assert found_order is not None
        assert found_order.customer_id == 1
        assert found_order.total_amount == Decimal("10.00")

    async def test_update_status(self, test_session):
        repo = OrderRepository(test_session)
        model = OrderModel(customer_id=1, status="pending")
        item_model = OrderItemModel(
            product_id=1, product_sku="S1", product_name="N1", quantity=1, unit_price=10.0
        )
        model.items.append(item_model)
        test_session.add(model)
        await test_session.commit()
        
        await repo.update_status(model.id, "confirmed")
        await test_session.commit()
        
        updated = await repo.get_by_id(model.id)
        assert updated.status == OrderStatus.CONFIRMED
