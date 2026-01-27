# app/api/consolidate.py
from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.chat.services import ChatService
from app.db import SessionLocal

router = APIRouter(prefix="/api")


class MessagesRequest(BaseModel):
    messages: list


# Temporary: no authentication
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/consolidate")
def consolidate(req: MessagesRequest, db=Depends(get_db)):
    chat_service = ChatService()

    # 1️⃣ Condense conversation into memories
    memories = chat_service.condense_memory(req.messages)

    # 2️⃣ Create identity stack
    identity_stack = chat_service.create_identity_stack(req.messages)

    # 3️⃣ Store memories (no user scoping yet)
    from app.chat.services import MemoryService
    memory_service = MemoryService(db)

    memory_service.store_memories(
        user_id=None,  # ← temporary
        memories=memories
    )

    memory_service.store_memories(
        user_id=None,
        memories=[{
            "type": "identity",
            "content": identity_stack
        }]
    )

    return {
        "status": "ok",
        "memories": len(memories),
        "identity_points": len(identity_stack)
    }

