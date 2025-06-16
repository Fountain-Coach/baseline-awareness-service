# app/routers/corpus_init.py

from fastapi import APIRouter, HTTPException
from app.schemas.corpus import InitIn, InitOut
from app.services.corpus_repository import initialize_corpus

router = APIRouter()

@router.post(
    "",
    operation_id="initializeCorpus",
    summary="Initialize Corpus",
    description="Creates a new corpus with the given corpus ID.",
    response_model=InitOut
)
async def init_corpus(payload: InitIn) -> InitOut:
    success = await initialize_corpus(payload.corpusId)
    if not success:
        raise HTTPException(
            status_code=400,
            detail=f"Corpus '{payload.corpusId}' already exists."
        )
    return InitOut(message=f"Corpus '{payload.corpusId}' initialized successfully.")
