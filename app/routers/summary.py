# app/routers/summary.py

from fastapi import APIRouter, Query
from app.schemas.summary import (
    HistoryListResponse,
    HistorySummaryResponse,
)
from app.services.corpus_repository import list_history
from app.services.summary_service import summarize_history

router = APIRouter()

@router.get(
    "/history/{corpus_id}",
    operation_id="listHistory",
    summary="List History",
    description="Lists the change history of the specified corpus, paginated.",
    response_model=HistoryListResponse
)
async def list_history_route(
    corpus_id: str,
    page: int = Query(1, ge=1, le=1000, description="Page number"),
    per_page: int = Query(50, ge=1, le=500, description="Items per page (max 500)"),
):
    all_entries = await list_history(corpus_id)
    total = len(all_entries)
    start = (page - 1) * per_page
    end = start + per_page
    page_entries = all_entries[start:end]
    pages = (total + per_page - 1) // per_page

    return HistoryListResponse(
        history=page_entries,
        total=total,
        page=page,
        per_page=per_page,
        pages=pages,
    )

@router.get(
    "/{corpus_id}",
    operation_id="summarizeHistory",
    summary="Summarize History",
    description="Provides a semantic summary of the corpus history.",
    response_model=HistorySummaryResponse
)
async def summarize_history_route(corpus_id: str):
    summary = await summarize_history(corpus_id)
    return HistorySummaryResponse(summary=summary)
