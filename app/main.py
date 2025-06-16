# app/main.py

from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

# ── Bring in every router (each defines its own path operations) ───────────────
from app.routers.baseline     import router as baseline_router
from app.routers.corpus_init  import router as corpus_init_router
from app.routers.drift        import router as drift_router
from app.routers.patterns     import router as patterns_router
from app.routers.reflections  import router as reflections_router
from app.routers.analytics    import router as analytics_router
from app.routers.summary      import router as summary_router
# ────────────────────────────────────────────────────────────────────────────────

app = FastAPI(
    title="Baseline Awareness Service",
    version="1.0.0",
    description="Generates baselines with OpenAI"
)

# ── PROMETHEUS METRICS ─────────────────────────────────────────────────────────
Instrumentator().instrument(app).expose(app)
# ────────────────────────────────────────────────────────────────────────────────

# ── MOUNT ROUTERS ───────────────────────────────────────────────────────────────
app.include_router(baseline_router,    prefix="/baseline",    tags=["Baseline"])
app.include_router(corpus_init_router, prefix="/corpus-init", tags=["Corpus Init"])
app.include_router(drift_router,       prefix="/drift",       tags=["Drift"])
app.include_router(patterns_router,    prefix="/patterns",    tags=["Patterns"])
app.include_router(reflections_router, prefix="/reflections", tags=["Reflections"])
app.include_router(analytics_router,   prefix="/analytics",   tags=["Analytics"])
app.include_router(summary_router,     prefix="/summary",     tags=["Summary"])
# ────────────────────────────────────────────────────────────────────────────────

@app.get(
    "/",
    tags=["Landing"],
    summary="Landing",
    operation_id="landingGet",
)
async def landing():
    """
    Service landing page.  
    Returns basic info about the service.
    """
    return {"service": "baseline-awareness", "version": app.version}
