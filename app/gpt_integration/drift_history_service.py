# src/baseline_service/gpt_integration/drift_history_service.py

from src.baseline_service.gpt_integration.drift_history_gpt import summarize_drift

async def generate_drift_history_summary(texts: list[str]) -> str:
    """
    Wrapper for the GPT-based drift summarizer.
    `texts` is a list of drift explanation strings.
    """
    return summarize_drift(texts)
