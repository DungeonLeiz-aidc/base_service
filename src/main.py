"""
main.py

Main entry point for the FastAPI application.
Configures middleware, routes, and startup/shutdown lifecycle events.
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger

from configs.service_config import settings
from configs.logging_config import setup_logging
from src.container import get_container
from src.interface.http.api.v1 import orders


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Handle application startup and shutdown events.
    Ensures absolute resource integrity with try...finally blocks.
    """
    # 1. Initialize logging
    setup_logging(settings)
    logger.info(f"SYSTEM | START | {settings.PROJECT_NAME} starting...")
    
    container = get_container()
    
    try:
        # 2. Connect to Infrastructure
        try:
            await container.event_publisher.connect()
            logger.info("SYSTEM | SUCCESS | Connected to RabbitMQ")
        except Exception as e:
            logger.error(f"SYSTEM | FAILED | RabbitMQ connection: {e}")
        
        yield
        
    finally:
        # 3. Defensive Cleanup (Execution guaranteed on Ctrl+C)
        logger.info(f"SYSTEM | SHUTDOWN | {settings.PROJECT_NAME} stopping...")
        try:
            # Centralized disposal of DB, Redis, Messaging, and Logger
            await container.dispose()
        except Exception as e:
            import sys
            sys.stderr.write(f"AUDIT | CRITICAL | Global Shutdown Cleanup Failed: {str(e)}\n")


from src.interface.http.middlewares import (
    LoggingMiddleware,
    global_exception_handler,
    domain_exception_handler,
)
from src.domain.exceptions import DomainException


def create_app() -> FastAPI:
    """
    Application factory to create and configure the FastAPI instance.
    """
    app = FastAPI(
        title=settings.PROJECT_NAME,
        description="Clean Architecture Order Management System Template",
        version="0.1.0",
        lifespan=lifespan,
    )
    
    # Global Exception Handlers
    app.add_exception_handler(Exception, global_exception_handler)
    app.add_exception_handler(DomainException, domain_exception_handler)
    
    # Middlewares
    app.add_middleware(LoggingMiddleware)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Adjust in production via settings.CORS_ORIGINS
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # Register API Routes
    app.include_router(orders.router, prefix="/api/v1")
    
    @app.get("/health", tags=["Health"])
    async def health_check():
        """Health check endpoint."""
        return {"status": "healthy", "service": settings.PROJECT_NAME}
    
    return app


app = create_app()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "src.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
