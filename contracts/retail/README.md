# Retail Integration Contracts — Evidence-First Pilot

**Status:** Public synthetic-only API proposal and interface reference. No hosted public API, customer-ready POS product, payment processing or production commitment. OPERIX remains an **uncleared internal codename**, not an approved commercial brand.

## Intended user journey
A store operator's existing POS and inventory systems disagree. The integration must first establish what happened using imported records. The manager sees issues in plain English, the reviewer can open the evidence references, and no stock or money moves without explicit verified authorization.

**Currently implemented for internal tests:** authenticated source-record import and a read-only bounded reconciliation preview. See [Reconciliation Preview v0.1](RECONCILIATION_PREVIEW_V1.md) for exact source formats and the response contract. A downloadable CSV preview uses the same organization authorization and evidence:

`GET /v1/organizations/{organization_id}/reconciliation/preview.csv`

This CSV is for **review only**, includes coverage warnings and source IDs, and escapes leading formula characters to reduce spreadsheet injection risk. It is not an accounting export or proof of full-period reconciliation. An offline sample HTML report can be generated from fictional inputs inside the private engineering repository; there is no deployed public UI.

## Future sale command (not implemented)
The earlier proposed POS sale contract is retained as an illustrative future interface, **not** a shipped payment or accounting flow:

```json
{
  "sale_id": "synthetic-sale-001",
  "sku": "demo-coffee",
  "quantity": 2,
  "unit_price_minor": 450,
  "currency": "CAD"
}
```

A future sale command needs validated currency precision, tax treatment, permissions, idempotency, properly tested accounting/stock integrity and independent operational approval. A client's provided tenant ID is not authentication. Never fabricate payment status or silently alter source records.

## Public/private boundary
Reviewed interfaces and sample fixtures are public under applicable Apache-2.0 terms. Proprietary implementation, commercial modules, confidential AI algorithms and production infrastructure remain private. All developer integrations must use tenant-scoped permissions, synthetic testing and documented consent/retention rules.

## Fit validation
Interview actual retail operators, owners and finance reviewers. Measure time spent finding inventory discrepancies, ability to complete tasks without a developer, false-positive rates and legitimate willingness to pay before promising enterprise-scale capabilities.
