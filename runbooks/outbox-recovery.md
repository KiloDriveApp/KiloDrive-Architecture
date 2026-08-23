# Runbook: Outbox Recovery

## Symptoms

Oldest-message age increases, failed count rises, worker heartbeat is stale,
provider notifications stop, or durable events do not reach realtime/provider
adapters.

## Procedure

1. Identify country cell, event type, handler, attempt count, and sanitized error.
2. Confirm that the domain transaction committed and the handler is registered.
3. Check worker health, database locks, leases, queue/broker state, and provider
   availability.
4. Classify messages as safe retry, reconciliation required, poison/invalid, or
   obsolete after a superseding entity version.
5. For mutating providers, reconcile provider state before retrying an unknown
   result.
6. Use the protected recovery action to release/requeue only reviewed messages.
7. Verify idempotency, downstream state, lag recovery, and no duplicate user
   communication or financial entry.
8. Archive completed rows only after the configured retention period.

Never delete pending/failed messages merely to make readiness healthy. Preserve
sanitized failure evidence and correct the handler/configuration.
