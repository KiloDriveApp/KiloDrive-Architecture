# Consumer 1.0.0+238 and System Admin 0.1.0+49: provider platform update

Reviewed 20 October 2026 against the committed product authorities recorded in
[source-derived facts](source-versions.generated.md). This is a public-safe
source architecture summary. Exact signed artifacts, store upload/review,
country activation, production settings and physical-device certification are
independent states; they are not inferred from a version number or this page.
Earlier build chapters retain their original dates and evidence.

## Account and service experience

The consumer app separates customer use from Transportation Service Provider
registration. The first-run choice persists through registration and recovery.
A customer can return to a preferred Hail a Ride, Rentals or Shipping screen
after sign-in; the compact navigation reaches the other services.
A provider can select individual or organization context, see My Services,
choose a startup workspace and pursue ride hailing, courier/delivery or rental
readiness independently. A courier-first or rental-first account should not
be routed through the driver's taxi checklist. Switching workspace does not
change identity or skip current country and service checks.

The app's provider membership experience uses one Free/Silver/Gold catalog.
Free is a limited ongoing plan with defined reset rules. Silver and Gold have
weekly, monthly and quarterly native-store products. The benefit comparison
changes with term and displays the applicable plan, usage and reset basis;
prices shown at purchase come from the active store offer. The current-plan
view, restore, cancellation request and financial history serve different
purposes. A paid plan grants specified capacity, not document approval or
vehicle eligibility. [Provider architecture](service-provider-platform.md)
explains beneficiary, revision, store and recovery rules.

Ride hailing retains versioned bids and trip actions. Courier/delivery is a
goods-and-custody service with progressive request and bearer flows, optional
contact details where policy allows, cash-errand evidence, and separate return
and dispute states. Rental providers manage structured branches and opening
hours, fleet listings, gallery and availability. Customers can reserve an
inventory window separately from booking; renter qualification and each
vehicle's reusable requirements are checked by the API. Customer and provider
views may simplify the journey, but do not take authority from the owning
server transition.

Courier drafts can resume the same request. Reusable templates retain the
service shape while leaving private contacts and payment authority to each
new job. Rental discovery keeps vehicle, provider, daily price and seats
together; search, sort and filters remain compact until opened. The branch
map, gallery, availability, policy and renter-requirement views answer
different customer questions before a booking decision.

The existing account and financial surfaces distinguish available wallet
money, holds, rewards points and verified plan access. Referral and trip
points require server-qualified events; showing an estimated award does not
mint it. Session, device, contact, export and account-deletion controls remain
under My Data and the applicable security or privacy authority.

## Provider organization and operator work

Team & Access makes organization collaboration visible without a shared
credential. Invitations are recipient-bound; owner, administrator and staff
authority is service-scoped and bounded by the current grant. Seat and new-bid
limits come from published benefits. Deactivating or replacing an owner must
not strand open work, paid obligations or an unresolved native-store
subscription. The person keeps their own global identity and customer account.

The restricted System Admin app remains the only mobile System Admin work
surface. Its country-scoped dashboards, People dossiers, membership catalog,
readiness/document review, vehicle/rental/courier operations, finance, devices,
notifications, support, audit and recovery tools are separate from consumer
navigation. Provider-team investigations, Exchange reviews and metric
definitions extend the operator source surfaces. Each action has its own API
capability, tenant/country scope, version and audit requirements. A screen or
operation inventory alone does not certify end-to-end administrative parity.

The Rental Risk Exchange candidate separates private incident evidence from
reviewed, limited publication and subject rights. Exchange access is a
separate potential wallet-funded organization service, not an Apple/Google
provider subscription. Its country policy, agreement, approved offer and
channel gates remain explicit prerequisites; no blanket activation is claimed.
The intelligence programme adds consented, bounded observations and
replayable metrics. Forecast and event guidance remains advisory or shadow
work until data quality, privacy and measurable benefit are established.
See [risk and intelligence boundaries](rental-risk-and-marketplace-intelligence.md).

## Platform invariants carried forward

- The API owns authentication, country scope, readiness, membership, money,
  booking and review decisions. Central identity and country operational cells
  retain their separate ownership.
- State-changing retries keep the original idempotency key, payload and
  revision after an unknown outcome. Readback or an original-operation receipt
  determines what happened; a new mutation is not a refresh operation.
- Native store, camera, location, secure storage and push providers are
  adapters. A callback or displayed success is not a ledger entry,
  entitlement, approved document or completed delivery.
- Private uploads require purpose authorization and independent scan/review
  states. Notification dispatch is durable, but provider acceptance, device
  delivery and reading are distinct.
- The consumer session never inherits System Admin authority. Organization
  membership never grants access to another person's wallet, sessions or
  security settings.
- Money uses currency-labelled integer minor units. Holds and rewards points
  are not available wallet funds. Committed financial history is corrected
  with linked entries, not overwritten.

## What this update does and does not prove

The [current baseline](../current-baseline.md) names the inspected source
revision and current version/schema authorities. This page does not refresh
the older curated public [API export](../api/README.md), claim that its
operation count covers new private endpoints, or transform historical tests
into build-238 evidence. Every country, native product, purchase, enrollment,
team change, rental handover, Exchange decision and intelligence projection
needs its own release and operational observations. The
[capability status guide](capability-status.md) explains the difference
between source implementation, configuration, activation and certification.

For the current product description, consult the
[website](https://kilodrive.com/),
[Transportation Provider and customer manuals](https://kilodrive.com/manuals),
[public release page](https://kilodrive.com/changelog),
[privacy policy](https://kilodrive.com/privacy),
[terms](https://kilodrive.com/terms), and the
[consumer Google Play listing](https://play.google.com/store/apps/details?id=com.kilodrive.app).
The restricted Admin app is not the public consumer listing.
