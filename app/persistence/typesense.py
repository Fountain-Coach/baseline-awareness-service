# src/baseline_service/persistence/typesense.py
from typesense import Client
from app.config import settings

ts_client = Client({
    "nodes": [{
        "host":     "typesense",      # service name in docker-compose
        "port":     "8108",
        "protocol": "http",
    }],
    "api_key": settings.typ_api_key,
    "connection_timeout_seconds": 2,
})
