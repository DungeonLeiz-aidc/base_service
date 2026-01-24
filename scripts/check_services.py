"""
Script to check the status of external services (PostgreSQL, Redis, RabbitMQ).
"""

import asyncio
import sys
from sqlalchemy.ext.asyncio import create_async_engine
from redis import asyncio as aioredis
import aio_pika
from configs.service_config import settings

async def check_postgres():
    try:
        engine = create_async_engine(settings.DATABASE_URL)
        async with engine.connect() as conn:
            await conn.execute("SELECT 1")
        print("✅ PostgreSQL is UP")
        await engine.dispose()
        return True
    except Exception as e:
        print(f"❌ PostgreSQL is DOWN: {e}")
        return False

async def check_redis():
    try:
        redis = aioredis.from_url(settings.REDIS_URL)
        await redis.ping()
        print("✅ Redis is UP")
        await redis.close()
        return True
    except Exception as e:
        print(f"❌ Redis is DOWN: {e}")
        return False

async def check_rabbitmq():
    try:
        connection = await aio_pika.connect_robust(settings.RABBITMQ_URL)
        async with connection:
            print("✅ RabbitMQ is UP")
        return True
    except Exception as e:
        print(f"❌ RabbitMQ is DOWN: {e}")
        return False

async def main():
    print("Checking services...")
    results = await asyncio.gather(
        check_postgres(),
        check_redis(),
        check_rabbitmq()
    )
    if all(results):
        print("\nAll services are up and running!")
    else:
        print("\nSome services are down. Please check your configuration.")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())
