from fastapi import APIRouter

from app.models.schema.health import HealthCheckResponse

router = APIRouter(prefix="/health", tags=["health"])

@router.get("/", response_model=HealthCheckResponse)
def get_app_health():
    return {"status": "ok"}