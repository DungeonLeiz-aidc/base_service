"""
seed_products.py

Script to seed the products table from a JSON file.
"""

import asyncio
import json
import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy import select
from loguru import logger

from src.infrastructure.models.product_model import ProductModel
from configs.service_config import settings


async def seed_products():
    """Seed products from JSON file to the database."""
    logger.info("Starting product seeding...")
    
    # Database setup
    engine = create_async_engine(settings.DATABASE_URL)
    Session = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
    
    # Load products from JSON
    seed_file = os.path.join("seed", "products.json")
    with open(seed_file, "r") as f:
        products_data = json.load(f)
    
    async with Session() as session:
        for p_data in products_data:
            # Check if product already exists
            stmt = select(ProductModel).where(ProductModel.sku == p_data["sku"])
            result = await session.execute(stmt)
            existing = result.scalar_one_or_none()
            
            if existing:
                logger.info(f"Product {p_data['sku']} already exists, updating...")
                existing.name = p_data["name"]
                existing.description = p_data["description"]
                existing.price = p_data["price"]
                existing.stock_quantity = p_data["stock_quantity"]
            else:
                logger.info(f"Creating product {p_data['sku']}...")
                product = ProductModel(**p_data)
                session.add(product)
        
        await session.commit()
    
    await engine.dispose()
    logger.info("Product seeding completed successfully!")


if __name__ == "__main__":
    asyncio.run(seed_products())
