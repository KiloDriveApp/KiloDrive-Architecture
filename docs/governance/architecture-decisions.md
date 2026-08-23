# Architecture Decision Process

Architecture is the set of decisions that remain expensive to change. KiloDrive
records those decisions so a new engineer can distinguish an intentional
boundary from an accident of implementation.

The public ADR index is in [`docs/adr`](../adr/README.md).

## When an ADR is required

Write or update an ADR when a change affects one or more of these areas:

- system-of-record or data ownership;
- country/tenant boundaries;
- security or privacy trust boundaries;
- externally visible API compatibility;
- financial invariants or settlement;
- event durability, ordering, or delivery semantics;
- technology/platform choice with long migration cost;
- availability, recovery, or operational ownership; or
- a dependency/licence decision that materially affects distribution.

A rename inside one private helper usually does not need an ADR. Moving driver
location from MySQL-only processing to a distributed geospatial index does.

## The decision conversation

### Start with the problem

Describe the observed limitation and the constraints. “Use Kafka” is a solution,
not a problem statement. A useful problem statement might be: “SQL outbox
polling creates unacceptable claim contention during dispatch bursts, while we
must retain recovery when cloud dispatch is unavailable.”

### Write the invariants

State what must remain true regardless of solution. Examples:

- one ride has at most one accepted assignment;
- one financial event is balanced and idempotent;
- a global identity has one authoritative credential record;
- a private document never becomes public during processing; and
- a stale client cannot overwrite a newer entity version.

Invariants make tradeoffs easier to evaluate and later tests easier to design.

### Compare realistic alternatives

Compare options under KiloDrive's actual constraints: migration risk, team
skill, operational burden, current providers, cost, compliance, and rollback.
Avoid a straw-man alternative that no reasonable team would choose.

### Decide the migration, not only the destination

Most architecture changes happen while users are active. The ADR should explain
compatibility, sequencing, backfill, dual-read/write duration if any, metrics,
rollback, and the point at which old behavior can be removed.

### Record consequences honestly

Every useful decision creates new work. Country cells improve financial and
jurisdictional isolation but make cross-country analytics and identity
projection harder. UUIDv7 improves key locality but still exposes approximate
creation order. Record both sides.

## Decision principles

- Prefer explicit ownership over shared mutable state.
- Keep a settlement transaction inside one country database.
- Use durable orchestration at cross-database and provider boundaries.
- Use distributed ephemeral state only where multi-node behavior needs it.
- Keep provider SDKs behind narrow interfaces.
- Publish truthful contracts and schema fingerprints.
- Prefer reversible evolution over synchronized breaking changes.
- Measure customer-visible outcomes, not only infrastructure health.
- Never trade validation or auditability for a temporarily green dashboard.

## Review and lifecycle

Architecture, domain, security/privacy, and operations owners review decisions
that affect them. Accepted ADRs are not silently rewritten; a changed decision
is superseded so future readers can understand the migration.

Implementation is complete only when code, schema, tests, observability,
runbooks, and public/restricted documentation agree.
