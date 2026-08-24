# Ride Dispatch and Bidding Recovery

- **Owner:** Marketplace operations with API/realtime support
- **Status:** Implemented architecture with configurable cloud dispatch
- **Last exercised:** Not yet recorded in this public repository
- **Related architecture:** [Realtime and events](../architecture/realtime-and-events.md), [geospatial processing](../architecture/geospatial.md), [ADR 005](../adr/005-eventbridge-sqs-outbox.md)

## Purpose

Use this runbook when eligible drivers do not receive current ride offers,
offers remain visible after cancellation, bids do not reach riders, or
acceptance leaves one or both clients stale.

The safety boundary is simple: never create a second assignment to repair a
display problem. Durable ride/bid/trip state is authoritative.

## Common symptom groups

| Symptom | Likely area |
| --- | --- |
| No eligible driver receives the request | eligibility, location freshness, filtering, outbox, broker, or worker |
| Some drivers receive it and others do not | country/tenant scope, vehicle/trust filters, location grid, subscription, or client state |
| Driver acts but rider only sees a notification | SignalR group/backplane, client merge, or missing reconciliation |
| Cancelled request remains visible | missing durable cancellation event, delayed worker, stale client cache, or failed fallback refresh |
| Two accepts appear possible | missing/incorrect lock, version, idempotency, or conditional transition—treat as high risk |
| Scheduled ride is stuck or falsely guaranteed | cutoff/reconfirmation job, eligibility recheck, replacement transition, clock/country policy, or stale client projection |
| Airport/venue queue position never changes | expired queue heartbeat, stale location, duplicate active entry, active assignment, or realtime/cache projection |

## Establish authoritative state

With authorized, read-only tooling, determine:

1. ride/request status and persisted version;
2. current bidding deadline and expiry state;
3. actionable bids, not cumulative historical bid count;
4. assignment/trip identity if accepted;
5. selected driver and snapshotted vehicle/compliance version; and
6. durable event/outbox records for create, fare change, bid change,
   cancellation, assignment, and completion.

If the assignment committed, do not replay acceptance. Repair delivery and
client convergence.

## Check driver eligibility at two moments

Eligibility is required both when displaying an offer and when accepting a bid.
At acceptance, revalidate inside the locked transaction:

- online state and fresh permitted location;
- no conflicting active assignment;
- duty/rest limits;
- verified licence and profile requirements;
- compliant selected vehicle and required documents;
- active membership/plan limits where applicable;
- requested vehicle capabilities and rider trust level; and
- block/safety restrictions.

A driver can become ineligible after bidding. A stale bid is not permission to
skip the final gate.

## Trace dispatch delivery

Follow one correlation ID and entity version through:

1. business commit and outbox insertion;
2. outbox claim/handler registration;
3. EventBridge publish or SQL recovery fallback;
4. SQS delivery/consumer result where enabled;
5. SignalR publish and Valkey backplane ACL;
6. push fallback; and
7. client receipt, version merge, and authorized refresh.

An IAM denial on the cloud bus should raise an operational signal while SQL
recovery continues. Do not suppress it indefinitely; the fallback protects
correctness but may not meet intended latency or capacity.

## Viewer counts and offer freshness

Do not infer “viewing” from a feed response. The driver client sends an explicit
short-lived heartbeat for the ride currently visible. Counts expire naturally
when the screen closes or connectivity is lost.

Offer expiry closes the ride even if stale bids exist. Fare reductions do not
silently rewrite a driver's previous acceptance; affected bids expire or
require renewed consent.

## Scheduled reservations and managed queues

A scheduled request is **Searching**, **Driver reserved**, **Confirmation
required**, **Guaranteed**, **Replacement searching**, or **Not guaranteed**
according to durable state and country timing policy. Saved is never a synonym
for guaranteed. Trace the expected-version delayed job, final eligibility
recheck, reconfirmation event and replacement transition on the same ride. Use
the [scheduled-ride guarantee runbook](scheduled-ride-guarantee.md) for recovery.

Airport/venue queues are expiring memberships, not permanent ranks. Joining
requires an online eligible driver, fresh permitted position inside the zone,
and no active assignment. A driver can occupy only one active queue. Check zone
configuration, location age, queue heartbeat, unique active membership, order,
assignment transition and client projection. Remove/expire a stale entry through
the supported queue command; do not reorder or delete competitors manually.

## Contain

- If duplicate assignment is possible, pause acceptance for the affected scope
  and preserve evidence.
- If only cloud publishing is broken, retain SQL recovery and reduce dispatch
  claims only if worker/database saturation requires it.
- If location freshness is invalid, expire drivers offline rather than matching
  against stale positions.
- If clients are stale but durable state is correct, increase bounded
  reconciliation—not business-command retries.

## Recover

Use supported outbox replay or broker redrive with the original event identity.
Repair missing consumer registration before replay. For old clients, ensure the
fallback query returns current state and versions.

Never manually change a ride status without its canonical lifecycle transition,
audit evidence, version increment, and event implications.

## Verify

Run a deterministic two-client fixture through:

1. create and publish;
2. fare adjustment;
3. bid, withdrawal, and replacement;
4. reject or accept;
5. chat;
6. arrive, start, and complete or cancel; and
7. disconnect/retry at commit and publish boundaries.

Add scheduled reserve/reconfirm/replacement/cutoff races and queue join,
heartbeat expiry, duplicate join, assignment removal, network loss and re-entry
when either feature changes.

Verify no duplicate assignment, both screens converge, cancelled/expired offers
disappear, event versions increase, and durable backlogs return to normal.

## Follow-up

Retain sanitized correlation evidence and add a regression test at the boundary
that failed. Update capacity thresholds only after observing legitimate peak
traffic; do not disable rate limiting globally to hide dispatch latency.
