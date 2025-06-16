<p align="right">
  <img src="https://raw.githubusercontent.com/Fountain-Coach/baseline-awareness-service/main/assets/logo/baseline-awareness-logo.png" alt="Baseline Awareness Logo" width="120" />
</p>

# Baseline Awareness Service

The **Baseline Awareness Service** provides semantic context memory, drift detection, and pattern tracking for LLM-based AI systems.

It is a core part of the [FountainAI](https://github.com/Fountain-Coach) ecosystem, enabling services to:
- Capture and snapshot the current semantic state
- Compare past and present knowledge for drift
- Detect narrative patterns and trends
- Support contextualized reasoning across agent chains

---

## 🧪 Usage

**Drift Detection Example:**

```bash
curl http://localhost:8000/drift \
  -H "Content-Type: application/json" \
  -d '{
    "corpusId": "my-project",
    "baseline": "...",
    "current": "..."
  }'
```

**Initialize a Corpus:**

```bash
curl -X POST http://localhost:8000/corpus/init \
  -H "Content-Type: application/json" \
  -d '{"corpusId": "my-project"}'
```

---

## 🛠️ Endpoints

- `/corpus/init` — Initialize persistent context
- `/baseline/snapshot` — Take semantic snapshots
- `/drift` — Compare snapshot vs. current input
- `/patterns` — Extract narrative structures
- `/summary` — Summarize evolving states
- `/analytics` — Trace GPT-based history

📘 [API Docs](https://fountain-coach.github.io/baseline-awareness-service/)

---

## 🌐 GitHub Pages

→ https://fountain-coach.github.io/baseline-awareness-service/

---

## 🧠 Part of FountainAI

FountainAI is a modular AI reasoning system designed to orchestrate autonomous LLM workflows with complete introspective transparency.

🔗 [FountainAI Overview](https://github.com/Fountain-Coach)
