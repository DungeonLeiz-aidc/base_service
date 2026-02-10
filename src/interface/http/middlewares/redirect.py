"""
redirect.py

FastAPI middleware to enforce HTTPS by redirecting HTTP requests.
"""

from fastapi import Request
from fastapi.responses import RedirectResponse
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from loguru import logger


class HTTPSRedirectMiddleware(BaseHTTPMiddleware):
    """
    Middleware to redirect all HTTP requests to HTTPS.
    """

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint):
        """
        Check request scheme and redirect if it's HTTP.
        """
        # In production environments (behind proxy), check X-Forwarded-Proto
        x_forwarded_proto = request.headers.get("x-forwarded-proto")
        
        if request.url.scheme == "http" or x_forwarded_proto == "http":
            url = request.url.replace(scheme="https")
            logger.info(f"AUDIT | HTTP | REDIRECT | {request.url} -> {url}")
            return RedirectResponse(url, status_code=301)
            
        return await call_next(request)
