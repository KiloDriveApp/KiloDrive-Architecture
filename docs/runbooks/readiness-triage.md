# Readiness triage runbook

- **Owner:** Site reliability and API platform operations
- **Status:** Operational incident-triage procedure
- **Last exercised:** Not yet recorded in this public repository
- **Related architecture:** [Observability](../architecture/observability.md), [hosting](../architecture/hosting.md), and [realtime and events](../architecture/realtime-and-events.md)

## Purpose and scope

Use this runbook when the API process is alive but `/health/ready` reports
`Degraded` or `Unhealthy`, or when a deployment cannot safely receive normal
traffic. It covers schema, database, Valkey, SignalR backplane, workers/outbox,
queues, accounting reconciliation, required providers, and telemetry.

Liveness answers “can this process answer?” Readiness answers “is this instance
safe to serve its intended workload?” Restarting an alive-but-unready process
without understanding the failed check often erases the best evidence and does
not fix the dependency.

## Owners and roles

| Role | Responsibility |
| --- | --- |
| Incident lead | Sets severity, scope, containment, communications, and closure |
| Application operator | Captures build/config/health evidence and manages node traffic |
| Database operator | Diagnoses reachability, pool/waits, schema, and fingerprints |
| Realtime/queue owner | Diagnoses Valkey ACL/backplane, EventBridge/SQS, and outbox |
| Financial owner | Reviews reconciliation and authorizes cashout/money controls |
| Provider owner | Reviews required provider configuration and safe canaries |

## Preconditions

Have access to the health endpoint, deployment/package identity, sanitized logs,
metrics/traces, database metadata through least-privilege credentials, Valkey and
queue status, and the current approved configuration shape. Know how to remove a
single node from traffic without shutting down healthy peers.

## Safety and stop conditions

Stop rollout and remove the affected node from traffic when:

- schema contract is invalid;
- the serving package/commit cannot be identified;
- accounting has an unexplained critical mismatch;
- global identity or tenant/country boundaries may be wrong;
- required signing/data-protection material is unavailable;
- database state may be corrupt; or
- a dependency “fix” would require broadening credentials, disabling TLS,
  bypassing schema validation, disabling the rate limiter, or hiding the check.

Do not change readiness to always return healthy. Do not mark missing provider
credentials optional when the selected feature depends on them. Do not dump
outbox payloads, connection strings, access tokens, customer records, or exact
private infrastructure identifiers into evidence.

## First five minutes

1. Record UTC time, health response, node, environment, reported commit/package,
   schema version, and recent deployment/config/schema change.
2. Capture the request correlation ID and a sanitized copy of each check's status,
   description, latency, and bounded metadata.
3. Confirm liveness from inside and outside the service boundary.
4. Determine scope: one node, all nodes, one country cell, global control, one
   capability, or all traffic.
5. Freeze rollout. Keep healthy nodes serving if doing so is safe.
6. Classify the failed check using the decision table below.
7. Apply the narrowest containment before attempting repair.

## Decision table

| Signal | Meaning | Immediate safe action |
| --- | --- | --- |
| Process not live | runtime/startup/site/ACL failure | keep node out; inspect startup and use API deployment rollback |
| Schema contract invalid | binary/configured fingerprint/live metadata disagree | remove node; run read-only metadata comparison |
| Database unreachable | network, credential, TLS, server, DNS, or failover issue | block writes; verify endpoint and role without exposing string |
| Database pool/waits saturated | slow/leaked/blocked queries or insufficient capacity | shed noncritical work; inspect bounded waits and pool metrics |
| Worker heartbeat stale | worker stopped, starved, cancelled, or crashed | pause dependent feature; identify worker/process scope |
| Outbox lag/pending rising | handler, queue, provider, poison data, or throughput issue | isolate oldest types and handler; do not replay everything |
| Permanent outbox failure | missing handler or non-transient contract/provider failure | disable affected producer; repair/recover typed message |
| Valkey unreachable | network/TLS/endpoint/capacity issue | preserve MySQL truth; degrade cache/realtime explicitly |
| Valkey `NOPERM` | authenticated principal lacks channel/key ACL | correct least-privilege namespace grants; do not use an admin user |
| Reconciliation mismatch | financial invariant or expectation defect | block cashout/affected money path; follow wallet runbook |
| Required provider missing | configured feature cannot operate | correct protected config/permission or disable feature intentionally |
| Optional canary not configured | probe enabled before destination/credential exists | disable that canary; do not page as provider outage |
| Telemetry exporter down | visibility degraded, application may still operate | restore observability; increase operational caution |

## Diagnostic sequence

### 1. Prove binary and configuration identity

Compare the process-reported version/package hash with the reviewed release and
Git commit. Do not infer binary currency from the database schema version. Verify
the process runs under the intended identity and reads the intended protected
configuration paths.

If only one node fails, compare package manifest, process identity, ACLs,
environment variables, clock, and network route with a healthy peer—without
printing secret values.

### 2. Schema and database

Capture server version, connection latency, pool usage, bounded wait/lock
information, schema versions, and normalized fingerprints for control and every
configured cell. A repeated `configuration:1` mismatch can mean metadata/config
disagrees even when tables look correct.

Never edit the expected hash to match an unexpected schema. Use the
[schema alignment runbook](schema-alignment.md).

### 3. Valkey and realtime

Separate reachability, authentication, TLS, keyspace ACL, Pub/Sub channel ACL,
latency, memory/eviction, and SignalR backplane behavior. A successful `PING`
does not prove `PUBLISH`/`SUBSCRIBE` permission for the hub namespace.

Confirm durable ride/bid/chat state remains in MySQL/outbox. During backplane
degradation, clients should reconcile through bounded polling rather than assume
an event was the only truth.

### 4. Workers, outbox, bus, and queue

Check heartbeat age, oldest pending message, lag by type, retry/permanent counts,
handler registration, queue depth, dead-letter state, and cloud permission errors.
Look for a missing handler or `PutEvents` denial before adding worker capacity.

Distinguish expected `OperationCanceledException` during deliberate host shutdown
from a background worker failure. A worker that throws unexpectedly must have a
restart/recovery strategy; configuring the host to ignore every exception hides
lost work.

### 5. Accounting

Check reconciliation query timestamp and exception categories. A stale “zero” is
not proof. If debit/credit, wallet, held funds, cashout clearing, membership
journal, or provider settlement is unexplained, block cashout and follow the
[wallet reconciliation runbook](wallet-reconciliation.md).

### 6. Providers and canaries

Confirm required-versus-optional status, selected provider, workload permission,
region, quota, and dedicated canary destination. Store only provider ID, latency,
sanitized status, and correlation ID. Never probe a real user to make readiness
green.

### 7. Telemetry path

Verify the app can emit and the collector can receive/export metrics/traces/logs.
Telemetry loss should be visible as its own degradation, not mistaken for zero
errors or zero queue lag.

## Containment and recovery by class

### One bad node

Remove it from traffic, retain evidence, and compare it with a healthy node. If a
release caused the difference, use the [API deployment runbook](api-deployment.md)
to switch back to the previous immutable package. Reintroduce only after two
healthy windows.

### Schema drift

Keep the binary out of traffic. Perform read-only comparison, clone rehearsal,
reviewed idempotent alignment, fingerprint verification, then canary startup. Do
not disable startup validation.

### Database capacity/connectivity

Shed expensive noncritical work, pause controlled workers, and restore the known
endpoint/credentials/network. Do not increase connection pool sizes blindly;
that can overwhelm MySQL faster. Verify waits and pool behavior before tuning.

### Valkey/backplane

Preserve MySQL as truth, expose degraded realtime, and use bounded reconciliation
polls. Correct TLS/ACL/endpoint/capacity narrowly. Force stale driver presence
offline rather than extending freshness indefinitely.

### Outbox/queue

Stop the affected producer if it creates unhandleable work. Add/fix the typed
handler or least-privilege bus permission, reconcile unknown provider outcomes,
then retry selected idempotent messages. Do not reset all failed rows to pending.

### Financial mismatch

Disable cashout and the affected mutation, preserve evidence, find the earliest
bad business reference, and repair through an approved compensating domain
transition. Never update balances/journals directly for cosmetic readiness.

### Provider missing/failing

Disable the selected feature if a safe fallback does not exist. A provider is
optional only when the user journey has an intentional alternative. Restore
protected configuration/permission and prove with a dedicated canary.

## Rollback

If readiness failed immediately after an application release and schema remains
backward compatible, remove the new canary and switch to the previous immutable
package. If a configuration change caused it, restore the last reviewed
configuration contract without overwriting protected keys.

Do not perform destructive schema rollback from this runbook. If data integrity
is uncertain, keep traffic blocked and invoke backup/recovery or schema alignment
under incident command.

## Verification criteria

Readiness is recovered only when:

- correct package identity is serving;
- every required check reports the expected status and fresh timestamp;
- schema version/fingerprints are valid;
- database pool/waits and Valkey latency/ACL are healthy;
- worker heartbeat is fresh and queue/outbox lag decreases to normal;
- reconciliation has zero unexplained critical exceptions;
- required provider canaries pass with dedicated destinations;
- representative success and sanitized error-path requests work; and
- the next scheduled worker/canary cycle completes.

Observe at least two full monitoring windows. Do not close immediately after one
green sample.

## Evidence to retain

Retain incident/change ID, roles, UTC timeline, health payload with sensitive
fields removed, package identity, schema fingerprints, bounded dependency
metrics, oldest outbox types/IDs, reconciliation summary, provider IDs/status,
mitigation, smoke correlation IDs, two-window recovery, rollback, and follow-up
owner.

## Escalation

Escalate to incident command for global outage, schema/data corruption,
cross-tenant/country risk, signing/data-protection failure, unreconciled money,
stalled privacy/safety work, repeated unknown provider outcomes, or inability to
identify the serving binary. Do not accept those as routine degradation.

## Common pitfalls

- Restarting first and losing the failure state.
- Calling liveness “healthy production.”
- Editing expected fingerprints to silence schema drift.
- Increasing MySQL pools when slow queries already saturate the server.
- Granting Valkey `allcommands allkeys` to fix one Pub/Sub ACL.
- Resetting all outbox failures without checking idempotency and handler support.
- Treating absent telemetry as zero failures.
- Letting optional unconfigured canaries generate permanent warning noise.
- Disabling a readiness check instead of disabling the unsafe feature.
