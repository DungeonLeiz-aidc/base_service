"""
test_auth_provider.py

Unit tests for JWTAuthProvider.
Verifies token creation, verification, and expiration logic.
"""

import pytest
from datetime import timedelta
from jose import jwt
from src.infrastructure.clients.auth_provider import JWTAuthProvider

@pytest.fixture
def auth_provider():
    return JWTAuthProvider(
        secret_key="test-secret-key",
        algorithm="HS256",
        access_token_expire_minutes=1
    )

def test_create_access_token(auth_provider):
    """Should create a valid JWT token with the given payload."""
    data = {"sub": "user123", "role": "admin"}
    token = auth_provider.create_access_token(data)
    
    assert isinstance(token, str)
    
    # Manually decode to verify
    payload = jwt.decode(token, "test-secret-key", algorithms=["HS256"])
    assert payload["sub"] == "user123"
    assert payload["role"] == "admin"
    assert "exp" in payload

def test_verify_valid_token(auth_provider):
    """Should successfully verify and return the payload of a valid token."""
    data = {"sub": "user456"}
    token = auth_provider.create_access_token(data)
    
    payload = auth_provider.verify_token(token)
    assert payload["sub"] == "user456"

def test_verify_invalid_token(auth_provider):
    """Should raise ValueError for an invalid token."""
    with pytest.raises(ValueError, match="Invalid or expired token"):
        auth_provider.verify_token("invalid-token-string")

def test_verify_token_missing_subject(auth_provider):
    """Should raise ValueError if 'sub' claim is missing."""
    # Manually create token without 'sub'
    token = jwt.encode({"role": "guest"}, "test-secret-key", algorithm="HS256")
    
    with pytest.raises(ValueError, match="Token missing subject"):
        auth_provider.verify_token(token)

def test_token_expiration(auth_provider):
    """Should raise ValueError for an expired token."""
    # Create an already expired token
    auth_provider.expire_minutes = -1  # Expire 1 minute ago
    token = auth_provider.create_access_token({"sub": "expired-user"})
    
    with pytest.raises(ValueError, match="Signature has expired"):
        auth_provider.verify_token(token)
