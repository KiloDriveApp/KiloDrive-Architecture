# ADR 013: Runtime-profile composition without transactional service splits

- **Status:** Accepted
- **Date:** 2026-09-23

## Context

REST, SignalR, country workers, media retention and reporting have different
exposure and scaling needs. Splitting the domain into network services would
also split country-cell transactions and create distributed consistency work.

## Decision

Keep one repository, API project and shared contract. Compose deployments as
`Combined`, `PublicApi`, `RealtimeGateway`, `CellWorker`, `MediaWorker` or
`ReportingWorker`. Each profile registers only its owned endpoints, workers and
providers. Country workers bind exactly one provisioned cell and fail startup
on missing or conflicting configuration. Global control-plane work has one
explicit owner.

## Consequences

Attack surface and workload scaling can differ without weakening trip, wallet
or ledger atomicity. Deployment needs explicit worker-ownership handoff,
backplane configuration and profile-aware health checks. Running both old and
new scheduler owners during migration is prohibited even where record leases
make duplicate execution unlikely.

## Validation

Composition tests start each profile, assert route/provider/worker presence and
absence, validate health, and prove invalid configuration fails closed. Runtime
certification adds backplane, worker handoff, duplicate-claim, queue-lag and
rollback exercises.
