from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter(prefix="/api")

# --- Models ---
class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]  # Full conversation from client

# --- Chat endpoint ---
@router.post("/chat")
def chat(req: ChatRequest):
    """
    Receives full conversation from client.
    Decides if a tool should be called or just respond via AI.
    """
    messages = req.messages
    last_msg = messages[-1].content if messages else ""

    tool_invoked = None
    if "sleep" in last_msg.lower():
        tool_invoked = "sleep"
        ai_reply = "AI going to sleep..."
    elif "remember" in last_msg.lower():
        tool_invoked = "memory_retrieve"
        ai_reply = "AI retrieving memory..."
    else:
        ai_reply = f"AI says: I received '{last_msg}'"

    return {
        "reply": ai_reply,
        "tool": tool_invoked
    }

