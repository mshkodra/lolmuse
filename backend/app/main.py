from fastapi import FastAPI

from app.routers import polynomial

app = FastAPI()

app.include_router(polynomial.router)


@app.get("/health")
def health():
    return {"status": "ok"}
