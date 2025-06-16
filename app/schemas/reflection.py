# src/baseline_service/schemas/reflection.py

from pydantic import BaseModel
from typing import List

class ReflectionRequest(BaseModel):
    corpusId: str
    reflectionId: str
    question: str
    content: str

class ReflectionListResponse(BaseModel):
    corpusId: str
    reflections: List[str]
