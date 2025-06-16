# app/services/corpus_repository.py

from app.persistence.typesense import ts_client

COLL = "corpus"

async def initialize_corpus(corpus_id: str):
    schema = {
        "name": COLL,
        "fields": [
            {"name": "corpusId",  "type": "string", "facet": False},
            {"name": "itemType",  "type": "string", "facet": True, "sort": True},
            {"name": "itemId",    "type": "string", "facet": True, "sort": True},
            {"name": "text",      "type": "string"}
        ]
    }
    try:
        ts_client.collections.create(schema)
    except Exception:
        # ignore “already exists”
        ...

async def ingest_baseline(corpus_id: str, baseline_id: str, content: str):
    return ts_client.collections[COLL].documents.create({
        "corpusId": corpus_id,
        "itemType": "baseline",
        "itemId":   baseline_id,
        "text":     content,
    })

async def ingest_drift(corpus_id: str, drift_id: str, content: str):
    return ts_client.collections[COLL].documents.create({
        "corpusId": corpus_id,
        "itemType": "drift",
        "itemId":   drift_id,
        "text":     content,
    })

async def ingest_patterns(corpus_id: str, patterns_id: str, content: str):
    return ts_client.collections[COLL].documents.create({
        "corpusId": corpus_id,
        "itemType": "patterns",
        "itemId":   patterns_id,
        "text":     content,
    })

async def ingest_reflection(corpus_id: str, reflection_id: str, question: str, content: str):
    return ts_client.collections[COLL].documents.create({
        "corpusId": corpus_id,
        "itemType": "reflection",
        "itemId":   reflection_id,
        "text":     f"Q: {question}\nA: {content}"
    })

async def list_reflections(corpus_id: str):
    results = ts_client.collections[COLL].documents.search({
        "q":         corpus_id,
        "query_by":  "corpusId",
        "filter_by": f"corpusId:={corpus_id}&&itemType:=reflection",
        "sort_by":   "itemId:asc"
    })
    return [hit["document"]["itemId"] for hit in results["hits"]]

async def list_history(corpus_id: str):
    results = ts_client.collections[COLL].documents.search({
        "q":         corpus_id,
        "query_by":  "corpusId",
        "filter_by": f"corpusId:={corpus_id}",
        "sort_by":   "itemType:asc,itemId:asc"
    })
    return [(doc["document"]["itemType"], doc["document"]["itemId"])
            for doc in results["hits"]]

async def build_semantic_arc(corpus_id: str):
    history = await list_history(corpus_id)
    return " ".join(item_id for _, item_id in history)
