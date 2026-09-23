# Runtime-profile rollout and rollback

- **Owner:** Platform Operations
- **Status:** Reviewed public procedure
- **Last exercised:** 2026-09-23 (composition-test review)
- **Related architecture:** [Runtime profiles](../architecture/runtime-profiles.md)

## Preconditions

- Exact source, package and schema contract are identified.
- Every target country is provisioned and schema-aligned.
- Shared SignalR/Valkey transport is healthy where multiple nodes participate.
- Worker leases, outbox idempotency, readiness and lag metrics are visible.
- Media/reporting secrets are present only at the deployment secret boundary.
- One current owner is named for global control-plane workers.

## Rollout

1. Deploy `Combined` with the new composition code and verify liveness,
   profile and readiness.
2. Start dedicated profiles without routing traffic or enabling duplicate
   schedulers. Validate their route/provider/worker inventory.
3. Route hub traffic to `RealtimeGateway`; exercise connect, reconnect, group
   restoration and backplane failover.
4. Route REST traffic to `PublicApi`; verify canonical paths, authentication,
   tenant/country resolution and health.
5. Start one `CellWorker` for one country. Observe claim ownership, oldest
   outbox age, retries and reconciliation before repeating by country.
6. Start `MediaWorker` or `ReportingWorker` only for approved cells and verify
   private storage/retention or signed evidence respectively.
7. Stop the old global worker owner, then enable the designated `PublicApi`
   control owner. Never overlap intentionally.
8. Retire `Combined` only after every owned workload and rollback signal is
   accounted for.

## Stop conditions

Stop for ambiguous country binding, two scheduler owners, increasing outbox
age, duplicate side effects, schema mismatch, backplane isolation, unsigned
evidence, cross-country work, missing readiness dependency or unexplained
reconciliation exceptions.

## Rollback

Route REST and hubs back to the healthy `Combined` host, disable dedicated
workers and restore the previous single control owner. Do not delete leases,
outbox rows, lifecycle evidence or accounting records. Verify that claims
expire/recover and queues drain once under the restored owner.

## Evidence

Retain profile inventory, package/schema identity, timestamps, safe deployment
references, health results, worker ownership transitions, lag/retry charts,
duplicate-effect checks and rollback outcome. Do not publish hostnames, account
IDs, private addresses, secrets or raw provider payloads.
