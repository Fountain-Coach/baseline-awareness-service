# app/routers/drift.py

from fastapi import APIRouter
from app.schemas.drift import DriftRequest
from app.services.corpus_repository import ingest_drift

router = APIRouter()

@router.post(
    "",
    operation_id="addDrift",
    summary="Add Drift",
    description="Adds a drift document to the corpus.",
    response_model=dict
)
async def add_drift(payload: DriftRequest):
    await ingest_drift(payload.corpusId, payload.driftId, payload.content)
    return {"message": f"Drift '{payload.driftId}' added to corpus '{payload.corpusId}'."}
