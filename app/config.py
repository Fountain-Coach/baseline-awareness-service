# File: /Users/benedikteickhoff/Development/TheFountainSprints/FountainAI/baseline_awareness_service/src/baseline_service/config.py

from pydantic import BaseSettings

class Settings(BaseSettings):
    # Typesense & OpenAI
    openai_api_key: str
    typ_api_key:     str        # ← Typesense API key
    corpora_root:    str = "./data"

    # GPT configuration
    gpt_model:       str   = "gpt-4"
    gpt_temperature: float = 0.3
    gpt_max_tokens:  int   = 800

    # System prompts for GPT roles
    semantic_arc_system_prompt: str = (
        "You are an expert at weaving disparate insights into a single coherent narrative."
    )
    history_system_prompt: str = (
        "You are a historian AI, skilled at weaving timelines into concise narratives."
    )
    patterns_system_prompt: str = (
        "You are an analyst AI, adept at distilling recurring themes and patterns."
    )
    drift_system_prompt: str = (
        "You are an AI specialist in detecting and explaining shifts over time."
    )

    class Config:
        env_file = ".env"
        case_sensitive = False
        extra = "ignore"

# Instantiate settings singleton
settings = Settings()
