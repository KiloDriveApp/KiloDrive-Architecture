# KiloDrive security posture

KiloDrive is a transportation and marketplace platform. It handles identity
evidence, location, conversations, vehicle documents, and money. Security is not
one middleware call or a claim that the mobile binary is hard to modify. It is a
chain of independent controls that keeps one mistake from becoming a complete
compromise.

This chapter describes the implemented architecture and the operational
expectations around it. It is not a guarantee of invulnerability, a penetration
test report, or permission to advertise “military-grade” security. Honest
security documentation names assumptions, failure modes, and remaining
deployment responsibilities.

The public [Privacy Policy](https://kilodrive.com/privacy),
[Cookie Policy](https://kilodrive.com/cookie-policy),
[Data protection overview](https://kilodrive.com/data-protection) and
[Terms of Service](https://kilodrive.com/terms) describe user-facing commitments.
This repository explains their supporting technical boundaries; it is not a
substitute for the current published documents.

For the separate operator client, read [System Admin data handling](admin-data-handling.md)
alongside [identity and access](identity-and-access.md). The former classifies
what an administrator may view, cache, export and retain for a permitted task.

## Detailed control and OWASP guides

Read [security controls and assurance boundaries](security-control-model.md)
for the current source baseline, a request-boundary diagram and the detailed
control model. Read [KiloDrive and OWASP API Security Top 10](owasp-api-top-10-2023.md)
for all ten 2023 risk categories, KiloDrive examples, source evidence, negative
test expectations and remaining verification responsibilities. This is a
self-assessment mapping, not OWASP certification.

| Area | What the controls protect | Essential distinction |
| --- | --- | --- |
| Authentication | Credentials, sessions, recovery, passkeys and social identities | A verified account does not authorize every operation |
| Authorization | Functions, records, fields, country scope and current lifecycle | Tenant filtering does not replace ownership or permission checks |
| Device admission | Application identity, installations, bans and session binding | Attestation does not prove the human or grant an admin role |
| Financial safeguards | Amounts, holds, entitlements, provider evidence and replay recovery | An uncertain outcome cannot justify another mutation |
| Abuse controls | Request frequency, expensive work and sensitive workflows | Rate limits do not prevent every abuse of otherwise valid commands |
| Assurance | Configuration, source tests, deployment and release evidence | Implementation presence is different from production verification |

## The short version

KiloDrive's main security boundaries are:

- one global identity control plane for credentials, sessions, passkeys, social
  links, 2FA, and country memberships;
- credential-free country projections for local rides, wallets, rentals, and
  compliance;
- asymmetric access-token signing with short lifetime, `kid`, and public JWKS;
- rotating refresh-token families, server-side logout, and compromise revocation;
- role, permission, tenant, country workspace, ownership, participant, lifecycle,
  compliance, and step-up authorization checks;
- idempotency and conditional entity versions on sensitive mutations;
- immutable double-entry journals alongside operational wallet transactions;
- private-object and encryption controls with fail-closed quarantine scanning,
  subject to verified storage and key configuration;
- durable outbox delivery, safe provider reconciliation, and redacted telemetry;
- trusted-proxy boundaries, rate limits, strict response headers, and sanitized
  Problem Details; and
- schema/configuration validation before a production process reports readiness.

## Defense in depth by layer

| Layer | Primary controls | What it cannot do alone |
| --- | --- | --- |
| Cloudflare/edge | Deployment-configured TLS, WAF, bot/probe filtering and rate limits | authorize a ride or wallet resource |
| IIS/reverse proxy | process isolation, request bounds, headers | decide tenant ownership |
| API middleware | correlation, authentication, tenant resolution, rate limits, redaction | replace handler-level domain authorization |
| Handlers/services | ownership, state, compliance, idempotency, accounting | protect a leaked signing key |
| MySQL cells | constraints, locks, immutable journals, local transactions | coordinate a cross-cell money transfer safely |
| Valkey | short-lived realtime/location/distributed state | become the durable ride or identity database |
| S3/scanner | private storage, encryption, quarantine | decide whether a reviewer is authorized now |
| Mobile/portal | safe UX, secure storage, platform biometrics | enforce trust against a modified client |
| Operations | least privilege, monitoring, rotation, runbooks | correct insecure application logic by itself |

The table assigns responsibilities; it does not attest that each external
control is enabled in production. App Check protected routes, device bootstrap,
browser admission and legacy session compatibility have different enforcement
boundaries. Request budgets are process-local unless an assessed aggregate
control is supplied. These qualifications are detailed in the
[control model](security-control-model.md).

## Seven principles used in reviews

1. **The API is the security boundary.** A rooted phone, modified APK, replayed
   HTTP request, or automated browser must not gain more authority.
2. **Credentials live only in the control plane.** Country rows support local
   foreign keys; they do not become a second authentication source.
3. **Country money stays in one local transaction.** We do not improvise a
   distributed financial transaction across cells.
4. **A timeout is an unknown result, not a safe retry.** Mutating provider calls
   reconcile before a second attempt.
5. **Logs describe behavior, not customer payloads.** Correlation is useful;
   tokens, contacts, documents, and routes are not telemetry.
6. **Protected flows fail closed; optional UX degrades safely.** Scanner failure
   quarantines an upload. A slow avatar does not block login.
7. **Production secrets are external to source and public runbooks.** Examples
   show shape, never a usable value.

## Security is also state-machine correctness

Many serious bugs are not cryptographic. Examples include accepting a bid after
the driver went offline, deleting another user's payout method by UUID, treating
a completed cashout as unreconciled forever, or returning an error after a
transaction committed because audit storage failed. KiloDrive therefore treats
conditional state transitions, resource ownership, idempotency, and durable side
effects as security controls.

For a sensitive mutation, reviewers ask:

- Is the current identity active, and is the token/session still valid?
- Which tenant and country cell own the resource?
- Does the caller own or participate in this specific entity?
- Is a recent step-up proof required?
- Is the entity still in the expected version and lifecycle state?
- Is the operation idempotent under a lost response or repeated tap?
- Do the financial entries balance in the same transaction?
- Is notification/audit work durable but outside the request's provider latency?
- Does a failure return a coarse, stable error with security headers?

## Implemented versus deployment-dependent

The repository contains controls and tests for JWT rollover, token redaction,
passkey distributed ceremony state, upload scanning, canaries, accounting
reconciliation, and provider resilience. Production effectiveness still depends
on correct configuration: persistent Data Protection keys, protected JWT private
key, restrictive IAM, confirmed alert destinations, provisioned Valkey, current
malware signatures, Cloudflare trusted-proxy settings, valid certificates, and
store/provider declarations.

An implementation can be present while a feature is disabled or awaiting
provider approval. Runbooks should say “configured and verified” only after a
real environment check.

## How to use this chapter

- [Security control model](security-control-model.md) joins the main protections,
  representative source evidence and deployment responsibilities.
- [OWASP API Top 10 mapping](owasp-api-top-10-2023.md) connects all ten risk
  categories to KiloDrive controls and bounded verification requirements.
- [Identity and access](identity-and-access.md) explains credentials, JWTs,
  refresh families, OTP, passkeys, TOTP, roles, and step-up.
- [Application security](application-security.md) covers edge, middleware,
  authorization, idempotency, uploads, mobile assumptions, and secure delivery.
- [Privacy and data protection](privacy-and-data-protection.md) covers data
  minimization, location, documents, recording, retention, and deletion.
- [Threat boundaries](threat-boundaries.md) is the practical threat model and
  review checklist.
- [Rider and driver safety](../architecture/rider-driver-safety.md) connects
  account, matching, location, communications, emergency, evidence, and human
  response controls across the full trip lifecycle.
- [Jurisdictional compliance](../architecture/jurisdictional-compliance.md)
  explains how those controls are approved, versioned, activated, evidenced,
  reviewed, and safely disabled per country.

Security defects should be reported privately using the repository's security
policy. Never paste a live credential, token, document, phone number, precise
route, or exploit against production into a public issue.
