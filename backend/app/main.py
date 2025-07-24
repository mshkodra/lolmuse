from fastapi import FastAPI
from app.api import api_router

app = FastAPI(title="Lol Muse API")
app.include_router(api_router, prefix="/api/v1")