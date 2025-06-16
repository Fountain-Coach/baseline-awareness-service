# src/baseline_service/schemas/summary.py

from pydantic import BaseModel
from typing import List, Tuple

class HistorySummaryResponse(BaseModel):
    summary: str

class HistoryListResponse(BaseModel):
    history: List[Tuple[str, str]]
    total:   int       # total number of entries in the corpus
    page:    int       # current page number
    per_page:int       # items per page
    pages:   int       # total number of pages
