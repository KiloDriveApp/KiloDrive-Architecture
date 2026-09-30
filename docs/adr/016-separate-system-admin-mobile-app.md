# ADR 016: Separate the System Admin mobile app from the consumer app

- **Status:** Accepted/Incremental
- **Date:** 2026-09-30

## Context

The former consumer Flutter package also contained privileged System Admin
navigation and workflows. Hiding a menu did not remove privileged code from a
public binary. It also mixed app identities, push routing, local state, release
evidence and store review with ordinary rider/driver journeys. Administrators
can legitimately hold a separate rider membership under one global identity,
so a blanket account-level prohibition on consumer login would break a valid
product case.

## Decision

The consumer package contains consumer journeys and no operative System Admin
UI or mutation client. A second Flutter package owns mobile System
Administration, with independent Android/iOS IDs, native/Firebase identity,
secure local state and release path. Both are untrusted clients of the same
canonical API. The API owns identity, session role, country and acting-tenant
grants, capabilities, record ownership, recent authentication, 2FA, revisioned
mutation and audit. The consumer HTTP client removes acting-tenant headers.

A SystemAdmin identity with an active rider membership may receive a separate
consumer-scoped rider session; the admin role is not presented in that session.
The same email and global user are allowed. The Admin session remains
capability-scoped and requires an authorized country/tenant workspace. An old
consumer binary's behavior is governed by server policy and a separately
reviewed legacy-client cutoff, not by the new source tree alone.

## Alternatives and tradeoffs

Keeping one binary with hidden admin routes would simplify deployment but keep
privileged code and native channels in the public package. Creating a second
identity for every administrator-rider would separate sessions but duplicate
account ownership, recovery and audit. The chosen split increases signing,
Firebase/App Check, notification, store-distribution and paired-device testing
work. It also requires an explicit operation-by-operation migration rather than
claiming the copied menus provide parity.

## Consequences

Each app has its own installation credential and push channel; hardware model,
IP or a claimed app header cannot authorize either. An admin alert is a generic
hint, reauthorized on tap. Both clients must preserve original idempotency
keys and revisions after unknown outcomes and reconcile with the API. Local
biometrics or app PIN protect screen privacy but do not authorize account,
security or money mutations. The API enforces the boundary even if a binary is
modified or an old version remains installed.

## Migration and release

The public source-boundary verifier and separate Admin package are present.
Operational parity, signed Android/iOS device evidence, admin push isolation,
App Check, private distribution, role denial and unknown-outcome recovery are
still incremental. Rollout keeps API changes backward-compatible, privately
tests the Admin app with least-privilege operators, and stages any legacy-client
cutoff only after independent review. Rollback never restores privileged UI to
the consumer build or erases financial/audit history.

## Validation

Review the [two-app source checkpoint](../architecture/two-mobile-apps-and-security-2026-09-30.md)
and current source migration ledger. Run the boundary verifier, both app
analyzers/tests, API permission and session-role tests, the required pre-push
gate, signed paired-install/device tests and provider/country matrices on the
exact candidate. An endpoint inventory is not release certification.
