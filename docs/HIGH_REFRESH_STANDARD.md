# GBOS High Refresh & Real-Time UX Standard v0.1

Status: design targets only; no performance measurements or hardware compatibility claims.

## Display and interaction
- Support 60 Hz displays as the baseline and target smooth 120 Hz interaction on capable devices.
- Adapt to supported 144–240 Hz displays without forcing excessive rendering or battery consumption.
- Frame budgets: 16.7 ms at 60 Hz; 8.3 ms at 120 Hz; 6.9 ms at 144 Hz; 4.2 ms at 240 Hz.
- Respect reduced-motion settings and battery/thermal constraints.
- Use frame-coordinated animation, composited transforms and virtualization for large data grids.
- Move expensive work off the main UI thread where feasible; prevent long tasks and layout thrashing.

## Data freshness
- Use authenticated WebSocket or server-sent events for subscribed, authorized changes.
- Use monotonic versions, event IDs, reconnect/resume, deduplication and backpressure.
- Separate optimistic UI acknowledgement from durable database commits and external settlement.
- POS and Treasury must display pending/confirmed/failed states truthfully.
- Apply tenant-aware access controls to every stream and cache entry.

## Measurement and release
- Record measured FPS, dropped frames, p95/p99 input latency, long tasks, CPU and battery usage on reference devices.
- Test 60/120 Hz classes and lower-powered hardware; avoid unsupported refresh-rate guarantees.
- Set per-module data freshness SLOs after measuring infrastructure and provider behavior.
- Security, ledger integrity, correctness and accessibility override animation speed.
