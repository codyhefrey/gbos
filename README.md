# Modular Business OS — Public Contracts and Community Interfaces

> **Working codename only: OPERIX.** The name has **not been cleared for commercial use**. Canadian trademark registration **TMA1233925** covers related construction-management SaaS services. This repository does not claim the right to commercialize under that name; seek legal clearance and choose a cleared brand before launch. This project is not affiliated with IFS Enterprises or any similarly named business.

## Project purpose
This is the **public, limited developer and integration layer** of a proposed global modular **Business Operating System** (formerly GBOS), not a generic RAG/voice AI knowledge platform. The wider product vision combines native ERP-style modules with opt-in integrations to existing business software, designed for global operations and Africa-first use cases.

Proposed domains include project/workforce/equipment management, procurement, inventory, POS, finance, treasury, integrations, governance and compliance. These are **design objectives**, not promises that a working ERP, payment rail or regulated service exists.

## What is public
Only independently reviewed API contracts, SDK/interfaces, integration examples, synthetic datasets, documentation and safe community contributions. The present `modules/` folders capture conceptual boundaries; a folder's presence does **not** establish feature completeness.

The planned first independently testable slice is a versioned retail contract with explicit tenant authorization, inventory changes, invoice posting, payment states and reconciliation. A [draft public contract pull request](https://github.com/codyhefrey/operix/pull/1) is **unmerged** and does not represent a production API.

## What remains private
The proprietary core, private AI logic, internal implementations, organization and customer data, credentials, security operations, hosting settings and paid product internals. The private repository is **not licensed through this repository**. Never copy confidential code or live records into a public issue, pull request, sample or release.

## Community and licences
Public source distributed under [Apache License 2.0](LICENSE) may be copied, forked and reused within its terms. **It is not legally possible to prohibit all replication of already published Apache-licensed files.** The separate private core is not public. Contributors must comply with [CONTRIBUTING.md](CONTRIBUTING.md), [GOVERNANCE.md](GOVERNANCE.md), [SECURITY.md](SECURITY.md) and [IP/reuse boundaries](docs/INTELLECTUAL_PROPERTY_AND_REUSE.md).

## Status and release gate
**Public documentation / experimental integration contracts only.** No production Business OS, authenticated multi-tenant service, payment service, app marketplace, external customer pilot or legal/trademark clearance is verified. Do not submit real data or claim the platform is production-ready. All changes need review for security, privacy, proprietary-source leakage, licensing and branding before release.
