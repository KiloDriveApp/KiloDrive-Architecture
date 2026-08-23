# Runbook: outbox backlog and failed messages

- **Owner:** API platform, eventing, and provider operations
- **Status:** Operational durable-work recovery procedure
- **Last exercised:** Not yet recorded in this public repository
- **Related architecture:** [Realtime and events](../architecture/realtime-and-events.md) and [EventBridge and SQS](../aws/eventbridge-sqs.md)

**Use when:** outbox oldest age grows, failed count is non-zero, a worker
heartbeat is stale, notifications/realtime updates stop, or readiness reports an
outbox problem.

**Safety rule:** an outbox row is evidence of committed work. Never delete or
mark it complete merely to make readiness green.

## What the outbox guarantees

A domain handler writes its business state and side-effect intent in one country
database transaction. The worker runs later. This means an email outage should
not roll back a wallet transfer and an API restart should not lose a ride event.

Delivery is at least once. Handlers must use stable references, entity versions,
or provider reconciliation to make repeats safe.

## Impact levels

| Severity | Example |
| --- | --- |
| Critical | financial/escrow/recording lifecycle stuck; correctness at risk |
| High | ride dispatch or security notification delayed across a country |
| Medium | one provider/template/tenant failing while recovery works |
| Low | archive lag with active processing healthy |

## First five minutes

1. Open the outbox/readiness dashboard and note environment, country cell,
   oldest age, pending/failed count, worker heartbeat, and recent deployment.
2. Start a restricted incident record with correlation IDs and safe message IDs.
   Do not copy payloads, contacts, routes, or tokens.
3. Determine whether domain mutations still commit. If financial correctness is
   uncertain, pause the narrow capability (for example cashout), not the entire
   API.
4. Check for a single message type versus broad worker failure.
5. Check EventBridge/SQS and provider health only after confirming the SQL worker
   state; an empty queue does not prove dispatch is healthy.

## Diagnosis

### 1. Worker loop and lease

- Is the heartbeat current?
- Is the process running the intended release and worker cell?
- Are database connections, thread pool, CPU, and memory healthy?
- Are leases expiring, duplicated, or stuck in processing after a crash?
- Did a cancellation during shutdown get logged as a real worker failure?

A stale heartbeat with no message-specific errors points to process, scope,
database, or scheduling failure. A current heartbeat with one repeating type
points to a handler or dependency.

### 2. Message contract

- Identify type, safe ID, tenant/cell, attempt count, availability time, and
  sanitized error.
- Confirm a handler is registered for the exact type.
- Confirm producer and consumer versions agree on payload schema.
- Reproduce with a sanitized fixture at the same entity lifecycle state.

KiloDrive previously produced `trip.status_changed` messages without a registered
handler. The correct response is to restore the release contract and replay—not
to discard the rows.

### 3. Dependency and unknown outcome

Classify the operation:

- pure/internal and safe to retry;
- provider call with stable idempotency key;
- provider call with queryable/reconcilable status;
- provider call with unknown result and no safe reconciliation; or
- obsolete because a later persisted entity version supersedes it.

For email/SMS/push, inspect the safe provider attempt record. For payment or
egress, reconcile the provider reference before retrying. A timeout does not mean
the provider rejected the request.

### 4. Database contention

Check query duration, deadlocks, locks, pool saturation, batch size, and claim
ordering. Avoid raising concurrency when MySQL is already saturated. Reduce a
worker batch temporarily only if the change is understood and reversible.

### 5. Broker acceleration

For broker-eligible dispatch:

- Did EventBridge accept or deny publication?
- Does the rule target the intended queue?
- Is queue policy valid?
- Is oldest SQS age rising?
- Is the consumer enabled and allowed to receive/delete?
- Is SQL recovery age working?

An IAM `PutEvents` denial leaves SQL recovery enabled. Fix the narrow permission;
do not grant administrator access or disable fallback.

## Containment

- Stop/reduce only the producer that is creating harmful poison messages.
- Put a provider/capability in documented maintenance mode if repeated sends
  could duplicate money or communication.
- Keep valid pending work intact.
- Preserve failed rows, safe error classification, release version, and metrics.
- If a handler causes an unsafe mutation, deploy/rollback the handler before
  replay.

## Recovery

1. Fix configuration, dependency, handler, or data-contract root cause.
2. Prove the corrected handler with a non-production or dedicated fixture.
3. For unknown external outcomes, reconcile before release.
4. Use the protected System Administrator recovery action or reviewed tooling to
   requeue only the selected messages.
5. Drain gradually. Watch database/provider saturation and user duplicates.
6. Leave later-version obsolete events as audited terminal outcomes according to
   policy; do not pretend they executed.
7. Archive completed rows only after normal retention.

## Rollback

If the fix worsens failures, stop the narrow consumer, restore the last compatible
binary/configuration, and keep rows pending. Do not roll the database backward.
When a new payload format caused the problem, a compatibility handler or forward
fix is usually safer than reverting producers while new rows already exist.

## Verification

- Worker heartbeat is current.
- Pending oldest age declines to normal without a failure spike.
- Failed rows are explained and resolved, not deleted.
- Replayed duplicates produce one logical side effect.
- EventBridge/SQS and SQL recovery agree on acknowledgement.
- Notification/provider records show no duplicate user communication.
- Wallet/ledger reconciliation remains clean.
- Readiness returns expected healthy/degraded state.
- Logs/traces contain correlation and safe IDs only.

## Closeout

Record timeline, message types, affected cells, customer impact, root cause,
recovery evidence, and follow-up owner. Add a producer-to-handler contract test if
the gap was missing registration. Review alarm thresholds only after the system
is stable; do not tune away a real incident.
