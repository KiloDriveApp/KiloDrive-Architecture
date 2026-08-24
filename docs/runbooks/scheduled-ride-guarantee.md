# Scheduled-Ride Guarantee and Replacement Runbook

- **Owner:** Ride operations with Dispatch, Realtime, Safety, and Support
- **Status:** Maintained runbook for an implemented, country-configured lifecycle
- **Last exercised:** Record in restricted release/incident evidence
- **Related architecture:** [Marketplace lifecycles](../architecture/marketplace-product-lifecycles.md), [Realtime and events](../architecture/realtime-and-events.md), and [Ride dispatch](dispatching.md)

Use this runbook when a scheduled ride is stuck in search, a driver cannot
reconfirm, a cancelled/ineligible reservation does not enter replacement search,
or the rider is shown a guarantee that durable state does not support.

## Promise boundary

A saved scheduled request is not a guaranteed pickup. The customer-visible state
must distinguish:

1. **Searching** — no reserved driver is authoritative.
2. **Driver reserved** — one driver accepted, but pre-pickup reconfirmation is
   still required.
3. **Confirmation required** — the configured reconfirmation window is open.
4. **Guaranteed** — the same eligible driver reconfirmed before the guarantee
   cutoff.
5. **Replacement searching** — the reserved driver cancelled or failed the
   pre-pickup recheck and the same ride is seeking a replacement.
6. **Not guaranteed** — the country cutoff passed without a qualifying
   confirmation. Search may continue only under the disclosed policy.
7. **Cancelled/expired/assigned terminal progression** — the ordinary ride/trip
   lifecycle is authoritative.

The exact confirmation lead and guarantee cutoff are country settings. Do not
copy a time from another cell or infer it from a push-notification timestamp.

## Invariants

- One scheduled request keeps one identity and monotonic lifecycle version
  through search, reservation and replacement.
- At most one actionable driver assignment exists.
- Guarantee requires current account, duty, membership, licence, vehicle,
  documents, trust, conflict, online and telemetry eligibility inside the
  locked confirmation transition.
- A delayed job checks the expected ride/trip version before changing state.
- Cancellation or replacement never manufactures a second customer charge,
  hold, bid history, support record, or ride.
- Outbox delivery communicates committed state; a push cannot create a
  guarantee.

## First response

1. Record the public support reference, country, scheduled pickup, app builds,
   safe correlation IDs, ride/trip IDs and current lifecycle version.
2. Compare the country timing configuration with current UTC and the rider's
   displayed local time.
3. Read the authoritative ride, assignment and trip state before inspecting
   notification delivery.
4. If the UI says Guaranteed but the durable state does not, contain the claim:
   correct the projection/client state and notify Support. Do not fabricate a
   confirmation row.
5. If pickup is near and no safe guarantee exists, follow the approved customer
   communication/escalation policy; do not silently leave the rider waiting.

## Diagnose by boundary

### Reservation never becomes confirmation-required

- Confirm the delayed cutoff/reconfirmation outbox message exists with the
  expected entity version and due time.
- Check worker heartbeat, lag, handler registration, attempt state and broker /
  SQL fallback without replaying the business acceptance.
- Check whether a newer cancellation, replacement or assignment legitimately
  made the delayed message stale.

### Driver cannot reconfirm

- Confirm actor ownership and that the reserved driver/trip match.
- Inspect the coarse eligibility decision and freshness timestamps; never copy
  licence numbers, coordinates or documents into the incident record.
- Check the expected version and deadline. A stale client should refresh, not
  overwrite a newer decision.
- If a document or vehicle became ineligible, replacement is correct. An
  administrator must not override a safety/compliance failure merely to preserve
  the guarantee label.

### Replacement search is stale

- Confirm the cancellation/ineligibility transition committed and produced the
  dedicated durable event.
- Verify the former assignment is no longer actionable and the request is
  visible under scheduled bidding rules.
- Follow outbox → EventBridge/SQS where configured → SignalR/push → bounded
  client reconciliation. Realtime failure does not justify creating another
  ride.

### UI and database disagree

- Compare persisted entity version with the latest client-accepted version.
- Check server clock, country timezone conversion and explicit-offset parsing;
  do not treat an offset-less timestamp as local time.
- Force the supported read/rejoin path. Never lower version checks or edit
  wall-clock ticks to make an event appear newer.

## Recovery

Use only a supported conditional command, delayed-message replay, or projection
rebuild with the original entity/event identity. The safe choice depends on
authoritative state:

- replay a failed pending handler only after proving it is idempotent and still
  version-current;
- let a stale delayed job complete as a no-op;
- restart replacement search on the same ride through its canonical transition;
- expire a missed guarantee truthfully; or
- cancel under the approved participant/operator policy with ordinary financial
  hold release and notifications.

Do not directly edit guarantee status, driver ID, deadlines or outbox completion
flags. Do not extend a cutoff after it passed to make metrics look successful.

## Verification

Run a deterministic two-client fixture for:

- create → reserve → window opens → reconfirm before cutoff → Guaranteed;
- reconfirm after cutoff → Not guaranteed with truthful copy;
- driver cancellation before and during the window → replacement on same ride;
- compliance, stale telemetry and conflicting-assignment races;
- duplicate reconfirmation/idempotency replay;
- worker crash before claim, after state commit, and before notification;
- killed/background clients and missed SignalR event followed by reconciliation;
- rider cancellation racing confirmation; and
- local-time display across a DST and non-DST country.

Close only when one authoritative assignment exists, the visible guarantee state
matches it on both clients, financial holds/references reconcile, outbox lag is
normal, the customer communication is accurate, and the next scheduled fixture
passes without manual intervention.

## Evidence and escalation

Retain build/schema/config versions, country timing rule version, safe IDs,
entity/event versions, UTC transition timeline, worker/provider identifiers,
recovery action and two-client result. Never retain addresses, precise routes,
contact details, tokens, or message payloads in general incident evidence.

Escalate immediately if two drivers appear guaranteed, a rider is charged twice,
a safety-ineligible driver remains guaranteed, or a public guarantee is shown
without durable confirmation.
