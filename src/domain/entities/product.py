"""
product.py

Product domain entity representing a product in the catalog.
"""

from dataclasses import dataclass
from decimal import Decimal
from typing import Optional


@dataclass
class Product:
    """
    Product domain entity.
    
    Represents a product with its business rules and invariants.
    """
    
    id: Optional[int]
    sku: str  # Stock Keeping Unit - unique identifier
    name: str
    description: str
    price: Decimal
    stock_quantity: int
    
    def __post_init__(self) -> None:
        """Validate product invariants after initialization."""
        self._validate()
    
    def _validate(self) -> None:
        """
        Validate product business rules.
        
        Raises:
            ValueError: If any business rule is violated.
        """
        if not self.sku or not self.sku.strip():
            raise ValueError("SKU cannot be empty")
        
        if not self.name or not self.name.strip():
            raise ValueError("Product name cannot be empty")
        
        if self.price < Decimal("0"):
            raise ValueError("Price cannot be negative")
        
        if self.stock_quantity < 0:
            raise ValueError("Stock quantity cannot be negative")
    
    def is_available(self, quantity: int = 1) -> bool:
        """
        Check if product is available in requested quantity.
        
        Args:
            quantity: Requested quantity to check.
            
        Returns:
            True if product has sufficient stock, False otherwise.
        """
        return self.stock_quantity >= quantity
    
    def calculate_total_price(self, quantity: int) -> Decimal:
        """
        Calculate total price for given quantity.
        
        Args:
            quantity: Number of items.
            
        Returns:
            Total price (price * quantity).
            
        Raises:
            ValueError: If quantity is negative.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        
        return self.price * Decimal(quantity)
    
    def reserve_stock(self, quantity: int) -> None:
        """
        Reserve stock for an order (decrease available quantity).
        
        This is a domain operation - actual persistence happens in repository.
        
        Args:
            quantity: Amount to reserve.
            
        Raises:
            ValueError: If quantity is invalid or insufficient stock.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        
        if not self.is_available(quantity):
            raise ValueError(
                f"Insufficient stock. Available: {self.stock_quantity}, Requested: {quantity}"
            )
        
        self.stock_quantity -= quantity
    
    def release_stock(self, quantity: int) -> None:
        """
        Release reserved stock (increase available quantity).
        
        Used when order is cancelled or fails.
        
        Args:
            quantity: Amount to release.
            
        Raises:
            ValueError: If quantity is invalid.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        
        self.stock_quantity += quantity
    
    def update_price(self, new_price: Decimal) -> None:
        """
        Update product price.
        
        Args:
            new_price: New price.
            
        Raises:
            ValueError: If price is negative.
        """
        if new_price < Decimal("0"):
            raise ValueError("Price cannot be negative")
        
        self.price = new_price
    
    def __repr__(self) -> str:
        """String representation of Product."""
        return (
            f"Product(id={self.id}, sku='{self.sku}', name='{self.name}', "
            f"price={self.price}, stock={self.stock_quantity})"
        )
