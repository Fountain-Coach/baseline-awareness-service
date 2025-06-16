from src.baseline_service.gpt_integration.patterns_history_gpt import summarize_patterns

async def generate_patterns_history_summary(texts: list[str]) -> str:
    """
    Wrapper for the GPT-based patterns summarizer.
    `texts` is a list of pattern insight strings.
    """
    return summarize_patterns(texts)
