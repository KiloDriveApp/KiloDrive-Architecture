# KiloDrive API Guide

This guide explains KiloDrive's HTTP contracts, their trust boundaries and the
workflows that make them useful. It includes a readable endpoint reference and
a curated OpenAPI export derived from the reviewed implementation. It is
intended for engineers, reviewers and prospective integration partners.

**Documentation does not grant integration access.** An anonymous endpoint
means no bearer requirement is declared for that action. Protected endpoints
are primarily first-party application contracts. They can require installation
admission, application attestation, a valid session, country context, ownership,
permissions and enabled dependencies. This repository does not establish an
open developer platform, issue API keys or promise a third-party service-level
agreement. Discuss approved integrations through
[Contact KiloDrive](https://kilodrive.com/contact).

## What is published

The reviewed snapshot covers **459 paths, 528 operations and 659 schemas** in
18 documentation groups. Of those operations, 64 declare anonymous bearer
metadata and 464 declare bearer security. The complete source artifact has
996 paths and 1,123 operations. The public subset is selected explicitly;
new source endpoints do not become public automatically.

The source snapshot was reviewed on **2026-10-03** at commit
`1cd27c58f0fd9df6d974fab3718c3cb0b485f251`, with consumer source
`1.0.0+172`, separate System Admin source `0.1.0+16`, and schema contract
`2026.10.03.1`. These identify the inspected source. They do not certify that
every production instance, country, provider or signed mobile artifact has
passed the corresponding workflow. Historical build chapters retain their
original baselines.

The [snapshot manifest](openapi/manifest.json) contains provenance, counts and
checksums. The complete private contract's SHA-256 is
`c66d1c238842d4523cdda63ba3caa2a96888ad17dd332c642d7cfba30a95f16b`.
The [public OpenAPI](openapi/kilodrive-public-v1.json) has its own
[SHA-256 sidecar](openapi/kilodrive-public-v1.json.sha256). The hashes differ
because this is a curated export, not a copy of the private contract.

## Reading order

| Guide | What it answers |
| --- | --- |
| [Getting started](getting-started.md) | Which surface can I use, and what is an honest integration prerequisite? |
| [Access and authentication](access-and-authentication.md) | How do registration, social login, contact proof, sessions and installation admission fit together? |
| [Authorization and country context](authorization-and-tenancy.md) | Why do a valid token and a guessed identifier not grant access? |
| [Wire conventions](wire-conventions.md) | How are IDs, numeric enums, money, dates, nulls and localized values represented? |
| [Errors and safe recovery](errors-and-recovery.md) | What should a client do after conflicts, interruptions, rate limits or expired sessions? |
| [Lists, caching and performance](pagination-and-caching.md) | How should pagination, seek cursors, refresh and cache scope work? |
| [Account and onboarding journeys](account-and-onboarding.md) | How does a user become verified, and how does a driver become ready for work? |
| [Rides, trips and service workflows](service-workflows.md) | How do bidding, payment, chat, delivery and rental lifecycles stay coherent? |
| [Money and memberships](money-and-memberships.md) | Which system owns balances, FX quotes, subscriptions and entitlements? |
| [Notifications and realtime](notifications-and-realtime.md) | What binds a push token, and what does delivery actually prove? |
| [Documents and privacy](documents-and-privacy.md) | How do private uploads, review, replacement, reports and evidence work? |
| [Examples](examples.md) | What do safe synthetic requests and interrupted-action recovery look like? |
| [Coverage and limitations](coverage-and-limitations.md) | What is excluded, incomplete or dependent on external configuration? |
| [Versioning and publication](versioning-and-publication.md) | How is the guide kept accurate without exposing the full private API? |
| [Endpoint reference](reference/README.md) | Which exact methods, routes, parameters, DTOs and recorded statuses are in this snapshot? |
| [Operation finder](reference/operations.md) | Where can I search every published method and route on one page? |
| [Coverage and review queue](reference/coverage.md) | Which explanations are specific, which are derived, and which source responses lack typed metadata? |
| [Field dictionary](schemas/README.md) | What does every referenced request/response field mean, with its type, requiredness, nullability and constraints? |

The endpoint reference has one page per domain, with a purpose explanation for
every operation and links to its models. The field dictionary covers **5,012
model properties and 103 numeric enums**, including source-verified enum labels.
The OpenAPI defines request and
response fields; the narrative chapters explain their meaning and safe use.
Explanation labels distinguish model-specific meanings from shared conventions
and type-only descriptions. A listed field is not proof that its business
meaning has been fully reviewed. The [model usage map](schemas/usage.json)
shows which operations use each schema, including nested references.
Neither should replace the other. In particular, a generated schema cannot
prove ownership, compliance, provider readiness or correctness after a lost
response.

## Administrative responsibility

System administration belongs to the **separate restricted System Admin app**
and authorized administrative clients. The consumer app provides rider, driver
and rental workflows. It does not provide system-administrator tools. A person
can have a central identity and a consumer profile alongside administrative
responsibilities; each client and session must still receive the authority
appropriate to that channel.

Administrative API routes, cross-workspace contracts, operator recovery tools
and provider callbacks are deliberately excluded from this export. Their
complete specification and executable runbooks remain in the private product
repository. Public architectural explanations are available in
[System Administration](../architecture/system-administration.md) and the
[System Admin mobile app chapter](../architecture/system-admin-mobile-app.md).

## Product and support links

For current country disclosures, use the [website](https://kilodrive.com/),
[user manuals](https://kilodrive.com/manuals),
[public release page](https://kilodrive.com/changelog),
[Privacy Policy](https://kilodrive.com/privacy) and
[Terms of Service](https://kilodrive.com/terms).
The public Android download is the
[consumer app on Google Play](https://play.google.com/store/apps/details?id=com.kilodrive.app).
Security reports follow [SECURITY.md](../../SECURITY.md); public issue reports
must not contain tokens, personal records, private document links or raw logs.
