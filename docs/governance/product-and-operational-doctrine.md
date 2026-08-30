# Product and Operational Doctrine

## Purpose and reviewed baseline

This chapter records the rules KiloDrive uses when a product idea crosses the
boundary from screen design into identity, location, money, safety, or
operations. It is deliberately stricter than a feature list. A feature list can
say that a button exists; doctrine explains what must remain true when the
network fails, two people act at once, a provider times out, or an operator has
to recover the system at 2 a.m.

- **Reviewed:** 2026-08-30
- **Application baseline:** mobile `1.0.0+82`, .NET `9`, MySQL `8`
- **Schema-contract baseline:** `2026.08.30.1`
- **Scope:** source-level architecture and public-safe operating principles
- **Not a claim of universal activation:** country, provider, store, legal, and
  physical-device evidence still decide whether a capability is active

The implementation changes faster than this public repository. When this page
and executable evidence disagree, treat the page as stale, correct it, and do
not bend the implementation to preserve an attractive sentence.

## Words with precise meanings

KiloDrive uses two independent axes. Source maturity says what is represented in
the reviewed repository. Deployment state says what a named release, country,
and environment can truthfully offer.

| Source maturity | Meaning |
| --- | --- |
| Implemented | The named behavior exists in reviewed code/schema and has focused automated evidence |
| Incremental | The target design exists in named slices while older compatibility paths remain |
| Planned | A reviewed direction that must not be presented as shipped |

| Deployment state | Meaning |
| --- | --- |
| Configurable | The adapter or path exists, but approved deployment configuration or infrastructure is still required |
| Uncertified | Source or configuration exists, but the required real provider/device/runtime matrix has no approved evidence for this release |
| Certified | The real provider/device/runtime boundary passed the approved matrix for a named release, country, and environment |
| Active | The country feature policy permits the capability and its certified/configured runtime dependencies are healthy |
| Unavailable | The server or trusted platform contract cannot currently prove that the action is safe or truthful |

**Operational policy** is a cross-cutting control, not a maturity or deployment
state. It means people or automation must perform a named procedure and retain
its evidence.

Avoid “fully integrated,” “seamless,” “guaranteed,” “instant,” and “real time”
unless the surrounding sentence names the boundary, recovery behavior, and
evidence. “A SignalR hint normally appears within seconds and the client
reconciles from MySQL after reconnect” is useful. “Updates are seamless” is not.

## Thirteen rules that outrank screen convenience

### 1. One user intent survives the whole journey

Registration, booking, checkout, and administrative changes carry one typed
intent from review to commit. Do not derive role, country, organization choice,
currency, or payment destination again from an old preference halfway through
the flow. A user may change the intent through an explicit review action; the
new value then replaces the old value as one coherent object.

The current registration path applies this rule with an immutable intent that
contains role, country, contact method, driver account type, and rental-
organization choice. The API validates the same combinations. This prevents a
screen that says “Passenger” from silently creating a rental organization.

### 2. Authentication success and account mutation are different proofs

A valid bearer token proves a session, not necessarily recent control of the
account. Password, contact, social-link, passkey, 2FA, payout, and other
security-boundary changes use the endpoint's reviewed policy: recent
reauthentication and, where required, a separate 2FA step-up. Recent
authentication accepts either the current session's `auth_time` within the
ten-minute window or a generic, single-use proof bound to the user and tenant.
It is not action-bound and is not a reusable second access token. A 2FA step-up
proof is different: it is single-use and bound to the specific protected action.
Accounts without enrolled 2FA follow the endpoint's enrollment policy; selected
System Administrator mutations fail closed until 2FA is enrolled.

Social signup collisions do not become a dead end or an automatic email match.
The system preserves a short-lived protected pending-link intent, asks the user
to authenticate the existing account, shows the identities being connected,
and requires explicit confirmation. Provider tokens and pending-link material
do not belong in URLs, logs, screenshots, or diagnostic payloads.

### 3. The server owns authorization and lifecycle truth

The client may hide an action for clarity, but it cannot grant it. The API
revalidates identity, role, permission, tenant, country workspace, ownership,
membership, compliance, block/trust rules, expected version, and current state
inside the authoritative operation. A cached profile, local biometric result,
or old screen state is never permission.

### 4. A partial success remains visible

Required data and optional enrichment have independent states. If rental
vehicles load but the map provider fails, the vehicle results remain. If a
membership entitlement loads but the native store mapping does not, the plan
remains visible and only the unsupported purchase action is disabled.

Initial loading, successful empty, whole-screen failure, refresh failure, and
mutation failure are different states. A refresh failure preserves the last
good data with a visible stale/partial warning and last-sync context. It must
not replace useful content with an infinite spinner or a false empty state.

### 5. Every uncertain mutation is replay-safe

Ride, bid, chat, wallet, membership, voucher, rental, support, and security
mutations must use the appropriate combination of idempotency key, request hash,
expected version, unique reference, row lock, and provider reconciliation. A
lost response must not create a second economic effect or contradictory state.

Automatic transport retry is for safe reads unless the provider adapter owns a
stable idempotency key and can reconcile an unknown outcome before retrying.

### 6. Realtime is delivery, not truth

MySQL records the lifecycle. The outbox records the promise to distribute a
committed fact. SignalR and push make that fact arrive quickly. Clients merge by
a persisted monotonic entity version and perform a bounded authoritative resync
after reconnect, resume, version gaps, API recycle, or backplane loss.

Notifications should tell a user that something needs attention; they do not
substitute for an in-screen offer, chat message, trip state, safety prompt, or
support case. Important pre-trip rider/driver interactions may use an audible
notification according to user and platform policy, while durable state remains
the source of truth.

### 7. Location carries age, accuracy, purpose, and consent

A coordinate without freshness and accuracy is not live location. Matching,
approach tracking, route monitoring, queue leases, and replay each have a
different purpose and retention rule. Drivers entering the bidding hall receive
an explicit location readiness gate; the app must not show them as ready while
permission or fresh telemetry is missing.

During an active assignment/trip, approved native background behavior is
visible to the user and limited to the lifecycle that needs it. The server emits
a telemetry-gap safety signal only after the configured threshold and never
formats an uninitialized timestamp as a real date. Completion, cancellation,
or assignment removal stops the active service and expires the lease.

### 8. Safety prompts are neutral, recoverable, and auditable

Route deviation and requested route changes are related but not identical. A
route-deviation detector raises a confidence-bounded safety observation. A
route-alteration request is an explicit, versioned proposal that the affected
participant can accept or reject. Neither silently rewrites the trip.

Pickup confirmation is off by default for a rider unless a country rule
requires it. When enabled, the server issues a short-lived, single-use,
participant- and trip-bound PIN/QR challenge, stores protected digests, limits
attempts, rotates or cancels it with the lifecycle, and audits exceptional
override without logging the proof.

### 9. Money is exact, immutable, and reconcilable

Amounts are integer minor units with an ISO currency. User input is parsed once
from locale-aware decimal text into an exact integer. Wallet history explains
the customer-facing balance; balanced journals explain the accounting event.
Neither is optional for a money movement.

Provider success is not inferred from an HTTP timeout. The implemented wallet
top-up flow exposes durable `Pending`, `Completed`, `Failed`, and
`Needs attention` payment status, and reconciliation owns unknown outcomes.
Other payment products must adopt the same pattern before documentation calls
their recovery equivalent. Store price, product, base plan, offer,
term, entitlement, and acknowledgement must agree before purchase is presented
as available.

### 10. Country schema parity is not country readiness

A country cell can match the schema and still be unready for customers.
Activation also needs reviewed licence/plate rules, fare/tax/money policy,
banks and reference data, emergency/privacy ownership, provider support,
payments, retention, safety operations, fixtures, and end-to-end evidence.

Unknown country readiness fails closed for destructive or financial actions.
Marketing, app navigation, API feature gates, and support guidance should derive
from one versioned capability policy instead of making independent promises.

### 11. Feature claims come from the same readiness policy as the API

An optional product has one tenant/country feature record with owner,
legal/provider dependencies, readiness predicate, policy version, rollout,
kill switch, maintenance state, customer-facing availability, and rollback.
Routes, Flutter, Portal, Website, and public documentation must consume or be
checked against that vocabulary; none may invent availability from a local
Boolean. The registry and its consumers remain incremental, so each capability
row must name the surfaces that have actually migrated.

A signed, TTL-bounded last-known policy can preserve safe read-only presentation
offline. Unknown or expired policy is unavailable for purchase, money movement,
safety-sensitive activation, and other destructive actions. Schema presence,
navigation visibility, and marketing copy are never substitutes for readiness.

### 12. Operators work from outcomes, not raw entities

System Administration keeps entity search, but daily work is organized around
queues: pending verification, safety/SLA risk, financial mismatch, cashout,
provider failure, outbox lag, scheduled-ride risk, rental dispute, and support
next action. Each item needs an owner, age, severity, country, next action,
step-up requirement, correlation evidence, and audit trail.

Investigation presenters are typed and allow-listed. They show localized enum
names, exact money, administrator-local time, participant/vehicle snapshots,
safe metadata, and a copyable correlation ID. They do not expose raw JSON,
storage keys, internal UUIDs, tokens, or bare numeric permission masks.

### 13. “Done” includes recovery evidence

A feature is not done when its happy path works on one phone. The evidence must
cover validation, authorization, ownership, duplicate/lost responses, stale
versions, cancellation, offline/resume, process death, partial dependencies,
cleanup, accessibility, localization, and the real database/provider/native
boundary appropriate to its risk.

Tests must be hermetic by default: an ordinary test run cannot contact
production, a real provider, or a customer destination because a developer
happens to have credentials in the environment. Explicit certification jobs
cross those boundaries with non-user fixtures, allowlists, run IDs, cleanup,
and retained sanitized evidence.

## Changes incorporated in the current baseline

| Capability | Status | Doctrine impact | Remaining boundary |
| --- | --- | --- | --- |
| Typed registration intent and interrupted-signup restore | Implemented | One reviewed role/country/contact/organization intent drives password and social registration | Provider-specific signup still needs configured native credentials and device tests |
| Pending social-link recovery | Implemented/configurable | Email equality never silently links accounts; recent authentication and explicit confirmation complete the ceremony | Apple relay/hidden-email and every configured provider need runtime certification |
| Recent authentication and action-bound 2FA step-up | Implemented | Recent authentication accepts a fresh session or one generic user/tenant-bound proof; enrolled 2FA uses a separate single-use action proof | Multi-node deployment must share the protected proof store/key ring and retain endpoint-specific enrollment policy tests |
| Account-bound profile/contact/avatar state | Implemented/incremental | Profile changes invalidate the right caches; upload success updates revisioned presentation state | Older screens still being migrated must not retain direct untyped API state |
| Profile-governance changes | Implemented/incremental | A profile photograph is revisioned media; a legal-name or identity change is reviewed evidence, not an ordinary local preference | Every affected client still needs typed partial states, review visibility, and account-bound cache tests |
| First-ride rider/driver guide and compact primary workflows | Implemented mobile behavior | Teach complex negotiation and safety once, then keep time-sensitive screens concise | Localization, accessibility, and small-device matrices remain release gates |
| Driver bidding-hall location readiness | Implemented/incremental | Online/available presentation requires permission and fresh permitted telemetry | Background availability remains platform/store-policy dependent |
| Recent ride-location suggestions | Implemented | Reuse is account-bound and purpose-limited; provider search remains authoritative for new places | Retention and country privacy policy govern history length |
| Route alteration lifecycle and durable event | Implemented | Proposed destination changes are versioned, accepted/rejected, audited, and distributed after commit | Fare/safety/provider recomputation must stay consistent for every country product |
| Assisted-rider profile and matching | Implemented backend foundation with partial Flutter; disabled/uncertified | Opt-in trip needs, driver capability and bounded backend snapshots are separate from diagnosis or inferred disability | Assigned-trip/offer presentation, caregiver delivery, policy fail-closed behavior, Portal, country/legal and field evidence remain incomplete |
| Immediate wallet fare splitting | Implemented source candidate; unavailable/uncertified | Invitations, allocation, holds, settlement and cancellation release belong to the trip lifecycle, not informal later transfers | Canonical bootstrap parity, mandatory version/stable retry, renewed-consent/fallback behavior, owner/Portal operations, reversal and country/provider certification remain incomplete |
| Automated payout control plane | Implemented backend foundation; dormant/uncertified | Protected destinations, durable initiation/reconciliation, provider outcomes and reversal accounting exist behind policy | No supported certification activation, named provider proof, tenant-safe callback certification or complete operator lifecycle; “instant” remains unavailable |
| Rider-controlled pickup confirmation | Implemented/configurable country override | Default off, explicit rider preference, protected one-time PIN/QR and audited emergency override; the standalone geofence helper is not an enforced start proof | Store/device accessibility, two-device field evidence, and any future location-gate policy remain required |
| Canonical support contract | Implemented/incremental | Received → Reviewing → Waiting for information → Resolved is shared vocabulary; legacy values map without lying | Queue staffing, assignee/SLA ownership, closure/reopen evidence are operational |
| Typed System Admin trip evidence presentation | Implemented/incremental | Investigation views prefer safe structured sections and partial states over raw payloads | Large legacy admin screens remain migration debt |
| Hermetic test boundary and form fuzz regression corpus | Implemented quality control | Default test runs cannot escape to real services; generated failures become deterministic regression fixtures | Provider/native/load certification remains separate and explicit |

## Known gaps and deliberately unfinished work

This table is as important as the implemented list. It prevents documentation
and product copy from outrunning evidence.

| Area | Honest current state | Do not claim yet | Evidence or work needed |
| --- | --- | --- | --- |
| Provider canaries | Transports and sanitized status paths are configurable; evidence support differs by provider | Provider acceptance means delivery, or every push/SMS/WhatsApp/email/voice/media path is certified | Dedicated non-user destinations, authenticated delivery/inbound producers, scheduled success/failure/maintenance, reply/egress cleanup and alert recovery |
| iOS runtime | Source, entitlements, simulator-compatible code, and artifact gates exist | Background location, CallKit, APNs, StoreKit, biometrics, and killed-state recovery work on every supported iPhone/iPad | Approved simulator plus physical-device matrix using signed release artifacts |
| Store billing | API/native mapping and lifecycle foundations exist | Every displayed paid term is purchasable in every active country | Exact active product/base-plan/offer and localized-price match, licensed-store device, acknowledgement/refund/restore certification |
| Rental marketplace | Browse, inventory, quote, organization/fleet, booking/evidence and lifecycle foundations are incremental | Rentals are active or insured in a country merely because tables/routes exist | Versioned country activation, provider/deposit/protection/legal evidence and renter/owner end-to-end tests |
| Family and supervised travel | Delegated profiles, roles, notifications, tracking scope, and supervised conversation foundations exist | A general family member row is a legally approved teen product | Country age/guardian policy, consent/revocation, retention, three-client and safeguarding review |
| Support operations | Typed cases, evidence, conversation, status and next-action foundations exist | A named response SLA is met everywhere | Staff ownership, escalation channels, breach monitoring, exercises and retained SLA measurements |
| Horizontal scale and recovery | Stateless API direction, Valkey/backplane, outbox and capacity harnesses exist | Unlimited scale, tested failover, or a measured RPO/RTO for every cell | Production-shaped staging ramps/soak, reconnect storms, PITR/restore/key recovery, database/Valkey/backplane drills |
| Flutter feature boundaries | Repository/AsyncNotifier slices and static gates are incremental | Every large screen is fully typed or independently rebuilding | Continue slice-by-slice migration; remove direct client calls and dynamic maps with race/frame tests |
| Country operations | Schema and country gates support multiple cells | Schema parity means legal/provider/product readiness | Owned country launch dossier and positive lifecycle evidence for every enabled product |
| Payment and payout automation | Exact ledger, holds, status and reconciliation foundations exist | Cashout is instant or every provider crash point is certified | Test-provider matrix, signed webhooks, reversal/return handling, destination protection and zero-unreconciled-money gate |
| Safety detection | Route/telemetry signals and SafetyCase foundations exist | GPS alone proves misconduct or replaces emergency services | Noisy-trace validation, fairness/legal review, responder tabletop, appeal and retention evidence |
| Assisted-rider experience | Backend profile, driver attestation, bounded snapshot and eligibility checks exist with partial Flutter surfaces; production seed is disabled | Caregiver notifications are delivered, the driver sees assistance through the full assigned-trip lifecycle, Portal parity exists, or country activation is approved | Fail-closed signed policy/kill-switch checks, assigned-trip/offer presentation, caregiver dispatcher, Portal, positive two-device accessibility, retention and country/legal evidence |
| Fare splitting | API/Flutter immediate-wallet candidate has invitations, allocations, holds, settlement and cancellation release; canonical bootstrap and full lifecycle are incomplete | Fallback protects every insufficient-funds case, fare changes renew payer consent, version/idempotency are mandatory, or reversal/scheduled/country deployment is certified | Canonical `schema.sql` parity, required versions and stable retries, renewed consent, expiry/audit/reconciliation queues, owner/Portal UI, reversal integration and country/PSP certification |
| Automated/instant payout | Backend adapter, protected destination, durable initiation/reconciliation, outcome accounting and language gates exist but are dormant | A generic adapter, local destination confirmation or approval is provider ownership verification, operational activation, or instant settlement | Supported dual-controlled certification command, tenant/country-safe callback proof, named provider sandbox/crash/replay matrix, reconciliation and measured SLA |

## Wording rules for product and engineering documents

Prefer statements that name ownership and failure behavior.

| Avoid | Prefer |
| --- | --- |
| “Realtime data is guaranteed.” | “SignalR provides a low-latency hint; the client reconciles durable state after reconnect.” |
| “The user is verified.” | “The named evidence was approved at the displayed time; current eligibility is revalidated for the action.” |
| “The payment failed.” after a timeout | “The outcome is unknown and reconciliation is in progress.” |
| “The country is supported.” | “The named capabilities are active under the reviewed country policy.” |
| “Location is live.” | “The last accepted sample is within the displayed freshness and accuracy window.” |
| “The driver viewed the ride.” | “An explicit, expiring visibility lease confirms that the ride card was visible.” |
| “No records exist.” after a failed load | “Records could not be loaded; the last successful result remains visible.” |
| “Unknown status: 17.” | “Unknown or unavailable,” plus a sanitized diagnostic |
| “Instant payout.” | The measured provider processing range, until an instant SLA is certified |
| “Guaranteed ride.” | The exact reservation state and support/compensation policy |

Human wording also matters. Explain the reason before the mechanism when a
reader is new. Replace generic claims with a concrete consequence. Admit when a
path is incremental. A young engineer should leave a chapter knowing what can
break, what evidence to trust, and what not to “fix” with a shortcut.

## Definition of done

Before a planned or incremental capability becomes active in a named deployment,
its owner can
answer yes to the applicable questions:

1. Is there one typed contract and one authoritative owner for the state?
2. Are authentication, permission, ownership, tenant, and country rules tested
   negatively as well as positively?
3. Are mutations versioned/idempotent, and can unknown outcomes reconcile?
4. Are money entries exact, balanced, immutable, and reconcilable?
5. Do loading, empty, partial, stale, offline, forbidden, conflict, rate-limit,
   and server-error states tell the truth?
6. Do realtime disconnect, provider outage, API recycle, and process death
   recover from durable state?
7. Are location, documents, communications, and identity data minimized,
   purpose-bound, retained, and deleted under the country policy?
8. Does the mobile/portal UI pass localization, accessibility, safe-inset,
   keyboard, narrow-screen, and role/workspace tests?
9. Has the real MySQL/native/provider boundary passed the appropriate approved
   certification rather than only a mock?
10. Are health, bounded metrics, sanitized correlation evidence, alarm, owner,
    rollback, and recovery runbook ready?
11. Do public claims and in-app availability derive from the same reviewed
    capability policy?
12. Can fixtures be closed, forced offline, anonymized, and reconciled without
    touching unrelated users?

## Related reading

- [Capability status and evidence](../architecture/capability-status.md)
- [Mobile architecture](../architecture/mobile.md)
- [Identity and access](../security/identity-and-access.md)
- [Realtime and events](../architecture/realtime-and-events.md)
- [Rider and driver safety](../architecture/rider-driver-safety.md)
- [Financial systems](../architecture/financial-systems.md)
- [Jurisdictional compliance](../architecture/jurisdictional-compliance.md)
- [Testing and verification](../quality/testing-and-verification.md)
- [Runbook index](../runbooks/README.md)
