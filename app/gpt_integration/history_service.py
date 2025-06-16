# src/baseline_service/gpt_integration/history_service.py

from typing import List

async def summarize_history(texts: List[str]) -> str:
    """
    Temporary stub: simply returns a bullet list of all reflections
    we loaded, so you can verify the pipeline end‐to‐end.
    """
    bullets = "\n".join(f"- {t.strip()}" for t in texts)
    return f"Found {len(texts)} reflection(s):\n{bullets}"
