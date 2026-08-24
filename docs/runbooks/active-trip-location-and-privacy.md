# Active-trip location and privacy runbook

- **Owner:** Mobile, Trip, Safety, Privacy, and Platform operations
- **Status:** Maintained production runbook
- **Last exercised:** Exercise before each store release that changes location behavior
- **Related architecture:** [Rider and driver safety](../architecture/rider-driver-safety.md), [geospatial](../architecture/geospatial.md), and [privacy](../security/privacy-and-data-protection.md)

Use this runbook when active-trip location does not start, remains active after
a trip, becomes stale, loses queued samples, shows the wrong rider freshness,
or disagrees with the published privacy/store declaration.

The safety rule is simple: location is collected only for a server-confirmed
Assigned, DriverArrived, or InProgress trip. It helps navigation, rider
visibility, route-change detection, RideCheck, investigation, and an authorized
trip replay. It cannot complete, cancel, charge, refund, or settle the trip.

## Expected behavior

### Android

The driver starts the trip tracking service while KiloDrive is visible. The
native service declares only the location foreground-service capability and
shows a persistent, user-visible “trip in progress” notification. It is not a
general online-driver keepalive, microphone service, or phone-call service.

### iOS

The driver starts an active Core Location background session from the visible
trip experience. The application explains the active-trip purpose and exposes
the platform location indicator. Ordinary bidding-hall availability does not
justify continuous background collection.

### Both platforms

- Samples have stable IDs, UTC capture time, accuracy, and trip/account binding.
- The protected on-device retry queue is bounded to 500 samples and 24 hours.
- Logout, account switch, assignment removal, terminal trip state, permission
  revocation, or an authoritative API rejection stops collection and clears or
  quarantines unusable queued data.
- The rider sees `Live`, `Last updated …`, or `Driver location temporarily
  unavailable`; the UI does not pretend a stale marker is live.
- A server-configured telemetry gap creates a safe metadata event and may start
  a RideCheck. It does not infer wrongdoing from one missing update.

## First response

1. Establish the authoritative trip ID, lifecycle state, driver identity, and
   assigned vehicle without copying PII into the incident record.
2. Record the correlation IDs and app/build versions from both participants.
3. Determine whether the problem is collection, local queueing, upload,
   authorization, durable persistence, realtime projection, or rider rendering.
4. If collection continues after a terminal state, treat it as a privacy
   incident: revoke the tracking session, contain the affected release, preserve
   sanitized evidence, and involve Privacy/Security.
5. If an active trip has a sustained telemetry gap, do not automatically cancel
   or financially settle it. Show truthful freshness, retain other contact and
   emergency paths, and follow the safety escalation policy.

## Diagnostic decision tree

### Native service/session never starts

- Confirm the server reported an eligible active state.
- Confirm location permission state and platform restrictions.
- Verify the start occurred from a visible user action; background-start rules
  intentionally reject some invisible launches.
- Confirm the signed artifact contains the reviewed location declarations and
  does not reintroduce unrelated microphone/phone-call foreground services.
- Verify the native-to-Flutter bridge received the account, trip, endpoint, and
  short-lived session context without logging them.

### Samples exist locally but do not reach the API

- Inspect bounded queue counters, oldest-sample age, last sanitized status, and
  correlation ID. Never export coordinates or tokens to general telemetry.
- Verify refresh/session validity and the trip/account binding.
- Check provider/network reachability and API rate-limit responses.
- Confirm replay uses the original sample ID. A retry must not generate a new ID.
- A 401/403 or terminal-state response is authoritative; stop or reacquire the
  permitted context rather than retrying forever.

### API receives samples but the rider is stale

- Verify the country-cell write and current-location projection independently.
- Check Valkey health, TTL, SignalR backplane, group membership, event version,
  and the client's last accepted version.
- Reconnect/rejoin from authoritative active-trip state. Do not fabricate a new
  trip or lower freshness thresholds to hide the problem.
- Confirm the polling/reconciliation fallback converges if SignalR delivery is
  missed.

### Collection does not stop

- Confirm the completion/cancellation/assignment-removal event committed.
- Check the durable trip event and client receipt/reconciliation path.
- Force an authoritative active-trip refresh. If no active trip exists, stop the
  native service/session and wipe that account's queue.
- Review whether a stale local workspace or another signed-in account retained
  ownership. Account-bound keys must prevent cross-account reuse.

## Privacy and retention controls

The production policy and technical settings must agree. The reviewed defaults
at 2026-08-24 are:

| Data | Default | Purpose and stop rule |
| --- | ---: | --- |
| Current live-location cache | 10 minutes | Realtime trip visibility; expires automatically |
| Device retry queue | 500 samples / 24 hours | Temporary offline delivery; wiped on logout/account change and after terminal reconciliation |
| Public trip-share link | 120 minutes | Authorized viewer access; revocable and expires |
| Shared moving-location window | latest 15 minutes | Bounded coarsened public view; excludes account/contact/payment data |
| Ordinary trip replay | 365 days | Safety, support, and dispute evidence; subject to country policy and legal hold |

Users stop active collection by ending/cancelling the trip through the supported
flow, going offline after the assignment ends, revoking location permission, or
logging out. Revoking permission can limit safety/navigation behavior but must
not be circumvented. Emergency calling must not depend on telemetry upload.

Deletion is orchestrated across the global identity and authorized country
cells. Legally required financial, dispute, or safety evidence may be retained
or de-identified under an approved rule. A legal hold is audited and narrowly
scoped; it is not a reason to retain every user's live cache indefinitely.

## Recovery proof

Do not close the incident after seeing one moving marker. Prove:

1. foreground start from an eligible visible flow;
2. background, lock-screen, network handoff, and process-pressure continuity;
3. bounded offline queue and idempotent reconnect flush;
4. truthful rider freshness during a forced gap;
5. server safety event after the configured sustained threshold;
6. cold-start active-trip recovery and realtime group rejoin;
7. immediate stop after complete, cancel, assignment removal, logout, and
   permission revocation;
8. queue/account isolation after login as another fixture;
9. Android and iOS store declarations match the signed binary and review video;
10. logs, traces, screenshots, and artifacts contain no coordinates, tokens,
    contact details, or customer payloads.

Retain build hashes, test run IDs, sanitized correlations, configuration
fingerprints, and reviewer sign-off. Do not retain a customer's route merely to
prove the test ran; use dedicated fixtures.

