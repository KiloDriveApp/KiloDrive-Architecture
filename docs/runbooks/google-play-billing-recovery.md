# Google Play Billing and RTDN recovery

- **Owner:** Membership and Store Billing Platform; restricted operator execution
- **Status:** Operational policy; current signed-provider exercise untested
- **Last verified:** 2026-10-05 source review
- **Last exercised:** Not exercised on the current signed consumer candidate
- **Environment:** Local modified product checkout; no live provider action
- **Evidence:** Product source commit [`8bfe08881bce51535d1165552f2d5be8e05fc872`](https://github.com/KiloDriveApp/KiloDrive/commit/8bfe08881bce51535d1165552f2d5be8e05fc872). Shared product checkout had uncommitted billing edits during review.
- **Related architecture:** [Google adapter lifecycle](../architecture/google-play-billing-native-adapter.md), [shared entitlement reconciliation](store-entitlement-reconciliation.md), [provider outage](provider-outage.md)

Use when a Play product/base plan/offer is not returned, checkout is pending or lost across process death, API entitlement lags a Play charge, a linked replacement conflicts, acknowledgement is late, or RTDN/voided-purchase/refund evidence disagrees with KiloDrive. This is a restricted diagnostic workflow, not permission to manually grant access or fabricate a payment.

## Detect and scope

1. Capture build/version and signed artifact, Play install track and licensed tester status, storefront country, product/base plan/offer, KiloDrive account/tenant/country/billing-account type, operation ID, support reference and UTC timestamps. Obtain identifiers from approved admin tooling; do not paste a raw token or customer details into a public report.
2. Read `/api/v1/store-billing/operations/{operationId}` and the current membership status. Compare prepared quote/mapping revision, operation state, purchase state, period, acknowledgement, payment/ledger/receipt and reconciliation issue. A `pending_reconciliation` prepared row is an owner fence, not proof of a charge or no charge.
3. Through the protected server adapter, query `purchases.subscriptionsv2.get` for the exact token when available; compare product/base plan/offer, linked token, external account/profile identifiers, subscription state, expiry, acknowledgement and exact order evidence. Do not use a Play UI screenshot, RTDN type or empty client Restore result as the final authority.

## Decision points and bounded recovery

| Finding | Safe recovery | Escalate when |
| --- | --- | --- |
| Product or term missing | Check exact API mapping and revision, returned product/base plan/offer, active Play Console product, country/price/metadata/agreement, licensed tester, Play-installed signed package and discovery time. Refresh bounded discovery. | One exact term remains absent or localized currency/price conflicts; disable that purchase action, do not synthesize price. |
| Pending provider purchase | Retain protected operation and owner fence. Re-query provider/status on bounded cadence; show checking. Do not acknowledge or grant until purchased evidence. | Pending exceeds policy window, account binding differs, or no provider lookup can identify it. |
| Charged/active at Play, no KiloDrive entitlement | Replay original verify/operation identity or let the durable RTDN-first prepared-owner path reconcile. Check exact owner, mapping, token family and country-cell commit. | Conflicting owner, missing exact prepared context or payment/order mismatch. Keep manual review and no second-buy control. |
| App killed or verify response lost | Restore the scoped protected journal; query operation and Play purchase evidence. Reuse original idempotency key/revision. | Journal is corrupt/unreadable or server and provider cannot establish one owner; preserve bytes for restricted investigation. |
| RTDN delayed/duplicate/out of order | Check OIDC authentication, unique message ID/payload hash, inbox receipt, lease/retry/manual-review status and lag alert. Re-query `subscriptionsv2.get`; duplicate receipt is not a second transition. | Inbox backlog grows, same ID has different payload, provider unavailable, or repeated manual-review rows. |
| Notification missing | Initiate bounded status/history reconciliation of known token or prepared profile; preserve current verified access until authoritative state changes. | Token lookup unavailable or ambiguity remains. Silence alone never expires access. |
| Acknowledgement pending | Verify purchase is purchased, server entitlement commit and durable acknowledgement outbox; retry existing outbox work under policy. Google requires acknowledgement of new purchases within three days; renewals do not need it. | Deadline warning/critical case, provider rejection or repeated transport failure. Never acknowledge an unverified foreign token. |
| Renewal, grace, hold or pause | Re-query current provider state and exact period. Grace retains access; account hold/paused do not mint new access. Reconcile financial order separately. | Exact order/amount/currency/period unavailable or provider state conflicts with cell projection. |
| Immediate upgrade/deferred downgrade | Verify linked predecessor hash and exact replacement mode. Retire predecessor only after verified transition; deferred target stays pending through current term. | Dual entitlement, unlinked target, two-line snapshot misread, or account mismatch. |
| Refund, revoke, void or chargeback | Reconcile provider disposition and protected order; run reviewed compensating access/accounting workflow once. | Pending refund review, uncertain final disposition, payment/ledger mismatch or unsupported product variant. |

For Google notification transport, the [controller](https://github.com/KiloDriveApp/KiloDrive/blob/8bfe08881bce51535d1165552f2d5be8e05fc872/src/server/KiloDrive.Api/Controllers/StoreBillingNotificationsController.cs) returns 200 after durable inbox acceptance, 401 for invalid sender and 503 for retryable verification/provider conditions. The [inbox worker](https://github.com/KiloDriveApp/KiloDrive/blob/8bfe08881bce51535d1165552f2d5be8e05fc872/src/server/KiloDrive.Api/Features/Membership/GoogleStoreNotificationRecovery.cs) leases bounded rows and classifies retry versus manual review. `subscriptionNotification` prompts current status lookup; `voidedPurchaseNotification` and `pendingRefundReviewNotification` use distinct reviewed paths. Never apply the RTDN numeric type directly to entitlement. See [Google RTDN reference](https://developer.android.com/google/play/billing/rtdn-reference) and [subscription lifecycle](https://developer.android.com/google/play/billing/lifecycle/subscriptions).

## Stop, rollback and retain evidence

Stop automated repair when ownership, token family, environment/package, mapping, exact charge, or country-cell scope is unresolved. Do not clear a financial journal, mark a prepared operation `not_committed` from timeout alone, force a new checkout, disable verification, reassign a token because email matches, or guess charge amount. A deployment rollback does not undo Play state: keep the old provider/operation records readable and reconcile before any schema or feature reversal. Escalate to the restricted membership exception queue with a single support reference and named owner.

Retain only sanitized chronology: signed artifact digest/build, Play track/storefront, product/base plan/offer, operation ID, hashed internal token reference in restricted evidence, provider state and timestamp, inbox message ID/hash/status, API entitlement revision, exact order/ledger references where access-controlled, acknowledgement status, support code and outcome. Never export raw purchase tokens, OAuth/OIDC tokens, service-account keys, private receipts, customer data or payment instruments. Record whether the observation came from source test, emulator, signed licensed device or live provider; mark absent cases **untested/blocked**, not passed.
