# app/auth/dependencies.py
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.auth.models import User


security = HTTPBearer()  # Basic token extraction

# --- DB dependency ---
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- Current user dependency ---
def current_user(credentials: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)):
    """
    Returns the current logged-in user based on token.
    For now, we will use a stub token "fake-jwt".
    Later, replace with real JWT decoding.
    """
    token = credentials.credentials

    if token != "fake-jwt":
        raise HTTPException(status_code=401, detail="Invalid or missing token")

    # For prototype, always return first user in DB
    user = db.query(User).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user

