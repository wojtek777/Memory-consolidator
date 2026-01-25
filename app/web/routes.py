from pathlib import Path
from fastapi import APIRouter
from fastapi.responses import HTMLResponse,RedirectResponse

router = APIRouter()

BASE_DIR = Path(__file__).resolve().parents[1]

@router.get("/")
def root():
    return RedirectResponse(url="/login", status_code=302)

@router.get("/login", response_class=HTMLResponse)
def login_page():
    return (BASE_DIR / "templates/login.html").read_text()

@router.get("/chat", response_class=HTMLResponse)
def chat_page():
    return (BASE_DIR / "templates/chat.html").read_text()

