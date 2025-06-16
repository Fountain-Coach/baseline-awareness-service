# app/gpt_integration/semantic_arc_service.py

from app.persistence.typesense import ts_client
from app.gpt_integration.semantic_arc_gpt import build_semantic_arc as gpt_build_semantic_arc
from app.gpt_integration.patterns_history_gpt import summarize_patterns as gpt_summarize_patterns
from app.services.corpus_repository import ingest_patterns

async def build_semantic_arc(corpus_id: str) -> str:
    """
    1) Fetch all documents by type for this corpus.
    2) Auto-generate patterns from baselines if none were ingested manually.
    3) Persist any auto-detected patterns back into Typesense.
    4) Call the GPT-4 semantic-arc helper with all four sections.
    """
    collection = ts_client.collections["corpus"]
    sections: dict[str, list[str]] = {}

    # 1) Fetch baseline, drift, and reflection texts
    for item_type in ["baseline", "drift", "reflection"]:
        resp = collection.documents.search({
            "q":         corpus_id,
            "query_by":  "corpusId",
            "filter_by": f"corpusId:={corpus_id}&&itemType:={item_type}",
            "sort_by":   "itemId:asc",
            "per_page":  100,
        })
        sections[item_type] = [hit["document"]["text"] for hit in resp["hits"]]

    # 2) Attempt to fetch any manually-ingested patterns
    resp_patterns = collection.documents.search({
        "q":         corpus_id,
        "query_by":  "corpusId",
        "filter_by": f"corpusId:={corpus_id}&&itemType:=patterns",
        "sort_by":   "itemId:asc",
        "per_page":  100,
    })
    manual = [hit["document"]["text"] for hit in resp_patterns["hits"]]

    if manual:
        sections["patterns"] = manual
    else:
        # 3) Auto-detect patterns by comparing the baselines
        detected = await gpt_summarize_patterns(sections["baseline"])
        patterns = [line.strip("- ").strip() for line in detected.splitlines() if line.strip()]
        sections["patterns"] = patterns
        # persist each auto-generated pattern back into Typesense
        for idx, text in enumerate(patterns, start=1):
            await ingest_patterns(corpus_id, f"auto-pattern-{idx}", text)

    # 4) Delegate to GPT‐4 to weave the final narrative
    return await gpt_build_semantic_arc(sections)
