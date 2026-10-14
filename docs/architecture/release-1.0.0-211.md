# Consumer build 211 and System Admin build 44

- **Owner:** Product architecture and release engineering
- **Source review:** 13 October 2026
- **Evidence type:** Committed implementation and source-derived contract facts
- **Product revision:** [`93491dac`](https://github.com/KiloDriveApp/KiloDrive/commit/93491dac97f4c458cf61873adb5c566430298e39)

The consumer app is `1.0.0+211`, the separate restricted System Admin app is
`0.1.0+44`, and the source schema contract is `2026.10.13.1`. These are source
identities, not proof of store availability, a particular country's enabled
features, a completed live transaction or a signed iOS device run. The
[current baseline](../current-baseline.md) explains which evidence establishes
each of those claims. Earlier build chapters retain their original observations.

## A clearer consumer workspace

Rider Home now puts Hail a Ride, Rental, Trip history, Wallet, Loyalty Rewards,
Contacts, My Data and Courier within direct reach. The four bottom destinations
are Home, Hail a Ride, Rentals and Courier. The Shipping & Delivery area groups
new requests, business shipping, drafts and templates. A requester does not
become a passenger in a courier job; the bearer transports goods and records
custody, handoff and any required proof. Driver and Courier each retain their
own work, readiness and vehicle rules even when one central identity has both
profiles.

The ride request form gives the proposed fare and estimated points a compact
entry point. Its breakdown lives in a dialog; the primary action reads Request
Bids by default and Request ride when exact-fare automatic acceptance is
selected. Rotation preserves the entered route rather than discarding the
request draft. Driver arrival, rider vehicle confirmation and Begin Ride remain
server-authorized lifecycle actions. UI movement or an old GPS sample alone
cannot establish a start or settlement result.

My Data brings together profile and picture, authentication contacts, active
sessions, passkeys, linked social accounts, readiness, favorite people and
places, export, deactivation and account deletion. Contact cards use
first-party share links and QR discovery, with rotation, expiry and revocation.
A saved favorite is an address-book relationship, not an authorization to
dispatch a provider, reveal private details or transfer funds. Editing contact
details preserves navigation context; the server still validates ownership,
conflicts and current authentication policy.

## Courier enrollment and readiness

An existing eligible account can enter courier enrollment from My Data's
Verification & readiness area. The progressive steps identify user details,
the current courier agreement, documents and vehicle/capacity information.
Accepting the agreement does not approve the bearer. Courier Home distinguishes
readiness, bidding hall, vehicle capacity, new delivery and existing jobs;
unavailable work remains gated. Motorcycle and motor-vehicle declarations,
capacity, country document policy and private review evidence remain separate
from taxi-driving eligibility. Administrators make a reasoned decision through
the courier review workflow, with replacement evidence after rejection.

The delivery lifecycle retains versioned request and offer decisions, custody
events, a tracking number, recipient proof, shopping-budget consent, cash/wallet
policy and settlement reconciliation. A phone losing its response does not
authorize a new delivery or a second hold. The [marketplace lifecycle
chapter](marketplace-product-lifecycles.md) owns the broader state model.

## Finance, membership and loyalty

Driver Finance collects membership, earnings and financial recovery. Billing &
Financial exposes Rewards & Referrals and Transaction resolution. The rewards
area distinguishes pending and available points, issued invites and referral
history. A referral award depends on qualifying completed activity and current
country policy, rather than mere signup or link sharing. Points are not cash;
wallet credit exists only after a server-confirmed conversion and ledger entry.
When conversion policy or a quote is unavailable, the client must not present
an enabled money-minting action. Rental activity and courier custody also form
deactivation blockers until their obligations are resolved. The confirmation
explains retained records, support-assisted reactivation and possible ongoing
store subscription renewals.

Membership grants, pricing, benefits and readiness review remain System Admin
tasks. The consumer app neither exposes an administrator workspace nor gains
privileged access because the same email has a rider or driver profile. The
[System Admin chapter](system-admin-mobile-app.md) and
[financial systems](financial-systems.md) explain the separate authorization and
ledger boundaries.

## Security and recovery posture

The control database owns one global identity, sessions, credentials, social
links and device admission. Country cells own operational trips, delivery,
wallet, notification and domain-audit records. Native adapters report local
StoreKit/Play, keychain, push, location and camera observations; the API
decides entitlement, money, readiness and privileged approval. A notification
attempt is not evidence that its recipient opened a message. Sensitive
mutations retain a stable operation identity and revision. Unknown results are
read back and reconciled before a second action; a blind retry with a new key
can duplicate value or state transitions.

The source KD catalogue contains 3,991 situation identities (1,855 semantic
bases and 2,136 exact-detail situations) with complete title/detail/action key
coverage in English, Spanish, French, Japanese, Simplified Chinese and
Traditional Chinese. The generated inventory reports zero stock base meanings
and zero incomplete explanation fields. The exact occurrence's outcome and
correlation reference still govern safe recovery. Key parity and source-backed
drafts do not constitute qualified linguistic approval. The curated public
OpenAPI export retains its older independent provenance; these catalogue
counts must not be mistaken for newly published API operation counts.

## Operator and publication boundary

Admin build 44 is a separate client for People dossiers, document inspection,
readiness decisions, membership management, financial investigation, devices,
notifications, outboxes and audit. Its routes are permission-checked on the
server and tenant-scoped. An apparent button or passing widget test does not
certify every signed-device or provider outcome. The current public
[user manuals](https://kilodrive.com/manuals) and
[release history](https://kilodrive.com/changelog) describe customer-facing
workflows; deployment and publication should be verified by artifact hash and
public readback. The [error-code guide](https://kilodrive.com/help/codes)
provides static explanations, never a lookup of a person's private transaction.

[Current baseline](../current-baseline.md) ·
[Official product links](../public-product-links.md) ·
[Historical build 198](release-1.0.0-198.md)
