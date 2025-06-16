# app/gpt_integration/history_gpt.py

import json
import openai
from app.config import settings

# Configure OpenAI client
openai.api_key  = settings.openai_api_key
_MODEL          = settings.gpt_model
_TEMPERATURE    = settings.gpt_temperature
_MAX_TOKENS     = settings.gpt_max_tokens

async def summarize_history(
    events: list[str],
    corpus_context: dict | None = None,
    system_prompt: str | None = None,
) -> str:
    """
    events: chronological list of notable events/texts.
    """
    prompt = system_prompt or settings.history_system_prompt
    messages = [{"role": "system", "content": prompt}]
    if corpus_context:
        messages.append({
            "role": "system",
            "content": "Corpus context: " + json.dumps(corpus_context)
        })

    user_content = (
        "Here is the sequence of events we extracted from the corpus:\n\n"
        + "\n".join(f"{i+1}. {e}" for i, e in enumerate(events))
        + "\n\nPlease summarize these into a coherent historical overview."
    )
    messages.append({"role": "user", "content": user_content})

    resp = await openai.ChatCompletion.acreate(
        model=_MODEL,
        messages=messages,
        temperature=_TEMPERATURE,
        max_tokens=_MAX_TOKENS,
    )
    return resp.choices[0].message.content.strip()
