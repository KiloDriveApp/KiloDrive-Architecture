# Rides, trips, delivery and rental workflows

[API Guide](README.md)

## Resource lifecycles are distinct

A ride request describes a rider's demand and proposed journey. A bid describes
a driver's offer. A trip records the accepted assignment and its execution.
A payment records the financial result. A notification or chat message is not
the lifecycle authority for any of them.

| Workflow | Useful reads | Consequential actions |
| --- | --- | --- |
| Rider request | Request detail, bids, search state and inquiries | Create, edit fare, accept/reject bid, extend search, cancel |
| Driver work | Available requests, route preview, readiness and status | Bid, withdraw bid, update online state |
| Accepted trip | Trip detail, assignment-related state, timeline, receipt | Arrival, pickup/start, stop progression, completion, cancellation, tip |
| Participant communication | Authorized chat history, unread state and call state | Send message, mark read, call consent/progression |
| Delivery | Quote, request, bids, sender tracking, custody/evidence | Accept, pickup, progress stops, attempt/return, complete or cancel |
| Rental | Search, availability, quote, booking, agreements and evidence | Book, checkout, sign, extend, cancel, inspect or dispute |

Use the [ride](reference/rides.md), [driver](reference/drivers.md),
[trip](reference/trips.md), [delivery](reference/deliveries.md),
[rental](reference/rentals.md) and [call](reference/communications.md) references
for exact operations and DTO fields.

## Request, bid and acceptance

A rider submits the documented ride model, including locations, category,
passenger count and proposed fare in minor units. Scheduling, stops, assistance
and product options have their own fields; do not assume a server will derive a
missing mandatory field from display text.

Available-work queries are scoped to the driver and current eligibility. Bids
are state mutations and retain one idempotency key. Acceptance rechecks current
state, driver/vehicle eligibility and payment rules inside the authoritative
transaction. A stale bid card must not create a second assignment.

Searching again, changing a fare and extending an existing search are different
intents. Read no-driver/recovery guidance returned by the actual request rather
than silently creating another ride. Concurrent acceptance and cancellation
must have one coherent terminal result.

## Trip execution

The trip detail and timeline describe persisted state. Arrival, pickup proof,
start, stop completion, route changes and completion use their corresponding
contracts. A route/map update is not proof that a lifecycle action succeeded.
Pickup challenges and participant verification are private ceremony data.

Cancellation, rider cancellation, driver termination and emergency stopping
have distinct meanings. Select the workflow the user intended, validate its
state and show any returned financial consequences. Do not translate every
problem into a generic cancel or complete request.

Completion records the payment and applicable commission/settlement outcome.
Receipts and their PDF/email forms are authoritative records. A cash payment
still creates financial evidence; choosing cash does not make the trip disappear
from the ledger. Tip requests are separate value-moving intent and must not be
repeated after a timeout without reconciliation.

## Chat and calls

Trip chat is participant-scoped. Sending a message preserves its client identity
and mutation key through reconnect. History ordering and read receipts use the
declared fields. A realtime echo should be merged with the pending message, not
shown as a second message.

Call eligibility depends on authenticated session and the applicable trip/work
relationship. Incoming-call polling must stop when the session is absent or the
workflow does not need it. Provider call consent, connection and completion
are separate states; neither a local dialer opening nor an API 200 proves that
the other person answered.

## Deliveries and escrow

Sender tracking is owner-scoped; driver delivery lists belong to the current
driver's profile. Driver availability does not grant access to another sender's
tracking, documents or recipient details.

Wallet delivery acceptance reserves the fare in held balance. Completion
releases the hold and settles the driver's net amount; permitted cancellation
refunds the reserved funds. Held money is not spendable or available for cashout.
Historical deliveries may use the established legacy completion path, so do not
infer escrow solely from a new client version.

Custody, stops, recipient/pickup confirmation, failed attempts and return
completion maintain evidence for the real delivery lifecycle. Product-protection
claims have separate authorization and configuration. A feature flag does not
establish that an insurance/provider dependency is operational.

## Rentals and organization membership

Rental search/availability, quoting, booking payment, agreements, inspection,
extension, damage and deposits are separate records/actions. Read current
availability and quote state before booking. Use returned checkout and payment
state; a provider screen closing is not payment authorization.

Rental-partner actions require the caller's authorized organization relationship.
Inventory edits, team invitations, billing, booking status and evidence cannot
be treated as globally accessible because the route includes an organization
ID. Organization-level disputes with administrative authority are excluded from
the curated export even when their route is outside `/admin`.

## Family, business and supervised travel

Travel profiles, dependent consent, corporate budgets and household membership
have relationship-specific permissions. Tracking and supervised conversation
access follow those relationships. A family or business account is not a way
to read every trip of an associated identity without consent and policy.

## Failure handling across products

After a response interruption, retain the original operation context and use
the applicable outcome/status read. Reconnect should refresh authoritative
resource state before resuming controls. Keep pending state visible across
cold restart. Unknown numeric status values must disable unsafe actions rather
than be interpreted as completed, paid or approved.

Related: [marketplace lifecycles](../architecture/marketplace-product-lifecycles.md),
[rental marketplace](../architecture/rental-marketplace.md),
[rider/driver safety](../architecture/rider-driver-safety.md) and
[recovery rules](errors-and-recovery.md).
