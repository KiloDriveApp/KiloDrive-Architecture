# Active navigation and pickup recovery

- **Owner:** Mobile, Trip, Geospatial and Safety operations
- **Status:** Implemented; native execution requires configured provider access
- **Last exercised:** 2026-11-03 on a stationary Android device; moving-road and
  native iOS checks remain separate certification obligations
- **Related architecture:** [Geospatial](../architecture/geospatial.md) and
  [trip location/privacy](active-trip-location-and-privacy.md)

## Purpose and safety boundary

Use this runbook when the driver sees a blank navigation map, an unavailable
route, stale ETA, unexpected audio, or an assignment that cannot be recovered.
The `navigation-service` client module owns guidance and camera presentation.
The server owns assignment, arrival, boarding, completion and money. Navigation
must never start, end, cancel or financially settle a trip by geofencing alone.

## Normal flow

An assigned driver opens the trip from Active jobs. Guidance targets the booked
pickup until the trip starts, then targets the destination. A moving passenger's
phone does not silently rewrite the agreed pickup. If that pickup is no longer
usable, participants use communication and the supported reasoned cancellation
flow; they reconcile an uncertain cancellation before requesting another trip.

Following mode uses a heading-up perspective. Overview shows the remaining
route, and full-screen free pan stays under the driver's control until Recenter.
The embedded map preserves page scrolling. Full screen keeps speed and ETA in
one row. A valid stationary GPS observation is zero; an absent, inaccurate or
stale observation is unavailable. ETA and arrival hints clear during rerouting
instead of retaining an obsolete estimate.

Audio belongs to the account and trip. Muting persists through embedded/full-
screen handoff and is applied before native guidance starts. Stream failure
invalidates pending route work and silences obsolete guidance. Signing out or
changing account cannot inherit the former account's audio preference.

## Diagnose before changing configuration

1. Check the authoritative trip state, participant, country and funding context.
   A six-character trip reference assists authorized search; it grants no access.
2. Compare app/build, native OS, location permission, recent fix quality and
   connectivity. Inspect safe error categories, not location payloads or keys.
3. For native `networkError`, verify Navigation SDK enablement, billing, and the
   consumer key's API restrictions as well as package/signing or bundle identity.
   A Maps-only key can render ordinary maps while native navigation fails.
4. Verify one route owner, current destination generation, and current app
   visibility. A realtime trip refresh must not repeatedly retry failed routing.
5. If arrival is unavailable, inspect the database-owned
   `trip-pickup-arrival-radius-by-membership` setting and the effective membership
   in the trip's frozen personal or organization context. Boarding and completion
   use independent country policies. Paid access does not approve documents.
6. For an absent road advisory, inspect freshness, route proximity, direction,
   dispute/expiry state, foreground ownership and repeat suppression. Community
   reports are advisory, not independently verified road facts or full coverage.

## Contain and recover

Keep the trip's ordinary status and communication controls available when native
navigation fails. Offer explicit Retry or the supported external-navigation
fallback. Neither changes the lifecycle or replaces arrival, start or completion.
Do not loosen key restrictions, synthesize GPS, create public fake hazards or
move a pickup in the database to make a test pass.

Make approved arrival-policy corrections through the audited administrative
settings API. Validate all three tier keys, finite allowed values and independent
readback. Do not reset accounts or overwrite a configured setting with a seed.

Reported checkpoints, cameras, faulty traffic lights, congestion, accidents and
road hazards may appear ahead. Spoken advisories require a suitable on-device
voice and enabled audio; they are suppressed around upcoming turns, rerouting,
background state and repeat cooldown. Unavailable audio leaves visual guidance.

## Native packaging and rollback

The reviewed integration pins `google_navigation_flutter` 0.10.0 and
`flutter_tts` 4.2.5, Android minimum API 24 and iOS 16. Android 12 uses hybrid
composition to avoid the observed texture/ImageReader failure. The scoped
Navigation/WebRTC JNI deduplication transform verifies exact duplicate class
hashes. An upstream mismatch must fail the build; never exclude whole packages
or accept whichever duplicate Gradle selects.

The packaged APK and AAB must pass the manifest permission gate. The native
SDK contributes a background-location permission transitively; the consumer
manifest removes it. The scoped telemetry service and the SDK guidance service
are separately owned. Both are private and location-only; native guidance stops
on view exit, app backgrounding, terminal trip state and task removal. Unknown
typed services, an exported guidance service or any extra foreground-service
type fail packaging. Permission checks include SDK-specific tags and reject
duplicate declarations. Legacy Bluetooth declarations are normalized to one
version-bounded entry per permission. Starting navigation from the background
is not supported. Native permission localization is checked locally and in the
Mac lane, including the motion permission required by navigation.

Abort rollout for map crashes, cross-account route ownership, continuing audio
after terminal state, false speed/ETA, or any lifecycle/financial side effect
from navigation. Roll back the consumer release using the release procedure;
preserve committed trip and financial evidence. A data-only arrival setting does
not require reverting compatible physical schema.

## Verify and record

Exercise fullscreen/embedded handoff, mute before first guidance, overview, free
pan and recenter, destination transition, explicit retry, stale-route fencing,
zero versus missing speed, rerouting estimates, logout and terminal cleanup.
Check cancellation independently in the server and confirm no residual hold or
active assignment. Replay must use real recorded samples and disclose gaps.

Stationary screenshots establish rendering and controls only. Physical road
accuracy, spoken timing, deviation recovery, weak-connectivity driving and iOS
background behavior require separate real-device evidence. Do not infer these
from unit tests, a build upload or a configuration flag.

Retain artifact hashes, sanitized test results, state readback and fixture-only
screenshots in restricted release evidence. Public manuals use reviewed captures
and distinguish provider guidance from customer trip progress. Record store
submission, review, processing and availability as separate states.

## Implementation references

The private source of truth is the consumer
`lib/features/navigation_service` module, `TripArrivalMembershipPolicy.cs`,
`TripWorkflowOptions.cs`, `TripReferenceReader.cs`, and
`database/updates/2026-11-02-trip-arrival-membership-settings.sql`. Regression
coverage includes navigation ownership/rerouting, road advisory filtering,
trip-speed presentation, policy validation and scoped reference lookup.
