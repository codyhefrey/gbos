# GBOS Retail Integration Contract v0.1 — Proposal

Status: public draft; no deployed API, SDK, payment processing or production guarantees.

## Intended sale command
```json
{
  "sale_id": "synthetic-sale-001",
  "sku": "demo-coffee",
  "quantity": 2,
  "unit_price_minor": 450,
  "currency": "CAD"
}
```

Authenticated tenant identity must come from verified server credentials, not an arbitrary client-provided tenant ID.

## Intended response
```json
{
  "sale_id": "synthetic-sale-001",
  "total_minor": 900,
  "currency": "CAD",
  "sale_status": "recorded",
  "payment_status": "not_processed"
}
```

## Contract principles
- Versioned schemas, strict input validation, integer minor-unit money representations and currency-aware precision.
- Tenant-scoped idempotency; reuse of a key with a different payload is an error.
- Stock and accounting updates must be transactionally consistent.
- Payment state must never be fabricated; asynchronous provider confirmation requires verified signed webhook processing and reconciliation.
- Auth, tenant isolation, audit and privacy are mandatory before any real deployment.
- Public repository hosts reviewed contracts and synthetic examples only; proprietary implementation stays private.

## Commercial test
Interview multi-location retailers; measure time spent on duplicate data entry, stock discrepancies, reconciliation delays and willingness to pay before claiming market fit.
