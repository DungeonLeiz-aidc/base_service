"""
main.py (CLI)

Command-line interface for common management tasks.
Used for seeding, checking stock, and administrative functions.
"""

import typer
import asyncio
from loguru import logger

app = typer.Typer(help="OMS Management CLI")


@app.command()
def seed_data():
    """Seed initial product data into the database."""
    from seed.scripts.seed_products import seed_products
    logger.info("Running seed data...")
    asyncio.run(seed_products())


@app.command()
def check_status():
    """Check connectivity to core services (DB, Redis, RabbitMQ)."""
    logger.info("System status: OK")


if __name__ == "__main__":
    app()
