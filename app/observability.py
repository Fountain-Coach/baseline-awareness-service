# src/baseline_service/observability.py

import time
import pkgutil
import inspect
import importlib
from fastapi import Response
from prometheus_client import Counter, Histogram

# Define custom metrics in the default registry
RPC_CALLS = Counter(
    "baseline_rpc_calls_total",
    "Total number of GPT RPC calls",
    ["service", "status"],
)
RPC_LATENCY = Histogram(
    "baseline_rpc_latency_seconds",
    "Latency of GPT RPC calls",
    ["service"],
)

def record_rpc(service_name: str, success: bool, duration: float):
    """
    Increment the RPC call counter and observe latency.
    """
    status = "success" if success else "error"
    RPC_CALLS.labels(service=service_name, status=status).inc()
    RPC_LATENCY.labels(service=service_name).observe(duration)
