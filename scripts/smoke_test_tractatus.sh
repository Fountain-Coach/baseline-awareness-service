#!/usr/bin/env bash
#
# File: scripts/smoke_test_tractatus.sh
# Purpose: exercise all major endpoints against data/tractatus

set -e
BASE_URL="http://localhost:8002"
CORPUS="tractatus"

echo
echo "=== 1) List Reflections (should see r1) ==="
curl -i -X GET "$BASE_URL/corpus/reflections?corpusId=$CORPUS"
echo

echo
echo "=== 2) Get Full History (b1, d1, p1, r1) ==="
curl -i -X GET "$BASE_URL/corpus/history?corpusId=$CORPUS"
echo

echo
echo "=== 3) Get Simple Semantic Arc ==="
curl -i -X GET "$BASE_URL/corpus/semantic-arc?corpusId=$CORPUS"
echo

echo
echo "=== 4) Reflection History Summary ==="
curl -i -X GET "$BASE_URL/corpus/reflections/summary?corpusId=$CORPUS"
echo

echo
echo "=== 5) Drift History Summary ==="
curl -i -X GET "$BASE_URL/corpus/history/drift-summary?corpusId=$CORPUS"
echo

echo
echo "=== 6) Patterns History Summary ==="
curl -i -X GET "$BASE_URL/corpus/history/patterns-summary?corpusId=$CORPUS"
echo

echo
echo "=== 7) Full Semantic Arc Narrative ==="
curl -i -X GET "$BASE_URL/corpus/semantic-arc/full?corpusId=$CORPUS"
echo
