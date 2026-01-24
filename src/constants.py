"""
constants.py

Application-wide constants for the Order Management System.
Includes status codes, event types, and default values.
"""

from enum import Enum


class AppEnv(str, Enum):
    """Application environment enumeration."""
    DEV = "development"
    STAGING = "staging"
    PROD = "production"


class EventTypes(str, Enum):
    """Domain event types for messaging."""
    ORDER_PLACED = "order.placed"
    ORDER_CONFIRMED = "order.confirmed"
    ORDER_FAILED = "order.failed"
    STOCK_UPDATED = "stock.updated"


# Database constants
PAGE_SIZE_DEFAULT = 20
PAGE_SIZE_MAX = 100

# Cache TTLs (in seconds)
CACHE_TTL_PRODUCT = 3600
CACHE_TTL_ORDER = 600
