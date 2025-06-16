# src/baseline_service/routers/health.py

from fastapi import APIRouter
from src.baseline_service.schemas.health import HealthOut

router = APIRouter()

@router.get(
    "",  # <-- here
    response_model=HealthOut,
    operation_id="getHealth",
    summary="Health Check",
    description=(
        "Simple endpoint to verify that the Baseline Awareness Service is up "
        "and running."
    ),
)
async def health_check():
    return HealthOut(status="ok")
