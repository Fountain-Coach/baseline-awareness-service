# src/baseline_service/schemas/patterns.py

from pydantic import BaseModel

class PatternsRequest(BaseModel):
    corpusId: str
    patternsId: str
    content: str

class PatternsResponse(BaseModel):
    message: str
