# Architecture Decision Records

An Architecture Decision Record (ADR) captures a decision that would otherwise
be rediscovered through code archaeology. It explains the pressures at the time,
the chosen option, the options declined, and the consequences engineers must
still manage.

ADRs are not marketing documents. A good ADR admits what became harder.

## Index

| ADR | Decision | Status |
| --- | --- | --- |
| [001](001-country-cell-sharding.md) | Country-cell sharding with a global identity control plane | Accepted |
| [002](002-uuidv7-identifiers.md) | RFC 9562 UUIDv7 for transactional identifiers | Accepted |
| [003](003-valkey-geospatial-state.md) | Valkey for fresh distributed geospatial state | Accepted |
| [004](004-osrm-map-matching.md) | Road-network map matching for route evidence | Accepted/Incremental |
| [005](005-eventbridge-sqs-outbox.md) | Hybrid cloud bus with SQL outbox recovery | Accepted |
| [006](006-private-object-storage.md) | Private, quarantined document storage | Accepted |
| [007](007-asymmetric-jwt-signing.md) | Asymmetric access-token signing and public JWKS | Accepted |
| [008](008-double-entry-wallet-accounting.md) | Wallet subledgers paired with double-entry journals | Accepted |
| [009](009-mysql-scripts-not-ef-migrations.md) | Reviewed idempotent MySQL scripts for schema evolution | Accepted |
| [010](010-flutter-feature-repositories.md) | Feature repositories and AsyncNotifiers in Flutter | Accepted/Incremental |

## Lifecycle

- **Proposed** — discussion is open; do not treat the design as deployed.
- **Accepted** — the decision governs current implementation.
- **Accepted/Incremental** — the direction is accepted, but migration is still
  occurring in clearly identified slices.
- **Superseded** — a newer ADR replaces the decision; the history remains.
- **Deprecated** — new work must not adopt the decision, but compatibility may
  remain during migration.

## Writing an ADR

Copy [000-template.md](000-template.md), choose the next number, and include:

1. context and forces;
2. decision and scope;
3. alternatives considered;
4. consequences—positive and negative;
5. security, privacy, reliability, performance, cost, and compliance effects;
6. migration and rollback;
7. observability and tests; and
8. affected documentation and runbooks.

Avoid hindsight theatre. Record the constraints that made the decision
reasonable, including team size, existing operational skill, provider limits,
and migration risk.
