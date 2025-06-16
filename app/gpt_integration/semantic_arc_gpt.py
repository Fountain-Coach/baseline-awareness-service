# app/gpt_integration/semantic_arc_gpt.py

import json
import openai
from app.config import settings

# Configure the OpenAI client from .env via settings
openai.api_key  = settings.openai_api_key
_MODEL          = settings.gpt_model
_TEMPERATURE    = settings.gpt_temperature
_MAX_TOKENS     = settings.gpt_max_tokens

async def build_semantic_arc(
    sections: dict[str, list[str]],
    corpus_context: dict | None = None,
    system_prompt: str | None = None,
) -> str:
    """
    Generate a cohesive narrative (semantic arc) from sectioned insights.

    - sections: mapping of section name to list of text snippets.
    - corpus_context: optional metadata about the corpus.
    - system_prompt: override for the default system-role instruction.
    """
    # 1) Build system messages
    prompt = system_prompt or settings.semantic_arc_system_prompt
    messages = [{"role": "system", "content": prompt}]
    if corpus_context:
        messages.append({
            "role": "system",
            "content": "Corpus context: " + json.dumps(corpus_context)
        })

    # 2) Build user prompt
    parts = []
    for section, texts in sections.items():
        header = f"## {section.title()}"
        body = "\n".join(f"- {t}" for t in texts)
        parts.append(f"{header}\n{body}")
    user_content = (
        "Below are extracts grouped by semantic section. "
        "Please weave them into a single coherent narrative:\n\n"
        + "\n\n".join(parts)
    )
    messages.append({"role": "user", "content": user_content})

    # 3) Call OpenAI
    response = await openai.ChatCompletion.acreate(
        model=_MODEL,
        messages=messages,
        temperature=_TEMPERATURE,
        max_tokens=_MAX_TOKENS,
    )

    # 4) Return the generated arc
    return response.choices[0].message.content.strip()
