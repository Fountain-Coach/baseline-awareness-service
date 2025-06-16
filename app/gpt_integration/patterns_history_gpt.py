# app/gpt_integration/patterns_history_gpt.py

import json
import openai
from app.config import settings

# Configure OpenAI client
openai.api_key  = settings.openai_api_key
_MODEL          = settings.gpt_model
_TEMPERATURE    = settings.gpt_temperature
_MAX_TOKENS     = settings.gpt_max_tokens

async def summarize_patterns(
    snippets: list[str],
    corpus_context: dict | None = None,
    system_prompt: str | None = None,
) -> str:
    """
    snippets: representative quotes or passages illustrating recurring patterns.
    """
    prompt = system_prompt or settings.patterns_system_prompt
    messages = [{"role": "system", "content": prompt}]
    if corpus_context:
        messages.append({
            "role": "system",
            "content": "Corpus context: " + json.dumps(corpus_context)
        })

    user_content = (
        "Below are some excerpts that illustrate emerging patterns in our corpus:\n\n"
        + "\n\n".join(f"- {s}" for s in snippets)
        + "\n\nIdentify and summarize the key recurring patterns."
    )
    messages.append({"role": "user", "content": user_content})

    resp = await openai.ChatCompletion.acreate(
        model=_MODEL,
        messages=messages,
        temperature=_TEMPERATURE,
        max_tokens=_MAX_TOKENS,
    )
    return resp.choices[0].message.content.strip()
