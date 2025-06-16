# src/baseline_service/schemas/baseline.py

from pydantic import BaseModel

class BaselineRequest(BaseModel):
    corpusId: str
    baselineId: str
    content: str

class BaselineResponse(BaseModel):
    message: str
