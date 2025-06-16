# API Usage

![API Usage Workflow](https://sdmntpritalynorth.oaiusercontent.com/files/00000000-1da4-6246-98f4-3e9cfccedc2c/raw?se=2025-05-05T06%3A31%3A17Z&sp=r&sv=2024-08-04&sr=b&scid=ae220924-9a44-57b7-afe7-22a9ad327e3c&skoid=59d06260-d7df-416c-92f4-051f0b47c607&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-05-04T18%3A38%3A28Z&ske=2025-05-05T18%3A38%3A28Z&sks=b&skv=2024-08-04&sig=Knm7R9n53FOy683mS9vIUjt2gt%2BsyImJmOKu2bmzKJ4%3D)

*Figure: Example `curl`-based interaction workflow.*

This document illustrates how to interact with the **Baseline Awareness Service** HTTP API. All endpoints are prefixed by the base URL:

```
http://localhost:8000
```

Most endpoints require an `Authorization` header with a bearer token:

```
Authorization: Bearer <YOUR_JWT_TOKEN>
```

---

## Health Check

### GET /

```bash
curl http://localhost:8000/
```

**Response** (`200 OK`)

```json
{ "status": "ok" }
```

### GET /health

```bash
curl http://localhost:8000/health
```

**Response** (`200 OK`)

```json
{ "status": "ok" }
```

### GET /metrics

```bash
curl http://localhost:8000/metrics
```

**Response** (`200 OK`)

```json
{ "requests_total": 123, "latency_ms": 50, "errors_total": 2 }
```

---

## Initialize a Corpus

### POST /corpus/init

```bash
curl -X POST http://localhost:8000/corpus/init \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"corpusId":"my-corpus"}'
```

**201 Created**

```json
{ "message": "Corpus 'my-corpus' initialized successfully" }
```

### GET /corpus/status

```bash
curl http://localhost:8000/corpus/status?corpusId=my-corpus
```

**Response** (`200 OK`)

```json
{ "corpusId":"my-corpus", "createdAt":"2025-05-01T00:00:00" }
```

---

## Ingest a Baseline

### POST /corpus/baseline

```bash
curl -X POST http://localhost:8000/corpus/baseline \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"corpusId":"my-corpus","baselineId":"2025_05_01","content":"Initial baseline text."}'
```

**201 Created**

```json
{ "baselineId":"2025_05_01","message":"Baseline ingested" }
```

---

## Ingest a Drift Explanation

### POST /corpus/drift

```bash
curl -X POST http://localhost:8000/corpus/drift \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"corpusId":"my-corpus","driftId":"2025_05_02_drift","content":"Drift explanation."}'
```

**201 Created**

```json
{ "driftId":"2025_05_02_drift","message":"Drift explanation ingested" }
```

---

## Ingest Pattern Insights

### POST /corpus/patterns

```bash
curl -X POST http://localhost:8000/corpus/patterns \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"corpusId":"my-corpus","patternsId":"2025_05_03_patterns","content":"Pattern insights."}'
```

**201 Created**

```json
{ "patternsId":"2025_05_03_patterns","message":"Pattern insights ingested" }
```

---

## Manage Reflections

### GET /corpus/reflections

```bash
curl "http://localhost:8000/corpus/reflections?corpusId=my-corpus" -H "Authorization: Bearer $TOKEN"
```

**Response** (`200 OK`)

```json
["reflection_2025-05-01T06-07-55","reflection_2025-05-02T14-22-10"]
```

### POST /corpus/reflection

```bash
curl -X POST http://localhost:8000/corpus/reflection \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"corpusId":"my-corpus","reflectionId":"2025-05-04T10-00-00","question":"What changed?","content":"Reflective analysis."}'
```

**201 Created**

```json
{ "reflectionId":"2025-05-04T10-00-00","message":"Reflection saved" }
```

### GET /corpus/reflection

```bash
curl "http://localhost:8000/corpus/reflection?corpusId=my-corpus&reflectionId=2025-05-04T10-00-00" -H "Authorization: Bearer $TOKEN"
```

**Response** (`200 OK`)

```json
{ "reflectionId":"2025-05-04T10-00-00","question":"What changed?","content":"Reflective analysis." }
```

### PUT /corpus/reflection

```bash
curl -X PUT http://localhost:8000/corpus/reflection \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"corpusId":"my-corpus","reflectionId":"2025-05-04T10-00-00","content":"Updated analysis."}'
```

**200 OK**

```json
{ "reflectionId":"2025-05-04T10-00-00","message":"Reflection updated" }
```

### DELETE /corpus/reflection

```bash
curl -X DELETE "http://localhost:8000/corpus/reflection?corpusId=my-corpus&reflectionId=2025-05-04T10-00-00" -H "Authorization: Bearer $TOKEN"
```

**204 No Content**

---

## Semantic Diff Between Reflections

### POST /corpus/reflections/diff

```bash
curl -X POST http://localhost:8000/corpus/reflections/diff \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"corpusId":"my-corpus","baseReflectionId":"2025-05-01T06-07-55","compareReflectionId":"2025-05-02T14-22-10"}'
```

**200 OK**

```json
{ "diffSummary":"The second reflection focuses more on user sentiment shifts." }
```

---

## Reflection History Summary

### GET /corpus/reflections/summary

```bash
curl "http://localhost:8000/corpus/reflections/summary?corpusId=my-corpus" -H "Authorization: Bearer $TOKEN"
```

**Response** (`200 OK`)

```json
{ "historySummary":"Over the course of four reflections, the service shifted to deep semantic analysis." }
```

---

## Full Corpus History

### GET /corpus/history

```bash
curl "http://localhost:8000/corpus/history?corpusId=my-corpus" -H "Authorization: Bearer $TOKEN"
```

**Response** (`200 OK**

```json
[
  {"type":"baseline","id":"2025_05_01","timestamp":"2025-05-01T00:00:00"},
  {"type":"drift","id":"2025_05_02_drift","timestamp":"2025-05-02T00:00:00"},
  {"type":"patterns","id":"2025_05_03_patterns","timestamp":"2025-05-03T00:00:00"},
  {"type":"reflection","id":"2025-05-04T10-00-00","timestamp":"2025-05-04T10:00:00"}
]
```

### GET /corpus/history/drift

```bash
curl "http://localhost:8000/corpus/history/drift?corpusId=my-corpus" -H "Authorization: Bearer $TOKEN"
```

**Response** (`200 OK**)

```json
{ "drifts":[ /* drift history items */ ] }
```

### GET /corpus/history/patterns

```bash
curl "http://localhost:8000/corpus/history/patterns?corpusId=my-corpus" -H "Authorization: Bearer $TOKEN"
```

**Response** (`200 OK**)

```json
{ "patterns":[ /* patterns history items */ ] }
```

### GET /corpus/history/arc

```bash
curl "http://localhost:8000/corpus/history/arc?corpusId=my-corpus" -H "Authorization: Bearer $TOKEN"
```

**Response** (`200 OK**)

```json
{ "semanticArc":"Coherent narrative of corpus evolution." }
```
