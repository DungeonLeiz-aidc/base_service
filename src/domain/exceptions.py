"""
exceptions.py

Domain-specific exceptions for the Order Management System.
"""


class DomainException(Exception):
    """Base exception for all domain exceptions."""
    
    pass


# ==================== Product Exceptions ====================

class ProductNotFoundError(DomainException):
    """Raised when a product is not found."""
    
    def __init__(self, product_id: int | None = None, sku: str | None = None):
        if product_id:
            message = f"Product with ID {product_id} not found"
        elif sku:
            message = f"Product with SKU '{sku}' not found"
        else:
            message = "Product not found"
        super().__init__(message)
        self.product_id = product_id
        self.sku = sku


class InsufficientStockError(DomainException):
    """Raised when there is insufficient stock for a product."""
    
    def __init__(self, product_id: int, requested: int, available: int):
        message = (
            f"Insufficient stock for product {product_id}. "
            f"Requested: {requested}, Available: {available}"
        )
        super().__init__(message)
        self.product_id = product_id
        self.requested = requested
        self.available = available


class InvalidPriceError(DomainException):
    """Raised when a product price is invalid."""
    
    pass


# ==================== Order Exceptions ====================

class OrderNotFoundError(DomainException):
    """Raised when an order is not found."""
    
    def __init__(self, order_id: int):
        message = f"Order with ID {order_id} not found"
        super().__init__(message)
        self.order_id = order_id


class OrderValidationError(DomainException):
    """Raised when order validation fails."""
    
    pass


class InvalidOrderStatusTransitionError(DomainException):
    """Raised when an invalid order status transition is attempted."""
    
    def __init__(self, current_status: str, target_status: str):
        message = (
            f"Cannot transition order from status '{current_status}' "
            f"to '{target_status}'"
        )
        super().__init__(message)
        self.current_status = current_status
        self.target_status = target_status


class OrderAlreadyProcessedError(DomainException):
    """Raised when attempting to modify an order that has already been processed."""
    
    def __init__(self, order_id: int, status: str):
        message = f"Order {order_id} is already in '{status}' status and cannot be modified"
        super().__init__(message)
        self.order_id = order_id
        self.status = status


# ==================== Inventory Exceptions ====================

class InventoryLockError(DomainException):
    """Raised when unable to acquire inventory lock."""
    
    def __init__(self, product_id: int, reason: str = ""):
        message = f"Failed to acquire inventory lock for product {product_id}"
        if reason:
            message += f": {reason}"
        super().__init__(message)
        self.product_id = product_id


class InventoryReservationError(DomainException):
    """Raised when inventory reservation fails."""
    
    pass


# ==================== Customer Exceptions ====================

class CustomerNotFoundError(DomainException):
    """Raised when a customer is not found."""
    
    def __init__(self, customer_id: int):
        message = f"Customer with ID {customer_id} not found"
        super().__init__(message)
        self.customer_id = customer_id


# ==================== Payment Exceptions ====================

class PaymentFailedError(DomainException):
    """Raised when payment processing fails."""
    
    def __init__(self, reason: str):
        message = f"Payment failed: {reason}"
        super().__init__(message)
        self.reason = reason


# ==================== General Business Rule Violations ====================

class BusinessRuleViolationError(DomainException):
    """Raised when a business rule is violated."""
    
    pass
