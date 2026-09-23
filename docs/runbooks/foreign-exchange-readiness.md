# Foreign-exchange readiness and incident response

- **Owner:** Payments Platform and Financial Controls
- **Status:** Reviewed public procedure
- **Last exercised:** 2026-09-23 (source and automated-test review)
- **Related architecture:** [Authoritative foreign exchange](../architecture/authoritative-foreign-exchange.md)

## Trigger

Use this runbook when an FX-dependent checkout is disabled, rate freshness is
degraded, provider settlement and wallet currency disagree, a fee/rate mismatch
opens a reconciliation case, or operators need to activate/suspend a pair.

## Diagnose before changing anything

1. Identify country, source/destination pair, operation type and safe support
   reference. Do not collect user identity or provider tokens in working notes.
2. Read pair state, current/scheduled version, effective window, freshness,
   direction, evidence status, fee policy and product/provider mapping.
3. Determine whether the failure happened before provider I/O, after a possible
   remote success, or after local posting.
4. Inspect the operation's immutable quote/snapshot. Do not compare a historical
   transaction only with the current active rate.
5. Check readiness, reconciliation and outbox age separately. A notification
   failure is not an FX failure.

## Containment

- Suspend only the affected pair or product path when evidence is unsafe.
- Preserve status/reconciliation endpoints for already-started operations.
- Do not delete pending payments or encourage a new checkout while a provider
  outcome is unknown.
- Do not edit an active rate, fee version, quote, ledger entry or transaction
  snapshot.

## Recovery

1. Create a new draft with reviewed evidence, hash, source classification,
   effective/freshness times, exact direction and reason.
2. Verify representative conversions and fee totals at small, typical and
   boundary amounts.
3. Obtain independent approval. Schedule or activate using the expected
   revision and original administrative idempotency key.
4. Reconcile open operations against their own snapshots.
5. Correct money only through a reviewed compensating posting linked to the
   original evidence graph.

## Verification

- Pair readiness reports the expected active version and freshness.
- A new quote displays source amount, fee, provider total, destination amount,
  direction, expiry and safe evidence reference.
- Expired or missing evidence creates no payment.
- A completed sandbox/test operation posts exactly once and its receipt,
  ledger, payment and snapshot agree.
- Refund/dispute uses the original snapshot.
- Metrics and alerts recover without suppressing a remaining exception.

## Abort and rollback

Abort if maker-checker separation, evidence hash, effective window, currency
metadata, provider mapping or representative conversion is wrong. Rollback is
a newly reviewed version using the prior value; never reactivate a superseded
row or rewrite history.

## Evidence safety

Retain version IDs, country/pair, timestamps, safe references, test amounts and
sanitized results. Keep credentials, provider payloads, purchase tokens,
destinations, customer data and private evidence out of this public record.
