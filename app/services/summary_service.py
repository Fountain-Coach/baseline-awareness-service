# app/services/summary_service.py

from app.persistence.typesense import ts_client
from app.gpt_integration.history_gpt import summarize_history as gpt_summarize_history

async def summarize_history(corpus_id: str) -> str:
    """
    1) Query Typesense for all documents in the 'corpus' collection
       with this corpusId, sorted by itemType and itemId.
    2) Extract their 'text' fields.
    3) Delegate to the GPT-4 helper with the real passages.
    """
    # 1) Perform the search
    search_params = {
        "q":         corpus_id,
        "query_by":  "corpusId",
        "filter_by": f"corpusId:={corpus_id}",
        "sort_by":   "itemType:asc,itemId:asc",
        "per_page":  100,
    }
    resp = ts_client.collections["corpus"].documents.search(search_params)

    # 2) Extract the actual text content
    texts = [hit["document"]["text"] for hit in resp["hits"]]

    # 3) Call into your GPT-4 helper with real document passages
    return await gpt_summarize_history(texts)
