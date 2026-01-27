### Data Mapper pattern

from sqlalchemy import Column, Integer, String
from app.db import Base
from app.db.timepoint import TimePointMixin

class User(TimePointMixin, Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, index=True)
    password_hash = Column(String)

