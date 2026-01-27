from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.web.routes import router as web_router
from app.api.chat import router as chat_router
from app.db import engine, Base
from app.auth.routes import router as auth_router

app = FastAPI(title="Memory Consolidator")
Base.metadata.create_all(bind=engine)

app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(web_router)
app.include_router(chat_router)
app.include_router(auth_router)

