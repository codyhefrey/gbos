# GBOS Performance Engineering Standard v0.1

Status: proposed SLOs, not benchmarked or production-verified.

## User-facing targets (p95, under documented load)
- Cacheable internal API GET: <100 ms server response.
- Typical regional API read: <250 ms server response.
- Eligible local POS sale recording: <500 ms, excluding payment authorization and synchronization.
- Initial interactive dashboard: <2 seconds on specified reference devices/network.

## Engineering rules
1. Measure p50/p95/p99 latency and error rates per module, endpoint, region and tenant tier.
2. Publish load-test conditions (concurrency, dataset, network, hardware) with results; no blanket speed guarantees.
3. Avoid chatty inter-module requests and N+1 database queries; add indexes and query budgets.
4. Cache only safe data with explicit TTL and invalidation; never bypass tenant authorization.
5. Use async events for noncritical work, with durable queues, idempotency and reconciliation.
6. For POS offline flows, distinguish local sale recording from authorized payment and final settlement.
7. For Treasury, show pending/confirmed/failed provider status accurately; do not equate fast acknowledgment with settlement.
8. Use regional deployment only where residency and legal requirements allow.
9. Protect p95/p99 latency with timeouts, backpressure, rate limits, circuit breakers and graceful degradation.
10. Gate releases on reproducible regression tests and security/integrity checks.

## Initial performance test plan
- Benchmark API cold/warm paths, tenant-isolation query overhead, POS sale posting and dashboard loading.
- Record baseline traces and budgets before implementing optimizations.
- Fail CI for material regressions after reliable benchmarks are established.
- Do not sacrifice ledger integrity, authorization, compliance or audit logging for latency.
