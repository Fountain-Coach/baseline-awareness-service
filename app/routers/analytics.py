# app/routers/analytics.py

from fastapi import APIRouter
from app.services.corpus_repository import list_history
from app.gpt_integration.semantic_arc_service import build_semantic_arc

router = APIRouter()

@router.get(
    "/history",
    operation_id="listHistory",
    summary="Read History",
    description="Retrieve the timeline of all semantic entries for the given corpus.",
    response_model=list  # or a more specific response schema later
)
async def history(corpus_id: str):
    return await list_history(corpus_id)

@router.get(
    "/semantic-arc",
    operation_id="readSemanticArc",
    summary="Read Semantic Arc",
    description="Construct and return the semantic arc based on the corpus history.",
    response_model=str
)
async def semantic_arc(corpus_id: str):
    return await build_semantic_arc(corpus_id)
