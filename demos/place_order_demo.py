"""
Demo script to place an order via the FastAPI HTTP API.
"""

import httpx
import asyncio
import json

BASE_URL = "http://localhost:8000/api/v1"

async def place_order_demo():
    async with httpx.AsyncClient() as client:
        # 1. Place an order
        order_data = {
            "customer_id": 123,
            "items": [
                {"product_id": 1, "quantity": 2},
                {"product_id": 2, "quantity": 1}
            ]
        }
        
        print(f"Placing order: {json.dumps(order_data, indent=2)}")
        try:
            response = await client.post(f"{BASE_URL}/orders", json=order_data)
            if response.status_code == 201:
                print("✅ Order placed successfully!")
                print(json.dumps(response.json(), indent=2))
            else:
                print(f"❌ Failed to place order: {response.status_code}")
                print(response.text)
        except Exception as e:
            print(f"❌ Connection error: {e}")

if __name__ == "__main__":
    asyncio.run(place_order_demo())
