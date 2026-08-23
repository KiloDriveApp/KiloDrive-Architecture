# ADR 001: Country-cell sharding with a global identity control plane

- **Status:** Accepted
- **Date:** 2026-08-23
- **Decision owners:** Architecture, Identity, Finance, and Operations
- **Related systems:** MySQL, API country routing, tenant resolution, privacy orchestration

## Context

KiloDrive serves transportation and rental workflows whose rules, money,
providers, support duties, and retention can vary by country. At the same time,
a person should have one security identity rather than unrelated passwords in
every country database.

A single global schema would make cross-country reporting easy, but it would
also put every country's hot ride and wallet workload, failure domain, and
regulated data in one place. A separate database for every tenant would maximize
isolation but multiply operational overhead far beyond the team's needs.

The hardest constraint is financial: a ride, delivery, transfer, cashout, or
rental settlement must not depend on an unreliable distributed transaction
between country databases.

## Decision drivers

- One global account-security authority is required.
- Country operational and financial data needs a clear jurisdictional owner.
- A busy or unavailable country should not corrupt another country's ledger.
- Local transactions must preserve wallet, payment, journal, and outbox
  invariants atomically.
- The team must be able to provision, back up, restore, align, and monitor the
  topology with familiar MySQL tooling.
- System Admin cross-country access must be explicit and audited.
- New countries need an activation gate, not only a connection string.

## Decision

KiloDrive uses:

1. one global MySQL control database (`kilodrive_control`) for identity,
   authentication/security state, country and shard directory, country/tenant
   memberships, global security audit, System Admin grants, and global
   orchestration; and
2. one complete MySQL operational cell per provisioned country, such as
   `kilodrive_jm`, containing tenant-local users (without credentials), drivers,
   vehicles, rides, deliveries, rentals, wallets, payments, accounting, audit,
   safety, notifications, and outbox records.

An ordinary authenticated request is pinned to the signed home-country and
tenant claims. A System Admin selects an authorized country and acting tenant;
middleware validates and audits that context. EF global filters apply tenant
scope inside the selected cell.

A financial transaction is never split between control and a cell or between
two cells.

Cross-store identity creation uses a durable saga:

- control commits the identity, checkpoint, and inactive cell membership;
- the cell projection is created idempotently;
- membership becomes active only after projection success; and
- a leased reconciliation worker retries or, under strict proof, compensates an
  abandoned projection.

## Alternatives considered

### One global database with `CountryCode` and `TenantId`

This is simpler for ad hoc joins and initially cheaper to operate. It was not
chosen because it couples country failures and write load, makes jurisdictional
separation less clear, and increases the blast radius of operational mistakes.
It may still be appropriate for a small non-financial product with one operating
region.

### Database per tenant

This provides very strong tenant isolation and independent restore. It was not
chosen because KiloDrive's immediate sovereignty and scaling boundary is the
country, while database-per-tenant would create excessive connection, schema,
backup, and deployment overhead. Tenant query filters and ownership checks
remain mandatory inside a cell.

### Database per domain service

Identity, rides, wallet, and rentals could each own a database. This aligns with
large independent teams but would split the transaction graph that currently
needs atomicity—especially bid acceptance and settlement. It also adds message
contracts and reconciliation work before scale or team ownership requires it.

### Distributed SQL spanning regions

A distributed SQL product could expose one logical database. It was not chosen
because global consensus latency, cost, operational unfamiliarity, and unclear
jurisdictional placement do not remove the need for application ownership
boundaries. It may be reconsidered if measured requirements exceed the current
cell model.

### Duplicate full identity in every country

This avoids cross-store projection but creates password, session, MFA, and
revocation drift. It was rejected. Country `Users` records are credential-free
projections only.

## Consequences

### Benefits

- Country failures and load are contained.
- Financial transactions remain local and understandable.
- Country-specific retention, rules, providers, and scaling can evolve
  independently.
- One global security identity supports consistent revocation and account
  protection.
- System Admin country access is explicit rather than inferred from a local
  projection.
- Country activation can require schema, reference, backup, monitoring, and
  policy readiness.

### Costs and risks

- Cross-country analytics cannot use casual request-time joins. It needs
  governed reporting/export projections.
- Registration and global compliance updates require sagas/outboxes and
  reconciliation.
- Every schema change must be applied and verified across all provisioned cells.
- Operational tooling must understand control versus cell ownership.
- A bad connection directory or admin country selection can route work to the
  wrong cell; signed claims, explicit headers, and audit mitigate this.
- Failover must fence the old writer to prevent split brain.

## Invariants

1. Control is the only authentication authority.
2. No password, MFA secret, refresh token, recovery code, or passkey ceremony is
   copied into a country projection.
3. A wallet/payment/accounting mutation touches exactly one country cell.
4. A cell user row cannot grant a global workspace membership.
5. `IgnoreQueryFilters()` requires explicit tenant predicates and documented
   authorization.
6. A country is not activated until shard provisioning and a fresh schema
   fingerprint succeed.
7. A failover has one writable cell; two writers are never an availability
   strategy.

## Security, privacy, and compliance

The design reduces the operational blast radius of local data and supports
country-specific retention. It does not automatically prove data residency or
regulatory compliance; infrastructure placement, backups, provider routes,
support access, and legal policy must match the country operating model.

Cross-tenant System Admin actions require a validated acting context, fine-grain
permission where applicable, and global/local audit. Anonymous country/tenant
routing is narrow and does not become authority after authentication.

Deletion is centrally orchestrated but cell-local for trip and financial
anonymization. Legal holds can delay a country checkpoint without exposing the
retained record globally.

## Reliability and operations

- Monitor registration sagas by status, age, attempts, and lease health without
  logging their payloads.
- Verify every cell's schema contract at production startup/readiness.
- Back up and test restore of control and each cell independently, while
  documenting consistent recovery points.
- Fence a failed cell writer before promoting another.
- Resume cell workers gradually after failover and inspect outbox, assignments,
  idempotency, and wallet reconciliation.
- Keep a country inactive when its fingerprint, references, providers, or
  operating approval drift.

Rollback normally means returning to the prior compatible API binary while
leaving additive schema in place. Reversing financial/cross-store data changes
requires an incident-led recovery decision, not ad hoc SQL.

## Validation

- Two-tenant query-filter and same-tenant IDOR integration tests.
- Ordinary-user header override rejection tests.
- Global System Admin with no local projection and country-switch tests.
- Registration failure between control and cell, worker retry, duplicate retry,
  and compensation tests.
- Empty bootstrap and upgrade fingerprint parity across every provisioned cell.
- Concurrent money lifecycle and crash-point tests proving no cross-cell write.
- Country activation and failover tabletop exercises.

## Follow-up

- Keep [tenancy and country-cell documentation](../architecture/tenancy-and-country-cells.md)
  aligned with the resolver and saga.
- Use [schema lifecycle](../database/schema-lifecycle.md) for every cell change.
- Use [data ownership](../database/data-ownership.md) to place new entities.
- Revisit the boundary only with measured scaling, regulatory, or team-ownership
  evidence.
