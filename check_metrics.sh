#!/usr/bin/env bash
# check_metrics.sh: fetch key observability numbers from Prometheus

PROM="http://localhost:9090"

query() {
  # usage: query "<PromQL>"
  curl -s --get "${PROM}/api/v1/query" --data-urlencode "query=$1" \
    | jq -r '.data.result[0].value[1] // "0"'
}

echo "==== FountainAI Baseline Service Metrics ===="
echo

# 1) GPT call volume (per 5m) by service
echo "GPT Call Volume (last 5m):"
for svc in history semantic-arc patterns drift reflections summary; do
  val=$(query "sum(increase(baseline_rpc_calls_total{service=\"$svc\",status=\"success\"}[5m]))")
  echo "  $svc: $val"
done
echo

# 2) GPT errors (last 5m) by service
echo "GPT Error Count (last 5m):"
for svc in history semantic-arc patterns drift reflections summary; do
  val=$(query "sum(increase(baseline_rpc_calls_total{service=\"$svc\",status=\"error\"}[5m]))")
  echo "  $svc: $val"
done
echo

# 3) GPT p95 latency (seconds, last 5m)
echo "GPT p95 Latency (last 5m):"
for svc in history semantic-arc patterns drift reflections summary; do
  val=$(query "histogram_quantile(0.95, sum by (le)(rate(baseline_rpc_latency_seconds_bucket{service=\"$svc\"}[5m])))")
  printf "  %s: %.3f s\n" "$svc" "$val"
done
echo

# 4) HTTP RPS overall
rps=$(query "sum(rate(http_requests_total[1m]))")
echo "HTTP RPS (1m rate): $rps req/s"

# 5) HTTP p95 latency
lat=$(query "histogram_quantile(0.95, sum by (le)(rate(http_request_duration_seconds_bucket[5m])))")
printf "HTTP p95 latency: %.3f s\n" "$lat"
