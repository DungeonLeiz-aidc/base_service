"""
order_service.py

PlaceOrderService - Core use case for order placement.
Orchestrates product validation, inventory reservation, order creation, and event publishing.
"""

from datetime import datetime, timezone, timezone
from typing import Protocol, List
from loguru import logger

from src.domain.entities import Product, Order, OrderItem, OrderStatus
from src.domain.events import OrderPlaced, OrderFailed
from src.domain.exceptions import (
    ProductNotFoundError,
    InsufficientStockError,
    InventoryLockError,
    OrderValidationError,
)
from src.application.dtos import PlaceOrderRequestDTO, OrderResponseDTO
from src.interface.protocols.repositories import IProductRepository, IOrderRepository
from src.interface.protocols.infrastructure import IInventoryCache, IEventPublisher




class PlaceOrderService:
    """
    Use case: Place a new order.
    
    This service orchestrates the order placement process:
    1. Validate products exist
    2. Check and reserve inventory (Redis with distributed locking)
    3. Create order entity
    4. Persist to database (PostgreSQL)
    5. Publish OrderPlaced event (RabbitMQ)
    
    If any step fails, it rolls back reservations and publishes OrderFailed event.
    """
    
    def __init__(
        self,
        product_repository: IProductRepository,
        order_repository: IOrderRepository,
        inventory_cache: IInventoryCache,
        event_publisher: IEventPublisher,
    ):
        """
        Initialize PlaceOrderService.
        
        Args:
            product_repository: Repository for product data access.
            order_repository: Repository for order data access.
            inventory_cache: Redis cache for inventory management.
            event_publisher: Service to publish domain events.
        """
        self.product_repo = product_repository
        self.order_repo = order_repository
        self.inventory_cache = inventory_cache
        self.event_publisher = event_publisher
    
    async def execute(self, request: PlaceOrderRequestDTO) -> OrderResponseDTO:
        """
        Execute the place order use case.
        
        Args:
            request: DTO containing order request data.
            
        Returns:
            OrderResponseDTO with created order details.
            
        Raises:
            ProductNotFoundError: If any product is not found.
            InsufficientStockError: If any product has insufficient stock.
            OrderValidationError: If order validation fails.
            InventoryLockError: If unable to acquire inventory lock.
        """
        logger.info(
            f"AUDIT | START | Placing order for customer {request.customer_id} "
            f"with {len(request.items)} items"
        )
        
        reserved_items: List[tuple[int, int]] = []  # (product_id, quantity)
        
        try:
            # Step 1: Fetch and validate products (Workflow)
            logger.debug("STEP 1 | Validating products")
            products = await self._fetch_and_validate_products(request)
            
            # Step 2: Check and reserve inventory
            logger.debug("STEP 2 | Reserving inventory")
            reserved_items = await self._reserve_inventory(request, products)
            
            # Step 3: Create order entity
            logger.debug("STEP 3 | Creating order entity")
            order = self._create_order_entity(request, products)
            
            # Step 4: Persist order
            logger.debug("STEP 4 | Persisting order to database")
            saved_order = await self.order_repo.save(order)
            
            # Step 5: Publish Side Effects
            logger.debug("STEP 5 | Publishing OrderPlaced event")
            await self._publish_order_placed_event(saved_order)
            
            logger.success(
                f"AUDIT | SUCCESS | Order {saved_order.id} placed for customer "
                f"{request.customer_id}. Total: {saved_order.total_amount}"
            )
            
            return OrderResponseDTO.from_entity(saved_order)
            
        except (ProductNotFoundError, InsufficientStockError) as e:
            # Domain Errors are already friendly, just re-raise
            logger.warning(f"AUDIT | BUSINESS_ERROR | {e}")
            await self._rollback_reservations(reserved_items)
            raise e
            
        except Exception as e:
            # Step 6: Error Translation (Fulfills Core Responsibility 4)
            logger.error(f"AUDIT | FAILED | Unexpected error: {e}. Starting rollback.")
            await self._rollback_reservations(reserved_items)
            
            # Wrap technical error into a business-level failure
            error_msg = f"System error during order placement: {str(e)}"
            await self._publish_order_failed_event(request.customer_id, error_msg)
            
            # We raise a Domain-level exception for the Interface layer to handle
            raise OrderValidationError(error_msg)
            
            # Re-raise the exception
            raise
    
    async def _fetch_and_validate_products(
        self, request: PlaceOrderRequestDTO
    ) -> dict[int, Product]:
        """
        Fetch products from repository and validate they exist.
        
        Args:
            request: Order request DTO.
            
        Returns:
            Dictionary mapping product_id to Product entity.
            
        Raises:
            ProductNotFoundError: If any product is not found.
        """
        product_ids = [item.product_id for item in request.items]
        products = await self.product_repo.get_many_by_ids(product_ids)
        
        # Create lookup map
        product_map = {p.id: p for p in products}
        
        # Validate all products were found
        for product_id in product_ids:
            if product_id not in product_map:
                raise ProductNotFoundError(product_id=product_id)
        
        return product_map
    
    async def _reserve_inventory(
        self,
        request: PlaceOrderRequestDTO,
        products: dict[int, Product],
    ) -> List[tuple[int, int]]:
        """
        Reserve inventory for all order items.
        
        Uses Redis distributed locking to prevent overselling.
        
        Args:
            request: Order request DTO.
            products: Map of product_id to Product entity.
            
        Returns:
            List of (product_id, quantity) tuples that were successfully reserved.
            
        Raises:
            InsufficientStockError: If stock is insufficient for any product.
            InventoryLockError: If unable to acquire lock.
        """
        reserved: List[tuple[int, int]] = []
        
        try:
            for item in request.items:
                product = products[item.product_id]
                
                # Check and reserve in Redis (with distributed lock)
                success = await self.inventory_cache.check_and_reserve_stock(
                    product_id=item.product_id,
                    quantity=item.quantity
                )
                
                if not success:
                    # Stock insufficient or lock failed
                    raise InsufficientStockError(
                        product_id=item.product_id,
                        requested=item.quantity,
                        available=product.stock_quantity,
                    )
                
                reserved.append((item.product_id, item.quantity))
                
                logger.debug(
                    f"Reserved {item.quantity} units of product {item.product_id}"
                )
            
            return reserved
            
        except Exception:
            # If any reservation fails, release all previous reservations
            for product_id, quantity in reserved:
                await self.inventory_cache.release_stock(product_id, quantity)
            raise
    
    def _create_order_entity(
        self,
        request: PlaceOrderRequestDTO,
        products: dict[int, Product],
    ) -> Order:
        """
        Create Order domain entity from request.
        
        Args:
            request: Order request DTO.
            products: Map of product_id to Product entity.
            
        Returns:
            Order domain entity.
            
        Raises:
            OrderValidationError: If order validation fails.
        """
        try:
            order_items = [
                OrderItem(
                    product_id=item.product_id,
                    product_sku=products[item.product_id].sku,
                    product_name=products[item.product_id].name,
                    quantity=item.quantity,
                    unit_price=products[item.product_id].price,
                )
                for item in request.items
            ]
            
            order = Order(
                id=None,  # Not yet persisted
                customer_id=request.customer_id,
                items=order_items,
                status=OrderStatus.PENDING,
            )
            
            return order
            
        except ValueError as e:
            raise OrderValidationError(str(e)) from e
    
    async def _publish_order_placed_event(self, order: Order) -> None:
        """
        Publish OrderPlaced event to message broker.
        
        Args:
            order: Saved order entity.
        """
        event = OrderPlaced(
            order_id=order.id,
            customer_id=order.customer_id,
            total_amount=order.total_amount,
            items_count=order.total_items,
            placed_at=datetime.now(timezone.utc),
        )
        
        await self.event_publisher.publish(event)
        logger.info(f"Published OrderPlaced event for order {order.id}")
    
    async def _publish_order_failed_event(
        self, customer_id: int, reason: str
    ) -> None:
        """
        Publish OrderFailed event to message broker.
        
        Args:
            customer_id: Customer ID.
            reason: Failure reason.
        """
        event = OrderFailed(
            order_id=0,  # Order was not created
            customer_id=customer_id,
            reason=reason,
            failed_at=datetime.now(timezone.utc),
        )
        
        await self.event_publisher.publish(event)
        logger.warning(f"Published OrderFailed event for customer {customer_id}")
    
    async def _rollback_reservations(
        self, reserved_items: List[tuple[int, int]]
    ) -> None:
        """
        Release all reserved inventory.
        
        Args:
            reserved_items: List of (product_id, quantity) tuples to release.
        """
        for product_id, quantity in reserved_items:
            try:
                await self.inventory_cache.release_stock(product_id, quantity)
                logger.debug(
                    f"Released {quantity} units of product {product_id}"
                )
            except Exception as e:
                logger.error(
                    f"Failed to release stock for product {product_id}: {e}"
                )
