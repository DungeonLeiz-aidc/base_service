"""
product_model.py

SQLAlchemy ORM model for Product.
"""

from decimal import Decimal
from sqlalchemy import Column, Integer, String, Numeric, Index
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class ProductModel(Base):
    """
    Product ORM model for PostgreSQL.
    
    Represents products table in database.
    """
    
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    sku = Column(String(50), unique=True, nullable=False, index=True)
    name = Column(String(255), nullable=False)
    description = Column(String(1000), nullable=False, default="")
    price = Column(Numeric(10, 2), nullable=False)
    stock_quantity = Column(Integer, nullable=False, default=0)
    
    # Indexes for common queries
    __table_args__ = (
        Index("idx_product_sku", "sku"),
        Index("idx_product_stock", "stock_quantity"),
    )
    
    def __repr__(self) -> str:
        """String representation of ProductModel."""
        return f"<ProductModel(id={self.id}, sku='{self.sku}', stock={self.stock_quantity})>"
