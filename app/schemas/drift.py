# src/baseline_service/schemas/drift.py

from pydantic import BaseModel

class DriftRequest(BaseModel):
    corpusId: str
    driftId: str
    content: str

class DriftResponse(BaseModel):
    message: str
