# app/routers/baseline.py

from fastapi import APIRouter
from app.schemas.baseline import BaselineRequest
from app.services.corpus_repository import ingest_baseline

router = APIRouter()

@router.post(
    "",
    operation_id="addBaseline",
    summary="Add Baseline",
    description="Adds a baseline text to the corpus.",
    response_model=dict
)
async def add_baseline(payload: BaselineRequest):
    await ingest_baseline(payload.corpusId, payload.baselineId, payload.content)
    return {
        "message": f"Baseline '{payload.baselineId}' added to corpus '{payload.corpusId}'."
    }
