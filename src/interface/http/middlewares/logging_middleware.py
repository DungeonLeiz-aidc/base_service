"""
logging_middleware.py

Middleware to log every HTTP request and response.
Provides observability into API traffic.
"""

import time
from fastapi import Request
from loguru import logger
from starlette.middleware.base import BaseHTTPMiddleware


import time
import json
from typing import Any, Dict
from fastapi import Request
from loguru import logger
from starlette.middleware.base import BaseHTTPMiddleware


class LoggingMiddleware(BaseHTTPMiddleware):
    """
    Middleware for logging HTTP requests and responses.
    Features PII masking for sensitive data.
    """
    
    SENSITIVE_FIELDS = {"email", "customer_id", "credit_card", "password", "token"}

    def _mask_pii(self, data: Any) -> Any:
        """
        Recursively mask PII in dictionary or list.
        """
        if isinstance(data, dict):
            return {
                k: ("***MASKED***" if k.lower() in self.SENSITIVE_FIELDS else self._mask_pii(v))
                for k, v in data.items()
            }
        elif isinstance(data, list):
            return [self._mask_pii(item) for item in data]
        return data

    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        
        # Capture basic info
        method = request.method
        path = request.url.path
        query_params = dict(request.query_params)
        
        # Mask sensitive query params
        masked_query = self._mask_pii(query_params)
        
        logger.info(f"Incoming request: {method} {path} | Params: {masked_query}")
        
        # We don't log body here by default to avoid performance hit and complex stream handling
        # but the masking infrastructure is ready for it.
        
        response = await call_next(request)
        
        process_time = (time.time() - start_time) * 1000
        
        logger.info(
            f"Response: {method} {path} | Status: {response.status_code} | "
            f"Duration: {process_time:.2f}ms"
        )
        
        return response
