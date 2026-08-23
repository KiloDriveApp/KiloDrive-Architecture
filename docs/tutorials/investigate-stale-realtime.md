# Tutorial: Investigate a Stale Realtime Screen

“The other phone did not update” is a symptom, not a diagnosis. Realtime flows
cross several boundaries, and each boundary can fail independently.

Use the following order. It avoids guessing and prevents operators from
replaying work that already happened.

## 1. Establish durable truth

Use an authorized API query and correlated database evidence to determine the
current entity state and version.

- If the intended transition did not commit, investigate the command path.
- If it committed, do not repeat the business mutation just to make the screen
  move. Continue down the delivery path.

This distinction matters most for assignment and money. A second accept or
charge can cause real harm.

## 2. Find the durable event

Confirm the transaction created the expected outbox type with the entity ID,
version, tenant, correlation ID, and safe status.

- **No event:** producer transaction is incomplete; fix the producer and decide
  how to backfill affected entities safely.
- **Pending:** inspect worker heartbeat, claim age, dependency readiness, and
  oldest pending lag.
- **Failed:** inspect sanitized handler classification and retry count.
- **Completed:** continue to broker/hub/client evidence.

An “unknown handler” failure usually means producer and handler registration
were deployed out of step. Do not mark the row successful without performing or
explicitly superseding its promised effect.

## 3. Separate broker delivery from SignalR delivery

EventBridge/SQS and SignalR solve different problems. Cloud dispatch can queue
work for consumers; SignalR publishes ephemeral updates to connected clients.

Check bounded metrics and traces for:

- broker authorization or policy denial;
- queue depth, oldest message, or dead-letter growth;
- hub publish result;
- Valkey backplane connectivity and publish/subscribe ACL;
- connected-instance and subscription counts; and
- correlation ID continuity.

A healthy TCP connection to Valkey does not prove the account can publish to
the SignalR channel namespace. Authentication and ACL are separate checks.

## 4. Check connection and subscription context

Confirm the device authenticated the hub with a short-lived, hub-specific token
and subscribed to the correct user/trip group. Verify country/tenant context and
that reconnect restored group membership.

Never paste the hub access token into a ticket or log search. Telemetry should
drop the query parameter before storage.

## 5. Inspect client merge behavior

The event may have arrived and still been rejected by the app. Check:

- entity identifier matches the screen;
- server version is newer than the local version;
- the event decoder matches the deployed contract;
- the notifier is still mounted and watching the correct repository;
- no superseded request overwrote a newer result; and
- refresh errors preserve previous data with a visible partial-error state.

Wall-clock ticks are unsafe entity versions because clocks can move or differ
between nodes. Persisted monotonic versions make this decision deterministic.

## 6. Verify fallback reconciliation

Realtime is an accelerator, not the only recovery path. Resume, reconnect, push
tap, and a bounded fallback poll should reconcile from the authorized API.

Do not compensate for a broken realtime path by polling every endpoint every
second. That moves the incident into the API and database. Use bounded backoff,
visibility-aware refresh, and cache validators where supported.

## 7. Close the incident with evidence

Record:

- durable entity version before and after;
- outbox and broker status;
- hub/backplane status;
- client receipt/merge evidence;
- fallback convergence time;
- customer-visible duration; and
- the prevention test added.

The strongest regression test uses two deterministic clients and introduces a
disconnect between commit and delivery. It proves that the durable event and
reconciliation path converge without duplicating the business action.
