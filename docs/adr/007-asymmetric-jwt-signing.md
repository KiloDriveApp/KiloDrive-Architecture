# ADR 007: Asymmetric access-token signing and public JWKS

- **Status:** Accepted
- **Date:** 2026-08-23
- **Decision owners:** Identity, Security, API, and Platform Operations
- **Related systems:** Authentication, API/Portal validation, mobile sessions, JWKS, key rotation, protected secret storage

## Context

KiloDrive has multiple first-party consumers and may run more than one API node.
With a symmetric HMAC token key, every service that validates a token also holds
the capability to mint one. Sharing that secret across hosts and applications
widens the blast radius and makes controlled rotation harder.

Access tokens also need a stable way to advertise the current and overlapping
verification keys without publishing private signing material. A deployment may
eventually move from a protected machine file to a managed signing service or a
different host, so the contract should depend on standard asymmetric
cryptography and key identifiers rather than a particular filesystem.

## Decision drivers

- Validators should not be able to sign tokens.
- Private signing material must not be stored in Git or ordinary public
  configuration.
- Multiple nodes must present a consistent issuer/audience/key set.
- Rotation must support a short overlap without accepting keys forever.
- Compromise response must revoke sessions as well as replace a key.
- Clients and services need a standard discovery/verification contract.
- Algorithm confusion, missing `kid`, weak key material, and unsafe production
  fallback must fail startup.

## Decision

KiloDrive signs access tokens with an approved asymmetric algorithm (currently
RS256 or ES256 as configured) and a unique key identifier (`kid`). The API loads
the private signing key from a protected deployment source such as a
machine-protected file, environment/secret manager, or future managed signer.
It never commits the private key or prints it.

The API publishes only active/overlapping public verification keys at
`/.well-known/jwks.json`. Validators pin issuer, audience, permitted algorithms,
lifetime/clock-skew policy, and key ID. They do not accept the token's requested
algorithm without server policy.

Access tokens are short lived. Refresh tokens are opaque, hashed at rest,
rotated on use, grouped into token families, and revoked family-wide when reuse
indicates compromise. Logout revokes the server refresh token and the mobile app
atomically clears credentials, account-bound caches, realtime connections, and
workspace metadata.

Production startup validates that:

- the algorithm is asymmetric and explicitly allowed;
- a usable private key with the expected strength/type is available;
- issuer, audience, and lifetimes are valid;
- the key has a non-empty stable `kid`;
- current and previous public keys do not conflict;
- development-only ephemeral or legacy symmetric fallback is disabled; and
- every API node exposes the intended public key set.

## Rotation procedure

1. Generate/provision a new private key in the protected environment. Never
   print it or copy it through chat/tickets.
2. Assign a new `kid` and deploy the new public key alongside the old public key.
3. Verify JWKS on every node and validation through a synthetic token path.
4. Switch signing to the new private key.
5. Observe issuance/validation, node consistency, refresh, and authentication
   metrics for at least the longest access-token lifetime plus clock skew.
6. Remove the old public key after no valid token can reference it.
7. Revoke/destroy old private material under the key custody policy.

For suspected compromise, shorten the overlap: rotate immediately, revoke
refresh-token families/sessions according to incident scope, and accept that
users may need to sign in again. A key change alone does not invalidate a copied
refresh token.

## Alternatives considered

### HS256 shared secret

It is simple and fast, but every validator can mint tokens and secret
distribution expands the trust boundary. It remains acceptable only for narrow
development/test scenarios—not production KiloDrive access tokens.

### Store the private key in application settings or Git

This is convenient for shared hosting and deployment copying, but it leaks into
source history, artifact backups, support bundles, and tooling. It was rejected.
A protected file or secret injection works on conventional hosting without
putting the key in public configuration.

### Ephemeral key on every process start

This avoids secret provisioning, but every restart invalidates tokens and
multiple nodes disagree. It is development-only.

### Remote token introspection for every request

This centralizes revocation but adds network latency and availability dependency
to every API authorization decision. It was not chosen for normal access tokens;
sensitive mutations still use current database/session/step-up checks.

### Managed cloud signer immediately

KMS/HSM-backed signing can reduce private-key exposure and strengthen custody,
but adds provider latency, cost, quotas, and operational complexity. The
asymmetric/JWKS contract permits this later without changing token consumers.

## Consequences

### Benefits

- Public-key validators cannot mint tokens.
- JWKS supports interoperable validation and planned rollover.
- Private material stays within the signing workload boundary.
- Multiple API nodes can verify a consistent key set.
- Migration to managed signing remains possible.
- Startup validation catches missing/unsafe production configuration early.

### Costs and risks

- Key provisioning, ACLs, backup, rotation, and recovery need disciplined
  operations.
- A missing/unreadable protected key prevents startup by design.
- Removing an old key too soon signs users out unexpectedly.
- Keeping old public keys indefinitely enlarges the validation window.
- Shared hosting still needs a protected secret mechanism and filesystem/process
  isolation.
- JWKS caching must honor rollover without accepting arbitrary origins.

## Security, privacy, and compliance

Private keys are restricted to the API signer identity and administrators under
audited break-glass procedure. Public keys contain no secret and may be cached.
Key metadata and rotation events are audited without key content.

Tokens carry the minimum authorization context and never contain secrets,
document content, payment data, or unnecessary PII. Tenant/country claims are
validated against current authorization for sensitive/cross-tenant operations;
possession of a signed token is not permission to bypass object ownership or
step-up rules.

SignalR/hub tokens are separate, purpose/role/trip scoped, and short lived. Query
parameters such as `access_token` are removed from logs/traces at ingress and
proxy/collector layers.

## Reliability and operations

Persist and protect ASP.NET Data Protection keys separately from JWT signing
keys; they solve different problems. An ephemeral Data Protection warning can
break cookies/CSRF/protected state after recycle even when JWT signing works.

Monitor signing/configuration startup failures, JWKS availability/latency,
unknown `kid`, invalid algorithm/issuer/audience, refresh reuse/family revocation,
and unusual authentication failure spikes. Never log the token to diagnose a
validation error.

See [identity and access](../security/identity-and-access.md) and the
[JWT rotation runbook](../runbooks/jwt-key-rotation.md).

## Validation

- Successful issue/validate through current key on every API node.
- Public JWKS contains only intended public parameters and unique `kid` values.
- Wrong issuer, audience, signature, algorithm, lifetime, and unknown `kid` fail.
- Private key file/secret is inaccessible to unrelated app identities.
- Missing/placeholder/symmetric/ephemeral production configuration fails
  startup with a safe message.
- Rotation overlap accepts old unexpired and new tokens, then rejects old after
  the window.
- Refresh reuse revokes the token family and logout blocks copied refresh use.
- Logs, traces, exceptions, and support exports contain no bearer token or key.
- Multi-node and process-recycle tests preserve expected verification behavior.

## Follow-up

- Exercise normal rotation and emergency compromise response.
- Record key owner, creation, activation, retirement, backup, and destruction in
  the restricted key inventory.
- Reassess KMS/HSM remote signing when scale/compliance/custody evidence warrants
  it.
- Keep public documentation architectural; exact paths, identities, key IDs, and
  recovery material remain restricted.
