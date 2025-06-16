# app/entrypoint.py

import time
import uvicorn
from fastapi import Request
from fastapi.middleware import Middleware
from starlette.middleware.base import BaseHTTPMiddleware

# Prometheus Instrumentator for HTTP metrics
from prometheus_fastapi_instrumentator import Instrumentator

# Your FastAPI application and RPC observability
from app.main import app
from app.observability import record_rpc


class RPCMetricsMiddleware(BaseHTTPMiddleware):
    """
    Middleware to record RPC-style metrics for any path under /corpus/{service}/...
    """
    async def dispatch(self, request: Request, call_next):
        path_parts = request.url.path.strip("/").split("/")
        if len(path_parts) >= 2 and path_parts[0] == "corpus":
            service = path_parts[1]
            start = time.time()
            response = await call_next(request)
            duration = time.time() - start
            record_rpc(
                service,
                success=200 <= response.status_code < 300,
                duration=duration
            )
            return response
        return await call_next(request)


# 1. Mount RPC metrics middleware
app.add_middleware(RPCMetricsMiddleware)

# 2. Instrument all HTTP endpoints and expose Prometheus metrics at /metrics
Instrumentator(
    should_group_status_codes=True,
    should_ignore_untemplated=True,
    should_instrument_requests_inprogress=True,
).instrument(app).expose(
    app,
    include_in_schema=False,
    endpoint="/metrics"
)

if __name__ == "__main__":
    # Run via `python app/entrypoint.py` for local development
    uvicorn.run(app, host="0.0.0.0", port=80)
