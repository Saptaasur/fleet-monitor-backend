from fastapi import FastAPI
from app.routes import api, websocket

app = FastAPI()

app.include_router(api.router, prefix="/api")
app.include_router(websocket.router)
