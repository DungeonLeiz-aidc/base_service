"""
main.py (CLI)

Command-line interface for common management tasks.
Engineered for ultimate transparency and reliability according to Perfectionist standards.
Includes real-time health diagnostics and audit-ready logging.
"""

import asyncio
import os
import typer
from loguru import logger
from sqlalchemy import select
from typing import Dict, Any

from src.container import get_container
from configs.service_config import settings

# Initialize Typer App
app = typer.Typer(
    help="OMS Management CLI - Perfectionist Edition",
    add_completion=False,
    rich_markup_mode="rich"
)


async def _check_db(container) -> str:
    """Perform actual database connectivity test."""
    try:
        async with container.session_factory() as session:
            await session.execute(select(1))
        return "OK"
    except Exception as e:
        logger.error(f"AUDIT | DB Health Check Failed: {e}")
        return f"FAILED: {e}"


async def _check_redis(container) -> str:
    """Perform actual Redis connectivity test."""
    try:
        await container.redis.ping()
        return "OK"
    except Exception as e:
        logger.error(f"AUDIT | Redis Health Check Failed: {e}")
        return f"FAILED: {e}"


async def _check_rabbitmq(container) -> str:
    """Perform actual RabbitMQ connectivity test."""
    try:
        # Event publisher already has connect/close logic
        await container.event_publisher.connect()
        await container.event_publisher.close()
        return "OK"
    except Exception as e:
        logger.error(f"AUDIT | RabbitMQ Health Check Failed: {e}")
        return f"FAILED: {e}"


@app.command()
def seed_data():
    """
    Seed initial product data into the database.
    """
    from configs.logging_config import setup_logging
    setup_logging(settings)
    
    logger.info("AUDIT | START | COMMAND: seed-data")
    
    async def run_seed():
        container = get_container()
        try:
            async with container.session_factory() as session:
                service = container.seed_service(session)
                seed_file = os.path.join(os.getcwd(), "seed", "products.json")
                result = await service.seed_products_from_json(seed_file)
                return result
        finally:
            await container.dispose()
            
    try:
        result = asyncio.run(run_seed())
        typer.secho(
            f"✅ Seeding Successful: Created {result['created']}, Updated {result['updated']}",
            fg=typer.colors.GREEN,
            bold=True
        )
        logger.info(f"AUDIT | SUCCESS | COMMAND: seed-data | Result: {result}")
    except Exception as e:
        typer.secho(f"❌ Seeding Failed: {e}", fg=typer.colors.RED, bold=True)
        logger.error(f"AUDIT | FAILED | COMMAND: seed-data | Error: {e}")


@app.command()
def check_status():
    """
    Execute exhaustive health diagnostics for all core services.
    """
    from configs.logging_config import setup_logging
    setup_logging(settings)
    
    logger.info("AUDIT | START | COMMAND: check-status")
    
    async def run_diagnostics():
        container = get_container()
        
        try:
            # Run all checks concurrently for maximum efficiency
            db_task = _check_db(container)
            redis_task = _check_redis(container)
            rmq_task = _check_rabbitmq(container)
            
            results = await asyncio.gather(db_task, redis_task, rmq_task)
            return {
                "Database": results[0],
                "Redis": results[1],
                "RabbitMQ": results[2]
            }
        finally:
            await container.dispose()

    try:
        results = asyncio.run(run_diagnostics())
        
        typer.secho("\n🔍 [bold]Detailed System Health Report:[/bold]", fg=typer.colors.CYAN)
        
        all_ok = True
        for service, status in results.items():
            color = typer.colors.GREEN if status == "OK" else typer.colors.RED
            icon = "✅" if status == "OK" else "❌"
            if status != "OK":
                all_ok = False
            typer.echo(f"  {icon} {service:10}: ", nl=False)
            typer.secho(status, fg=color, bold=(status != "OK"))
            
        if all_ok:
            logger.info("AUDIT | SUCCESS | COMMAND: check-status | All systems operational.")
        else:
            logger.warning("AUDIT | WARNING | COMMAND: check-status | Partial system failure detected.")
            
    except Exception as e:
        typer.secho(f"❌ Diagnostic logic failed: {e}", fg=typer.colors.RED, bold=True)
        logger.error(f"AUDIT | FAILED | COMMAND: check-status | Logic Error: {e}")


if __name__ == "__main__":
    app()
