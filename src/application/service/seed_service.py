"""
seed_service.py

Application service for managing initial data seeding.
Orchestrates the population of initial datasets into the system.
"""

import json
import os
from typing import List, Dict, Any
from loguru import logger

from src.interface.protocols.repositories import IProductRepository
from src.domain.entities.product import Product


class SeedService:
    """
    Service responsible for seeding the system with initial data.
    Ensures that the core product catalog and other baseline datasets are populated.
    """

    def __init__(self, product_repository: IProductRepository):
        """
        Initialize SeedService.

        Args:
            product_repository: Repository for product persistence.
        """
        self.product_repo = product_repository

    async def seed_products_from_json(self, file_path: str) -> Dict[str, int]:
        """
        Load products from a JSON file and persist them.

        Args:
            file_path: Absolute or relative path to the seed JSON file.

        Returns:
            Dictionary containing 'created' and 'updated' counts.
        """
        logger.info(f"AUDIT | Seeding products from {file_path}")
        
        if not os.path.exists(file_path):
            error_msg = f"Seed file not found: {file_path}"
            logger.error(f"AUDIT | FAILED | {error_msg}")
            raise FileNotFoundError(error_msg)

        with open(file_path, "r") as f:
            products_data: List[Dict[str, Any]] = json.load(f)

        created_count = 0
        updated_count = 0

        for p_data in products_data:
            sku = p_data.get("sku")
            existing_product = await self.product_repo.get_by_sku(sku)

            if existing_product:
                # Update existing product
                logger.debug(f"AUDIT | Updating existing product SKU: {sku}")
                existing_product.name = p_data["name"]
                existing_product.description = p_data["description"]
                existing_product.price = p_data["price"]
                existing_product.stock_quantity = p_data["stock_quantity"]
                await self.product_repo.save(existing_product)
                updated_count += 1
            else:
                # Create new product
                logger.debug(f"AUDIT | Creating new product SKU: {sku}")
                new_product = Product(
                    id=None,
                    sku=sku,
                    name=p_data["name"],
                    description=p_data["description"],
                    price=p_data["price"],
                    stock_quantity=p_data["stock_quantity"]
                )
                await self.product_repo.save(new_product)
                created_count += 1

        logger.info(f"AUDIT | SUCCESS | Seeded {created_count} created, {updated_count} updated.")
        return {"created": created_count, "updated": updated_count}
