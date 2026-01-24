"""
Manual test script for concurrency issues (overselling).
Simulates multiple concurrent requests for the same product.
"""

import asyncio
import httpx
import time

BASE_URL = "http://localhost:8000/api/v1"
PRODUCT_ID = 1  # Standard Laptop in seed data
CONCURRENT_REQUESTS = 10

async def place_single_order(client, customer_id):
    order_data = {
        "customer_id": customer_id,
        "items": [
            {"product_id": PRODUCT_ID, "quantity": 1}
        ]
    }
    
    start_time = time.time()
    try:
        response = await client.post(f"{BASE_URL}/orders", json=order_data)
        duration = time.time() - start_time
        return response.status_code, duration
    except Exception as e:
        return str(e), 0

async def run_concurrency_test():
    print(f"Simulating {CONCURRENT_REQUESTS} concurrent orders for product {PRODUCT_ID}...")
    
    async with httpx.AsyncClient() as client:
        tasks = [place_single_order(client, i) for i in range(CONCURRENT_REQUESTS)]
        results = await asyncio.gather(*tasks)
    
    success_count = sum(1 for status, _ in results if status == 201)
    failed_count = sum(1 for status, _ in results if status == 400) # Insufficient stock
    other_count = CONCURRENT_REQUESTS - success_count - failed_count
    
    print("\nTest Results:")
    print(f"- Success (201): {success_count}")
    print(f"- Failed (Stock/Lock) (400): {failed_count}")
    print(f"- Other: {other_count}")
    
    if success_count > 0:
        print("\nNote: Check database stock and Redis items to verify no over-selling occurred.")

if __name__ == "__main__":
    asyncio.run(run_concurrency_test())
