from fastapi import APIRouter
from pydantic import BaseModel
import uuid

router = APIRouter(prefix="/api")

SESSIONS = {}

class ChatRequest(BaseModel):
    session_id: str
    message: str

@router.post("/session")
def create_session():
    session_id = str(uuid.uuid4())
    SESSIONS[session_id] = []
    return {"session_id": session_id}

@router.post("/chat")
def chat(req: ChatRequest):
    SESSIONS[req.session_id].append(("user", req.message))

    # AI stub (replace later with real Logical Processor)
    reply = f"AI says: I received '{req.message}'"

    SESSIONS[req.session_id].append(("assistant", reply))
    return {"reply": reply}

