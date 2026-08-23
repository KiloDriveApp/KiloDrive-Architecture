# Engineering Lessons from Building KiloDrive

Architecture diagrams show the system after decisions have settled. They rarely
show the confusing symptoms that forced those decisions. This chapter records
the lessons that are most likely to save another engineer time.

The examples are intentionally public-safe. They preserve the engineering cause
and prevention control without reproducing customer data, credentials, private
infrastructure, or active defensive thresholds.

## 1. A healthy database marker does not identify the running API

### What we saw

An environment could have the expected schema version while the deployed API
binary was older, or the API could expect a newer fingerprint than one or more
country cells contained. “The database is up to date” and “the API is current”
were sometimes treated as the same statement.

### Why the assumption failed

Application deployment and schema application are independent operations. A
version row says what script last recorded, not which DLL IIS loaded. A hash in
configuration can also be stale even when the underlying tables are correct.

### The durable practice

Identify and record separately:

- deployed build/commit and artifact hash;
- configured schema contract version/fingerprint;
- normalized control and every country-cell metadata fingerprint; and
- public readiness result after restart.

Startup reports normalized differences—not only a hash—and fails before serving
incompatible work. Deployment evidence proves the binary independently.

## 2. Configuration files are data, not formatting exercises

### What we saw

A general-purpose serializer rewrote a production JSON file and escaped single
quotes inside CSP strings. The JSON remained technically valid, but the result
was hard to review and could change how operators understood or copied policy.

### Why the assumption failed

Serializers preserve data according to their own escaping and ordering rules,
not the exact human-reviewed representation of a security policy. Rewriting an
entire file to change one setting creates a large, noisy diff and can disturb
comments or deployment conventions.

### The durable practice

Read configuration without printing secrets, apply a narrow reviewed edit,
parse it again, and run the same production validator the application uses.
Never log the resulting configuration object. Keep secrets out of public source
and prefer protected files, environment/config providers, or managed secret
stores appropriate to the hosting model.

## 3. “Connected to Valkey” does not mean “authorized for SignalR”

### What we saw

The API authenticated to Valkey and basic reachability passed, yet the SignalR
backplane reported a publish/subscribe permission error.

### Why the assumption failed

Network reachability, authentication, and command/channel authorization are
three separate gates. An ACL can permit `PING` and ordinary keys while denying
the channel namespace used by the backplane.

### The durable practice

Health checks exercise the capability the application needs with a dedicated
least-privilege account: connect, authenticate, publish, subscribe, and clean up
a synthetic channel. ACL changes are tested against the precise namespace, not
by granting broad access.

## 4. An event producer without a handler creates permanent work

### What we saw

A valid business transaction inserted an outbox event whose type had no
registered handler. The worker retried, then marked the message permanently
failed. Backlog alarms were correct; there was simply no code that could
complete the promise.

### Why the assumption failed

The producer and consumer were reviewed as separate changes. Compilation
cannot prove a string event type has a handler.

### The durable practice

A contract test enumerates produced event types and registered handlers. New
producers, handler registration, retry policy, observability, and recovery
documentation ship as one unit. Unknown types fail visibly; they are never
silently marked complete.

## 5. Cloud-bus failure must not erase SQL recovery

### What we saw

Dispatch publishing received an IAM authorization failure. SQL recovery still
protected durability, but outbox lag rose because the faster broker path was
unavailable.

### Why the assumption failed

It is easy to treat a cloud SDK call as ordinary application code. In reality,
identity policy, resource policy, region, bus name, and network path all
participate. A fallback can preserve correctness while hiding a capacity or
latency regression.

### The durable practice

The outbox remains authoritative. Broker publish has least-privilege policy,
bounded telemetry, and a controlled failure test. Alarms distinguish “SQL
recovery active” from “full dispatch path healthy.” Operators repair IAM or
broker state rather than disabling the warning indefinitely.

## 6. Post-commit failure can lie to the caller

### What we saw

A handler could commit a ride, bid, or financial transition and then await an
audit, realtime, or webhook action. If that later action failed—or the HTTP
request was cancelled—the client received an error even though durable state
had changed.

### Why the assumption failed

The code visually appeared to be one operation, but the transaction boundary
ended before the external work. Returning failure invited the client to repeat
an already completed command.

### The durable practice

Commit durable side-effect intent in the same transaction. Workers use their
own scopes and cancellation lifetime. The API returns the committed result;
delivery failure appears in outbox/provider health and is retried idempotently.

## 7. Realtime speed cannot replace reconciliation

### What we saw

One phone accepted or cancelled an offer while another phone remained on stale
state for several seconds—or indefinitely when SignalR failed. Push might
arrive, but the open screen did not merge the change.

### Why the assumption failed

Realtime delivery is ephemeral. Apps are backgrounded, connections move between
networks, subscriptions are restored after reconnect, and events can race with
HTTP refreshes.

### The durable practice

Each entity has a persisted monotonic version. Realtime events carry that
version; repositories merge only newer state. Resume/reconnect/push and a
bounded fallback refresh reconcile from the API. Two-client tests intentionally
disconnect between commit and publish.

## 8. A feed response is not a viewer count

### What we saw

Periodic driver-feed responses were counted as “drivers viewing.” One driver
could be counted for many offers never opened.

### Why the assumption failed

Eligibility to receive a list is different from human attention to one item.
Polling also makes counts lag by the refresh interval.

### The durable practice

The client sends a short-lived visibility heartbeat only for the ride currently
visible. The count expires when the screen closes or connectivity is lost. The
UI labels the metric according to what it actually measures.

## 9. GPS proximity is not road traversal

### What we saw

A fixed corridor around a route or toll plaza could report a toll when the
vehicle used a parallel frontage road. Stale last-known location could also
produce a brief but incorrect route/fare.

### Why the assumption failed

Consumer GPS has noise, age, and varying accuracy. Haversine distance ignores
road topology. A polyline sampled sparsely can miss or overinclude nearby
features.

### The durable practice

Location carries age and accuracy. Implausible movement is rejected. Candidate
features use a spatial bounding/index prefilter, then road-network map matching
and traversal order. Ambiguous evidence is surfaced rather than converted into
false certainty. Fresh location upgrades the UI asynchronously; last-known data
has an explicit freshness limit.

## 10. Fare changes require renewed consent

### What we saw

Changing a rider's fare could rewrite pending “accept rider fare” bids. If the
rider lowered the fare, a driver's earlier consent appeared to accept the lower
amount.

### Why the assumption failed

The implementation treated the bid as a derived mirror of current fare rather
than a driver's time-stamped offer/acceptance.

### The durable practice

Offer amounts are immutable facts. A material fare change expires or requires
reconfirmation of affected bids and publishes a new versioned event. Acceptance
uses the exact agreed amount inside the locked transaction.

## 11. Eligibility is checked at acceptance, not only discovery

### What we saw

A driver could bid while eligible, then go offline, acquire another assignment,
lose document compliance, change vehicle, or exceed duty limits before a rider
accepted.

### Why the assumption failed

The bid was treated as proof that eligibility remained true.

### The durable practice

Discovery filters reduce noise. Acceptance revalidates the entire gate under
lock and snapshots the accepted vehicle/compliance version onto the trip. A
stale bid cannot override current safety rules.

## 12. Money references must be canonical across every path

### What we saw

Initial purchase, renewal, store purchase, refund, and reconciliation could use
different journal-reference patterns for the same concept. Completed cashouts
could disappear from an “expected” calculation while their clearing journals
remained, creating a permanent mismatch.

### Why the assumption failed

Each workflow locally chose a plausible reference and status filter. No shared
contract described the complete lifecycle.

### The durable practice

Posting rules and reference builders are shared, pure, and tested. Reconciliation
covers every terminal/intermediate state deliberately. Property and crash-point
tests prove balanced entries, unique references, held-fund reconciliation, and
provider totals.

## 13. The purchased membership term is part of financial truth

### What we saw

Renewal logic could use a plan's default fee and period instead of the actual
week/month/quarter term the customer purchased. Proration had the same risk.

### Why the assumption failed

The plan catalogue was treated as the subscription history. Catalogues change;
a purchased entitlement needs its own immutable pricing/service-period
snapshot.

### The durable practice

Persist plan foreign key, term, charged price source, service period, renewal
and grace state, provider product/base-plan/offer identity, and payment/journal
references. Renewal locks membership and wallet and posts one atomic economic
operation.

## 14. Provider acknowledgement belongs to a durable workflow

### What we saw

An app-store entitlement could commit before provider acknowledgement. If
acknowledgement then failed, the API looked failed while access had already been
granted; the store might later refund the unacknowledged purchase.

### Why the assumption failed

Acknowledgement was treated as a final synchronous line rather than a retryable
provider obligation with its own state.

### The durable practice

Entitlement and payment record the verified transaction, then a durable outbox
performs acknowledgement with stable provider identity. The subscription
exposes `acknowledgement_pending`; monitoring and replay resolve it.

## 15. OTP failures must not become password denial of service

### What we saw

Invalid OTP attempts could increment the global password lockout counter. An
attacker who knew an email or phone number could lock normal login.

### Why the assumption failed

All failed authentication was treated as one counter, even though password and
per-challenge OTP threats differ.

### The durable practice

Each OTP challenge has a short lifetime, attempt budget, purpose, user/contact
scope, invalidation rule, and keyed HMAC. Password lockout remains independent.
Rate limiting combines trusted IP, challenge, contact, and user signals without
revealing whether an account exists.

## 16. Do not create an active identity before contact proof

### What we saw

Passwordless registration could create an active placeholder user before OTP
confirmation. Abandoned attempts reserved contact values and left incomplete
control/cell projections.

### Why the assumption failed

Login and registration shared a convenient early “find or create user” path.

### The durable practice

Store an expiring provisional registration first. After ownership proof, a
durable registration saga creates global identity and idempotent country
projection. Reconciliation repairs cross-database partial failure.

## 17. Social email is not an automatic linking ceremony

### What we saw

A new social identity could be linked to an existing account merely because an
email string matched. Provider claim differences made that unsafe.

### Why the assumption failed

Email is an identifier, not always fresh proof that the person controls the
existing KiloDrive account.

### The durable practice

Require verified provider claims, issuer/audience/nonce validation, and an
explicit signed-in linking ceremony or confirmation challenge to the existing
account. Send provider tokens through protected headers/body, not query strings.

## 18. Multi-node ceremonies cannot live only in process memory

### What we saw

Passkey ceremonies stored in one process failed after IIS recycle or when
completion reached another API node.

### Why the assumption failed

Local memory was convenient during single-node development but not part of the
distributed session boundary.

### The durable practice

Use a single-use, expiring distributed store bound to user, purpose, relying
party, and challenge. Consume atomically. Require recent step-up proof for
registration/deletion and test cross-node begin/complete.

## 19. Ephemeral Data Protection breaks browser continuity

### What we saw

ASP.NET warned that Data Protection keys were in memory. Cookies or protected
payloads became unreadable after process exit.

### Why the assumption failed

Development defaults started successfully and looked harmless. Production
restart/scale-out requires shared persistent protected keys.

### The durable practice

Persist keys in an access-controlled location available to intended nodes and
protect them at rest. Alert on ephemeral-key warnings. Test restart and
cross-node cookie/protected-payload continuity.

## 20. Quarantine is a state, not a generic client error

### What we saw

An administrator opening a document could receive an opaque conflict response
because the file was still quarantined or awaiting a trusted scan result.

### Why the assumption failed

The security guard was correct, but transport/UI mapped a meaningful lifecycle
state to a generic error.

### The durable practice

Keep the fail-closed guard. Return a stable coarse code and structured status;
render `Scanning`, `Rejected`, `Retry available`, or `Clean` without exposing
scanner internals. Timeout never means clean.

## 21. Scan the signed binary, not only source code

### What we saw

Apple detected a private selector embedded in a third-party framework. A broad
string scan then produced false positives from inert resources before a
Mach-O-only scan identified the actual offender.

### Why the assumption failed

Native transitive frameworks are part of the shipped app. Source grep sees too
little; scanning every resource sees too much.

### The durable practice

Inspect executable Mach-O images with `strings` and Objective-C metadata, report
the exact framework, and verify the signed IPA. For Android, inspect merged
release manifests and native libraries in the AAB/APK, including 16 KB page
alignment and both supported ARM ABIs.

## 22. Store permissions are dependency output

### What we saw

An advertising-related permission appeared although KiloDrive did not use
advertising IDs. It came from the merged dependency manifest.

### Why the assumption failed

The source manifest was reviewed instead of the final merged release manifest.

### The durable practice

Diff store permissions per dependency batch, remove unwanted permissions with a
reviewed merger directive or dependency configuration, and fail CI if forbidden
permissions reappear. Keep store declarations consistent with the actual
binary.

## 23. “Uninstall” may not mean “forget”

### What we saw

Android backup/restore could preserve preferences, causing a fresh installation
to skip first-run selection or restore an inappropriate workspace.

### Why the assumption failed

Local first-run state was treated as disposable without considering platform
backup behavior and account binding.

### The durable practice

Classify each preference, exclude sensitive/account-bound state from backup,
validate restored choices against authenticated claims, and clear identity
metadata on logout. A single-role driver cannot render a customer shell because
an old preference says customer.

## 24. Insets and keyboards are functional requirements

### What we saw

Buttons at the bottom of dialogs and forms could sit behind Android navigation
controls or the keyboard. On narrow screens, action rows overflowed and became
untappable.

### Why the assumption failed

Layouts were tested at one screen size and text scale. A visually attractive
fixed row was mistaken for a stable interaction model.

### The durable practice

Use SafeArea/viewInsets, viewport-derived constraints, scrollable controlled
dialogs, expanded dropdowns, and responsive action groups with 48 dp targets.
Render critical routes at narrow/landscape/tablet, large text, light/dark/high
contrast, keyboard open/closed, and gesture/three-button navigation.

## 25. Numbers are not user-facing enum names

### What we saw

Administrative screens displayed numeric type/status values or raw JSON. Dates
appeared as server timestamps and money sometimes used ambiguous symbols.

### Why the assumption failed

Transport representation leaked directly into presentation.

### The durable practice

Map enums through a shared tolerant name layer, timestamps through nullable UTC
parsing plus local display, and money through ISO-aware minor-unit formatting.
Invalid data shows a localized unavailable marker and a sanitized diagnostic;
it never silently becomes “now.”

## 26. Disabled canaries should be quiet and explicit

### What we saw

Unconfigured providers produced repeated warning logs on every scheduled canary
cycle. The noise obscured real warnings.

### Why the assumption failed

“Not configured” was treated as a failed probe even when the provider was
intentionally disabled.

### The durable practice

Canaries run only after a dedicated non-user destination and least-privilege
credentials exist. Disabled and maintenance are explicit states. Alerts require
consecutive real failures and store only provider ID, latency, sanitized status,
and correlation ID.

## 27. A canonical fixture is part of the test contract

### What we saw

End-to-end tests failed because the test driver lacked one of many required
relationships: approved licence, compliant primary vehicle, current documents,
membership term, fresh location, wallet, or clean assignment state.

### Why the assumption failed

The test assumed “driver exists” meant “driver can bid.” In a mature domain,
eligibility is a graph and changes over time.

### The durable practice

Fixture utilities build the graph through supported APIs/lifecycle operations.
A readiness assertion lists every prerequisite and `canBid=true` before a
two-client test. Cleanup runs in `finally`, and test credentials come from CI
secrets.

## 28. A public guide must distinguish code from deployment

### What we saw

Documentation could describe an adapter, canary, recording workflow, or country
as though it were universally enabled.

### Why the assumption failed

Source code is visible and easy to inspect; deployment approval, credentials,
networking, destinations, and legal policy are separate evidence.

### The durable practice

Every chapter uses **Implemented**, **Configurable**, **Operational policy**, or
**Planned**. Claims come from code, schema, tests, and approved evidence. The
guide teaches architecture without promising what it cannot prove.

## Use the lessons, do not worship them

These lessons reflect KiloDrive's constraints and history. A different system
may choose a different database, bus, map engine, or hosting model. Keep the
invariant and re-evaluate the mechanism when scale, regulation, team capability,
or failure cost changes.

The [ADR index](adr/README.md) records the current decisions. The
[runbook index](runbooks/README.md) explains how to respond when their failure
modes appear.
