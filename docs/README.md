# Documentation Guide

This guide is the front door to the KiloDrive documentation set. You do not
need to read every file before making a useful contribution. You do need to
understand the ownership and failure boundaries touched by your change.

Before describing a new product as ready, read the
[product and operational doctrine](governance/product-and-operational-doctrine.md).
It defines separate source-maturity and deployment-state language and records
gaps explicitly.

Changes that cross public routing, client state, realtime recovery, or load
boundaries should also use the
[runtime-boundary certification guide](architecture/runtime-boundaries-and-certification.md).
It joins controls that are easy to review separately but dangerous to operate
as unrelated concerns.

## Choose a path

### I am new to backend systems

Start with the [system context](architecture/system-context.md), then read the
[API architecture](architecture/api.md) and
[realtime/event model](architecture/realtime-and-events.md). After that, follow
[a request from phone to durable state](tutorials/follow-a-request.md).

Pay particular attention to the difference between:

- a command being accepted;
- a database transaction committing;
- a realtime message being observed;
- an external provider accepting work; and
- a user seeing the result.

Those are separate moments. Treating them as one moment is a frequent cause of
duplicate commands, stale screens, and misleading error messages.

### I work on mobile

Read [mobile architecture](architecture/mobile.md),
[API contracts](architecture/api.md), and
[realtime/event processing](architecture/realtime-and-events.md). Then read the
[mobile release runbook](runbooks/mobile-release.md).

Mobile engineers should also understand the backend idempotency contract. A
retry button, reconnect loop, or offline queue can repeat a command long after
the first response was lost. The UI cannot make an unsafe endpoint safe by
being careful.

Before deciding that a feature is covered, read
[testing and verification](quality/testing-and-verification.md). It explains
which behavior belongs in unit, provider, widget, integration, native artifact,
and physical-device tests.

For active-trip behavior, continue with the
[active-trip location and privacy runbook](runbooks/active-trip-location-and-privacy.md).
For store releases, distinguish source/widget evidence from signed Play/StoreKit
device certification as described in the
[mobile release runbook](runbooks/mobile-release.md).

### I work on identity, onboarding, or social authentication

Read [identity and access](security/identity-and-access.md),
[mobile architecture](architecture/mobile.md), and the
[authentication/session runbook](runbooks/authentication-session.md). Then read
the registration, recent-authentication, social-link, projection, and
account-switch rules in the
[product and operational doctrine](governance/product-and-operational-doctrine.md).

Do not treat provider email equality, a local biometric result, or a restored
workspace preference as account authority. Preserve one registration intent
and require a server proof for security-boundary changes.

### I work on the Portal or corporate website

Read [Portal and website architecture](architecture/portal-and-website.md),
[API contracts](architecture/api.md), [identity and access](security/identity-and-access.md),
and the [Portal/website release runbook](runbooks/portal-website-release.md).

Browser rendering is not allowed to invent authorization. Views must not bind
directly to unvalidated `JsonElement` or raw JSON. Typed view models,
anti-forgery, permission-driven navigation,
security headers, localized display, safe Problem Details, and partial states
are part of the feature—not decorative cleanup.

### I work on data or money

Read [tenancy and country cells](architecture/tenancy-and-country-cells.md),
[database architecture](database/README.md), and
[financial systems](architecture/financial-systems.md). Continue with the
[wallet reconciliation runbook](runbooks/wallet-reconciliation.md).

Do not begin with table names. Begin with invariants: debits equal credits,
held funds are not spendable, a provider reference is unique, and one financial
transaction never straddles two country cells.

Use the financial invariant and real-MySQL requirements in
[testing and verification](quality/testing-and-verification.md); controller
coverage alone is not evidence of correct settlement.

### I work on the rental marketplace

Read [rental marketplace architecture](architecture/rental-marketplace.md),
[financial systems](architecture/financial-systems.md),
[documents, media, and voice](architecture/documents-media-voice.md), and
[tenancy and country cells](architecture/tenancy-and-country-cells.md). A rental
is not ordinary CRUD: inventory, payment authorization, immutable policy,
condition evidence, deposit handling, and settlement must move together.
Use the [rental booking recovery runbook](runbooks/rental-booking-recovery.md)
before changing a lifecycle or attempting operational repair.

### I work on providers, messaging, maps, payments, or media

Start with [provider boundaries](integrations/providers.md), then read the
appropriate [AWS integration chapter](aws/README.md),
[observability](architecture/observability.md), and
[provider outage runbook](runbooks/provider-outage.md).

An adapter plus a fake-provider test certifies KiloDrive's local behavior, not
the external provider. Live certification uses dedicated non-user destinations,
least-privilege credentials, maintenance controls, alerts, cleanup, and
sanitized evidence.

### I work on System Administration or support operations

Read [System Administration architecture](architecture/system-administration.md),
[Portal and website architecture](architecture/portal-and-website.md),
[capability status](architecture/capability-status.md),
[identity and access](security/identity-and-access.md), and the
[support/dispute runbook](runbooks/support-dispute-cases.md).

Prefer permission- and country-scoped work queues over raw entity menus. Keep
the selected investigation stable while deltas load, require recent proof for
security mutations, and present allow-listed metadata rather than payloads or
internal identifiers.

### I am on call

Read the [runbook index](runbooks/README.md) before an incident. The index
explains severity, evidence handling, safe rollback, and how to separate a
customer-facing symptom from its underlying dependency.

During an incident, use the narrowest matching runbook. Do not copy commands
from a public document into production. Exact targets, thresholds, and access
procedures live in restricted operational material.

### I work on performance or capacity

Start with [scaling and capacity planning](architecture/scaling-and-capacity.md),
then read [observability](architecture/observability.md),
[realtime and events](architecture/realtime-and-events.md), and the component
chapter for the workload under test. Capacity is recorded as a workload and an
operating envelope—not as one unsupported “maximum users” number.

Use dedicated fixtures and controlled ramps. Measure local stage time,
provider time, database waits, queue lag, saturation, errors, and recovery
together. Do not disable production safeguards merely to obtain a larger test
number.

### I review security or privacy

Begin with [threat boundaries](security/threat-boundaries.md), then read
[identity and access](security/identity-and-access.md),
[application security](security/application-security.md), and
[privacy and data protection](security/privacy-and-data-protection.md).

The best security review follows data from collection to deletion. Checking the
login endpoint alone misses object storage, logs, analytics, backups, support
tools, and country-cell projections.

### I work on rider or driver safety

Begin with [rider and driver safety](architecture/rider-driver-safety.md), then
read [geospatial processing](architecture/geospatial.md),
[documents, media, and voice](architecture/documents-media-voice.md), and the
[security incident runbook](runbooks/security-incident.md).

Safety is an end-to-end property. Matching eligibility, pre-trip confirmation,
communications, route signals, emergency actions, evidence custody, human case
ownership, and post-trip support must agree. A visible SOS button cannot repair
an unsafe assignment or an unstaffed escalation path.

### I work on a country launch or compliance change

Start with [jurisdictional compliance](architecture/jurisdictional-compliance.md),
then read [tenancy and country cells](architecture/tenancy-and-country-cells.md),
the [country activation runbook](runbooks/country-activation.md), and
[privacy and data protection](security/privacy-and-data-protection.md).

Code can enforce an approved country rule; it cannot interpret law or approve a
launch. Keep authoritative sources, applicability analysis, legal and domain
owners, effective dates, tests, deployment evidence, exceptions, and rollback
in the governed country dossier.

## How the documentation is organized

| Directory | Purpose |
| --- | --- |
| [`architecture/`](architecture/README.md) | Component design, request flow, data ownership, realtime, geospatial, money, mobile, System Administration, and hosting |
| [`database/`](database/README.md) | MySQL control/cell model, schema lifecycle, ownership, retention, and fingerprinting |
| [`aws/`](aws/README.md) | Public-safe cloud integration patterns for storage, messaging, eventing, monitoring, IAM, and media |
| [`security/`](security/README.md) | Authentication, authorization, threat boundaries, privacy, redaction, and incident prevention |
| [`runbooks/`](runbooks/README.md) | Trigger-oriented diagnosis, containment, recovery, rollback, and verification |
| [`adr/`](adr/README.md) | Why important architectural choices were made and what tradeoffs remain |
| [`third-party/`](third-party/README.md) | Package inventories, licensing, SBOM, provenance, and native binary checks |
| [`integrations/`](integrations/providers.md) | Valkey and external-provider trust, retry, degradation, and certification boundaries |
| [`quality/`](quality/README.md) | Test taxonomy, hermetic boundaries, fixtures, certification, and release evidence |
| [`tutorials/`](tutorials/README.md) | Guided walkthroughs that connect multiple architecture chapters |
| [`diagrams/`](diagrams/README.md) | Compact visual explanations for common system flows and failure boundaries |
| [`governance/`](governance/README.md) | Product/operational doctrine, documentation safety, decision process, and review expectations |

Use [Further reading from primary sources](further-reading.md) when you need the
standard or official project documentation behind a concept used here.

For a symptom-first view of the architecture, read
[Engineering lessons from building KiloDrive](engineering-lessons.md).

## The status box convention

Detailed chapters state both axes where they matter:

- **Source maturity:** Implemented, Incremental, or Planned.
- **Deployment state:** Configurable, Uncertified, Certified, Active, or
  Unavailable.
- **Operational policy:** a separately named human/automated procedure and its
  retained evidence, not a maturity level.

A chapter may contain more than one status. For example, private S3 storage can
be implemented in source while its scanner is configurable and the named mobile
release remains uncertified. State both boundaries instead of choosing the more
impressive word.

The [capability status matrix](architecture/capability-status.md) collects the
main cross-cutting claims and the deployment evidence required before an
implemented adapter may be called active.

## How to read a diagram

Arrows in distributed-system diagrams can hide important differences. Each
chapter should say whether an arrow represents:

- a synchronous request;
- an atomic database write;
- an at-least-once message;
- an ephemeral publish;
- a periodic reconciliation; or
- a human approval.

If a diagram does not make that clear, assume nothing and read the surrounding
text. “Service A sends to service B” is not enough to explain durability,
ordering, authentication, or retries.

## A practical review checklist

Before approving a change to this repository, ask:

1. Does it match current code, schema, tests, or an explicitly named policy?
2. Does it accidentally describe a configurable feature as universally active?
3. Does it explain the reason and tradeoff in language a new engineer can use?
4. Does it distinguish durable state from cached, queued, and provider state?
5. Does it include the failure symptoms and safest recovery path?
6. Does it avoid credentials, internal identifiers, private locations, personal
   data, exploitable thresholds, and copied production output?
7. Are links relative, valid on a case-sensitive checkout, and easy to follow?

The automated audit catches broken links and common secret patterns. It cannot
decide whether an architectural claim is true. That still requires an informed
reviewer.
