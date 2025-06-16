#!/usr/bin/env bash
set -euo pipefail

BASE_URL="http://localhost:8002"
echo
echo "=== HEALTH ==="
curl -s -o /dev/null -w "%{http_code}\n" "$BASE_URL/health"

echo
echo "=== INIT test-corpus ==="
curl -i -X POST "$BASE_URL/corpus/init" \
     -H "Content-Type: application/json" \
     -d '{"corpusId":"test-corpus"}'

echo
echo "=== INGEST BASELINE b1 ==="
curl -i -X POST "$BASE_URL/corpus/baseline" \
     -H "Content-Type: application/json" \
     -d '{"corpusId":"test-corpus","baselineId":"b1","content":"First snapshot"}'

echo
echo "=== LIST REFLECTIONS (expect none) ==="
curl -i -X GET "$BASE_URL/corpus/reflections?corpusId=test-corpus"

echo
echo "=== INGEST REFLECTION r1 ==="
curl -i -X POST "$BASE_URL/corpus/reflection" \
     -H "Content-Type: application/json" \
     -d '{"corpusId":"test-corpus","reflectionId":"r1","question":"Why?","content":"Because."}'

echo
echo "=== LIST REFLECTIONS (expect r1) ==="
curl -i -X GET "$BASE_URL/corpus/reflections?corpusId=test-corpus"

echo
echo "=== GET HISTORY ==="
curl -i -X GET "$BASE_URL/corpus/history?corpusId=test-corpus"

echo
echo "=== GET SEMANTIC ARC ==="
curl -i -X GET "$BASE_URL/corpus/semantic-arc?corpusId=test-corpus"

echo
echo "=== GET REFLECTION SUMMARY ==="
curl -i -X GET "$BASE_URL/corpus/reflections/summary?corpusId=test-corpus"

echo
echo "=== GET DRIFT SUMMARY (expect empty) ==="
curl -i -X GET "$BASE_URL/corpus/history/drift-summary?corpusId=test-corpus"

echo
echo "=== GET PATTERNS SUMMARY (expect empty) ==="
curl -i -X GET "$BASE_URL/corpus/history/patterns-summary?corpusId=test-corpus"

echo
echo "=== GET FULL SEMANTIC ARC ==="
curl -i -X GET "$BASE_URL/corpus/semantic-arc/full?corpusId=test-corpus"
