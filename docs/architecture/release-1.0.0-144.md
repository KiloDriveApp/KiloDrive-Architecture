# Release architecture baseline: KiloDrive 1.0.0 build 144

- **Status:** Source baseline reviewed; deployment and external certification remain separate
- **Date:** 2026-09-23
- **Application source:** `KiloDriveApp/KiloDrive` build `1.0.0+144`
- **Schema contract:** `2026.09.23.2`
- **Reviewed API:** `/api/v1`, 826 paths and 925 operations
- **OpenAPI SHA-256:** `34f98ce9a71b4a9130394f15c9d8647920c73551cc9510f27de18ebed49c7749`
- **Mobile locales:** English, Spanish, French, Japanese, Simplified Chinese, Traditional Chinese

This chapter records the public-safe architecture represented by the build 144
source corpus. It is not a claim that every country, provider, product mapping,
webhook, device boundary, or optional feature was active and healthy at the same
time. Source implementation, automated tests, deployment configuration,
provider certification, store review, physical-device evidence, and current
production health are intentionally separate facts.

## What changed since the build 130 baseline

The release family between builds 130 and 144 concentrated on making broad
feature coverage operate through a smaller number of authoritative boundaries.
The largest changes are:

1. a database-backed foreign-exchange authority replaced independent settings
   and ad hoc conversion paths;
2. wallet top-up, payout and membership flows gained stronger unknown-outcome
   recovery and clearer customer states;
3. native-store membership changes became explicit lifecycle records rather
   than transient client decisions;
4. driver navigation moved from a flat list toward task workspaces with typed
   child destinations;
5. rider Home refuses to start a second request while an active journey exists;
6. vehicle eligibility, driver readiness and bid acceptance use the same
   server-side gate;
7. System Administration gained operational readiness, FX, billing-recovery
   and investigation surfaces without exposing secrets or provider tokens;
8. the public website gained responsive, searchable manual pages, architecture
   attribution, sitemap separation and stricter indexability rules; and
9. release metadata, changelog records and documentation facts are generated or
   checked against authoritative source values.

## Authoritative workspace model

The mobile shell represents destinations as a parent workspace plus a typed
child page. A destination is no longer inferred from several strings that all
collapse to the same parent route.

The Driver surface keeps five persistent outcomes in reach: Home, Work, Active
journey, Earnings and Readiness. Secondary work is grouped under Work, Money,
Readiness and vehicle, Reputation and growth, Tools, Help and safety, and
Account and settings. The selected child, expanded group and workspace are
device preferences only; server permissions and the current role remain
authoritative.

The Rider surface treats an assigned or active trip as the primary journey.
Opening Hail a Cab while such a trip exists redirects to, or presents, the
active journey rather than rendering a second request form. A failed request
submission preserves the rider's draft and returns a specific safe recovery
action instead of clearing the form or encouraging a blind retry.

Every workspace follows the same presentation contract:

- initial content uses a bounded skeleton;
- refresh preserves last-good data;
- an optional-section failure cannot erase the authoritative core;
- successful empty state is distinct from load failure;
- unknown enum or mutation state is neutral and disables unsafe actions;
- interrupted mutations retain their operation ID, idempotency key and original
  revision; and
- a blocked action exposes one server-derived next action and support reference.

## Financial and foreign-exchange authority

The control database owns currency definitions, versioned FX evidence, pair
state, approved rate lifecycle and provider-fee policy. Country cells own
customer quotes, immutable transaction snapshots, payments, wallet postings,
reconciliation evidence and review cases.

An FX-dependent checkout cannot start merely because a numeric rate exists. It
requires active country/currency policy, a reviewed and fresh effective rate,
the correct rate direction, rounding policy, provider settlement currency,
provider-fee policy and a compatible product or payment mapping. Every accepted
quote snapshots the exact version and evidence used before provider I/O. Refund,
dispute, chargeback, receipt and reconciliation read that snapshot; they do not
reconstruct history using today's rate.

Administrative rate management is a maker-checker lifecycle:

```text
Draft -> Pending approval -> Scheduled or Active -> Superseded/Suspended
```

Maker and approver are distinct. Transitions require capability, recent
authentication, action-bound step-up where configured, current revision,
idempotency and a reason. Historical active rows are never edited or silently
reactivated. A rollback is a new reviewed version.

## PayPal and wallet operation recovery

PayPal checkout for a local-currency wallet presents the provider charge in a
supported settlement currency and the authoritative wallet credit in the
wallet currency. The quote separates source amount, provider fee, provider
total, destination amount, conversion evidence and expiry.

The browser return is only a navigation hint. The app matches a safe operation
reference to its encrypted account-scoped journal and asks the API for status.
Provider query values and client callbacks do not prove capture. The application
distinguishes:

- confirmed completion;
- deterministic provider rejection;
- customer cancellation;
- pending provider processing;
- outcome unknown after an interrupted response; and
- manual review when automated reconciliation cannot establish truth.

A deterministic provider 4xx before a remote commit becomes a failed checkout,
not a permanent “check outcome” case. A timeout after possible remote success
does the opposite: it retains the original operation and reconciles before any
new attempt. Only confirmed completion clears the entered amount and refreshes
wallet balance and history.

Cashout requests use the same evidence discipline. Available and held balances,
payout-method ownership, plan limits, cooldown/fraud decisions, ledger posting,
provider outcome and compensating reversal remain connected by stable
references. Read-only reconciliation may open an exception; it never repairs
money by editing immutable rows.

## Membership lifecycle and store authority

Free/trial, wallet purchase, native purchase, renewal, retry, grace, hold,
cancellation, expiry, upgrade, downgrade, refund, dispute, revocation and
restoration are reviewed events in one membership state machine.

`PendingMembershipChange` records a future or unresolved transition with target
plan, source/provider, effective date, revision, cancellation state and audit.
An immediate upgrade records its price/proration evidence. A deferred downgrade
keeps current paid access through the effective date. Provider cancellation does
not mean immediate access loss unless verified lifecycle evidence says so.

StoreKit and Google Play product discovery provide the customer-facing price
and currency. KiloDrive product mappings bind reviewed plan/term/product
identity, but the app does not invent a missing storefront price. Apple Server
API/Notifications V2 and Google `subscriptionsv2.get`/RTDN drive independent
history recovery. Notifications are invalidation signals; verified provider
history and the country-cell state machine are authority.

## Driver readiness and vehicle consistency

Identity, driver profile, reviewed documents, approved vehicle, membership
eligibility, payout readiness and training/safety acknowledgment form one
server-derived activation checklist. Vehicle list, vehicle detail, My Status,
available offers, bid placement and acceptance consume the same eligibility
service. A client-visible “verified” label can no longer independently grant
bidding authority.

Each blocked checklist item returns a stable reason, evidence expectation,
review guidance, support path and one next action. Unknown state fails closed.
The client may retain last-good display data during refresh but cannot use it to
authorize bidding or going online.

## Notifications and durable user history

The country-cell notification record is the durable user inbox projection.
Push, email, SMS and WhatsApp are delivery channels, not the business record.
Provider attempts are append-only and payload-minimized. Account and safety
messages remain mandatory; category preferences govern optional delivery.

Device-token ownership follows the authenticated installation. A token moved
between test or real accounts is rebound atomically so stale ownership cannot
route a private event to the previous account. Rejection of an old token is an
expected cleanup condition; alerting focuses on a newly registered token that
is immediately rejected.

## System Administration

The mobile System Administrator surface is organized around work rather than
raw tables. Current boundaries include driver readiness, users, documents,
vehicles, money exceptions, cashouts, top-up cards, transaction resolution,
FX management, provider health, outbox recovery, audit search and feature
readiness.

The readiness dashboard keeps four evidence classes separate:

1. source and automated-test status;
2. provider/store certification;
3. operational configuration; and
4. current production health.

A green feature-policy flag is therefore never labelled “production
certified.” Each check exposes source, last success, freshness, owner, safe
evidence reference and one remediation action. Secrets, purchase tokens,
private keys, raw documents and personal data are excluded.

## Public website and manuals

Driver, Rider and Rental Entity manuals are available as responsive HTML pages
with a table of contents, scoped search, illustrations and downloadable source
artifacts. The corporate navigation and footer expose the manual catalogue and
the public architecture repository.

Search discovery separates page, tool, blog, manual and changelog sitemaps.
Only HTTP 200, self-canonical and indexable URLs belong in those feeds. Fallback
translations, empty taxonomies, duplicate URLs and `noindex` pages are excluded.
Both GET and HEAD are supported for public robots and sitemap resources so
crawlers can validate them without a false 404. The API hostname publishes a
robots policy that disallows crawling rather than advertising API endpoints as
web content.

## Runtime composition

KiloDrive remains one modular-monolith repository and one shared contract. It
can run as a compatibility `Combined` host or as composition profiles:
`PublicApi`, `RealtimeGateway`, one-country `CellWorker`, `MediaWorker` and
`ReportingWorker`. Profiles control registered endpoints, workers and providers;
they do not split a trip, wallet or settlement transaction across services.

Workers that touch country state bind exactly one provisioned country cell and
fail startup on missing or conflicting configuration. Global control-plane
schedulers have one explicit owner. Every profile exposes liveness, profile and
readiness probes appropriate to its owned dependencies.

## Contract and database facts

The canonical REST surface uses native `/api/v1/...` route selectors. The
compatibility `/api/...` alias is telemetry-observed and scheduled for removal
on 10 February 2027; middleware does not rewrite paths. Doubled version and
malformed routes fail normally.

Schema changes remain reviewed, rerunnable MySQL scripts. EF migrations and
runtime EF seeding are not part of the lifecycle. The control database owns
global identity and configuration; each country cell owns its complete
transactional mobility and money graph. Dedicated reporting storage receives
privacy-safe facts and is not the transactional control database.

## Verification represented by the corpus

The source corpus includes deterministic unit, contract, architecture, widget,
MySQL, failure-injection and Codemagic-equivalent gates. A bounded two-device
Android run covered installation, role login, driver navigation, membership
routing, financial back navigation, readiness presentation and resume
restoration on the build-143 candidate immediately before build 144.

That evidence did not execute every provider or trip lifecycle. Store
renewal/refund, PayPal capture/refund/dispute, physical GPS journeys, RTC network
handoff, APNs, multi-node SignalR failure and production webhooks require their
own named sandbox or production-safe certification. They remain “not run” when
the evidence does not show otherwise.

## Related architecture decisions and runbooks

- [Native API v1 routing and generated contracts](../adr/012-native-api-v1-and-generated-contract.md)
- [Runtime profile composition](../adr/013-runtime-profile-composition.md)
- [Authoritative foreign exchange](../adr/014-authoritative-foreign-exchange.md)
- [Account, membership and notification authority](../adr/015-account-membership-notification-authority.md)
- [Foreign-exchange readiness](../runbooks/foreign-exchange-readiness.md)
- [Store entitlement reconciliation](../runbooks/store-entitlement-reconciliation.md)
- [Runtime profile rollout](../runbooks/runtime-profile-rollout.md)
- [Payment and wallet operation recovery](../runbooks/payment-operation-recovery.md)
