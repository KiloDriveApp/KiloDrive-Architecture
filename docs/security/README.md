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
- private encrypted object storage with fail-closed quarantine scanning;
- durable outbox delivery, safe provider reconciliation, and redacted telemetry;
- trusted-proxy boundaries, rate limits, strict response headers, and sanitized
  Problem Details; and
- schema/configuration validation before a production process reports readiness.

## Defense in depth by layer

| Layer | Primary controls | What it cannot do alone |
| --- | --- | --- |
| Cloudflare/edge | TLS, WAF, bot and probe filtering, rate limits | authorize a ride or wallet resource |
| IIS/reverse proxy | process isolation, request bounds, headers | decide tenant ownership |
| API middleware | correlation, authentication, tenant resolution, rate limits, redaction | replace handler-level domain authorization |
| Handlers/services | ownership, state, compliance, idempotency, accounting | protect a leaked signing key |
| MySQL cells | constraints, locks, immutable journals, local transactions | coordinate a cross-cell money transfer safely |
| Valkey | short-lived realtime/location/distributed state | become the durable ride or identity database |
| S3/scanner | private storage, encryption, quarantine | decide whether a reviewer is authorized now |
| Mobile/portal | safe UX, secure storage, platform biometrics | enforce trust against a modified client |
| Operations | least privilege, monitoring, rotation, runbooks | correct insecure application logic by itself |

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
