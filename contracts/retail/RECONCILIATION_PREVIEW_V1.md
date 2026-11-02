# Retail reconciliation preview API — draft v0.1

Status: public interface contract for a **synthetic-only internal sandbox**. No public hosted API, SDK, vendor connector or production SLA is offered. No private implementation is published.

## What the endpoint does
`GET /v1/organizations/{organization_id}/reconciliation/preview`

Requires an **authenticated OIDC bearer token**, an **active membership** for the requested organization and permission `discrepancy.read`. Identity and membership must be verified server-side; organization UUID in the URL is never proof of authorization.

This is a safe *read-only* preview: compare importer-asserted POS sale quantities against importer-asserted stock-out quantities keyed by sale ID and SKU. It does not make inventory adjustments, calculate accounting losses, move money or approve corrective actions.

## Source record format (synthetic fixtures only)
An authenticated sandbox operator may use the existing source-record import API with a payload of the following shape:

```json
{
  "source_system": "example-pos",
  "external_key": "line-s10",
  "payload": {
    "kind": "sale",
    "sale_id": "s-10",
    "sku": "COFFEE",
    "units": 3
  }
}
```

The corresponding stock-out source record has `"kind": "stock_out"`, the same sale ID/SKU, and `"units": 2`. Stock-out units are **positive quantities consumed**, not signed changes or inventory balances. `units` must be an integer between 1 and 1,000,000 (booleans and floats rejected by the comparison engine). Sale IDs and SKUs are limited to 64 simple ASCII characters; SKUs normalize to uppercase. Schema versions and real vendor mappings require review before customer data.

## Example response (illustrative values)
```json
{
  "mode": "read_only_preview",
  "source_trust": "importer_asserted_not_independently_verified",
  "scope": "latest_records_only",
  "complete_snapshot": true,
  "truncated": false,
  "summary": {
    "records_examined": 2,
    "ignored_unmapped_records": 0,
    "invalid_records": 0,
    "sale_sku_groups": 1,
    "matched_lines": 0,
    "issues_requiring_review": 1
  },
  "issues": [
    {
      "reference": "generated-evidence-digest",
      "category": "quantity_mismatch",
      "severity": "attention",
      "sale_id": "s-10",
      "sku": "COFFEE",
      "expected_units": 3,
      "observed_units": 2,
      "source_record_ids": [
        "00000000-0000-4000-8000-000000000001",
        "00000000-0000-4000-8000-000000000002"
      ],
      "status": "needs_review"
    }
  ],
  "notice": "Preview only: investigate findings before taking any action."
}
```

The `reference` shown is illustrative, not a real computed digest. Actual implementation returns a deterministic short SHA-256-derived reference from category, business key and source record IDs. This reference is not a cryptographic attestation or proof of authentic source records.

## Categories and meaning
| Category | Human-friendly interpretation |
| --- | --- |
| `quantity_mismatch` | POS sale units and recorded stock-out units differ |
| `sale_without_stock_out` | Sale exists in the selected records but no corresponding stock movement exists |
| `stock_out_without_sale` | Stock movement exists in the selected records but no corresponding sale exists |
| `duplicate_sale_line` | Multiple sale records share a sale ID and SKU; investigate before declaring a match |
| `invalid_import_record` | A recognized record type is missing valid fields |

Unknown record types are counted as ignored, not silently reconciled. Missing data can be explained by import gaps, latency, returns or other legitimate causes—**not proof of fraud or financial loss**.

## Coverage and errors
The API examines the **latest 500 source records** and fetches one extra to detect truncation; if more exist it returns `truncated: true` and `complete_snapshot: false`. If malformed or unknown records are encountered it marks the snapshot incomplete. This is **not** a statement about full-period reconciliation. Full batch- and period-based coverage is a future workflow.

Expected HTTP statuses include `401` unauthenticated, `403` unauthorized role or unavailable pilot mode. Records from another organization must never be returned. Other errors are not evidence of a successful reconciliation.

## Privacy, IP and operational boundary
No real customer records, passwords, payment credentials or sensitive exports should enter these examples or public issues. Only reviewed, Apache-2.0-compatible public interface material belongs here; proprietary code and internal security implementation remain private. Commercial branding remains legally uncleared.
