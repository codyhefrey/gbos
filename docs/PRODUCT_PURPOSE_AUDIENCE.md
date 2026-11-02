# Who this platform is for — prerelease product charter

**Temporary project codename:** OPERIX. Commercial naming and trademark clearance are unresolved. This is not a launched or certified service, and this public repository contains only reviewed contracts, synthetic examples and supporting documentation.

## Purpose
Provide a modular and provider-neutral **Business Operating System** to connect business records and workflows, identify issues with evidence and support permissioned decisions. Rather than claiming an all-in-one replacement for every business application, we are testing one valuable workflow before expanding.

## First users
- **Retail store owners/managers:** understand which sales and inventory records disagree.
- **Operations/inventory teams:** see expected versus recorded item quantities and find the relevant source records.
- **Finance reviewers and auditors:** investigate clearly labeled exceptions without changing stock or payments.
- **Software integration developers:** connect approved POS/inventory sources using stable contracts and synthetic test examples.
- **Larger businesses:** future permissions, multi-site reporting and controls after evidence-backed pilots.

The initial target is **small/mid-sized retailers and wholesalers**, designed with African market realities in mind and extensible internationally. No country-specific tax, currency conversion or financial compliance capability is asserted by this draft.

## Example user story
A store's POS system says **3 coffees sold**, while its inventory system shows **2 coffees removed**. The tool should flag **“Needs review: sale S-10, COFFEE, expected 3, recorded 2”**, link source record IDs and let a human investigate. It must not assume fraud, alter inventory or fabricate a financial loss.

Current private development implements an API-first, **read-only, synthetic** reconciliation preview; there is not yet a completed customer-facing interface, live connector, real business pilot or production deployment. The public developer contract is documented in `contracts/retail/RECONCILIATION_PREVIEW_V1.md`.

## Design commitments
Plain language, accessible 2D/mobile-friendly workflows, low bandwidth as a design goal, role-based access, cross-tenant separation, verifiable source provenance and visible uncertainty. More complex AI, finance, payments, worldwide regulatory packs and 3D views are deferred until the basic workflow is correct and useful.

## Intended editions (unvalidated)
Public/community interfaces and deliberately licensed source remain available under the repository's existing Apache License 2.0 as applicable. Proprietary internals and commercial integrations remain private. Managed hosting and enterprise service are future options, not existing prices or products. Every edition needs baseline security.

## How success will be judged
Actual retailer interviews, task completion without a developer, measured reconciliation coverage/false positives, time-to-detection and willingness-to-pay testing. No forecast, revenue, client count or expert approval is claimed without evidence.

**Commercial release gate:** genuine name clearance, security/privacy assessment, controlled staging and human approval. Do not submit customer data or sensitive vendor credentials to public issues.
