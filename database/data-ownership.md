# Data Ownership, Retention, and Consistency

## Ownership matrix

| Data class | Authority | Notes |
| --- | --- | --- |
| Credentials and sessions | Control plane | Never copied to country projections |
| Country authorization | Control plane | Maps a global identity to approved cell/tenant workspaces |
| Trips, deliveries, rentals | Country cell | Operational lifecycle remains local |
| Wallets and accounting | Country cell | One settlement transaction never crosses cells |
| Support and deletion orchestration | Control plane | Country execution checkpoints coordinate local work |
| Country financial/trip retention | Country cell | Local legal and accounting rules apply |
| Private object metadata | Control or owning cell by content class | Bytes remain in private object storage |
| Realtime cache | Valkey | Ephemeral; MySQL is authoritative where durability is required |

## Consistency model

Within one database, domain state, ledger/audit linkage, and outbox work are
committed transactionally. Between control and a country projection, a durable
registration/orchestration saga provides eventual consistency with idempotent
reconciliation and compensation.

## Retention

Retention is content-class and jurisdiction aware. Financial journals are
immutable and corrected with reversing entries. Completed outbox rows may be
archived after configured retention. PII is deleted or anonymized when permitted;
legal holds suspend automated removal without making artifacts public.
