# Baseline Awareness Service

## Diagram

![Baseline Awareness Service Architecture](https://chatgpt.com/backend-api/public_content/enc/eyJpZCI6Im1fNjgxODQ1ODllMzc4ODE5MTg3NWJjZjEwYjAwZDY0YzY6ZmlsZV8wMDAwMDAwMDhjOGM2MjQzODVlMWUwNTFlZjIxYjU3NCIsInRzIjoiNDg1MTE3IiwicCI6InB5aSIsInNpZyI6ImI4MzBkZTc2NGQwOTA3OThiZTAxNWFjZWEyOTM0OGJkMWRmYWJiYTczZDQyMzY0OGY0YjgwNTc5NjIzYzU2OGEiLCJ2IjoiMCIsImdpem1vX2lkIjpudWxsfQ==)

*Figure: High-level architecture diagram using component logos.*

## Overview

The **Baseline Awareness Service** is a microservice designed to manage and analyze evolving textual corpora using OpenAI’s GPT models. Built on **FastAPI**, it follows a layered architecture to ensure maintainability, testability, and scalability.

## Components

- **API Layer**  
  FastAPI routers (`src.baseline_service.routers`) expose HTTP endpoints for:
  - Health & Landing: `GET /`, `GET /health`
  - Metrics: `GET /metrics`
  - Corpus Operations:
    - Initialize: `POST /corpus/init`
    - Status: `GET /corpus/status`
  - Baseline Ingestion: `POST /corpus/baseline`
  - Drift Explanations: `POST /corpus/drift`
  - Pattern Insights: `POST /corpus/patterns`
  - Reflections:
    - List: `GET /corpus/reflections`
    - CRUD: `POST /corpus/reflection`, `GET /corpus/reflection`, `PUT /corpus/reflection`, `DELETE /corpus/reflection`
    - Diff: `POST /corpus/reflections/diff`
    - Summary: `GET /corpus/reflections/summary`
  - History:
    - Raw History: `GET /corpus/history`
    - Drift History: `GET /corpus/history/drift`
    - Patterns History: `GET /corpus/history/patterns`
    - Semantic Arc: `GET /corpus/history/arc`

- **Service Layer**  
  Located in `src.baseline_service.services`, this layer:
  - Orchestrates persistence operations via `corpus_repository.py`.
  - Manages reflections CRUD and semantic diffs via `reflection_service.py`.
  - Invokes GPT summarizers in `summary_service.py`.

- **Persistence Layer**  
  Implemented through filesystem-based storage in `src.baseline_service.persistence`:
  - `filesystem.py`: low-level I/O helpers for file and directory operations.
  - `models.py`: Pydantic models representing on-disk metadata.  
  This layer can be replaced with databases or object stores without impacting higher layers.

- **GPT Integration Layer**  
  Encapsulated in `src.baseline_service.gpt_integration`, containing:
  - `diff_service.py`: semantic diff generation.
  - `history_service.py`: reflections history summarization.
  - `drift_history_service.py`: drift explanations summarization.
  - `patterns_history_service.py`: pattern insights summarization.
  - `semantic_arc_service.py`: integrated semantic arc narrative.

- **Security & Configuration**  
  - `config.py`: Pydantic-based settings and secret injection.
  - `security/auth.py`: JWT validation, CORS, and RBAC enforcement.
  - `security/secrets.py`: secret loader (Vault/KMS or environment files).

- **Observability & Monitoring**  
  `observability.py` provides:
  - Structured JSON logging with request IDs.
  - Prometheus metrics (request counts, GPT call latencies, error rates).

- **Testing**  
  - Unit tests under `tests/unit` cover individual service, persistence, and GPT modules.
  - Integration tests under `tests/integration` verify end-to-end HTTP behaviors and GPT mocks.

## Data Flow

1. **Client** sends HTTP requests to the API layer.  
2. **API routers** parse and validate inputs, then forward to service functions.  
3. **Service layer** executes business logic, interacting with persistence and GPT integration.  
4. **Security middleware** ensures authentication, authorization, and CORS compliance.  
5. **Observability hooks** log request/response cycles and record metrics.  

## Project Structure

Below is the complete directory tree (including hidden files) for the **Baseline Awareness Service**:

    baseline_awareness_service
    ├── .github
    │   └── workflows
    │       └── ci.yml
    ├── docker
    │   └── Dockerfile
    ├── docs
    │   ├── api_usage.md
    │   └── architecture.md
    ├── pytest.ini
    ├── requirements.txt
    ├── scripts
    │   ├── build_image.sh
    │   ├── init-refactor.sh
    │   └── lint.sh
    ├── src
    │   └── baseline_service
    │       ├── __init__.py
    │       ├── config.py
    │       ├── entrypoint.py
    │       ├── main.py
    │       ├── observability.py
    │       ├── schemas
    │       │   ├── analytics.py
    │       │   ├── baseline.py
    │       │   ├── corpus.py
    │       │   ├── drift.py
    │       │   ├── patterns.py
    │       │   └── reflection.py
    │       ├── security
    │       │   ├── auth.py
    │       │   └── secrets.py
    │       ├── routers
    │       │   ├── analytics.py
    │       │   ├── baseline.py
    │       │   ├── corpus_init.py
    │       │   ├── drift.py
    │       │   ├── health.py
    │       │   ├── metrics.py
    │       │   ├── patterns.py
    │       │   ├── reflection.py
    │       │   ├── reflections.py
    │       │   └── status.py
    │       ├── services
    │       │   ├── corpus_repository.py
    │       │   ├── reflection_service.py
    │       │   └── summary_service.py
    │       ├── persistence
    │       │   ├── filesystem.py
    │       │   └── models.py
    │       └── gpt_integration
    │           ├── diff_service.py
    │           ├── history_service.py
    │           ├── drift_history_service.py
    │           ├── patterns_history_service.py
    │           └── semantic_arc_service.py
    └── tests
        ├── integration
        │   ├── test_endpoints.py
        │   └── test_gpt_mocks.py
        └── unit
            ├── test_corpus_repository.py
            ├── test_reflection_service.py
            └── test_summary_service.py
