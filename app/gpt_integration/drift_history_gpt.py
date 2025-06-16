# src/baseline_service/gpt_integration/drift_history_gpt.py

import json
import openai
from src.baseline_service.config import settings

# Configure OpenAI client
openai.api_key  = settings.openai_api_key
_MODEL          = settings.gpt_model
_TEMPERATURE    = settings.gpt_temperature
_MAX_TOKENS     = settings.gpt_max_tokens

async def summarize_drift(
    deltas: list[str],
    corpus_context: dict | None = None,
    system_prompt: str | None = None,
) -> str:
    """
    deltas: textual descriptions of change between snapshots.
    """
    prompt = system_prompt or settings.drift_system_prompt
    messages = [{"role": "system", "content": prompt}]
    if corpus_context:
        messages.append({
            "role": "system",
            "content": "Corpus context: " + json.dumps(corpus_context)
        })

    user_content = (
        "The following list shows how the corpus has changed between snapshots:\n\n"
        + "\n".join(f"{i+1}. {d}" for i, d in enumerate(deltas))
        + "\n\nPlease explain the main drift trends and their possible significance."
    )
    messages.append({"role": "user", "content": user_content})

    resp = await openai.ChatCompletion.acreate(
        model=_MODEL,
        messages=messages,
        temperature=_TEMPERATURE,
        max_tokens=_MAX_TOKENS,
    )
    return resp.choices[0].message.content.strip()
