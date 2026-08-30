# Mobile Architecture

KiloDrive's mobile client is a Flutter application for Android and iOS. The same
binary can expose rider, driver, rental organization, tools-only, and authorized
System Administrator workspaces. This chapter explains the boundaries that keep
that breadth manageable and the release controls needed when Dart code depends
on native SDKs.

## Verified technology baseline

The current source targets Flutter 3.41.7 and Dart 3.11.5. The application uses
Material 3, Riverpod 3, Dio, Firebase services, Google Maps, platform secure
storage, local authentication, social sign-in, Play/App Store billing, and
LiveKit/WebRTC. Exact resolved versions are recorded in the reviewed product
lockfile; this public guide intentionally contains no provider credentials.

Package presence does not prove that a feature is enabled. Firebase, maps,
social identity, store billing, push, and voice require signed native
configuration and approved server-side settings. Google Maps is the implemented
mobile rendering engine. A map abstraction makes another engine possible, but
Mapbox or Apple Maps rendering is not claimed as a shipped runtime option.

## Startup: render first, initialize safely

The app calls `runApp` immediately with a deterministic bootstrap state. It does
not wait for storage, Firebase, device information, connectivity, or a network
request before Flutter can paint. Optional plugin initialization begins after
the first frame and each operation has its own timeout.

```mermaid
stateDiagram-v2
    [*] --> Starting: Flutter renders immediately
    Starting --> Ready: required configuration valid
    Starting --> ConfigurationError: required API origin invalid
    ConfigurationError --> Starting: user selects Retry
    Ready --> FirstRun
    FirstRun --> ToolsOnly
    FirstRun --> Authentication
    Authentication --> WorkspaceReconciliation
    WorkspaceReconciliation --> AppShell
```

A missing optional provider produces a bounded degraded capability, not an
infinite splash. Invalid required API configuration is different: the app shows
a localized, retryable configuration error. Tests use never-completing fakes to
prove the splash resolves.

The background Firebase message entry point is top-level and registered before
the widget tree. It cannot depend on a `BuildContext` or an in-memory provider
that will not exist in a killed process.

## Authentication and workspace reconciliation

Before account creation, the app carries one immutable registration intent:
role, country, contact method, driver account type, and rental-organization
choice. First-run selection and registration do not maintain competing copies.
An interrupted signup restores that intent, while an authenticated user resumes
the authorized workspace or incomplete server-backed onboarding journey instead
of being sent through country/language selection again.

Tokens are stored in platform secure storage. Access tokens are short-lived;
refresh is serialized so concurrent 401 responses do not rotate the same token
multiple times. A failed refresh emits a typed session-expired event. The event
atomically clears tokens and identity metadata, disconnects SignalR/voice,
evicts account-bound caches, and routes to login.

Logout first requests server refresh-token revocation and then performs local
cleanup even if the network response cannot be completed. Offline cleanup must
not leave another user's role, tenant, name, or workspace preference on the
device.

The last workspace is only a preference. After password, OTP, social login,
refresh, or secure-state restore, the app derives authorized workspaces from the
authenticated API claims/profile. A single-role driver cannot accidentally
render the rider shell because an old device preference says `customer`.
Multi-role users see only authorized choices, and a System Administrator selects
an authorized country workspace before administrative data loads.

The APK/IPA is an untrusted client. Changing Dart code, replaying an HTTP call,
or modifying a local role cannot grant server permission. The API revalidates
role, tenant, country, plan, compliance, wallet, and state-transition rules.

Social registration and social account linking are separate actions. If a
provider identity collides with an existing account, the app preserves a
protected pending-link intent and guides the user through authentication,
recent reauthentication, review, explicit confirmation, or cancellation. It
does not silently link by email and does not discard the provider transaction
into an unexplained loading state.

Sensitive profile/security actions obtain a short-lived recent-authentication
proof from the API after the user re-enters the current password or proves an
already-linked social identity. The proof complements any required 2FA step-up;
local app unlock is not an account-security proof.

### App lock and device lifecycle

App lock is a local privacy boundary. When enabled for an authenticated account,
a cold launch locks before authenticated content is revealed. The sixty-second
grace applies only when an already-visible app moves to the background and then
resumes. Biometrics use the platform prompt; the fallback is KiloDrive's own
four-digit app PIN, not the Android or iOS device PIN. Neither unlock method is
proof for a wallet, payout, or account-security API. Logout, account switch,
missing account-bound state, and process restoration cannot inherit another
user's unlocked session.

Tests distinguish a user-cancelled biometric prompt, temporary failure,
platform lockout, unavailable hardware, cold launch, short backgrounding, and
an actual timeout. “Wait one minute before app lock works” is not an acceptable
substitute for a deterministic policy.

## Driver onboarding: resumable but not bypassable

New drivers move through one server-backed, twelve-page journey. The mobile app
renders immutable view models and saves the current page; it does not keep an
untyped JSON checklist or infer completion from one local flag.

| Page | Purpose | Blocking rule |
| ---: | --- | --- |
| 1 | Identity, profile photo, driver-licence details and licence document | Required |
| 2 | Proof of address and background/police evidence | May be deferred for up to 21 days; overdue evidence locks operations |
| 3 | Membership introduction and Free/Silver/Gold choice | A deliberate choice is required; paid membership is not required |
| 4 | Verified email and phone review | Both contacts must be present and verified |
| 5 | Language, currency display, distance unit, text/accessibility and optional 2FA preferences | Required confirmation; preferences do not change ledger currency |
| 6 | Vehicle make, model, year, condition and images | An existing complete verified vehicle satisfies it |
| 7 | Registration details, expiry and document | Required |
| 8 | Insurance details, expiry and document | Required |
| 9 | Fitness/inspection details, expiry and document | Required for every driver at the current implementation baseline |
| 10 | Optional reviewed Uber, Lyft or inDrive rating screenshots | Skippable; imported evidence remains separately labelled |
| 11 | Hourly-hire rate, distance unit, currency view and driver business preferences | Required confirmation; reviewed default hourly rate is USD 6.00 |
| 12 | Terms, Privacy and manual links plus explicit legal acceptance | Required to complete; cancel-and-delete follows the separate governed deletion flow |

Each page offers Back, Next, Save for later and Logout; the restricted settings
action exposes only basic preferences and cannot escape into the ordinary app
shell. Progress is server-derived. Saving after a completed journey is a safe
no-op, and completion is monotonic: a future checklist or document change may
make the driver operationally ineligible, but it must not send an already-
completed driver back to “add a vehicle.” Ongoing compliance and onboarding
history are different facts.

The API remains the enforcement boundary. Completion stages an outbox event for
administrator and driver notification, while operational bidding still requires
current licence, vehicle, document, membership, assignment, online and telemetry
eligibility. A client cannot unlock bidding by skipping screens or editing
local preferences.

### Managed queue location session

Airport and venue queues do not depend on the toolkit screen remaining open.
After an explicit, successful join, Flutter requests a short server-authorized
queue telemetry session and hands it to the same narrow native location bridge
used for active-trip reliability. Native tracking renews one zone/lease only;
the UI displays lease freshness and expiry. Leaving the zone, going offline,
receiving an assignment, lease expiry, logout, or an authoritative server denial
stops tracking and removes the active position. This is not permission for
general background driver surveillance.

Vehicle fitness is not country-conditional in the reviewed implementation:
onboarding, vehicle validation, readiness, and primary-vehicle selection all
require current fitness evidence. A country setting cannot waive that gate
today. Introducing country-conditional fitness later requires one versioned
server rule, matching client guidance, and positive/negative readiness tests;
documentation alone must never imply that behavior exists.

## Feature-first layering

New and migrated functionality lives under `features/<feature>/`. A mature
slice normally has these responsibilities:

```text
features/<feature>/
  data/          concrete API repository, cache adapters, DTO mapping
  domain/        immutable application models and repository interfaces
  presentation/ AsyncNotifier/view state and focused widgets
  <feature>.dart public barrel exported to consumers
```

Concrete `data/` implementations are private to their feature. Screens import
the feature barrel, not another feature's API repository. The repository owns
transport cancellation, caching, DTO conversion, and diagnostics. The notifier
owns user intent and presentation state. Widgets render state and dispatch
intent; they do not coordinate several raw HTTP calls.

Some older screens remain in the top-level `screens/` directory while migration
continues. Compatibility exports preserve routes during that work. Their
presence should be documented as migration debt, not proof that the boundary is
unnecessary.

## Riverpod state model

Feature controllers use auto-disposed asynchronous notifiers and immutable view
models. Watching a narrow selector keeps an unrelated dashboard card from
rebuilding when another card refreshes.

An asynchronous screen distinguishes:

- initial loading: shared shimmer appropriate to the content shape;
- successful empty: illustrated empty state and relevant next action;
- whole-screen failure: shared tonal error state with Retry;
- refresh failure: previously successful data plus a compact partial-error
  banner; and
- mutation state: the affected action is disabled without hiding the rest of
  the screen.

Optional endpoint failure cannot erase required core data. A membership screen,
for example, can retain plan/entitlement data while store availability displays
its own recoverable error.

## Request cancellation, generations, and caches

Dio `CancelToken`s cancel autocomplete, route, and other superseded reads when
the provider supports cancellation. When cancellation cannot stop a response,
the notifier attaches a monotonically increasing request generation and ignores
a response from an older generation. Disposal also invalidates the generation.

Type-ahead is debounced. Place details are cached briefly and keyed by provider
identity plus locale/country context. Image bytes use a bounded account-aware
LRU with requested decode dimensions based on logical size and device pixel
ratio. Logout and avatar revision changes evict relevant entries.

A successful profile-photo upload updates the authenticated profile revision
and provider state before the UI reports completion. Screens use the revisioned
avatar provider rather than holding an old URL or byte array, so the new image
appears immediately and survives relaunch after the next authoritative profile
load.

Legal-name changes do not share the avatar fast path. They create or update a
governed review state, preserve the last approved identity while review is
pending, and present the review outcome without exposing evidence URLs or raw
payloads. This distinction prevents a harmless media refresh from becoming an
identity-boundary shortcut.

Caches have explicit TTLs and are never an authority for authorization,
financial balance, driver eligibility, or document approval.

### Assisted-rider and fare-split surface status

Flutter has rider assistance-profile and driver-capability screens, plus fare-
split owner/invitation screens. These are incremental source surfaces, not an
active-country claim.

Assisted-rider activation must fail closed on a verified feature policy. The
current migration still needs to reject an invalid policy signature, gate every
entry point, render the operational need on the driver offer and assigned trip,
stop hard-coding option labels/bounds, and connect the stored caregiver
notification preference to a reviewed dispatcher. Portal parity and real-device
accessibility remain incomplete.

Fare-split retries must preserve one idempotency key and mandatory expected
version. The owner needs durable status/expiry/recovery presentation, and a fare
change that alters a payer's share needs renewed consent. Until server bootstrap,
client lifecycle, reversal, and country/provider evidence are complete, the
feature policy keeps purchase/acceptance entry unavailable.

## Realtime and offline behavior

SignalR events merge by a server-persisted entity version, not device wall-clock
time. An older event cannot overwrite a newer state. Polling remains a recovery
path rather than the primary real-time experience.

Only operations designed for replay enter an offline queue. Queue entries bind
to the account and tenant, retain the original idempotency key, have a TTL, and
are removed on logout. Wallet, payout, account-security, or other step-up
operations are not authorized by a local PIN or a stale offline decision.

The bid outbox is the currently reviewed replayable mutation slice. It stores
encrypted records in account-bound SQLite using a device-protected key and
authenticated encryption. Each record retains the idempotency key, request
hash, expected entity version, workspace ownership, and authoritative offer
expiry. Missing/malformed expiry fails closed; corrupt or wrong-workspace rows
are quarantined instead of dispatched; logout removes both records and the
account binding. This does not authorize offline wallet, payout, profile-
security, or trip-settlement commands.

Connectivity is advisory: a network indicator may say online while an API or
provider is unreachable. Repositories classify timeout, cancellation, 401
refresh, forbidden, successful empty, validation, conflict, rate limit, and
server failure into stable view outcomes.

Wallet top-up is the reviewed durable customer payment-status slice. After
checkout the app navigates to a typed `Pending`, `Completed`, `Failed`, or
`Needs attention` resource keyed by payment ID and idempotency key. A protected,
account-bound pending reference survives process death; repository/background
reconciliation refreshes wallet state after completion and exposes receipt or
support actions. Last-good state remains visible on a recoverable refresh error.
This does not claim equivalent recovery for every membership, ride, rental, or
cashout payment path.

## Navigation and shell ownership

Named route construction goes through the application routing layer so
transitions, deep links, and authorization checks remain consistent. Shell tabs
are body widgets owned by the shared app shell. Pushed detail/edit screens own a
scaffold. Phones use a navigation drawer; wider layouts can use a rail.

Deep links are treated as untrusted input. The app validates route shape,
authentication, workspace, and entity access before opening a destination.
External links use an allow-listed URI and a checked launcher with a localized
fallback.

Peer tab content uses the shared accessible tab standard, including swipe when
it does not conflict with a map, carousel, signature canvas, or another
horizontal gesture owner. Chat and similar pushed screens also provide a
platform-appropriate back gesture while preserving unsent input and focus.

Complex first-ride concepts are taught in a one-time, account-bound rider or
driver guide. Time-sensitive creation and bidding screens then use concise
labels and progressive disclosure rather than repeating a manual above the
primary action. Dismissing or completing the guide is not permission and never
changes server eligibility.

## UI, localization, and accessibility

Colors, typography, shapes, and semantic statuses come from the theme. Content
loading uses shimmer rather than indefinite progress indicators. Controls have
at least a 48 by 48 logical-pixel interactive surface and a useful semantics
label, selected state, and focus order.

The app composes its preference scale with the platform text scaler instead of
replacing accessibility settings. Layout certification covers 320-pixel phones,
tablet portrait/landscape, split-screen, 1.3x and 2.0x system text, light, dark,
high contrast, open keyboard, three-button navigation, and gesture navigation.
Safe areas and `viewInsets` keep primary actions above the keyboard and system
navigation areas.

English, Spanish, French, Japanese, Simplified Chinese, and Traditional Chinese
ARB resources retain exact key and ICU-placeholder parity. The generic Chinese
resource is the Simplified fallback, not a separate language choice. Money uses
the active currency context and ISO-aware formatter. Server UTC timestamps go
through the nullable UTC parser and localized display helpers; malformed input
shows an unavailable marker rather than the current time. Offset-less server
values are treated as UTC by the centralized parser; date-picker/local-only
values stay a separate type of input. KiloDrive's reviewed presentation policy
uses a localized twelve-hour AM/PM display, including Japanese and Chinese
resources; rendered locale tests, rather than the device formatter's default,
prove that policy. Seconds appear only where chat or operational ordering needs
them.

## Location and maps

Location selection returns a last-known fix immediately only when age and
accuracy meet policy, requests a fresh balanced-accuracy fix in parallel,
updates coordinates first, and reverse-geocodes asynchronously. Nearby
reverse-geocode results are cached briefly. The UI shows an explicit locating or
retry state and can display coordinates when geocoding is unavailable.

Recent rider locations are an account-bound convenience list, not a geocoder or
authorization source. Suggestions retain reviewed display information and
coordinates under the configured privacy/retention policy; selecting one still
passes the same quote/create validation as a newly searched place.

Entering the driver bidding hall evaluates service availability, permission,
location settings, and telemetry freshness before presenting the driver as
offer-ready. Denial or stale telemetry produces a focused recovery action. A
driver must not sit in an apparently active hall while the server will reject
matching because no fresh permitted location exists.

Foreground/background driver telemetry follows platform permissions and store
policy. An online indicator is not a promise of infinite background execution.
The server expires stale telemetry and driver availability. Active-trip safety
and background location need visible, user-understood behavior and matching
store declarations.

## Native security and permission boundary

Permission prompts occur only when a user invokes a feature that needs them.
KiloDrive does not use a dismissible custom pre-prompt that steers the Apple
system choice. A denied permission produces feature-specific recovery guidance;
it never causes a startup loop.

Release manifests are inspected after merging because transitive native SDKs
can introduce permissions. Android gates reject advertising identifiers and
unapproved foreground-service permissions. iOS declares remote notifications
but does not use background audio or legacy VoIP keep-alive merely to preserve a
process.

The customer application contains no proxy-server settings or proxy wording.
Network interception for an approved support investigation belongs in a
separately controlled diagnostic environment/build and must never become an
end-user toggle or silently weaken wallet/security transport.

## Testing pyramid

1. **Every change:** pure models, formatters, repositories, providers, and widget
   tests with fakes. Form/property fuzzing uses recorded deterministic seeds so
   a discovered boundary failure becomes a permanent regression.
2. **Merge:** semantics-driven emulator smoke for tools-only, rider, driver, and
   rental workspaces; no credentials in screenshots or artifacts.
3. **Required nightly/release lane:** real-device permissions, background
   location, push, biometrics, offline queue, SignalR reconnect, store billing,
   and calls. Source and CI configuration do not prove that the lane ran for a
   release; signed device evidence is retained separately, and iOS remains
   uncertified until that evidence exists.
4. **Visual matrix:** pairwise screen harness for dimensions, text scale, theme,
   keyboard, navigation mode, touch target, semantics order, and overflow.

Race tests cover refresh versus mutation, dispose versus response, realtime
versus refresh, logout versus queued work, and session expiry during navigation.

The default test process is hermetic. It refuses production/external origins
and real providers even when a developer machine happens to have credentials.
Crossing a real boundary requires an explicit certification job, non-user
fixtures, allowlists, a run ID, cleanup, and sanitized evidence.

## Native dependency release discipline

Release Dart code is built with the reviewed obfuscation and split-debug-info
controls. Obfuscation reduces casual recovery of symbols; it is not
authorization, encryption, or a place to hide a secret. Split debug symbols are
retained in protected release evidence and linked to the exact artifact hash so
crashes remain diagnosable.

CI scans AOT snapshots, native binaries, archive metadata and packaged resources
for developer workstation paths, source roots, debug service markers and other
release-only privacy regressions. It also checks that an IPA archive contains
the expected executable symbols rather than treating an empty scan as success.
Endpoints and feature concepts may remain discoverable in a client; the server
still enforces every permission and resource boundary.

Native upgrades are performed in isolated batches:

1. LiveKit/WebRTC;
2. social authentication and local authentication; then
3. Riverpod/state-management changes.

Each batch runs format, fatal analysis, tests, Android manifest/ABI/16 KB checks,
arm32+arm64 APK/AAB builds, iOS archive/entitlement/private-selector scans,
background/killed call tests, and store-permission diffs. Unrelated major
upgrades are not combined because a failure must have a small, attributable
change set.

See [Flutter package inventory](../third-party/flutter-packages.md) and the
[mobile release runbook](../runbooks/mobile-release.md) for the executable gates.
The feature ownership decision is recorded in
[ADR 010: Flutter feature repositories](../adr/010-flutter-feature-repositories.md).
