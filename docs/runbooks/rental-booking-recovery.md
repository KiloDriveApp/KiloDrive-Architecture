# Rental Booking, Handover, and Settlement Recovery Runbook

- **Owner:** Rental operations with Payments, Finance, Support, and Safety
- **Status:** Maintained runbook for implemented/incremental, provider-gated flows
- **Last exercised:** Record in restricted release/incident evidence
- **Related architecture:** [Rental marketplace](../architecture/rental-marketplace.md), [Financial systems](../architecture/financial-systems.md), and [Provider outage](provider-outage.md)

Use this runbook when availability conflicts, authorization and booking state
disagree, check-in/out evidence is missing, an extension overlaps another
reservation, a return is late, or deposit/settlement/dispute totals do not agree.

## State and inventory model

The authoritative lifecycle is:

`Quote → PaymentAuthorized → Confirmed → CheckedIn → Active → CheckedOut →`
`Settled` or `Disputed`.

Cancellation, declined approval, failed authorization, no-show, late return,
extension, damage and maintenance are explicit branches. The calendar is an
interval allocation with maintenance blackouts; `IsAvailable=true` is never
sufficient proof.

## Invariants

- A quote snapshots vehicle, rate, taxes/fees, deposit, mileage/fuel, insurance,
  cancellation, delivery/pickup and expiry policy.
- One vehicle cannot have overlapping confirmed/active allocations.
- Instant book still rechecks renter, vehicle, compliance, interval, payment and
  country policy in the locked confirmation transition.
- Provider authorization is not confirmation; confirmation owns the inventory
  claim.
- Check-in/out evidence is private, scan-gated, timestamped and linked to the
  participant acknowledgement and booking version.
- An extension is a new conditional quote against future availability, not a
  direct edit to the return date.
- Deposit authorization/hold, capture, release, refund, claim and chargeback use
  stable provider/payment/journal references.
- One booking version moves forward; operators do not overwrite historical
  quote or handover snapshots.

## First response

1. Record country, organization, booking support reference, vehicle ID, current
   version/state, interval, payment/provider references and safe correlations.
2. Protect the physical vehicle and people. If two renters appear entitled to
   the same vehicle, stop handover for both until authority is established and
   offer the approved support path.
3. Pause only the affected booking/vehicle settlement or allocation path when
   state is ambiguous. Do not disable the full rental marketplace by default.
4. Open a support/dispute or SafetyCase when damage, injury, theft, coercion, or
   identity concerns require accountable evidence handling.

## Diagnose by symptom

### Two bookings claim one interval

- Compare persisted intervals, statuses, versions, unique allocation evidence,
  extension attempts and maintenance blackouts.
- Identify whether the conflict is durable or only a stale availability cache.
- Preserve both customer records. Do not delete the later row to make the query
  look correct.

### Provider authorized but booking is not confirmed

- Treat timeout as unknown outcome. Query/consume provider authority using the
  existing idempotency/reference.
- Check whether local transition lost its race to another allocation or failed
  a final compliance/policy check.
- Release/void the authorization through the supported compensating path if the
  booking cannot legally confirm. Do not send a second authorization blindly.

### Booking confirmed but a client still shows quote/pending

- Read durable version and outbox delivery.
- Reconcile the API read, SignalR/push and client revision merge.
- Do not call confirmation again; an idempotent retry should replay one result.

### Check-in/out evidence blocked

- Verify the object belongs to booking, participant and evidence class.
- Inspect scan disposition, KMS/IAM and signed-access audit. Pending/rejected
  evidence remains quarantined.
- If required evidence is missing, stop the transition or use the approved
  documented exception workflow. Never set `clean` or fabricate acknowledgement.

### Late return or extension conflict

- Compare actual/expected return, country grace/fee policy, next confirmed
  allocation and maintenance window.
- Reprice extension from an immutable new quote and conditionally allocate only
  the available future interval.
- Notify the next renter truthfully through durable work. Notification success
  does not reserve another vehicle.

### Deposit, charge, payout, or settlement mismatch

- Reconcile provider authorization/capture/refund/dispute, booking charge
  components, organization entitlement, customer liability, deposit clearing,
  wallet/subledger and journal.
- Separate damage claim evidence/adjudication from automatic capture. Country
  policy and provider terms decide what may be charged.
- Fail affected payout/cashout closed until the mismatch is explained; never
  alter an immutable journal or raw provider response.

## Recovery

Use a supported expected-version command, idempotent outbox replay, provider
reconciliation, scan retry, conditional reallocation, or balanced compensating
journal. A repair has a reviewed reference, owner and pre/post reconciliation.

Do not:

- directly edit dates/status to defeat overlap checks;
- reuse a mutable current tariff as the historical agreement;
- mark handover complete because an image exists;
- capture a deposit merely because a damage case opened;
- retry an unknown provider mutation with a new key; or
- settle while the booking is still Active, evidence-required, or Disputed.

## Verification matrix

Use deterministic non-user organization/renter fixtures and fake providers:

- quote expiry and repricing;
- approval and instant-book success/denial;
- two concurrent confirmations for one vehicle/interval—exactly one wins;
- authorization timeout before/after provider acceptance;
- maintenance/compliance expiry racing confirmation and check-in;
- check-in/out photos, signature, odometer and fuel/battery round trips;
- scanner timeout/rejection and authorized document access;
- no-show, cancellation at every legal state, late return and extension race;
- partial/full refund, deposit release/capture, damage dispute and chargeback;
- optional delivery/pickup assignment; and
- outbox/client disconnect after each committed transition.

Cleanup executes in `finally`, preserving only sanitized correlations and
provider-fake IDs. Do not leave a fixture vehicle allocated or a financial hold
active.

## Closeout

One booking version and one inventory interval are authoritative; physical
handover/return is accounted for; private evidence has the correct disposition;
payment, deposit, journal and provider totals reconcile; affected clients and
operators see the same state; alarms/queues are normal; and the regression
fixture passes without direct data edits.
