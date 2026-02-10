"""
order_handler.py

gRPC service handler for Order management.
Maps gRPC requests to Application Use Cases.
"""

import grpc
from google.protobuf import timestamp_pb2
from loguru import logger

from src.application.dtos import PlaceOrderRequestDTO, OrderItemDTO
from src.application.service import PlaceOrderService
from src.interface.grpc.protos import order_pb2_grpc, order_pb2


class OrderHandler(order_pb2_grpc.OrderServiceServicer):
    """
    gRPC Handler for OrderService.
    
    This class implements the Order Service defined in the protobuf file.
    It acts as an adapter between gRPC and the Application layer.
    """

    def __init__(self, place_order_service: PlaceOrderService):
        """
        Initialize the OrderHandler.
        
        Args:
            place_order_service: The application service to handle order placement.
        """
        self.service = place_order_service
        logger.info("AUDIT | GRPC | OrderHandler initialized")

    async def PlaceOrder(self, request, context):
        """
        Handle PlaceOrder gRPC request.
        
        Args:
            request: The gRPC request object.
            context: The gRPC context.
            
        Returns:
            order_pb2.OrderResponse: The gRPC response object.
        """
        logger.info(f"AUDIT | GRPC | START | Placing order for customer {request.customer_id}")
        
        try:
            # Map gRPC request to Application DTO
            dto = PlaceOrderRequestDTO(
                customer_id=request.customer_id,
                items=[
                    OrderItemDTO(product_id=item.product_id, quantity=item.quantity)
                    for item in request.items
                ]
            )
            
            # Execute Use Case
            result = await self.service.execute(dto)
            
            # Map Domain result to gRPC response
            created_at = timestamp_pb2.Timestamp()
            created_at.FromDatetime(result.created_at)
            
            response = order_pb2.OrderResponse(
                id=result.id,
                customer_id=result.customer_id,
                total_amount=float(result.total_amount),
                status=result.status,
                created_at=created_at
            )
            
            logger.success(f"AUDIT | GRPC | SUCCESS | Order {result.id} placed")
            return response
            
        except Exception as e:
            logger.error(f"AUDIT | GRPC | FAILED | Order placement failed: {str(e)}")
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(str(e))
            return order_pb2.OrderResponse()
