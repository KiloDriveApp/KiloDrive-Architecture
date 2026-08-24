# Marketplace product lifecycles

- **Owner:** Product architecture with Rider, Driver, Rental, Courier, Safety, and Finance service owners
- **Status:** Implemented baseline with country-configurable controls
- **Last reviewed:** 2026-08-24
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

Multi-stop rides persist each stop with sequence, type, planned wait, status,
arrival, departure, and skip evidence. Round trips add an explicit turnaround
and return to the original pickup. Hourly rides snapshot the booked period and
package price. Completion is rejected while an actionable stop remains; an
operator does not fix that condition by editing the destination text.

Scheduled rides distinguish a reservation request from a guarantee. The
lifecycle tells the rider whether KiloDrive is searching, has reserved a driver,
is waiting for reconfirmation, is replacing a driver, is guaranteed, or could
not guarantee the pickup. Before the country cutoff, the system revalidates the
reserved driver's account, duty, membership, documents, assigned vehicle,
conflicting work, online state, and telemetry freshness. A replacement keeps the
same rider request and evidence chain. It does not silently manufacture a new
ride.

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

