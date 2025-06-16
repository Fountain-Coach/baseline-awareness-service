# src/baseline_service/persistence/models.py

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class CorpusModel(BaseModel):
    corpus_id: str = Field(..., alias="corpusId")
    created_at: datetime = Field(default_factory=datetime.utcnow)

class BaselineModel(BaseModel):
    corpus_id: str = Field(..., alias="corpusId")
    baseline_id: str = Field(..., alias="baselineId")
    content: str
    ingested_at: datetime = Field(default_factory=datetime.utcnow)

class DriftModel(BaseModel):
    corpus_id: str = Field(..., alias="corpusId")
    drift_id: str = Field(..., alias="driftId")
    content: str
    ingested_at: datetime = Field(default_factory=datetime.utcnow)

class PatternsModel(BaseModel):
    corpus_id: str = Field(..., alias="corpusId")
    patterns_id: str = Field(..., alias="patternsId")
    content: str
    ingested_at: datetime = Field(default_factory=datetime.utcnow)

class ReflectionModel(BaseModel):
    corpus_id: str = Field(..., alias="corpusId")
    reflection_id: str = Field(..., alias="reflectionId")
    question: str
    content: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

class HistoryEntry(BaseModel):
    type: str
    id: str
    timestamp: datetime
