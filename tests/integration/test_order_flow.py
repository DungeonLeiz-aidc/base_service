"""
test_order_flow.py

Integration tests for the Order Placement flow.
Tests the connection between API, Service, and Repository using an in-memory database.
Infrastructure clients (Redis, RabbitMQ) are mocked for individual testing.
"""

import pytest
import pytest_asyncio
from httpx import AsyncClient
from decimal import Decimal
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.pool import StaticPool

from src.main import app
from src.dependencies import get_session, get_place_order_service
from src.infrastructure.models.product_model import Base as ProductBase, ProductModel
from src.infrastructure.models.order_model import Base as OrderBase
from src.container import get_container


# Setup an in-memory SQLite for integration testing
@pytest_asyncio.fixture
async def test_db_session():
    engine = create_async_engine(
        "sqlite+aiosqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    async with engine.begin() as conn:
        await conn.run_sync(ProductBase.metadata.create_all)
        await conn.run_sync(OrderBase.metadata.create_all)
    
    Session = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
    async with Session() as session:
        yield session
    await engine.dispose()


@pytest_asyncio.fixture
async def async_client(test_db_session):
    # Override get_session to use our test DB
    app.dependency_overrides[get_session] = lambda: test_db_session
    
    # Mock infrastructure in the container
    container = get_container()
    container.inventory_cache = AsyncMock()
    container.inventory_cache.check_and_reserve_stock.return_value = True
    container.event_publisher = AsyncMock()
    
    from httpx import ASGITransport
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        yield ac
    
    app.dependency_overrides.clear()


from unittest.mock import AsyncMock

@pytest.mark.asyncio
async def test_successful_order_placement_flow(async_client, test_db_session):
    """
    Test a full successful order placement flow:
    1. Seed product in DB
    2. Place order via API
    3. Verify response status and data
    4. Verify order is saved in DB
    """
    # 1. Seed a product
    product = ProductModel(
        sku="PROD-123",
        name="Integration Test Product",
        price=100.0,
        stock_quantity=10
    )
    test_db_session.add(product)
    await test_db_session.commit()
    await test_db_session.refresh(product)
    product_id = product.id

    # 2. Place order via API
    payload = {
        "customer_id": 1,
        "items": [
            {"product_id": product_id, "quantity": 2}
        ]
    }
    
    response = await async_client.post("/api/v1/orders", json=payload)

    # 3. Verify response
    assert response.status_code == 201
    data = response.json()
    assert data["total_amount"] == "200.00"
    assert data["status"] == "pending"
    assert len(data["items"]) == 1

    # 4. Verify DB state (PlaceOrderService doesn't automatically decrease DB stock, only Redis)
    # But it should have saved the order
    from src.infrastructure.models.order_model import OrderModel
    from sqlalchemy import select
    from sqlalchemy.orm import selectinload
    
    stmt = select(OrderModel).options(selectinload(OrderModel.items)).where(OrderModel.id == data["id"])
    result = await test_db_session.execute(stmt)
    order_in_db = result.scalar_one_or_none()
    
    assert order_in_db is not None
    assert order_in_db.customer_id == 1
    assert len(order_in_db.items) == 1
    assert order_in_db.items[0].product_sku == "PROD-123"
