# Consumer build 196 and System Admin build 33

- **Owner:** Product architecture and release engineering
- **Last verified:** 2026-10-06
- **Environment:** Committed source comparison and retained release records; this documentation update did not conduct a new device or provider test
- **Evidence:** Product revision [`027869db`](https://github.com/KiloDriveApp/KiloDrive/commit/027869dbcb4d8b1ff5c7d94931f8d1266cb4ad94), source pubspecs, schema contract, host verification and restricted deployment/submission receipts

This checkpoint describes consumer `1.0.0+196`, restricted System Admin
`0.1.0+33` and schema contract `2026.10.05.2`. It supersedes the earlier
build-192 *current source* observation while preserving the historical API
export and dated test evidence. [Current baseline](../current-baseline.md)
explains those separate scopes. A consolidated public changelog is an
editorial presentation of changes, not a claim that historical artifacts,
test results or store approvals were produced for build 196.

## Separate products and operational countries

The consumer app serves riders, drivers and rental participants. System Admin
tasks belong to the separate restricted app: people management, readiness
review, membership administration, investigations, security, notifications,
audit and recovery. One global identity may have both an administrator role
and an eligible consumer profile, but the two apps obtain separately scoped
sessions. The consumer client cannot select an administrator workspace or
gain cross-tenant access through a remembered setting.

KiloDrive supports operational workspaces for Jamaica, Cayman Islands,
Barbados, Trinidad and Tobago, Bermuda, the United States and Canada. Central
identity and country-cell membership resolve the account's operational
country. Its trips, wallet and local operational records remain in that
country cell. This differs from the Apple or Google storefront used to buy a
digital driver membership. An account in Jamaica may use a United States
Apple storefront; the native sheet supplies the applicable store price and
currency. A storefront is neither a country migration nor authorization to
another workspace. See [tenancy](tenancy-and-country-cells.md) and
[billing](native-adapters-and-store-billing.md).

## Installation, session and notification ownership

Fresh iOS installation preparation distinguishes deletion/reinstallation
from an ordinary upgrade or offload. It uses an app-data marker and durable
reset intent before account restore. A true fresh installation clears
KiloDrive-owned protected credential services and stale account/navigation
preferences. It does not indiscriminately delete the device Keychain or
Firebase/App Attest material owned by other SDKs. Existing pre-marker users
have an explicit upgrade path rather than an automatic sign-out that discards
an unresolved payment journal.

The fresh-install push reset is a separate, resumable operation. A pending
marker requires a one-time Firebase token rotation before the app reads or
binds its provider token. Concurrent startup, resume, Settings and Retry
paths share that boundary. Successful rotation clears the pending intent;
failure keeps it retryable. Push registration remains separate from app
startup. A token is a replaceable delivery address, not a person's identity
or a permanent physical-device identifier.

Device admission distinguishes App Check proof failure, network/server
unavailability and authoritative session or installation denial. A retryable
provider outage does not approve a protected mutation, and a known restriction
cannot be bypassed by reinstalling or pressing Retry. Scope/generation fences
discard old credential, notification, location and API callbacks after logout
or account/workspace change. See [session lifecycle](mobile-session-and-device-lifecycle.md)
and [notification lifecycle](notification-delivery-lifecycle.md).

Source anchors: [installation preparation](https://github.com/KiloDriveApp/KiloDrive/blob/027869dbcb4d8b1ff5c7d94931f8d1266cb4ad94/src/client/mobile/ios/Runner/AppDelegate.swift),
[fresh-install push rotation](https://github.com/KiloDriveApp/KiloDrive/blob/027869dbcb4d8b1ff5c7d94931f8d1266cb4ad94/src/client/mobile/lib/core/notifications/fresh_install_push_reset.dart)
and [push registration](https://github.com/KiloDriveApp/KiloDrive/blob/027869dbcb4d8b1ff5c7d94931f8d1266cb4ad94/src/client/mobile/lib/core/notifications/push_token_service.dart).

## Paid membership and StoreKit recovery

Paid native-store memberships are driver products. Silver and Gold each have
weekly, monthly and three-month terms. The Free driver plan is distinct from
a paid storefront subscription; rider wallet payments and trip fares are
distinct from digital membership purchases. Exact product mappings and term
revisions come from the server catalog; localized native-store prices govern
the purchase sheet.

The recovery path separates four facts: a sheet was launched, the store has a
transaction, the API verified its evidence and ownership, and the country cell
committed an entitlement/payment period. A `purchased` callback alone does not
grant benefits. A timeout is not a cancellation and must not start a second
purchase. Protected operation journals retain original keys, payloads and
scope until authoritative status resolves the result.

Build 196 adds a read-only review for an exact unfinished Apple transaction.
The verifier checks signed evidence, product, transaction and supported
environment. Only a verified expired period may receive a finish-only result.
That disposition performs no payment, membership grant, account reassignment
or database mutation. A still-active foreign-account transaction remains an
ownership conflict; deleting/reseeding a KiloDrive identity or changing an
email does not transfer the original purchase. Unknown or unverified evidence
is retained for reconciliation. Finishing an expired queue item is not a refund
or cancellation of a subscription.

Membership synchronization now loads the authoritative current snapshot
without waiting for optional product discovery/history. Same-account reads
respect membership revisions so an older initial response cannot replace a
newer entitlement. Account changes clear private snapshots; late status,
catalog and billing callbacks are discarded through lifecycle fences.
Cross-device refresh reconciles server state rather than inventing a tier from
the local store cache. See [store reconciliation](../runbooks/store-entitlement-reconciliation.md).

Source anchors: [unfinished transaction review](https://github.com/KiloDriveApp/KiloDrive/blob/027869dbcb4d8b1ff5c7d94931f8d1266cb4ad94/src/server/KiloDrive.Api/Features/Membership/AppleUnfinishedTransactionReview.cs)
and [membership state owner](https://github.com/KiloDriveApp/KiloDrive/blob/027869dbcb4d8b1ff5c7d94931f8d1266cb4ad94/src/client/mobile/lib/features/membership/data/membership_notifier.part.dart).

## Marketplace, participant profiles and trip continuity

Driver availability uses a dedicated state owner for permission, location,
server availability and interruption. Visible offer presence is bounded by
the actual on-screen lease. Attention is deduplicated across realtime and push
events, and closing/removing an offer updates that state instead of leaving a
stale selectable card. Marketplace lifecycle signals expose only the request
identity, version and state required to remove a closed offer; participant or
bid payloads are not broadcast to unrelated marketplace viewers.

Participant-profile dialogs use typed, relationship-scoped reads. Vehicle
photos and approved display fields have explicit projections; profile access
does not grant contact data or administrative dossier access. Trip rating is
composed through the trip feature with current scope and ownership. Ride
inquiry sends have a durable original operation and an outcome read before any
same-key replay; unknown/in-progress results never dispatch a blind repeat.

Trip rendering, refresh, action dialogs and mutations use the owning
account-scoped provider. Location evidence and lifecycle eligibility remain
server decisions; the client does not reapply an unrelated arrival check after
accepted evidence. Native location continues through route changes without
starting a second tracking owner. Stable map/form composition preserves scroll
and keyboard state; marker sizing, freshness/accuracy presentation and journey
copy communicate the actual stage. A safety mismatch remains a distinct action,
not proof that a driver or vehicle matches.

Destination navigation can open the authorized screen, scroll to the precise
section and briefly highlight it. The reusable target system preserves route,
account and workspace ownership, respects reduced motion, and does not submit
the destination form. Money/date/time settings use shared formatters; money is
still integer minor units in storage and input grouping does not change value.

Source anchors: [marketplace lifecycle projection](https://github.com/KiloDriveApp/KiloDrive/blob/027869dbcb4d8b1ff5c7d94931f8d1266cb4ad94/src/server/KiloDrive.Api/Services/Realtime/RideMarketplaceLifecycleSignal.cs),
[participant-profile boundary](https://github.com/KiloDriveApp/KiloDrive/blob/027869dbcb4d8b1ff5c7d94931f8d1266cb4ad94/src/server/KiloDrive.Api/Features/Trips/ParticipantProfiles.cs)
and [inquiry recovery](https://github.com/KiloDriveApp/KiloDrive/blob/027869dbcb4d8b1ff5c7d94931f8d1266cb4ad94/src/client/mobile/lib/features/rides/data/ride_inquiry_recovery.part.dart).

## System Admin work surfaces and readiness

The [System Admin chapter](system-admin-mobile-app.md) describes the independent
operator app in detail. People dossiers organize identity, security,
vehicles, financials, readiness, rides, activity and actions into accessible
tabs. Membership is a dedicated center with plan/member drill-down, catalog
creation, benefits/pricing editing and authorized individual grants/expiry
management. New paid catalog entries can remain inactive drafts while native
store mappings and country prices are configured; creating a plan is not the
same as publishing a purchasable native product.

Country-specific readiness distinguishes Hidden, Optional and Mandatory
requirements. PPV badge and road-license defaults are optional rather than a
universal requirement. Reviewers inspect protected documents, choose an
approved/rejected outcome and supply a rejection reason. Replaced documents
return through review; an upload alone is not approval. Driver and vehicle
requirements contribute to the computed readiness result, and an authorized
final decision has its own API checks and audit evidence.

Document decisions enqueue provisioned notification destinations through the
outbox and provider adapters. Email identifies the document type. Email, SMS,
WhatsApp and push availability depend on configured providers, verified
destinations and channel policy; enqueueing work does not establish delivery.

Independent second-reviewer approval, document-review second-factor verification,
sensitive-action verification and native viewing-lease policies are separate
API settings. Reviewed example defaults disable those additional requirements,
allowing one authorized reviewer;
capability, scope, validation, document access and audit still apply. Turning a
policy on later requires exercising that mode, not only exposing a settings
flag. The public repository describes the policy boundary without publishing
production secrets, internal access instructions or bypass recipes.

## Verification record

Dated execution observations are retained in the
[quality record](../quality/historical-release-evidence.md#build-196).
