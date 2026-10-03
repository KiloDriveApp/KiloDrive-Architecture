# Native-store entitlement reconciliation

- **Owner:** Membership and Store Billing Platform
- **Status:** Reviewed public procedure
- **Last exercised:** 2026-10-03 (bounded source/current-schema review; retained build-167 licensed Play observations remain build 167, not a new iOS exercise)
- **Related architecture:** [Financial systems](../architecture/financial-systems.md) and [Native adapters and store billing](../architecture/native-adapters-and-store-billing.md)

## Trigger

Use this runbook when a purchase remains pending, a renewal/cancellation/refund
is not reflected, provider notifications are stale, acknowledgement approaches
its deadline, product discovery omits a reviewed term, or account entitlement
and Apple/Google history disagree.

## Establish authority

1. Identify platform, environment, application account, product, operation and
   safe support reference without copying raw purchase tokens.
2. Read the current membership period, access-through date, pending change,
   lifecycle reason, local store-purchase evidence and revision.
3. Query authoritative provider history through the protected server adapter:
   Apple signed status/transaction/refund history or Google
   `subscriptionsv2.get`.
4. Treat App Store Notifications V2 and RTDN as invalidation signals. Confirm
   state from provider history before changing entitlement.
5. Verify product mapping, term, country/storefront availability and price
   evidence separately from lifecycle state.

## Recovery rules

- Reuse provider transaction identity and KiloDrive idempotency on duplicate or
  out-of-order events.
- A missing notification starts bounded history recovery; it does not prove
  cancellation or expiry.
- A deferred downgrade keeps current access until its effective date.
- A verified cancellation disables future renewal but normally preserves
  current paid access.
- Refund, revoke, chargeback and restoration follow explicit state-machine
  events and immutable audit.
- A stale or mismatched account binding opens restricted review and never grants
  access to the wrong KiloDrive account.
- A native sheet dismissal is cancellation unless authoritative evidence makes
  the result uncertain. Do not tell a user the store may have charged them
  merely because they cancelled.
- Expired membership is not an assigned Free plan. Current must show the actual
  active tier/term, or no active membership, without expired paid benefits.
- Renewed access and accounting proof are separate. Create a renewal charge only
  from the exact verified order, price/currency and service period; missing
  charge evidence cannot be replaced with a guessed payment or zero fee.

## Verification

Confirm the provider status, product/term, current period, access-through date,
pending change, payment, membership lifecycle event, receipt, notification and
reconciliation case agree. Verify the app shows Current Plan after confirmed
success and a recoverable Checking state—without a second purchase button—when
the outcome is unresolved.

## Product-discovery failure

If StoreKit or Play Billing does not return a product, verify exact product ID,
subscription group/base plan, storefront/territory, price, metadata, agreement,
licensed tester and signed distribution channel. Do not synthesize a storefront
price or blame a missing product on currency conversion.

## Abort and escalation

Stop automated repair for conflicting provider accounts, invalid signatures,
environment mismatch, dual entitlement, unknown product/term, missing price
evidence or financial mismatch. Preserve evidence and route to the restricted
membership exception queue.

## Current handover and unperformed cases

Use the [build-168 handover](build168-operational-handover.md) for the current
source and deployment checkpoint. Automated first-token context recovery and
pending-refund workflow tests cover controlled provider boundaries, not a
physical first-purchase kill or genuine provider refund. Historical Play
purchase/cancellation and RTDN observations remain attributed to their tested
build. A fresh post-fix renewal charge, iOS physical quarterly lifecycle and
Apple production notification activation still require their own observations.
