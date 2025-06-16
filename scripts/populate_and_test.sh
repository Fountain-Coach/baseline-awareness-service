#!/usr/bin/env bash
set -euo pipefail

CORPUS="test-corpus"

echo "1) Adding a drift explanation…"
curl -s -i -X POST http://localhost:8000/corpus/drift \
  -H "Content-Type: application/json" \
  -d '{
    "corpusId": "'"${CORPUS}"'",
    "driftId": "d2",
    "content": "The scope shifted from feature A to feature B, changing the narrative."
  }'
echo -e "\n"

echo "2) Adding a pattern insight…"
curl -s -i -X POST http://localhost:8000/corpus/patterns \
  -H "Content-Type: application/json" \
  -d '{
    "corpusId": "'"${CORPUS}"'",
    "patternsId": "p2",
    "content": "Users repeatedly mention performance and security as key themes."
  }'
echo -e "\n"

echo "3) Re-running summaries…"
bash << 'EOF'
echo "== Drift History Summary =="
curl -s -i "http://localhost:8000/corpus/history/drift-summary?corpusId=test-corpus"
echo -e "\n"

echo "== Patterns History Summary =="
curl -s -i "http://localhost:8000/corpus/history/patterns-summary?corpusId=test-corpus"
echo -e "\n"

echo "== Full Semantic Arc =="
curl -s -i "http://localhost:8000/corpus/semantic-arc/full?corpusId=test-corpus"
echo -e "\n"
EOF
