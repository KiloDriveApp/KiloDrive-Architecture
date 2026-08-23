# ADR 009: Manage schema evolution with reviewed idempotent MySQL scripts

- **Status:** Accepted
- **Date:** 2026-08-23
- **Decision owners:** Database, Architecture, API, and Operations
- **Related systems:** MySQL control database, country cells, EF Core model metadata, deployment, readiness, and country activation

## Context

KiloDrive has one global control database and multiple country-cell databases.
Every active cell must agree with the API's entity model and with the canonical
empty-database bootstrap. A change that succeeds on one schema and silently
misses four others is more dangerous than an obvious migration failure: one
country can start returning runtime errors while health checks elsewhere look
normal.

Early operational experience also showed that a version label is not proof of
shape. A database can claim the current version while a column has the wrong
nullability, decimal precision, collation, index, or foreign key. Conversely, a
correct additive schema may be rejected when a stale fingerprint was copied
into deployment configuration. We need one process that compares actual MySQL
metadata, model expectations, and bootstrap output—not a collection of loosely
related version strings.

The API uses EF Core as an object-relational mapper. That does not require EF
migration classes to be the deployment authority.

## Decision drivers

- One reviewed process must cover control and every country cell.
- A fresh empty bootstrap and an upgraded database must converge on the same
  normalized metadata.
- Scripts need to be inspectable, rerunnable, and safe after partial deployment.
- Operations must be able to apply and verify changes without a developer
  workstation or runtime migration privilege.
- Country activation and API readiness must fail on real contract drift.
- Empty tables are not evidence that a table is obsolete.
- Rollback must respect irreversible data transformations and financial audit.

## Decision

MySQL 8 scripts are the schema-change authority. KiloDrive maintains:

- a canonical, idempotent `database/schema.sql` that bootstraps the complete
  control and baseline country-cell shape plus reviewed reference data;
- ordered, approved, idempotent update/alignment scripts for deployed estates;
- EF Core model metadata used as an independent comparison input, not as a
  migration executor;
- normalized information-schema fingerprint specifications for control and
  country cells; and
- a schema contract version/fingerprint checked by startup, readiness, CI, and
  country activation.

Engineers do not generate or apply EF migration classes for production schema
evolution. The API deployment identity does not receive broad DDL authority.

### Idempotent change style

An update script determines whether the intended table, column, index, foreign
key, charset, collation, or seed exists in the expected form. It makes the
smallest reviewed change, records the schema contract only after verification,
and can run again without duplicating data or failing because the first run
partly succeeded.

Idempotent does not mean “ignore every error.” If an object exists with an
incompatible definition, the script stops with a diagnostic rather than
pretending success. Destructive operations require separate proof of zero
references, retention/legal approval, a recoverable backup, and explicit review.

### Canonical comparison

The comparison normalizes metadata from `information_schema` into stable rows
for tables, columns, indexes, foreign keys, charset/collation, generated/spatial
properties, and other contract-relevant details. Names and values are compared
with defined casing/order rules so MySQL's output order does not create a false
fingerprint.

The process compares four things:

1. a fresh schema created only from the canonical bootstrap;
2. a disposable clone upgraded through every approved update script;
3. EF Core model metadata; and
4. read-only fingerprints from control and every provisioned country cell.

The expected fingerprint is derived from reviewed canonical output. It is not
changed merely to silence a failing deployment.

### Deployment sequence

1. Back up and record recovery evidence.
2. Create disposable clones from representative metadata/data.
3. Apply the update to the clones and run bootstrap/model/fingerprint checks.
4. Run targeted application/fixture tests against the clone.
5. Apply control/cells in the reviewed order with an operator-owned script.
6. Verify each database immediately and record sanitized counts/hashes.
7. Deploy or start the compatible API binary.
8. Verify liveness, readiness, critical routes, workers, outbox, and
   reconciliation.

For an additive backward-compatible change, schema normally goes first and the
compatible binary follows. A rename/removal uses expand–migrate–contract across
multiple releases.

## Alternatives considered

### EF Core migrations as the production authority

EF migrations are convenient for application-local schemas and can produce a
useful development history. They were not chosen because the KiloDrive estate
needs one controlled script across several named databases, reference-data
alignment, information-schema fingerprints, and operator review independent of
application startup. Maintaining both EF migrations and SQL as competing
authorities would create drift.

### Let the API migrate on startup

This reduces deployment steps but grants the runtime broad DDL privilege and
mixes irreversible schema work with process availability. Multiple API nodes
can race, a long DDL can make startup opaque, and rollback becomes harder. It
was rejected for production.

### Manual database changes with a version table

This can repair an emergency quickly but is not reproducible. A version row says
nothing about actual column/index shape. Manual DDL is limited to an approved
incident procedure and must be folded back into the canonical scripts.

### Adopt a separate migration product immediately

Tools such as Flyway or Liquibase can orchestrate SQL well. They may be useful
later, but adopting one would not replace KiloDrive's need for idempotent MySQL,
cross-cell comparison, bootstrap parity, and governance. The current approach
keeps the executable contract transparent while leaving room for a future
orchestrator.

## Consequences

### Benefits

- A new environment and an upgraded environment converge on one schema.
- Database operators can review exact DDL and run it independently of the API.
- Runtime identities keep least-privilege DML access.
- Drift is detected before customer traffic and before country activation.
- Schema incidents can be diagnosed from normalized evidence instead of a vague
  “version mismatch.”
- Reference seeds, encoding, spatial definitions, and data constraints evolve
  with the tables that depend on them.

### Costs and risks

- Engineers must update SQL, EF configuration, fingerprints, fixtures, and
  documentation together.
- Idempotent MySQL DDL is more verbose than generating a migration.
- Large table changes need explicit online-DDL and capacity planning.
- A mistaken canonical fingerprint can block every cell; clone verification and
  review are mandatory.
- Differences that MySQL reports semantically but not textually require careful
  normalization.

## Security, privacy, and compliance

Production comparison uses read-only metadata credentials. The deployment
credential is time-bounded and scoped to the exact databases and DDL needed.
Scripts and evidence contain no connection strings, passwords, customer rows,
or private infrastructure identifiers.

Backups and clones preserve the source data classification. Production data is
not copied to an unmanaged developer environment. Retirement of privacy,
support, or financial tables follows retention, legal hold, audit, and
zero-reference proof; empty row count alone never authorizes a drop.

## Reliability and operations

- Startup/readiness reports the database name, mismatch count, expected/actual
  fingerprint, and a bounded safe sample of normalized metadata differences.
- Country activation remains blocked while control/cell fingerprints, shard
  directory, reference data, backup, or readiness evidence drift.
- Failed alignment stops at the first unsafe incompatibility and leaves an
  operator-readable checkpoint.
- Rollback uses the previous compatible binary for additive changes. Data-loss
  rollback requires restore or a reviewed compensating script.
- The [schema alignment runbook](../runbooks/schema-alignment.md) and
  [country activation runbook](../runbooks/country-activation.md) are the
  operational procedures.

## Validation

- Empty bootstrap versus fully upgraded clone metadata parity.
- EF model versus MySQL table/column/index/foreign-key comparison.
- Rerun tests proving each update is idempotent.
- MySQL 8 clone tests with representative data and constraints.
- API startup/readiness tests for match, safe mismatch reporting, timeout, and
  unavailable database.
- Activation tests proving a drifting cell cannot be enabled.
- UTF-8/collation round-trip tests for reference data and localized text.
- Restore rehearsal before any destructive or high-volume change.

## Follow-up

- Keep [schema lifecycle](../database/schema-lifecycle.md) and
  [database overview](../database/README.md) synchronized with the scripts.
- Generate a human-readable metadata diff beside every fingerprint failure.
- Measure DDL duration/locking on production-sized clones before rollout.
- Review whether a dedicated SQL orchestrator adds value as cell count grows.
