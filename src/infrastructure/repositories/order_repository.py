"""
order_repository.py

Order repository implementation using SQLAlchemy.
Maps between Order domain entity and OrderModel ORM.
"""

from typing import Optional, List
from decimal import Decimal
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from loguru import logger

from src.domain.entities import Order, OrderItem, OrderStatus
from src.interface.protocols.repositories import IOrderRepository
from src.infrastructure.models import OrderModel, OrderItemModel


class OrderRepository(IOrderRepository):
    """
    Order repository implementation.
    
    Handles persistence of Order entities using PostgreSQL.
    """
    
    def __init__(self, session: AsyncSession):
        """
        Initialize repository.
        
        Args:
            session: SQLAlchemy async session.
        """
        self.session = session
    
    async def get_by_id(self, order_id: int) -> Optional[Order]:
        """Get order by ID with items eagerly loaded."""
        logger.debug(f"Fetching order by ID: {order_id}")
        
        stmt = (
            select(OrderModel)
            .options(selectinload(OrderModel.items))
            .where(OrderModel.id == order_id)
        )
        result = await self.session.execute(stmt)
        model = result.scalar_one_or_none()
        
        if model is None:
            logger.debug(f"Order {order_id} not found")
            return None
        
        return self._to_entity(model)
    
    async def get_by_customer_id(self, customer_id: int) -> List[Order]:
        """Get all orders for a customer."""
        logger.debug(f"Fetching orders for customer: {customer_id}")
        
        stmt = (
            select(OrderModel)
            .options(selectinload(OrderModel.items))
            .where(OrderModel.customer_id == customer_id)
            .order_by(OrderModel.created_at.desc())
        )
        result = await self.session.execute(stmt)
        models = result.scalars().all()
        
        return [self._to_entity(model) for model in models]
    
    async def save(self, order: Order) -> Order:
        """Save order (create or update)."""
        if order.id is None:
            # Create new
            logger.debug(f"Creating new order for customer {order.customer_id}")
            model = self._to_model(order)
            self.session.add(model)
        else:
            # Update existing
            logger.debug(f"Updating order: {order.id}")
            model = await self._get_model_by_id(order.id)
            if model is None:
                raise ValueError(f"Order {order.id} not found for update")
            
            self._update_model_from_entity(model, order)
        
        await self.session.flush()
        await self.session.refresh(model, ["items"])
        
        return self._to_entity(model)
    
    async def update_status(self, order_id: int, status: str) -> None:
        """Update order status."""
        logger.debug(f"Updating order {order_id} status to: {status}")
        
        model = await self._get_model_by_id(order_id)
        if model is None:
            raise ValueError(f"Order {order_id} not found")
        
        model.status = status
        await self.session.flush()
    
    async def _get_model_by_id(self, order_id: int) -> Optional[OrderModel]:
        """Get OrderModel by ID."""
        stmt = (
            select(OrderModel)
            .options(selectinload(OrderModel.items))
            .where(OrderModel.id == order_id)
        )
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()
    
    def _to_entity(self, model: OrderModel) -> Order:
        """Convert ORM model to domain entity."""
        order_items = [
            OrderItem(
                product_id=item.product_id,
                product_sku=item.product_sku,
                product_name=item.product_name,
                quantity=item.quantity,
                unit_price=Decimal(str(item.unit_price)),
            )
            for item in model.items
        ]
        
        return Order(
            id=model.id,
            customer_id=model.customer_id,
            items=order_items,
            status=OrderStatus(model.status),
            created_at=model.created_at,
            updated_at=model.updated_at,
        )
    
    def _to_model(self, entity: Order) -> OrderModel:
        """Convert domain entity to ORM model."""
        order_model = OrderModel(
            id=entity.id,
            customer_id=entity.customer_id,
            status=entity.status.value,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )
        
        # Add order items
        for item in entity.items:
            item_model = OrderItemModel(
                product_id=item.product_id,
                product_sku=item.product_sku,
                product_name=item.product_name,
                quantity=item.quantity,
                unit_price=float(item.unit_price),
            )
            order_model.items.append(item_model)
        
        return order_model
    
    def _update_model_from_entity(self, model: OrderModel, entity: Order) -> None:
        """Update ORM model fields from domain entity."""
        model.customer_id = entity.customer_id
        model.status = entity.status.value
        model.updated_at = entity.updated_at
        
        # Update items (simple approach: clear and recreate)
        model.items.clear()
        for item in entity.items:
            item_model = OrderItemModel(
                product_id=item.product_id,
                product_sku=item.product_sku,
                product_name=item.product_name,
                quantity=item.quantity,
                unit_price=float(item.unit_price),
            )
            model.items.append(item_model)
