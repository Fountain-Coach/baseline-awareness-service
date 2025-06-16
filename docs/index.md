---
title: Baseline Awareness Service
description: Detects and narrates baseline shifts in AI-driven conversations.
image: https://raw.githubusercontent.com/Fountain-Coach/baseline-awareness-service/main/assets/logo/baseline-awareness-logo.png
---

<p align="right">
  <img src="https://raw.githubusercontent.com/Fountain-Coach/baseline-awareness-service/main/assets/logo/baseline-awareness-logo.png" alt="Baseline Awareness Logo" width="120" />
</p>

# Baseline Awareness Service

The **Baseline Awareness Service** is part of the [FountainAI](https://fountain.coach) ecosystem. It detects, explains, and tracks semantic drift across LLM conversations using per-corpus baselines and GPT analysis.

---

## 🚀 Quickstart

```bash
curl http://localhost:8000/baseline/status
```

Returns:
```json
{ "status": "ok", "corpus": "tractatus" }
```
