# Native adapters and store billing

- **Owner:** Mobile platform and membership engineering
- **Last reviewed:** 2026-10-03
- **Environment:** [Current reviewed source baseline](../current-baseline.md); historical test records keep their original builds
- **Evidence:** [Historical build-168 handover](../runbooks/build168-operational-handover.md) and the source repository's dated adapter inventory and verification records

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

The iOS adapter requests the exact Silver/Gold weekly, monthly, and quarterly product IDs for the device storefront. It presents Apple's purchase sheet and listens for transaction updates and restore. StoreKit returning a product or a local transaction is **evidence, not entitlement**. The API verifies signed Apple transaction/server history, bundle ID, product ID, environment, account binding, term, and price evidence before updating the membership period. App Store Notifications V2 prompts recovery; it is not accepted blindly as the final state.

Product discovery records sanitized per-product evidence: requested/returned ID, storefront, timestamp/duration, localized currency/price, subscription period/group when available, mapping revision/status, build, and a bounded failure category. The client does not infer sandbox versus production when the SDK cannot prove it. It never logs receipts, JWS payloads, private keys, raw purchase tokens, or personal data. A quarterly product missing from StoreKit must be diagnosed across storefront availability, subscription group, metadata, agreement, mapping, and timing—not treated as proof of a currency-conversion fault.

A verified cancellation normally stops renewal but preserves access through the paid period. Immediate upgrade, deferred downgrade, renewal, billing retry/grace, expiry, refund, revocation, and restore are server lifecycle events. The Current Plan view uses the authoritative active period's exact term, such as `Gold-Weekly`; a later payment or pending quarterly change cannot relabel it.

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
