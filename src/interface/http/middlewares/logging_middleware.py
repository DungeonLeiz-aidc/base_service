"""
logging_middleware.py

Middleware to log every HTTP request and response.
Provides observability into API traffic.
"""

import time
from fastapi import Request
from loguru import logger
from starlette.middleware.base import BaseHTTPMiddleware


class LoggingMiddleware(BaseHTTPMiddleware):
    """
    Middleware for logging HTTP requests and responses.
    """
    
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        
        # Log request
        logger.info(f"Incoming request: {request.method} {request.url.path}")
        
        response = await call_next(request)
        
        process_time = (time.time() - start_time) * 1000
        
        # Log response
        logger.info(
            f"Response: {response.status_code} "
            f"Duration: {process_time:.2f}ms"
        )
        
        return response
