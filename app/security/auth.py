# src/baseline_service/security/auth.py

import os
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

_scheme = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(_scheme)) -> str:
    """
    Validates the Authorization header against OPENAI_API_KEY.
    Raises 401 if missing or incorrect.
    Returns a dummy user identifier on success.
    """
    token = credentials.credentials
    expected = os.getenv("OPENAI_API_KEY")
    if not expected:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Server misconfiguration: missing OPENAI_API_KEY",
        )
    if token != expected:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # You could return more user info here; for now return the token itself
    return token
