from sqlalchemy.orm import Session
from app.auth.models import User
from app.auth.utils import hash_password, verify_password
from fastapi import HTTPException

class AuthService:
    def __init__(self, db: Session):
        self.db = db

    def register_user(self, username: str, password: str) -> User:
        # Check if user exists
        if self.db.query(User).filter(User.username == username).first():
            raise HTTPException(status_code=400, detail="User already exists")

        ### Data Mapper pattern ###
        # Create user
        user = User(
            username=username,
            password_hash=hash_password(password)
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)  # Load ID and other defaults
        return user

    def login_user(self, username: str, password: str) -> User:
        user = self.db.query(User).filter(User.username == username).first()
        if not user or not verify_password(password, user.password_hash):
            raise HTTPException(status_code=401, detail="Invalid credentials")
        return user

