# Runtime profiles

KiloDrive remains a modular monolith. Runtime profiles change deployment
composition; they do not move a ride, wallet, membership or settlement
transaction across services or databases.

## Profile catalogue

| Profile | Public surface | Owned workload | Fail-closed requirements |
| --- | --- | --- | --- |
| `Combined` | REST, SignalR, health | Compatibility host with existing workers | Full request and worker configuration |
| `PublicApi` | REST and health | Request handling; optionally the single global control-plane worker owner | Shared backplane in multi-instance production; explicit ownership when global workers are enabled |
| `RealtimeGateway` | SignalR and health | Authenticated hub connections only | Shared SignalR backplane and token/tenant authorization |
| `CellWorker` | Health only | Outbox, lifecycle, expiry, reconciliation and transactional country work | Exactly one provisioned country cell |
| `MediaWorker` | Health only | Recording/media retention for one country | Exactly one country, enabled recording policy, private storage and retention role |
| `ReportingWorker` | Health only | Reporting schedules, metrics and signed evidence for one country | Exactly one country, signing-key identifier and protected key material |

## Composition invariants

- A health-only profile does not register controllers, hubs or unrelated
  provider clients.
- A country worker reads an immutable deployment binding. Request headers and
  user claims cannot change its cell.
- Missing, unsupported or conflicting profile/country settings fail startup.
- Media and reporting profiles do not dispatch the general country outbox. The
  corresponding `CellWorker` owns durable side-effect dispatch.
- Global identity expiry, global administrative notification, provider canary
  scheduling and similar control-plane work have one explicit deployment owner.
- Health checks report the profile and only the dependencies that profile owns.
  A reporting-only host is not degraded because it lacks a login provider.
- Shared contracts, identifiers, schema scripts and country-cell transaction
  boundaries remain common across profiles.

## Why this is not microservices

The profiles reduce endpoint exposure and let expensive or differently scaled
workloads run separately. They do not create independent databases or eventual
consistency inside one business command. A trip completion still settles the
trip, payment, wallet, journal, audit and first outbox row in one country-cell
transaction.

Splitting those writes into network services would introduce distributed commit
and recovery complexity without creating a product benefit. A future extraction
needs its own ADR and migration proof; profile composition is not permission to
perform it accidentally.

## Migration sequence

1. Deploy the unchanged `Combined` profile and validate `/health/profile`.
2. Start dedicated profiles without production traffic and validate
   composition/readiness.
3. Route hubs to `RealtimeGateway`, then REST to `PublicApi`.
4. Start one `CellWorker` per provisioned cell and verify outbox lease, lag and
   reconciliation metrics before retiring worker ownership in `Combined`.
5. Start media/reporting profiles only where their country, provider and secret
   gates are approved.
6. Transfer the single global control-plane owner during a coordinated handoff.

Rollback routes traffic to `Combined` and scales dedicated workers down. It
does not alter country data or roll back completed transactions.

## Verification

Composition tests start real hosts for supported profiles and assert route
presence/absence, dependency registration and failure on invalid configuration.
Deployment certification additionally needs a shared-backplane exercise,
worker handoff, duplicate-claim proof, readiness and lag observation, and a
rollback rehearsal.

Related material: [Hosting](hosting.md), [Realtime and events](realtime-and-events.md),
[country cells](tenancy-and-country-cells.md), and the
[runtime-profile rollout runbook](../runbooks/runtime-profile-rollout.md).
