# ADR 010: Use feature repositories and AsyncNotifiers in Flutter

- **Status:** Accepted/Incremental
- **Date:** 2026-08-23
- **Decision owners:** Mobile, API Contract, and Quality Engineering
- **Related systems:** Flutter feature slices, Riverpod, Dio, SignalR, caches, offline queues, and UI tests

## Context

As KiloDrive grew, several screens called the shared API client directly and
managed `isLoading`, errors, timers, controllers, caches, and realtime events in
large widget classes. That approach is quick for one endpoint. It becomes
fragile when a screen must debounce autocomplete, cancel an old route request,
retain successful data while one optional card fails, merge SignalR updates,
survive logout, and remain testable without a live server.

The user-visible failures were predictable: infinite spinners, stale data
winning races, swallowed errors, a response updating a disposed screen, an
optional store call blanking a valid membership, and nearly identical loading
or error UI implemented differently in many places. Moving HTTP calls into a
different file alone would not solve those lifecycle problems; the state and
ownership rules also need to be explicit.

At the same time, KiloDrive must preserve its public mobile routes and API DTO
wire shapes while migration proceeds one feature at a time.

## Decision drivers

- Widgets should render state and send user intent, not orchestrate transport.
- Features need testable interfaces that can be replaced with deterministic
  fakes.
- Superseded and disposed requests must not overwrite current state.
- Realtime and HTTP responses need one monotonic merge rule.
- Initial, empty, whole-screen error, partial error, refresh, and mutation states
  have different UX.
- Account-bound caches and offline work must be evicted safely on logout.
- Migration cannot require a route or DTO breaking change.
- Rebuilds and memory use must remain bounded on small phones and long lists.

## Decision

Each migrated feature exposes a public application/presentation barrel and uses
three conceptual layers:

```text
features/<feature>/
  data/          private API/cache implementation and DTO mapping
  domain/        immutable models and repository interfaces
  presentation/ AsyncNotifier, typed view state, and focused widgets
  <feature>.dart public barrel
```

Consumers import the owning feature's barrel. Concrete `data/` classes remain
private to the feature and are wired through providers. A static dependency
test rejects `/data/` imports outside the owning feature and its tests.

Feature state is represented by auto-disposed `AsyncNotifier`s or an equivalent
typed immutable view state when several independent cards need separate status.
The repository owns transport, DTO mapping, brief caches, cancellation, and
safe diagnostics. The notifier owns user intent, refresh/mutation coordination,
last-successful state, and which error is whole-screen versus partial. The
widget owns layout, semantics, text input controllers, and navigation.

### Cancellation and request generations

When Dio/provider work supports cancellation, the repository cancels a request
that has genuinely been superseded, such as an older autocomplete or route
query. Cancellation is not used as a general cleanup hammer: disposing an
optional store request must not cancel required membership data that already
belongs to the view.

When the underlying call cannot be cancelled, the notifier records a
monotonically increasing local generation. Only a response matching the current
generation may update state. Disposal invalidates the generation. Expected
cancellation is classified separately from a recoverable service failure and
does not create a noisy user error.

### Realtime merge

Entities received from HTTP and SignalR carry a server-persisted monotonic
version. The repository/notifier accepts an event only when its version is newer
than the stored entity. Wall-clock ticks and device time are not used as entity
versions because multiple API nodes and clock movement can reorder them.

### View-state contract

- **Initial load:** shared content-shaped shimmer.
- **Successful empty:** illustrated empty state and a useful next action.
- **Whole-screen failure:** shared tonal error state with Retry.
- **Refresh failure:** keep the last successful data and show a compact,
  retryable partial-error notice.
- **Partial-card failure:** fail only that card; other successful cards remain.
- **Mutation:** disable the relevant action, preserve context, and reconcile the
  authoritative result.

401 refresh, 403, 404-as-empty, validation, conflict, rate limit, offline,
timeout, and 5xx remain distinct typed outcomes. Diagnostics contain an
operation name and correlation ID, never credentials, payloads, addresses, or
tokens.

### Caches and offline work

Brief place-details/reference caches have an explicit TTL and context key.
Authenticated image caches bind to account and revision and have a strict memory
budget. Logout evicts tokens, account metadata, caches, realtime subscriptions,
and replay queues.

Only mutations designed for safe replay enter the offline queue. Entries retain
the original idempotency key, account/tenant binding, request generation, and
expiry. Local PIN or biometric success never authorizes a server-side wallet,
payout, or security boundary.

### Migration strategy

Slices migrate independently. Compatibility exports and existing routes stay in
place until all consumers/tests import the feature barrel. After zero references
to the legacy implementation are proven, compatibility exports are removed.
Vehicles, security/privacy, profile governance, recurring rides, wallet
commerce, trips, deliveries, offers, chat/calls, onboarding, reports, settings,
and admin workspaces follow the same boundary without one high-risk rewrite.

### Reviewed migration baseline

The feature-first directory and repository/provider pattern now exist across
account, calculators, chat, dashboard, membership, onboarding, privacy,
profile, recurring rides, rentals, reports, rides/trips, security, settings,
support, System Admin, vehicles, voice, and wallet areas. This proves the
pattern and gives new work an owning feature boundary.

The migration is **not complete**. Legacy top-level screen and presentation
code still contains direct `apiClientProvider` references, and compatibility
exports remain while consumers move to feature barrels. A directory existing
under `features/` is not enough to call its slice complete.

The exit criterion is mechanical and behavioral:

1. no presentation/widget outside an owning data adapter calls
   `apiClientProvider` directly;
2. no consumer imports another feature's `/data/` implementation;
3. all consumers use the public feature barrel and repository interface;
4. cancellation, request-generation, realtime-version, refresh/mutation, and
   dispose/response races have focused tests;
5. shared shimmer, empty, whole-screen error, and partial-error states replace
   local ad hoc state; and
6. codewide zero-reference proof permits deletion of compatibility exports.

## Alternatives considered

### Continue calling the API client from widgets

This minimizes files but couples layout, request lifecycle, business intent,
and error handling. It makes race and dispose behavior difficult to test and was
rejected for feature work.

### One global application state object

A global store can centralize data but encourages broad watches and unrelated
rebuilds, makes account/workspace eviction risky, and blurs feature ownership.
Shared session/currency/connectivity contexts remain global; domain state stays
inside its feature.

### Use repositories without typed notifiers

Repositories improve transport testing but do not by themselves define refresh,
partial failure, mutation, or disposal behavior. The presentation controller is
still required.

### Replace Riverpod with another state framework

BLoC, Redux, or another framework could enforce similar boundaries. A rewrite
would add risk without addressing the core ownership problem. Riverpod already
supports lifecycle, dependency injection, selectors, and deterministic tests.

### Generate an API client and expose it directly to screens

Generation can improve DTO correctness, but a generated client remains a
transport boundary. It does not own caching, races, realtime merge, user-facing
state, or account cleanup. Generated code may sit behind a repository later.

## Consequences

### Benefits

- Transport and state races can be tested without rendering a full screen.
- Screens share consistent shimmer, empty, error, and refresh behavior.
- Optional failures no longer erase valid core content.
- Realtime state converges by server version instead of arrival timing.
- Narrow provider watches and immutable models reduce unnecessary rebuilds.
- Routes and DTO contracts remain stable during incremental migration.
- A map/provider implementation can change behind an interface without
  rewriting feature state.

### Costs and risks

- A small feature uses more files and explicit models.
- Poorly designed view models can duplicate transport DTOs without adding
  meaning; domain models should reflect application needs.
- Auto-dispose can surprise engineers who start unowned background work;
  repository lifetimes and cancellation ownership must be explicit.
- Temporary compatibility exports create two apparent import paths and need a
  tracked removal condition.
- Inconsistent partial migrations can be confusing; feature READMEs/barrels and
  dependency tests reduce this risk.

## Security, privacy, and compliance

Repositories attach authentication and correlation through the shared network
boundary rather than individual screens. Diagnostics redact query tokens,
payloads, PII, and provider secrets. Account-bound data is wiped on logout and
cannot be restored into another user's workspace. Local caches never decide
authorization, membership, compliance, wallet balance, or document approval.

Deep links and routes remain untrusted until the authenticated workspace and
entity authorization are resolved by the server.

## Reliability and operations

- Repository metrics separate app time, API time, and external provider time.
- Warm autocomplete/route/quote p95 is monitored without logging location text.
- A recoverable error includes safe operation and correlation context for
  support.
- SignalR is accelerated delivery; bounded refresh/polling recovers durable
  state after disconnect.
- Feature flags and provider availability map to an explicit disabled/degraded
  view rather than an exception or blank screen.

## Validation

- Provider/notifier race tests for refresh-versus-mutation,
  dispose-versus-response, older-generation response, and older realtime event.
- Offline, timeout, refresh-401, forbidden, 404-empty, 409, 429, and 5xx tests.
- Widget tests for initial shimmer, empty, whole-screen error, previous data plus
  partial error, and successful retry.
- Rebuild-count and frame-budget tests for dashboards and long lists.
- Registry-driven render tests at narrow/tablet portrait/landscape, 1.3x/2.0x,
  light/dark/high contrast, keyboard open/closed, and Android navigation insets.
- Static import test forbidding cross-feature data-layer access.
- Deterministic integration flows use fake repositories first and production-like
  API fixtures at the outer test layer.

## Follow-up

- Keep [mobile architecture](../architecture/mobile.md) synchronized with the
  current migration state.
- Remove each compatibility export only after codewide zero-reference proof.
- Publish a feature template showing repository, notifier, typed state, tests,
  and public barrel.
- Reassess module boundaries when team ownership or build times—not fashion—show
  a need for separate Dart packages.
