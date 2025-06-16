# app/routers/reflections.py

from fastapi import APIRouter
from app.schemas.reflection import (
    ReflectionRequest,
    ReflectionListResponse,
)
from app.services.corpus_repository import ingest_reflection, list_reflections

router = APIRouter()

@router.post(
    "",
    operation_id="addReflection",
    summary="Add Reflection",
    description="Adds a reflection (Q&A) to the corpus.",
    response_model=dict
)
async def add_reflection(payload: ReflectionRequest):
    await ingest_reflection(
        payload.corpusId,
        payload.reflectionId,
        payload.question,
        payload.content,
    )
    return {"message": f"Reflection '{payload.reflectionId}' added to corpus '{payload.corpusId}'."}

@router.get(
    "/{corpus_id}",
    operation_id="listReflections",
    summary="List Reflections",
    description="Lists all reflection IDs for the given corpus.",
    response_model=ReflectionListResponse
)
async def list_reflections_route(corpus_id: str):
    reflection_ids = await list_reflections(corpus_id)
    return ReflectionListResponse(corpusId=corpus_id, reflections=reflection_ids)
