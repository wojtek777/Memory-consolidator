from sqlalchemy import Column, Integer, Text
from app.db import Base
from app.db.timepoint import TimePointMixin

class Memory(Base):
    __tablename__ = "memories"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    type = Column(String)
    content = Column(Text)

class MemoryLink(Base):
    __tablename__ = "memory_links"

    from_id = Column(Integer, ForeignKey("memories.id"), primary_key=True)
    to_id = Column(Integer, ForeignKey("memories.id"), primary_key=True)
    relation = Column(String)

