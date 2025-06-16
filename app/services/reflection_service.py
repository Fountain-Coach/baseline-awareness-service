# src/baseline_service/services/reflection_service.py

from typing import List, Dict
from src.baseline_service.services.corpus_repository import (
    list_reflections,
    save_reflection,
    load_reflection,
    delete_reflection,
    CorpusNotFound,
)

class ReflectionServiceError(Exception):
    pass

def get_all_reflections(corpus_id: str) -> List[str]:
    """
    Return a list of all reflection IDs in the given corpus.
    """
    try:
        return list_reflections(corpus_id)
    except CorpusNotFound as e:
        raise

def create_reflection(corpus_id: str, reflection_id: str, question: str, content: str) -> None:
    """
    Save a new reflection (or overwrite existing) under the corpus.
    """
    try:
        save_reflection(corpus_id, reflection_id, question, content)
    except CorpusNotFound:
        raise

def retrieve_reflection(corpus_id: str, reflection_id: str) -> Dict[str, str]:
    """
    Load and return a single reflection by ID.
    """
    try:
        return load_reflection(corpus_id, reflection_id)
    except (CorpusNotFound, FileNotFoundError):
        raise

def update_reflection(corpus_id: str, reflection_id: str, question: str, content: str) -> None:
    """
    Overwrite an existing reflection.
    """
    try:
        save_reflection(corpus_id, reflection_id, question, content)
    except CorpusNotFound:
        raise

def remove_reflection(corpus_id: str, reflection_id: str) -> None:
    """
    Delete the specified reflection.
    """
    try:
        delete_reflection(corpus_id, reflection_id)
    except (CorpusNotFound, FileNotFoundError):
        raise
