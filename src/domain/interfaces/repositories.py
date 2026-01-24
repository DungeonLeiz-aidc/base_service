"""
repositories.py

Abstract repository interfaces for application layer.
These define contracts that infrastructure must implement.
"""

from abc import ABC, abstractmethod
from typing import Optional, List
from src.domain.entities import Product, Order


class IProductRepository(ABC):
    """Abstract interface for Product repository."""
    
    @abstractmethod
    async def get_by_id(self, product_id: int) -> Optional[Product]:
        """
        Get product by ID.
        
        Args:
            product_id: Product ID.
            
        Returns:
            Product entity or None if not found.
        """
        pass
    
    @abstractmethod
    async def get_by_sku(self, sku: str) -> Optional[Product]:
        """
        Get product by SKU.
        
        Args:
            sku: Product SKU.
            
        Returns:
            Product entity or None if not found.
        """
        pass
    
    @abstractmethod
    async def get_many_by_ids(self, product_ids: List[int]) -> List[Product]:
        """
        Get multiple products by IDs.
        
        Args:
            product_ids: List of product IDs.
            
        Returns:
            List of Product entities.
        """
        pass
    
    @abstractmethod
    async def save(self, product: Product) -> Product:
        """
        Save product (create or update).
        
        Args:
            product: Product entity to save.
            
        Returns:
            Saved product with ID assigned.
        """
        pass
    
    @abstractmethod
    async def update_stock(self, product_id: int, quantity_delta: int) -> None:
        """
        Update product stock quantity.
        
        Args:
            product_id: Product ID.
            quantity_delta: Change in quantity (positive or negative).
        """
        pass


class IOrderRepository(ABC):
    """Abstract interface for Order repository."""
    
    @abstractmethod
    async def get_by_id(self, order_id: int) -> Optional[Order]:
        """
        Get order by ID.
        
        Args:
            order_id: Order ID.
            
        Returns:
            Order entity or None if not found.
        """
        pass
    
    @abstractmethod
    async def get_by_customer_id(self, customer_id: int) -> List[Order]:
        """
        Get all orders for a customer.
        
        Args:
            customer_id: Customer ID.
            
        Returns:
            List of Order entities.
        """
        pass
    
    @abstractmethod
    async def save(self, order: Order) -> Order:
        """
        Save order (create or update).
        
        Args:
            order: Order entity to save.
            
        Returns:
            Saved order with ID assigned.
        """
        pass
    
    @abstractmethod
    async def update_status(self, order_id: int, status: str) -> None:
        """
        Update order status.
        
        Args:
            order_id: Order ID.
            status: New status.
        """
        pass
