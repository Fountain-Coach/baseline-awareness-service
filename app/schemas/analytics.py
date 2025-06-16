"""DTOs for analytics endpoints."""
from pydantic import BaseModel
from typing import List, Literal

class HistoryEntry(BaseModel):
    type: Literal["baseline", "drift", "patterns", "reflection"]
    id: str

class SemanticArcResponse(BaseModel):
    semanticArc: str
