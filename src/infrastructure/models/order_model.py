"""
order_model.py

SQLAlchemy ORM models for Order and OrderItem.
"""

from datetime import datetime
from sqlalchemy import (
    Column,
    Integer,
    String,
    Numeric,
    DateTime,
    ForeignKey,
    Index,
)
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class OrderModel(Base):
    """
    Order ORM model for PostgreSQL.
    
    Represents orders table in database.
    """
    
    __tablename__ = "orders"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, nullable=False, index=True)
    status = Column(String(20), nullable=False, default="pending", index=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationship to order items
    items = relationship("OrderItemModel", back_populates="order", cascade="all, delete-orphan")
    
    # Indexes for common queries
    __table_args__ = (
        Index("idx_order_customer", "customer_id"),
        Index("idx_order_status", "status"),
        Index("idx_order_created", "created_at"),
    )
    
    def __repr__(self) -> str:
        """String representation of OrderModel."""
        return f"<OrderModel(id={self.id}, customer_id={self.customer_id}, status='{self.status}')>"


class OrderItemModel(Base):
    """
    OrderItem ORM model for PostgreSQL.
    
    Represents order_items table in database.
    """
    
    __tablename__ = "order_items"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id", ondelete="CASCADE"), nullable=False)
    product_id = Column(Integer, nullable=False, index=True)
    product_sku = Column(String(50), nullable=False)
    product_name = Column(String(255), nullable=False)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Numeric(10, 2), nullable=False)
    
    # Relationship to order
    order = relationship("OrderModel", back_populates="items")
    
    # Indexes
    __table_args__ = (
        Index("idx_order_item_order", "order_id"),
        Index("idx_order_item_product", "product_id"),
    )
    
    def __repr__(self) -> str:
        """String representation of OrderItemModel."""
        return (
            f"<OrderItemModel(id={self.id}, order_id={self.order_id}, "
            f"product_id={self.product_id}, quantity={self.quantity})>"
        )
