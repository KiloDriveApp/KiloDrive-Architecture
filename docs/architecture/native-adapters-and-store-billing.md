# Native adapters and store billing

- **Owner:** Mobile platform and membership engineering
- **Last verified:** 2026-10-05 source review
- **Environment:** Local modified product checkout at the [captured source baseline](../current-baseline.md); historical test records keep their original builds
- **Evidence:** [Native adapter inventory](native-adapter-inventory.json), [historical build-168 handover](../runbooks/build168-operational-handover.md) and the source repository's dated verification records

**2026-10-06 amendment:** The current committed source is consumer
`1.0.0+196` and System Admin `0.1.0+33`. The
[build-196 checkpoint](release-1.0.0-196.md) documents exact unfinished-Apple
transaction review, expired finish-only disposition, cross-device membership
revision handling, typed observations and remaining signed-iPhone checks.
The build-192 source anchors and working-tree observations below retain their
original inspection date; they are historical observations, not current
uncommitted-release or complete-certification claims.

This page retains its build-156 and build-168 verification history. The
current source is newer, and the System Admin client is a separate app.
The [two-app source checkpoint](two-mobile-apps-and-security-2026-09-30.md)
describes the historical ownership split and additional device, notification and identity
adapters. Its source observations are not a signed release certification.

Native adapters isolate Flutter from device and store SDKs. They do not own account identity, trip state, money, or membership entitlement. Those decisions are API and country-cell responsibilities. An adapter reports a typed observation or performs a bounded device action; its caller verifies account, tenant, country, role, and operation generation before accepting a callback. A late callback from a previous account or disposed screen cannot replace current state.

The common operation shape is **prepare → check scope → invoke native API → classify result → retain sanitized evidence → reconcile with the API → show one safe next action**. Completed, explicitly cancelled, unavailable, failed, and outcome-unknown are different states. An unknown purchase cannot be retried as a new purchase simply because a network response was lost. It retains its original operation identity and is checked against server history. A confirmed cancellation of the StoreKit sheet, by contrast, must clear the local in-flight state without alleging that Apple charged the user.

## Adapter ownership

| Boundary | Native responsibility | Authority and recovery |
| --- | --- | --- |
| Store billing | Product discovery, purchase sheet/stream, restore, finish/acknowledgement observation | API verifies provider evidence and projects the membership; client operation journal survives interruption. |
| Location | Foreground fixes, background trip tracking, permission/service state | API owns trip/session; clients preserve fix time and accuracy and never invent a precise location. |
| Document capture | Camera, gallery, picker, cropper, local file preflight | Protected upload and server scan/review determine usable evidence. Transient security checks obscure rather than dispose the route. |
| Attestation and secure credentials | App Attest/Play Integrity result, app lock, scoped device storage | Server validates protected requests. Biometrics/PIN are local UI unlock, not proof for financial mutations. |
| Push, sound, and calls | Installation token, notification/sound presentation, OS calling and RTC media | Server notification/call record and recipient scope determine what may be shown or accepted. |
| Deep links and background work | OS intents, lifecycle signals, bounded read-only observations | RootGate/server state determines destination; background observation never replays a value mutation. |

The full file-level inventory and remaining physical-device certification are in the [source inventory](https://github.com/KiloDriveApp/KiloDrive/blob/main/docs/architecture/platform-adapter-migration-inventory.md). This public architecture page does not imply every native provider is active in every country.

## Apple: StoreKit 2 and subscriptions

This section is a **source review, not a signed-iPhone certificate**. It pins
product source revision [`8bfe08881bce51535d1165552f2d5be8e05fc872`](https://github.com/KiloDriveApp/KiloDrive/tree/8bfe08881bce51535d1165552f2d5be8e05fc872)
(consumer pubspec `1.0.0+192`, inspected 2026-10-05). The product checkout also
had uncommitted edits to the billing coordinator and native adapter at review
time; details explicitly called *working-tree observations* below require a new
revision and verification before becoming release evidence. The source of the
six driver IDs, group reference and weekly/monthly/quarterly mapping is
[`StoreMembershipCatalog.cs`](https://github.com/KiloDriveApp/KiloDrive/blob/8bfe08881bce51535d1165552f2d5be8e05fc872/src/server/KiloDrive.Api/Features/Membership/StoreMembershipCatalog.cs),
not a separately maintained list here.

```mermaid
flowchart LR
  Driver[Signed-in driver] --> UI[Consumer membership screen]
  UI --> Coordinator[StoreBillingService + protected journal]
  Coordinator --> Plugin[in_app_purchase / StoreKit 2]
  Coordinator --> API[/api/v1/store-billing]
  Plugin --> Apple[App Store storefront and transaction stream]
  Apple --> Notifications[Notifications V2]
  Notifications --> API
  API --> Server[Signed-JWS verifier + App Store Server API]
  Server --> Cell[Country-cell purchase, period, payment and exception]
  Cell --> UI
```

The [native adapter](https://github.com/KiloDriveApp/KiloDrive/blob/8bfe08881bce51535d1165552f2d5be8e05fc872/src/client/mobile/lib/core/platform_adapters/native_store_billing_adapter.dart)
uses `in_app_purchase` plus `in_app_purchase_storekit`: query products,
`buyNonConsumable`, `purchaseStream`, explicit `restorePurchases`, and a
StoreKit-2 unfinished-transaction probe. It carries `applicationUserName` on
purchase/Restore. A returned product has StoreKit's localized display price
and currency; the [API catalogue and quote](https://github.com/KiloDriveApp/KiloDrive/blob/8bfe08881bce51535d1165552f2d5be8e05fc872/src/server/KiloDrive.Api/Features/Membership/StoreBillingFeature.cs)
provide the licensed plan, term, mapping revision and operational-country
price evidence. Those prices are not interchangeable when the device storefront
differs from the operational country. The plugin DTO visible at this revision
does **not** independently expose Apple subscription-group/period metadata to
the Dart diagnostic record; mark those StoreKit fields *unknown* unless a
separate verified source supplies them. The server validates its configured
group during paid-transaction recovery.

```mermaid
sequenceDiagram
  participant D as Driver
  participant C as Consumer + protected journal
  participant S as KiloDrive API
  participant K as StoreKit 2
  participant A as App Store Server API
  D->>C: Select an available term
  C->>S: Quote exact mapping/term
  S-->>C: Quote evidence
  C->>C: Persist scoped quote + operation before launch
  C->>K: Launch with account binding
  K-->>C: Cancel, pending, purchase, error or late update
  alt Transaction identifier and signed evidence available
    C->>S: Verify or Restore with original operation/idempotency
    S->>S: Verify signature, app, bundle, environment, product, account
    S->>A: Status/history/refund lookup when recovery requires it
    S-->>C: Authoritative entitlement or review state
    C->>K: Finish only after verification/commit
  else Outcome uncertain or no transaction identifier
    C->>C: Retain journal; checking or manual review
    C->>S: Read exact operation status where available
  end
```

| Observation / transition | Local behavior and durable evidence | Authority for next step |
| --- | --- | --- |
| Product absent or delayed | Keep per-product diagnostic; do not manufacture a price or infer a charge | StoreKit discovery and current App Store Connect territory/group/metadata, then API mapping |
| Sheet requested | A persisted operation is not proof that a sheet appeared or Apple charged | Explicit plugin result or transaction; never infer from an absent server row |
| User explicitly cancelled | Clear only that no-charge checkout after definite native cancellation | Native cancellation classification; a generic error/timeout is not cancellation |
| Pending, interrupted, or duplicate unfinished | Preserve scoped journal, original quote and operation; no blind second purchase | Transaction stream/unfinished probe plus server reconciliation |
| Signed purchase or Restore | Verify exact transaction and account; retain charged-or-possibly-charged recovery if rejected or unavailable | API verification and provider status/history, not local `purchased`/`restored` alone |
| Renewal/cancellation/grace/expiry/replacement/refund/revoke | Apply event to the correct original-transaction family and period; preserve paid-through access unless revoked | Signed renewal/status/refund evidence and server membership projection |

The [server verifier](https://github.com/KiloDriveApp/KiloDrive/blob/8bfe08881bce51535d1165552f2d5be8e05fc872/src/server/KiloDrive.Api/Features/Membership/AppleStoreTransactionVerifier.cs)
checks signed transaction data against bundle/app ID, product, environment,
transaction ID and `appAccountToken`; [paid-transaction recovery](https://github.com/KiloDriveApp/KiloDrive/blob/8bfe08881bce51535d1165552f2d5be8e05fc872/src/server/KiloDrive.Api/Features/Membership/ApplePurchaseRecovery.cs)
also checks App Store Server transaction info, subscription-family status,
bounded history and refund history. An Apple account reused after a KiloDrive
identity reseed is not ownership proof: old evidence cannot transfer because
an email or Apple sandbox login happens to match. Server membership projection,
not StoreKit's `currentEntitlements` or a notification, authorizes KiloDrive
benefits. Apple's [current-entitlement definition](https://developer.apple.com/documentation/storekit/transaction/currententitlements)
does not include every expired or revoked historical transaction; the source's
Restore path probes unfinished transactions separately. An empty Restore or an
absent KiloDrive row cannot prove that Apple did not charge.

| Decision | Trusted source | Not sufficient alone |
| --- | --- | --- |
| Displayed checkout price/currency | Localized StoreKit product | API operational-country text, guessed FX |
| Eligible plan/term and mapping revision | KiloDrive API quote/catalogue | Returned StoreKit ID alone |
| User's account and tenant entitlement | Signed transaction + server binding and country-cell period | Apple login/email or a Dart stream event |
| Renewal intent | Signed renewal info or current App Store Server status | Bare transaction JWS |
| Money and period accounting | Exact provider order/price/currency/period evidence and idempotent server records | Entitlement change or notification alone |

There is an important **source limitation**: the signed-transaction verifier
initializes `WillAutoRenew=false` while `RenewalState="unknown"`, and the
purchase handler persists that Boolean. Therefore `false` at first JWS
verification cannot be presented as a verified iOS Settings cancellation.
The notification/status path must bind signed renewal information to the
exact original transaction family before applying it; missing or mismatched
family identity needs review. This is a source-audit finding, not a claim that
an exploit or wrong-account grant was observed. The [operator runbook](../runbooks/store-entitlement-reconciliation.md)
keeps cancellation, grace, billing retry, expiry, refund and revocation
separate.

**Working-tree observations (uncommitted on 2026-10-05):** the local
`store_billing.dart` writes a launch journal before native invocation, has
per-transaction Restore slots, checks an exact legacy Restore transaction,
and fences account changes. It still emits string events and keeps a shared
catalogue map; those are not a typed account/product/operation/transaction
event contract or proved audience-isolated discovery. The local native
adapter includes explicit StoreKit unfinished replay. Treat these as
implementation under review until committed and re-tested. The
[source test families below](#what-was-actually-tested-for-build-156) are
host-level evidence only; no current `+192` physical iPhone purchase matrix,
App Store Connect configuration capture or Notifications V2 delivery record
was established by this documentation review.

## Google Play Billing and subscriptions

The Android adapter discovers products/base plans for the signed-in Play storefront, presents the Play purchase flow, and observes purchase updates/restore. The API binds verified evidence to the KiloDrive account, uses `subscriptionsv2.get` as the provider status authority, projects the entitlement, and acknowledges a valid purchase exactly once. RTDN is a notification to reconcile provider status, not an entitlement command. Linked purchase tokens, replacement modes, duplicate/out-of-order events, pending purchases, pause, grace, hold, cancellation, refund, and revocation must converge without dual access or duplicate charges.

Both platforms preserve an operation journal and original idempotency/revision information across response loss and process death. Confirmed success moves to Current Plan; unresolved provider outcomes show checking/recovery with a support reference and no blind second-buy action. Server reconciliation and a restricted exception case handle disagreement. See the [operator runbook](../runbooks/store-entitlement-reconciliation.md).

The build-159 checkpoint's first-token recovery gap was subsequently addressed
through durable prepared-account context and a replay-safe notification inbox.
The recorded build-168 schema tests recreate the API context and exercise recovery
without client verification, including concurrent duplicate arrival. This is
not a physical purchase-then-process-kill certificate. Conflicting ownership
still fails closed. Exact provider order/charge/period evidence remains distinct
from renewed access; the server never guesses money from an entitlement update.
StoreKit and Play lifecycle certification still needs the exact signed artifact,
provider history and server ledger/outbox timeline.

## Installation attention and authentication races

Push registration carries versioned channel capabilities on the current verified
installation/token generation, plus an authoritative notification preference
revision and mutation identity. A late in-flight registration must not defeat
a newer opt-out. Explicit opt-in reads fresh state. Missing or stale quiet or
no-vibration channel proof uses data-only handoff instead of an audible default
channel. Provider acceptance, device receipt, display, sound and vibration are
five different observations. Existing OS channel choices are not overwritten.

Session refresh is single-flight and native/secure-storage callbacks are fenced
by account, tenant, country, role and generation. Temporary device validation
obscures and disables the mounted route while retaining pending picker/cropper
results; an authoritative ban/revocation still performs terminal cleanup. A
restored route is not authority to replay a financial command. Its scoped journal
retains original operation, payload and revision until server reconciliation.

The support situation uses a catalogued `KD-XXXXX` code; the occurrence uses a
separate correlation reference. Native diagnostic categories never invent a KD
code. Public recovery meaning comes from [the code catalog](https://kilodrive.com/help/codes),
not from raw SDK messages or provider payloads.

## What was actually tested for build 156

The recorded release evidence reports a passing Flutter analyzer, complete Codemagic-equivalent gate (4,739 Flutter tests), 71 focused membership widget tests, .NET solution build without warnings/errors, 87 focused billing-lifecycle tests, release governance, and Android APK/AAB packaging. The host tests cover adapter contracts, typed cancellation versus unknown outcomes, product-discovery states, purchase journal/recovery, active-plan term display, and account-scope fencing. These are **recorded source/host results**, not a fresh physical-device run by this documentation change. Reproduce the full mobile lane with `pwsh -File tools/verify-codemagic-prepush.ps1` in the source repository; run the focused Flutter tests under `src/client/mobile/test/` and the .NET tests from `tests/KiloDrive.Tests`.

| Source test family | What it exercises | Boundary it does not prove |
| --- | --- | --- |
| `native_store_billing_adapter_contract_test.dart` | StoreKit dismissal and cancellation classification, pending confirmation, typed adapter contract | Actual iOS purchase sheet or App Store Server response |
| `native_store_product_discovery_test.dart` | Missing product, group-query failure, bounded retry and sanitized per-product diagnostics | Product availability in a real storefront |
| `store_billing_operation_recovery_test.dart` | Journal replay, original operation identity, late-event fencing, account/tenant/country switch, serial verification and finish-after-commit | Real provider callbacks after OS process death |
| `store_billing_quote_test.dart` | Mapping and price/term presentation boundaries | Licensed store price configuration |
| `membership_plans_widget_test.dart` and `membership_purchase_state_widget_test.dart` | Rendered current-plan term, actionable/cancelled/checking states, safe purchase controls | Native billing UI or payment settlement |
| `AppleAppStoreServerApiTests`, `NativeStoreDiagnosticsTests`, `MembershipStoreStatusProjectionTests`, `StoreBillingContractTests` | Server request/response contracts, diagnostic redaction, entitlement projection and API gates | Current App Store Connect metadata or Notifications V2 delivery |

For an end-to-end certification, start with an isolated licensed/sandbox account and a signed build, capture the exact product IDs returned, perform purchase/cancel/restore/renewal/upgrade/downgrade/refund scenarios, then compare the provider history, server purchase/period/notification records, and the device Current Plan state. Repeat across process death and an interrupted response. Record build, storefront, provider environment, timestamps, sanitized references, expected and observed state; never put receipts or tokens in a public report. A scenario remains **untested**, not passed, when its provider or device boundary was only mocked.

The following still require candidate-specific evidence before a full certification
claim: physical iOS quarterly lifecycle and notification activation; genuine
refund/chargeback; first-purchase OS-kill and fresh post-fix renewal financial
proof; current signed App Attest/Play Integrity, push, RTC and sustained GPS
matrices. Retained build-167 licensed Play/RTDN observations do not become
build-168 results because the source or public documentation changed. Source
tests or a green policy flag cannot stand in for unperformed outcomes.
