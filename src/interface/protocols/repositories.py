"""
repositories.py

Abstract repository interfaces for the application.
These interfaces define the data access contracts that the application expects.
"""

from typing import Protocol, List, Optional
from src.domain.entities import Order, Product


class IProductRepository(Protocol):
    """Protocol for product data access."""
    
    async def get_by_id(self, product_id: int) -> Optional[Product]:
        """Get product by ID."""
        ...
    
    async def get_by_sku(self, sku: str) -> Optional[Product]:
        """Get product by SKU."""
        ...
    
    async def get_many_by_ids(self, product_ids: List[int]) -> List[Product]:
        """Get multiple products by IDs."""
        ...
    
    async def save(self, product: Product) -> Product:
        """Save product."""
        ...
    
    async def update_stock(self, product_id: int, quantity_delta: int) -> None:
        """Update product stock quantity."""
        ...


class IOrderRepository(Protocol):
    """Protocol for order data access."""
    
    async def get_by_id(self, order_id: int) -> Optional[Order]:
        """Get order by ID."""
        ...
    
    async def get_by_customer_id(self, customer_id: int) -> List[Order]:
        """Get all orders for a customer."""
        ...
    
    async def save(self, order: Order) -> Order:
        """Save order."""
        ...
    
    async def update_status(self, order_id: int, status: str) -> None:
        """Update order status."""
        ...
