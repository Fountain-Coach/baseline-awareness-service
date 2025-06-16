#!/bin/bash

set -e

echo "📚 Initializing corpus: tractatus"
curl -s -X POST http://localhost:8000/corpus/init \
  -H "Content-Type: application/json" \
  -d '{"corpusId":"tractatus"}' | jq

echo "📝 Adding baseline #1: 'The world is all that is the case.'"
curl -s -X POST http://localhost:8000/corpus/baseline \
  -H "Content-Type: application/json" \
  -d '{
    "corpusId": "tractatus",
    "baselineId": "tractatus_001",
    "content": "The world is all that is the case."
  }' | jq

echo "📝 Adding baseline #2: 'What is the case — a fact — is the existence of states of affairs.'"
curl -s -X POST http://localhost:8000/corpus/baseline \
  -H "Content-Type: application/json" \
  -d '{
    "corpusId": "tractatus",
    "baselineId": "tractatus_002",
    "content": "What is the case — a fact — is the existence of states of affairs."
  }' | jq

echo "🔄 Adding drift #1: conceptual movement between proposition 1 and 2."
curl -s -X POST http://localhost:8000/corpus/drift \
  -H "Content-Type: application/json" \
  -d '{
    "corpusId": "tractatus",
    "driftId": "tractatus_drift_001",
    "fromBaselineId": "tractatus_001",
    "toBaselineId": "tractatus_002",
    "comment": "Shifts focus from the totality of facts to the nature of facts themselves.",
    "content": "The movement reflects a conceptual transition from the world as a set of facts to an analysis of what constitutes a fact — states of affairs."
  }' | jq

echo "💭 Adding reflection #1: philosophical significance of the drift."
curl -s -X POST http://localhost:8000/corpus/reflections \
  -H "Content-Type: application/json" \
  -d '{
    "corpusId": "tractatus",
    "reflectionId": "tractatus_reflection_001",
    "driftId": "tractatus_drift_001",
    "question": "What philosophical significance does this drift represent?",
    "content": "This transition marks the philosophical movement from considering the totality of facts towards dissecting the constitution of facts themselves, laying the groundwork for logical atomism."
  }' | jq

echo "📜 Listing history (chronological order)"
curl -s "http://localhost:8000/corpus/history?corpus_id=tractatus" | jq

echo "🌈 Reading semantic arc"
curl -s "http://localhost:8000/corpus/semantic-arc?corpus_id=tractatus" | jq

echo "✅ All actions completed."
