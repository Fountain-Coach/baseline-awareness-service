# app/routers/patterns.py

from fastapi import APIRouter
from app.schemas.patterns import PatternsRequest
from app.services.corpus_repository import ingest_patterns

router = APIRouter()

@router.post(
    "",
    operation_id="addPatterns",
    summary="Add Patterns",
    description="Adds narrative patterns to the corpus.",
    response_model=dict
)
async def add_patterns(payload: PatternsRequest):
    await ingest_patterns(payload.corpusId, payload.patternsId, payload.content)
    return {"message": f"Patterns '{payload.patternsId}' added to corpus '{payload.corpusId}'."}
