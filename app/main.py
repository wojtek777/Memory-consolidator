from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.web.routes import router as web_router
from app.api.chat import router as chat_router

app = FastAPI(title="Basic AI Chat")

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(web_router)
app.include_router(chat_router)

