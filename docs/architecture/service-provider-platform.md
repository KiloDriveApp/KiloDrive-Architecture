# Service Provider accounts, workspaces and memberships

This chapter describes the reviewed product-source design as of 20 October
2026. It is a guide to responsibility and recovery, not a statement that every
country, purchase channel, service, or physical-device journey is active or
certified. The [current baseline](../current-baseline.md) records the exact
source revision and evidence boundary.

## One person, several kinds of work

KiloDrive has a global human identity and country-specific operational records.
At registration, a person chooses **Customer**, **Transportation Service
Provider**, or calculator-only access. A provider may register as an individual
or on behalf of an organization and select a first service. The registration
intent carries that choice through verification, social signup, restart, and
onboarding. It must not be reconstructed from a stale device preference.

The provider can use more than one service under the same personal identity:
ride hailing, courier/delivery, and vehicle rental. My Services presents the
available workspaces and a preferred startup choice. Customer use remains a
separate, authorized workspace. The API verifies the current country membership
and service grant when entering each workspace; merely displaying a navigation
item, owning a business, or having a global role does not grant access.

Each service has its **own readiness**. A courier-only applicant is not asked to
complete taxi eligibility. A rental business does not become a driver because
it lists a car. Driver identity, licence, vehicle compliance, country rules and
final approval remain independent of courier custody and rental publication.
The dashboard should show missing, submitted, rejected with reason, expired,
and approved evidence, with one useful next action. It must not display a paid
membership as legal or safety approval.

| Question | Authoritative answer |
| --- | --- |
| Who can sign in? | Central identity, current session and device admission. |
| Which country may this person use? | Current country membership and country-cell authorization. |
| Which service may they open? | Service enrollment and the effective personal or organization grant. |
| May they accept new work? | Current service readiness, country policy, capacity and membership allowance, rechecked when work is accepted. |
| What did an interrupted action do? | Its original operation receipt and a fresh authorized read, not the last screen state. |

## One Service Provider catalog

The provider catalog has **Free, Silver and Gold**. Free is an indefinite,
limited entitlement with configured reset periods, not an unreviewed trial
that silently begins billing. Paid Silver and Gold have weekly, monthly and
quarterly terms. The six native-store identifiers follow the exact
`kilodrive.provider.{silver|gold}.{weekly|monthly|quarterly}` pattern.
Apple and Google determine the actual storefront charge; a local comparison
amount is not a billing authority. The account country and store country can
differ. Native-store availability, country pricing and approval must be
verified independently before a purchase is called available.

Published benefit revisions define service-specific allowances, for example
new ride bids, courier offers, rental listings, vehicle changes, staff seats,
trip capacity, points multipliers and withdrawal thresholds. The benefit's
unit and reset period matter as much as the number. Current usage comes from
the service's server-side ledger. A plan downgrade or catalog edit must not
rewrite usage or historical purchased terms. A new plan or price is prepared
as a draft until the corresponding store and country setup is valid.

The consumer comparison view may switch weekly, monthly and quarterly terms
and display each tier's effective benefits, price and current state. The
separate [System Admin app](system-admin-mobile-app.md) manages the published
catalog, revisions, member review and permitted grants. Neither app can grant
an entitlement by changing a color, showing a receipt, or trusting a client
callback. The API applies only verified store periods to the named beneficiary.
An organization membership and an individual's membership are different
beneficiaries even when one person can see both.

The native store owns renewal, cancellation and upgrade charging. KiloDrive
records the verified effective period and reconciles late renewals, refunds,
replacements and duplicate provider events. An old successful checkout must
not revive a superseded tier. When checkout is interrupted, the client keeps
the original operation, account, beneficiary, product, key and revision; it
reads that operation and the current membership before suggesting any further
action. A second checkout is not a recovery method.

## Ride, courier and rental service boundaries

**Ride hailing** joins an eligible driver, assigned vehicle and customer
request. Bids and trip actions are versioned state transitions. Current
location, vehicle compliance and work allowance are rechecked when necessary;
the map marker or a locally enabled button is not proof of arrival or trip
start. The trip record, not a push message, is the durable result.

**Courier and delivery** moves goods or performs a defined service. The
requester is not an onboard passenger. A courier has a distinct enrollment,
availability, bidding/claiming and custody lifecycle. The customer can enter
a pickup, destination, goods/instructions, optional contact where policy
allows, a budget and timing through a progressive wizard. The bearer records
pickup, custody, visits, delivery or return evidence. Cash errands need a
bounded spending authority, receipt comparison and a path for a purchase that
cannot be completed. A tracking number is a human reference, never sufficient
authorization to reveal location or personal details. Active custody stays
recoverable even if permission for **new** jobs is suspended.

**Rental** separates a physical vehicle from its listing, branch, policies,
calendar and price. Provider identity and branch hours are structured data;
an unavailable calendar date does not imply a booked customer. A reservation
is a temporary unpaid inventory hold, while booking, contract acceptance,
payment, handover, actual return, inspection and dispute are separate states.
The same physical vehicle cannot be committed to conflicting taxi, rental or
maintenance work. Each listing can use an approved reusable customer
requirement profile. A customer can browse without being a taxi driver, while
rental licence and identity evidence are reviewed for the particular rental
qualification. Gallery, map, availability and condition evidence help people
decide; they do not replace the server's final availability and eligibility
check. [Rental marketplace](rental-marketplace.md) explains the deeper
allocation and money invariants.

Across all three services, wallet balance and rewards points are distinct.
Only a server-confirmed conversion moves value into a wallet. Holds are not
spendable; refunds and chargebacks use linked accounting evidence instead of
editing history. [Financial systems](financial-systems.md) and
[native store billing](native-adapters-and-store-billing.md) cover those
boundaries.

## Organizations and staff

A provider organization adds team access to personal accounts; it does not
create a shared password or a second identity. Driver/courier/rental provider
grants, rental-company grants and business-shipping grants have separate
service-specific engines. A unified Team & Access presentation cannot flatten
them into an all-powerful role. A verified recipient accepts an invitation
under their own account, subject to current inviter authority, country scope,
seat limits and service scope. A forwarded link alone is not acceptance proof.

Owner, administrator and staff are bounded by their effective permissions.
Managers cannot grant powers they do not hold; branch or service scope cannot
be widened by a client-side form. Team suspension removes new organizational
authority without erasing the person's customer account or the actor trail.
Open rides, courier custody, rental handovers and financial holds require safe
resolution before an access or ownership change that would strand them.
Organization ownership transfer is separate from native-store subscription
purchaser identity. Recovery of an unavailable owner requires a narrowly
audited case and current independent evidence rather than an Admin silently
taking the business over.

## Security, devices and communications

The consumer app holds consumer-scoped sessions even if the person also holds
an administrative role. The separate Admin app carries administrative
capabilities and an explicit country/tenant workspace. The API enforces
authorization, ownership, service readiness and country filters on every
relevant operation. Device admission binds an installation and verified app
identity to a session; model names and IP addresses are metadata, not a
hardware identity. Reinstall, account switch, logout and token rotation must
not revive another person's session or push binding.

Native SDKs are adapters. StoreKit/Play, camera, location, secure storage and
push callbacks become typed observations; server verification and persisted
state establish the business result. Notifications use durable outbox work.
Enqueue, provider acceptance, device delivery and a person's reading are
different states. A failed email or push may be retried without repeating the
original review, payment or custody mutation. Sensitive documents remain
private, scanned and purpose-authorized; upload success is not reviewer
approval. See [sessions and installations](mobile-session-and-device-lifecycle.md),
[notification delivery](notification-delivery-lifecycle.md), and the
[security control model](../security/security-control-model.md).

## Evidence required before calling a feature ready

An implemented handler, schema table, navigation item, passing host test,
signed package, deployed API, active country policy and successful real-device
provider journey prove different things. The [current baseline](../current-baseline.md)
lists the inspected source and retained evidence. A new service or purchase
path needs its own negative authorization, race/recovery, native-device,
provider-mode and country-policy checks. Avoid copying a historical passing
count to a newer build or treating a schema fingerprint as commercial
activation.

For public users, the [Transportation Provider manual](https://kilodrive.com/manuals/KiloDrive-Transportation-Provider-Operations-Manual.pdf),
[Rental Entity manual](https://kilodrive.com/manuals/KiloDrive-Vehicle-Rental-Entity-Operations-Manual.pdf),
[KiloDrive website](https://kilodrive.com/),
[release page](https://kilodrive.com/changelog),
[privacy policy](https://kilodrive.com/privacy) and
[terms](https://kilodrive.com/terms) are the appropriate product resources.
