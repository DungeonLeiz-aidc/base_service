"""
auth_provider.py

JWT-based implementation of IAuthProvider.
Handles creation and verification of JSON Web Tokens for secure communication.
"""

from datetime import datetime, timedelta, timezone
from typing import Dict, Optional
from jose import JWTError, jwt
from loguru import logger

from src.interface.protocols.infrastructure import IAuthProvider


class JWTAuthProvider(IAuthProvider):
    """
    JWT Authentication Provider.
    
    Provides services for generating and validating access tokens using
    HMAC with SHA-256 (HS256) algorithm.
    """

    def __init__(
        self,
        secret_key: str,
        algorithm: str = "HS256",
        access_token_expire_minutes: int = 30,
    ):
        """
        Initialize JWT Auth Provider.

        Args:
            secret_key: Secret key used for signing tokens.
            algorithm: Algorithm used for signing (default: HS256).
            access_token_expire_minutes: Token expiration time in minutes.
        """
        self.secret_key = secret_key
        self.algorithm = algorithm
        self.expire_minutes = access_token_expire_minutes

    def create_access_token(self, data: dict) -> str:
        """
        Create a new JWT access token.

        Args:
            data: Payload data to encode in the token.

        Returns:
            Encoded JWT token string.
        """
        logger.debug(f"AUDIT | Creating access token for payload: {data.get('sub', 'unknown')}")
        
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + timedelta(minutes=self.expire_minutes)
        to_encode.update({"exp": expire})
        
        encoded_jwt = jwt.encode(to_encode, self.secret_key, algorithm=self.algorithm)
        return encoded_jwt

    def verify_token(self, token: str) -> dict:
        """
        Verify the validity of a JWT token and extract its payload.

        Args:
            token: Encoded JWT token string.

        Returns:
            Dictionary containing the decoded payload.

        Raises:
            ValueError: If the token is invalid or expired.
        """
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            subject: Optional[str] = payload.get("sub")
            
            if subject is None:
                raise ValueError("Token missing subject (sub) claim")
            
            logger.debug(f"AUDIT | Token verified for subject: {subject}")
            return payload
            
        except JWTError as e:
            error_msg = f"Invalid or expired token: {str(e)}"
            logger.warning(f"AUDIT | FAILED | {error_msg}")
            raise ValueError(error_msg) from e
