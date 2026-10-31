# GBOS Nanosecond Research Track

## Scope
100 nanoseconds (0.1 microseconds) is a research benchmark for **selected isolated in-memory operations**, not a platform-wide latency SLO. No performance has been measured or verified yet.

## Candidate workloads
- Fixed-size lookup in a preallocated memory structure.
- Simple deterministic arithmetic or flag evaluation.
- Carefully bounded cached routing-table lookup.

## Non-candidates
- Network APIs, database transactions, authentication end-to-end, POS settlement, bank/mobile-money transfers, SWIFT messaging or settlement.

## Benchmark protocol
- Specify CPU, frequency, cache state, compiler, optimization flags, OS, dataset and concurrency.
- Use calibrated monotonic/high-resolution timing and batched iterations; subtract measurement overhead cautiously.
- Ensure the optimizer cannot eliminate the measured work.
- Report throughput, median, p95, p99, confidence intervals and warm/cold results.
- Run security, correctness and tenant-isolation tests independently; never remove required controls to meet a latency target.
- Treat results below timer resolution as estimates requiring validation with hardware performance counters or a suitable microbenchmark framework.

## Engineering principle
Optimize the critical path only after profiling. Prefer safe architecture, correct financial records and verifiable measurements over blanket nanosecond promises.
