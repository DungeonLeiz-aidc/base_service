"""
product_repository.py

Product repository implementation using SQLAlchemy.
Maps between Product domain entity and ProductModel ORM.
"""

from typing import Optional, List
from decimal import Decimal
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from loguru import logger

from src.domain.entities import Product
from src.interface.protocols.repositories import IProductRepository
from src.infrastructure.models import ProductModel


class ProductRepository(IProductRepository):
    """
    Product repository implementation.
    
    Handles persistence of Product entities using PostgreSQL.
    """
    
    def __init__(self, session: AsyncSession):
        """
        Initialize repository.
        
        Args:
            session: SQLAlchemy async session.
        """
        self.session = session
    
    async def get_by_id(self, product_id: int) -> Optional[Product]:
        """Get product by ID."""
        logger.debug(f"Fetching product by ID: {product_id}")
        
        stmt = select(ProductModel).where(ProductModel.id == product_id)
        result = await self.session.execute(stmt)
        model = result.scalar_one_or_none()
        
        if model is None:
            logger.debug(f"Product {product_id} not found")
            return None
        
        return self._to_entity(model)
    
    async def get_by_sku(self, sku: str) -> Optional[Product]:
        """Get product by SKU."""
        logger.debug(f"Fetching product by SKU: {sku}")
        
        stmt = select(ProductModel).where(ProductModel.sku == sku)
        result = await self.session.execute(stmt)
        model = result.scalar_one_or_none()
        
        if model is None:
            logger.debug(f"Product with SKU '{sku}' not found")
            return None
        
        return self._to_entity(model)
    
    async def get_many_by_ids(self, product_ids: List[int]) -> List[Product]:
        """Get multiple products by IDs."""
        logger.debug(f"Fetching {len(product_ids)} products")
        
        stmt = select(ProductModel).where(ProductModel.id.in_(product_ids))
        result = await self.session.execute(stmt)
        models = result.scalars().all()
        
        return [self._to_entity(model) for model in models]
    
    async def save(self, product: Product) -> Product:
        """Save product (create or update)."""
        if product.id is None:
            # Create new
            logger.debug(f"Creating new product: {product.sku}")
            model = self._to_model(product)
            self.session.add(model)
        else:
            # Update existing
            logger.debug(f"Updating product: {product.id}")
            model = await self._get_model_by_id(product.id)
            if model is None:
                raise ValueError(f"Product {product.id} not found for update")
            
            self._update_model_from_entity(model, product)
        
        await self.session.flush()
        await self.session.refresh(model)
        
        return self._to_entity(model)
    
    async def update_stock(self, product_id: int, quantity_delta: int) -> None:
        """Update product stock quantity."""
        logger.debug(f"Updating stock for product {product_id}: delta={quantity_delta}")
        
        model = await self._get_model_by_id(product_id)
        if model is None:
            raise ValueError(f"Product {product_id} not found")
        
        model.stock_quantity += quantity_delta
        await self.session.flush()
    
    async def _get_model_by_id(self, product_id: int) -> Optional[ProductModel]:
        """Get ProductModel by ID."""
        stmt = select(ProductModel).where(ProductModel.id == product_id)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()
    
    def _to_entity(self, model: ProductModel) -> Product:
        """Convert ORM model to domain entity."""
        return Product(
            id=model.id,
            sku=model.sku,
            name=model.name,
            description=model.description,
            price=Decimal(str(model.price)),
            stock_quantity=model.stock_quantity,
        )
    
    def _to_model(self, entity: Product) -> ProductModel:
        """Convert domain entity to ORM model."""
        return ProductModel(
            id=entity.id,
            sku=entity.sku,
            name=entity.name,
            description=entity.description,
            price=float(entity.price),
            stock_quantity=entity.stock_quantity,
        )
    
    def _update_model_from_entity(self, model: ProductModel, entity: Product) -> None:
        """Update ORM model fields from domain entity."""
        model.sku = entity.sku
        model.name = entity.name
        model.description = entity.description
        model.price = float(entity.price)
        model.stock_quantity = entity.stock_quantity
