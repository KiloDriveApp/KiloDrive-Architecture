# Architecture Decision Process

Material decisions are recorded as Architecture Decision Records (ADRs). An ADR
contains:

1. title, date, status, and owners;
2. context and forces;
3. decision and scope;
4. alternatives considered;
5. security, privacy, reliability, performance, cost, and compliance effects;
6. migration, rollback, and observability plan;
7. tests and release gates; and
8. runbooks/documentation affected.

## Decision principles

- favor explicit ownership over shared mutable state;
- keep financial consistency inside one country database;
- use durable orchestration at cross-database/provider boundaries;
- use distributed ephemeral state only where multi-node behavior requires it;
- keep provider SDKs behind narrow interfaces;
- publish truthful contracts and schema fingerprints; and
- choose reversible evolution over simultaneous breaking change.

Public ADRs must follow the documentation safety policy. Restricted operational
parameters belong in the private engineering repository.
