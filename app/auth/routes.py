from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.db import SessionLocal
from app.auth.services import AuthService

router = APIRouter(prefix="/api/auth")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register(username: str, password: str, db: Session = Depends(get_db)):
    service = AuthService(db)
    user = service.register_user(username, password)
    return {"status": "ok", "username": user.username}

@router.post("/login")
def login(username: str, password: str, db: Session = Depends(get_db)):
    service = AuthService(db)
    user = service.login_user(username, password)
    return {"status": "ok", "username": user.username}

