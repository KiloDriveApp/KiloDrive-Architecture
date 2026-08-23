# Security Posture

KiloDrive applies defense in depth across the edge, API, identity control plane,
country cells, mobile client, provider adapters, and operations.

## Core controls

- asymmetric RS256/ES256 access-token signing with `kid` and public JWKS;
- short access-token lifetime, refresh rotation, token-family compromise
  handling, logout revocation, and token-version invalidation;
- role, permission, tenant, country-workspace, ownership, and domain-state
  authorization enforced server-side;
- step-up 2FA for security, contact, payout, cashout, and account-boundary
  mutations;
- passkey ceremonies stored as single-use distributed state;
- rate limits partitioned by authenticated user or trusted client IP and tenant;
- idempotency and conditional versions for financial and lifecycle mutations;
- strict response headers, CSP, correlation, request limits, and sanitized
  Problem Details;
- private encrypted object storage with fail-closed upload scanning;
- durable audit and outbox processing with sensitive-data redaction; and
- schema fingerprints and production configuration validation at startup.

## Security principles

1. The client is never trusted to enforce entitlement or authorization.
2. Authentication data belongs only to the global identity control plane.
3. Country-local financial transactions remain within one durable cell.
4. Provider failure must not create an ambiguous committed result.
5. Logging and observability collect operational metadata, not payloads.
6. Protected defaults fail closed; optional UX dependencies degrade safely.
7. Production secrets do not belong in source control or public documentation.

This is an architectural posture statement, not a claim of invulnerability or a
substitute for independent security testing.
