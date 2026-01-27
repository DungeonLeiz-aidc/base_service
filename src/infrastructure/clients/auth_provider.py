"""
infrastructure/clients/auth_provider.py

Hybrid Infrastructure client for the Supabase Auth Service.
Features:
1. Local Validation: Uses SUPABASE_JWT_SECRET for instant signature checks.
2. Remote Authorization: Calls Auth Service for centralized RBAC/Permission checks.
"""

import httpx
from loguru import logger
from typing import Dict, Any, Optional
from jose import jwt, JWTError
from src.interface.protocols.infrastructure import IAuthProvider


class AuthProvider(IAuthProvider):
    """Hybrid client for Authentication (Local) and Authorization (Remote)."""

    def __init__(self, base_url: str, api_key: str, jwt_secret: str):
        self.base_url = base_url.rstrip("/")
        self.headers = {
            "X-Internal-API-Key": api_key,
            "Content-Type": "application/json"
        }
        self.jwt_secret = jwt_secret

    async def verify_token(self, token: str) -> Optional[Dict[str, Any]]:
        """
        Verify a JWT token. 
        PERFORMANCE: Performs local signature validation first.
        """
        try:
            # 1. Local Signature Validation (Ultra-fast)
            payload = jwt.decode(
                token, 
                self.jwt_secret, 
                algorithms=["HS256"], 
                audience="authenticated"
            )
            
            # Extract basic info
            user_id = payload.get("sub")
            logger.success(f"Audit: Token verified LOCALLY for user {user_id}")
            return payload
            
        except JWTError as e:
            logger.warning(f"Audit: Local token verification failed: {str(e)}")
            return None
        except Exception as e:
            logger.error(f"Audit: Unexpected error during local verification: {str(e)}")
            return None

    async def authorize(self, token: str, required_permission: str) -> bool:
        """
        Check if a user has a specific permission.
        CONSISTENCY: Calls central Auth Service for single point of truth.
        """
        url = f"{self.base_url}/api/v1/internal/authorize"
        payload = {
            "token": token,
            "required_permission": required_permission
        }

        try:
            async with httpx.AsyncClient(timeout=5.0) as client:
                logger.debug(f"Action: Checking permission '{required_permission}' for token")
                response = await client.post(url, json=payload, headers=self.headers)
                
                if response.status_code == 200:
                    data = response.json()
                    is_authorized = data.get("is_authorized", False)
                    return is_authorized
                
                logger.warning(f"Audit: Authorization check failed | Status: {response.status_code}")
                return False
        except Exception as e:
            logger.error(f"Audit: Error communicating with Auth Service for authorization: {str(e)}")
            return False
