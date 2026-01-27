from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Optional

from app.chat.services import ChatService

router = APIRouter(prefix="/api")

# --- Models ---
class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]

# --- Chat endpoint ---
@router.post("/chat")
def chat(req: ChatRequest):
    """
    Receives full conversation from client.
    Delegates reply generation to ChatService.
    """
    service = ChatService()

    messages = [m.dict() for m in req.messages]

    last_msg = messages[-1]["content"] if messages else ""
    tool_invoked = None

    if "sleep" in last_msg.lower():
        tool_invoked = "sleep"
        reply = "AI going to sleep..."
    else:
        reply = service.reply(messages)

    return {
        "reply": reply,
        "tool": tool_invoked
    }

