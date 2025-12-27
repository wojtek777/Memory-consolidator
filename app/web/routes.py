from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from pathlib import Path

router = APIRouter()

BASE_DIR = Path(__file__).resolve().parent.parent

@router.get("/login", response_class=HTMLResponse)
def login_page():
    return (BASE_DIR / "templates/login.html").read_text()

@router.get("/chat", response_class=HTMLResponse)
def chat_page():
    return (BASE_DIR / "templates/chat.html").read_text()

