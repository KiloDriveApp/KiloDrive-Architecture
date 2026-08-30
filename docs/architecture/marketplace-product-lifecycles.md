# Marketplace product lifecycles

- **Owner:** Product architecture with Rider, Driver, Rental, Courier, Safety, and Finance service owners
- **Status:** Implemented baseline with country-configurable controls
- **Last reviewed:** 2026-08-30
- **Related chapters:** [Rider and driver safety](rider-driver-safety.md), [financial systems](financial-systems.md), and [realtime and events](realtime-and-events.md)

KiloDrive no longer treats a trip, parcel, rental, or support request as a form
that becomes a database row. Each is a versioned lifecycle. The distinction is
important: a screen can disappear, a phone can lose its network, and a provider
can time out, but the service must still be able to say exactly what state the
customer is in and which transition is safe next.

This chapter is a map of the newer product capabilities and the architectural
rules they share. It deliberately avoids route dumps and schema listings. Those
change faster than the ownership, consistency, privacy, and recovery decisions
an engineer needs to understand.

## Capability status at this baseline

“Implemented” below means the core server/schema behavior and focused tests are
present. It does not mean every country, provider, store client, or operations
team has activated every optional branch.

| Product area | Public status | Important boundary |
| --- | --- | --- |
| Scheduled reservation and guarantee | Implemented; timing is country-configurable | Saved is not guaranteed; driver reconfirmation before the cutoff is required |
| Multi-stop, round-trip, and hourly rides | Implemented with incremental client coverage | Stops/rates are snapshotted and versioned; country availability may differ |
| Marketplace intelligence | Implemented advisory projection | Probability, response time, fare range, and heatmap are estimates, never assignment or safety proof |
| Driver professional toolkit | Implemented/incremental | Queues and forecasts require fresh eligible state and remain non-authoritative |
| Family and business profiles | Implemented/incremental | Booking, billing, administration, notification, and tracking are separate permissions |
| Assisted-rider profile and matching | Backend foundation with partial Flutter; disabled/uncertified | Opt-in profile and matching checks exist, but offer/assigned-trip disclosure, caregiver delivery, Portal and field certification are incomplete |
| Immediate wallet fare splitting | Source candidate; unavailable/uncertified | Core wallet lifecycle exists, but bootstrap parity, mandatory versions/stable retries, consent/fallback behavior, owner operations and reversal certification are incomplete |
| Courier chain of custody | Implemented/incremental and policy-gated | Protection, prohibited contents, insurance and business shipping require country approval |
| Rental lifecycle | Implemented/incremental and provider-gated | Deposit, insurance, adjudication and payout paths require configured providers and operators |
| Two-sided reputation | Implemented/incremental operations | Imported history is reviewed and labelled separately; moderation/appeals need ownership |
| Structured support and disputes | Implemented/incremental operations | A case record does not prove a staffed SLA or country-specific remedy |

See [Capability status and evidence](capability-status.md) for the release-level
evidence language and the relevant runbooks for active operations.

## Rules shared by every lifecycle

1. **The country cell owns operational truth.** Trips, parcels, rentals,
   assignments, payments, evidence, cases, and lifecycle events stay with the
   country operation that provided the service.
2. **Mutations are conditional and idempotent.** A command supplies the expected
   version and an idempotency key. A retry must replay the result or fail
   coarsely; it must not create a second booking, bid, charge, voucher, or
   message.
3. **Realtime delivery is an optimization.** SignalR and push make changes
   visible quickly. The database transition and durable outbox explain what
   happened after a disconnect.
4. **Eligibility is rechecked at commitment.** A driver, vehicle, member,
   payment source, rental unit, or document can become ineligible after a quote.
   The locked acceptance/confirmation transaction checks again.
5. **Evidence is private by default.** Documents, package photographs,
   signatures, inspections, and dispute attachments remain quarantined until
   scanned and are delivered only through authorized, expiring access.
6. **A projection never becomes money or safety authority.** Forecasts,
   heatmaps, pickup probability, UI badges, and cached counters are explanatory.
   They do not assign a driver, settle a wallet, or declare a person safe.

## Immediate, scheduled, multi-stop, round-trip, and hourly rides

An immediate point-to-point ride is the simplest member of the family, not a
special implementation. The accepted route, ordered stops, fare, payment method,
driver, vehicle and compliance revision are snapshotted when the assignment is
made. Later profile or vehicle edits cannot rewrite historical evidence.

The trip summary also snapshots meters plus typed distance provenance from the
validated route and may advance to validated telemetry at completion. Old trips
without authoritative retained evidence remain unavailable. Presentation may
convert meters to kilometres or miles; it never derives distance from fare.

Multi-stop rides persist each stop with sequence, type, planned wait, status,
arrival, departure, and skip evidence. Round trips add an explicit turnaround
and return to the original pickup. Hourly rides snapshot the booked period and
package price. Completion is rejected while an actionable stop remains; an
operator does not fix that condition by editing the destination text.

Drivers can maintain an hourly-hire rate in the business toolkit and during the
driver onboarding preferences step. The reviewed default is USD 6.00 per hour;
the accepted configuration range is USD 1.00–1,000.00. A quote stores the exact
rate, source and booked duration used for the offer. The app may display a
country-currency conversion, but conversion does not rewrite the driver's USD
setting or the transaction's ISO-currency accounting evidence. A rider-facing
estimate before assignment remains an estimate until the accepted driver/rate
is snapshotted.

Scheduled rides distinguish a reservation request from a guarantee. The
lifecycle tells the rider whether KiloDrive is searching, has reserved a driver,
is waiting for reconfirmation, is replacing a driver, is guaranteed, or could
not guarantee the pickup. Before the country cutoff, the system revalidates the
reserved driver's account, duty, membership, documents, assigned vehicle,
conflicting work, online state, and telemetry freshness. A replacement keeps the
same rider request and evidence chain. It does not silently manufacture a new
ride.

When pickup confirmation is enabled by country policy or rider preference, trip
start requires the active short-lived challenge rather than a deterministic
trip-lifetime PIN. The server stores only a protected participant/trip/purpose
digest, limits attempts, rotates older challenges, and invalidates it after use,
expiry, cancellation, or terminal state. The same challenge may be presented as
a signed QR. A narrowly authorized emergency override records actor, reason, and
audit evidence; it is not a general bypass.

### Failure lesson

Do not label a future booking “confirmed” simply because it was saved. A durable
row proves that the request exists, not that an eligible driver has committed.
Truthful intermediate states reduce support incidents and prevent the product
from promising capacity it does not have.

## Marketplace intelligence without surveillance

The fare quote may include a reasonable range, estimated first-response window,
and bounded pickup-probability interval. These are cohort estimates based on
route characteristics, eligible supply, open demand, recent acceptance history,
service type, schedule, and—when enough samples exist—local time bands. Sparse
data is shrunk toward a conservative prior and displayed with wider uncertainty.
It must never claim certainty from a handful of trips.

Drivers see delayed, coarse demand cells. The server first reduces demand to one
contribution per rider and grid cell, suppresses cells below the privacy
threshold, and returns bands rather than exact rider counts or coordinates.
The heatmap can fail while the ordinary eligible-request list continues.

The rider always retains the ability to suggest a valid fare and negotiate. The
guidance is not an automatic price, an assignment, or a promise of response.

## Driver professional toolkit

Membership gives drivers business tools in addition to marketplace access:
destination mode, preferred service areas, recurring availability, managed
airport or venue queues, earnings goals, mileage and expense records,
profitability views, plan utilization, demand guidance, payout projections, and
downloadable statements.

These tools share the driver's country currency and IANA timezone. Queue entry
requires a fresh position inside the configured zone, an online eligible driver,
and no active assignment. A unique active membership prevents a driver from
occupying two queues. Heartbeats expire; an abandoned phone does not hold a
place forever. Forecasts are clearly labelled estimates and never mutate wallet
or cashout state.

## Family and business profiles

A family manager may book or pay for a member. A business may define members,
cost centres, ride policies, delegated bookers, notification preferences,
central billing, statements, and receipts. Authorization remains capability-
based: being allowed to book is not automatically permission to change billing,
view every trip, or follow a live location.

An invitation is single-use, expiring, and bound to the intended verified
contact. Acceptance creates an auditable membership. Final ride acceptance
rechecks active membership, booking policy, local-time rules, budget, payment,
and live-tracking permission. Removing a member ends future authority but does
not erase completed-trip or accounting evidence.

## Assisted riders

The assisted-rider backend foundation and partial Flutter surfaces exist, but
the feature remains disabled by default and uncertified. A rider can opt into
practical trip needs: mobility equipment
and bounded dimensions where necessary, service-animal accommodation, hearing
or vision communication preferences, extra boarding time, and an optional
protected caregiver contact/notification preference. A driver separately
attests the assistance they can provide.

Ride creation snapshots bounded operational detail and backend discovery,
bidding, and acceptance can check the active vehicle and driver capability. The
backend accepted trip preserves the profile revision. The system must never
infer disability or expose diagnostic information.

Important product gaps remain visible: the driver offer UI and assigned-trip DTO
do not yet present the operational snapshot, the stored caregiver-notification
preference has no delivery consumer, Flutter surfaces and existing-ride checks
do not consistently fail closed on policy/kill-switch state, and Portal has no
assisted-rider workspace.

Source behavior is not country activation. Positive two-device matching,
caregiver delivery, small-screen and assistive-technology testing, retention,
driver training/consent, privacy, accessibility, discrimination, and legal
approval remain required before the product is advertised as active.

## Courier product and chain of custody

A parcel records declared contents and value, pickup/recipient contacts,
delivery window, optional protection, and policy eligibility before dispatch.
Pickup and delivery use short-lived OTP or QR challenges. Package photographs,
recipient signature, and delivery proof are private evidence, not public image
URLs.

The chain of custody records who performed each authorized transition and when:
created, accepted, arrived at pickup, pickup confirmed, in transit, delivery
attempted, delivered, failed, and returning/returned to sender. A failed delivery
therefore remains an explicit operational state with reason and next action; it
is not disguised as cancellation. Business accounts can create bounded bulk
orders through the same command and idempotency rules as the app.

## Rental marketplace

Rental availability comes from calendars and maintenance blackouts, not from a
single `IsAvailable` flag. A quote snapshots rate, taxes/fees, mileage and fuel
rules, insurance/policy terms, cancellation terms, and deposit. Instant-book
still performs eligibility, overlap, payment-authorization, and vehicle checks;
approval mode adds an explicit owner decision.

The booking lifecycle is Quote → PaymentAuthorized → Confirmed → CheckedIn →
Active → CheckedOut → Settled/Disputed. Check-in/out evidence captures signed
agreement, odometer, fuel, timestamped inspection photographs, and participant
acknowledgement. Extensions are new conditional terms, not edits to old terms.
Late return, damage, maintenance, optional delivery/pickup, refunds, settlement,
and disputes retain their own evidence and accounting references.

## Two-sided reputation

One star average is too blunt for a transportation marketplace. Verified-trip
feedback records categories such as cleanliness, punctuality, communication,
and safe driving for drivers, plus structured, policy-reviewed rider feedback.
Publication is delayed or paired where appropriate to reduce retaliation.
Eligibility, completed-trip ownership, uniqueness, moderation, imports, and
appeals are enforced server-side.

Imported Uber, Lyft, or inDrive evidence is reviewed rather than silently mixed
with KiloDrive feedback. The UI identifies its source and count. Achievements
such as verified completed-trip bands, long-term reliability, and current
document verification are derived summaries with revision and expiry; they are
not permanent safety guarantees.

## Support, disputes, and safety escalation

A support case binds an owned trip, payment, document, delivery, rental, or
general concern. It receives a short human-readable reference while its UUIDv7
remains the internal identity. Structured issue type, urgency, private evidence,
secure participant messages, unread state, owner, SLA, and timeline move through
Received → Reviewing → Waiting for information → Resolved. Safety matters may
escalate to the separate SafetyCase lifecycle rather than being buried in a
normal support queue.

The API publishes a versioned support vocabulary for status, issue, priority,
subject, next action, reopen policy, and escalation policy. Flutter and Portal
localize those stable codes rather than displaying enum/wire names. Legacy
Open/Answered/Closed records map deterministically; the old Answered state uses
message chronology to distinguish “support is waiting for the user” from
“support must review a newer user reply.” Unknown future values render a neutral
unavailable state and disable unsafe mutations instead of exposing a number.

Notifications are outbox work. A provider outage cannot roll back a committed
case reply. Administrators access only an authorized country workspace and all
view, download, status, assignment, and reply actions are audited.

## Review checklist for the next feature

Before extending any lifecycle, require answers to these questions:

- What is the authoritative state machine, and which terminal states exist?
- Which country cell owns it, and what global identity reference is required?
- What is locked and revalidated at the irreversible transition?
- Which request key/reference makes an uncertain retry harmless?
- Which evidence must remain private, scanned, encrypted, and retained?
- Which realtime notification is backed by a durable outbox event?
- How does the client recover after a killed process or expired token?
- What does a user see when an optional provider or projection fails?
- Which accounting journal, reconciliation rule, or safety case is created?
- Which fixture, race, authorization, and crash-point tests prove the answer?
