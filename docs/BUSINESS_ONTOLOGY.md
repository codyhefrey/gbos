# GBOS Business Ontology and Knowledge Graph v0.1

Status: design proposal; no graph or inference engine deployed.

## Core entities
Tenant, LegalEntity, BusinessUnit, Branch, Person, Role, Asset, Product, Service, Customer, Supplier, Contract, Obligation, Order, InventoryMovement, Invoice, JournalEntry, PaymentInstruction, PaymentStatus, WorkItem, Policy, Decision, Evidence and Event.

## Core relationships
owns, operates, employs, authorizes, supplies, purchases, fulfills, invoices, pays, posts, depends_on, governs, approved_by, derived_from and audited_by.

## Invariants
- Every entity and edge is tenant-scoped, with explicit cross-entity permissions.
- Relationships carry provenance, effective dates and version history.
- The graph is a read model, not a replacement for authoritative ledgers or payment-provider status.
- Never infer beneficial ownership, fraud or legal status as established fact from graph proximity alone.
- Data minimization, access-controlled traversals, retention and export requirements apply.

## First implementation
Define versioned entity schemas; event-driven projections from POS, Inventory and Finance; permission-aware graph queries; relationship integrity tests; explainable decision provenance.
