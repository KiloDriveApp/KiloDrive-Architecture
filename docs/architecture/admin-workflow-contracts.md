# System Admin workflow contracts and evidence map

This is a public-safe map of **operator outcomes**, not an endpoint inventory or
permission specification. It complements the [System Admin mobile app](system-admin-mobile-app.md)
and the source repository's more detailed migration ledger. The 2026-10-06
committed consumer-196/Admin-33 checkpoint contains implemented and incomplete slices; this page does not
certify a signed build, a production configuration, or every operation in a
domain. The consumer app has no operative System Admin workspace.

## How to read a row

| Term | Meaning |
| --- | --- |
| Source working | A scoped UI and API path exist and have at least local test evidence. Native/provider behavior may remain untested. |
| Partial | A useful investigation or narrow action exists, but some records, actions, or recovery contracts are absent. |
| Deferred | The app deliberately withholds an action until the authority, permission or recovery boundary is reviewable. |
| Certified | A named signed artifact has passed the role, country, tenant, failure, process-death and device/provider cases for this exact workflow. No row below claims this state. |

A capability visible in navigation is presentation eligibility only. Every
detail read and mutation must independently check the current session, action
grant, country, acting tenant and target record. An ordinary failure must not
fall back to a wider administrative query. The audit record identifies the
actor, affected party, action, outcome and correlation without copying private
material into a general-purpose log.

## Operator workflow map

| Outcome the operator needs | Current source surface | Authority and expected audit/result | Maturity and evidence still needed |
| --- | --- | --- | --- |
| Enter an authorized workspace | Sign-in and country/tenant selector, then capabilities and home | Central identity and API grants determine choices; scope changes discard stale data | Source working; signed role and cross-country denial matrix pending |
| See what needs attention | Dashboard and My Work queues with freshness | API aggregates from the selected country; an unavailable metric is labelled unavailable | Partial; authenticated non-empty data, drill-down and device evidence pending |
| Find an individual | Searchable People lists and dossier | API resolves person/role within current tenant and country; access is logged where policy requires | Source working; limited-role and pagination/device evidence pending |
| Inspect account facts | User details, security, vehicles, financials, readiness, rides and activity tabs | Control identity plus country operational records; user-local time and currency-aware amounts | Partial; individual section permissions, error/empty states and full record links need per-section review |
| Correct contact or status | Confirmed People actions | Identity owner validates conflict, current state and authorization; mutation audit records before/after meaning | Narrow source actions; concurrency, denial, response-loss and signed-device proof pending |
| Initiate password recovery | Reasoned recovery action and status receipt | Identity service issues the existing expiring ceremony; admin never sets or sees a plaintext password | Source working for the reviewed path; delivery and account-owner completion need native/provider evidence |
| Revoke a session or restrict an installation | Security and Devices workspaces | Central session/device authority revokes access; audit records target and reason | Narrow source actions; cross-device and process-death checks pending |
| Review driver/vehicle readiness | Readiness dossier, protected identity/vehicle document viewers, approval/rejection and replacement workflow | Country requirement policy, current evidence and API checks determine eligibility; document decisions and final approval are separate audited actions | Source working for implemented review paths; exact signed-device, denial and multichannel delivery evidence remains workflow-specific |
| Manage membership catalog and benefits | Dedicated membership center, plan cards, active-member drill-down, plan creation/editing and term-price/benefit editor | Catalog revision, country pricing, native product setup and effective entitlement determine availability | Source working for reviewed edits; new paid plans remain inactive drafts until required store setup; store/provider and cross-client propagation require exact evidence |
| Grant or extend an individual's plan | Dossier financial/actions pages and membership workflows | Current entitlement, permitted grant, expiry validation and stable mutation identity; audit and fresh read-back | Source working for reviewed actions; interrupted response, limited-role and signed-device form checks remain separate |
| Investigate a trip | Trip/ride detail, timeline, retained replay and call metadata | Country trip record is authoritative; communication evidence has separate access/retention | Partial; missing/expired evidence, lifecycle actions and device presentation need review |
| Inspect money | Wallet, transaction, payment, top-up, cashout and dispute evidence | Country ledger and provider reconciliation establish financial truth; every amount has a currency | Partial; no UI value may be inferred from a provider callback alone |
| Decide a pending bank transfer or cashout | Reviewed financial decision screens | Conditional API mutation with current revision and stable operation identity; ledger and audit read-back | Narrow source actions; duplicate, interruption, provider and database certification pending |
| Inspect notification delivery | Notification history and attempt evidence | Outbox/attempt records distinguish queued, provider-accepted, failed and skipped | Partial; provider acceptance is not device receipt or human read |
| Send a permitted notification | Guarded compose or exact-installation template flow | API rechecks recipient/channel, stages an audited operation and worker delivery | Partial and deployment-gated; signed App Check/FCM and account-switch proof pending |
| Receive an administrator alert | Opt-in inbox with permitted target navigation | Admin alert record, current grants and selected scope decide what can open | Source working for narrow reads; push, terminated-launch and email certification pending |
| Read an audit event or export its PDF | Scoped history, readable detail, one-record PDF | Owning audit store supplies actor, affected subject, action and timestamps | Source working for reviewed domain history; other security histories remain separate |
| Resolve support work | Ticket queue, detail and reviewed lifecycle actions | Country support case version, owner and audit determine the result | Partial; attachments and external channels remain incomplete |
| Recover outbox work | Queue/history/detail with guarded retry or dismissal | Outbox worker state, not a second domain command, controls delivery retry | Narrow source actions; crash, retention and operational-alert evidence pending |
| Change reference or policy data | Selected bank/plan and governance views | Domain owner validates revision, scope and audit | Partial; many governance mutations are read-only or unavailable in mobile |

The [build-196 amendment](release-1.0.0-196.md) corrects the older blanket
claim that document viewers and membership editors were unavailable. It also
records API policy gates separately: single-reviewer approval, review
second-factor verification, sensitive-action verification and viewer lease.
Disabling an additional policy does not disable capability, scope, validation,
protected media authorization or audit. An operation remains unverified on a
specific signed device until its retained evidence establishes that journey.

The [dated source migration checkpoint](system-admin-mobile-app.md#current-limits-and-evidence-needed)
is more useful than a single percentage. The source repository's
`src/client/system_admin/MIGRATION_PARITY.md` and operation ledger must be
regenerated after new work before their counts are quoted. A generated route
match can miss a dynamic client path, while a matching route can lack an actual
operator result; neither proves parity by itself.

## Contract for one consequential action

For each supported mutation, its owner records these facts in the restricted
implementation ledger and its public-safe summary here:

1. **Intent:** actor, target type, selected scope and the human consequence.
2. **Authority:** which server record owns the state; required role/capability
   category; whether recent authentication or second-factor step-up is needed.
3. **Precondition:** the resource revision or other condition captured when the
   operator reviewed it, plus validation and identity-conflict behavior.
4. **Attempt identity:** a stable idempotency key and frozen payload, retained
   until the original outcome is known. Private proof material is never stored
   in the pending-operation journal.
5. **Outcome:** success, rejected/no mutation, conflict, still processing or
   unknown. A lost response does not permit a fresh mutation key.
6. **Read-back:** a scoped status/result lookup and fresh target read; an audit
   reference and support-safe code when human review is needed.
7. **Side effects:** notifications or provider calls staged after the owning
   transaction through an outbox, with independent delivery status.
8. **Verification:** allowed/denied actor, wrong country/tenant, duplicate key,
   stale revision, interrupted response, process restart, and signed-device
   presentation on the same release candidate.

Use [critical-journey diagrams](../diagrams/admin-critical-journeys.md) for
examples and [testing and verification](../quality/testing-and-verification.md)
for what each test level actually proves. This public file deliberately omits
permission bit values, private API payloads, customer records and defensive
thresholds.

## Source pointers for reviewers

The source repository's `src/client/system_admin/lib/features/` contains the
`people`, `admin_trips`, `finance`, `cashout_decisions`, `alerts`, `notifications`,
`audit`, `support`, `devices`, `outbox_recovery`, `driver_review`, `verification`,
`governance` and `reference_data` presentation slices. `lib/admin_api.dart`
owns the scoped client boundary. The API's `Features/Admin/`, Admin controllers,
identity services, notification workers and canonical OpenAPI contract provide
the server side. `MIGRATION_PARITY.md` and the dated operation ledger record
individual dispositions. These are navigation aids into the source checkout;
they are not immutable links or evidence that every directory is feature
complete.
