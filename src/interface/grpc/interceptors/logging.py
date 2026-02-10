"""
logging.py

gRPC interceptor for logging request and response information.
"""

import time
import grpc
from loguru import logger


class LoggingInterceptor(grpc.aio.ServerInterceptor):
    """
    gRPC Server Interceptor for logging requests.
    """

    async def intercept_service(self, continuation, handler_call_details):
        """
        Intercept the gRPC service call and log details.
        """
        method = handler_call_details.method
        start_time = time.time()
        
        logger.info(f"AUDIT | GRPC | REQUEST | Method: {method}")
        
        try:
            response = await continuation(handler_call_details)
            duration = (time.time() - start_time) * 1000
            logger.success(f"AUDIT | GRPC | SUCCESS | Method: {method} | Duration: {duration:.2f}ms")
            return response
        except Exception as e:
            duration = (time.time() - start_time) * 1000
            logger.error(f"AUDIT | GRPC | FAILED | Method: {method} | Error: {str(e)} | Duration: {duration:.2f}ms")
            raise e
