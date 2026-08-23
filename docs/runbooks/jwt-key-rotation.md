# JWT Signing-Key Rotation Runbook

- **Owner:** Security and API Operations
- **Status:** Operational policy; exercise before first production rotation and
  at the approved cadence
- **Last exercised:** Record in restricted release/incident evidence
- **Related architecture:** [Identity and access](../security/identity-and-access.md)
  and [ADR 007](../adr/007-asymmetric-jwt-signing.md)

## Purpose

Use this runbook to rotate the asymmetric key that signs KiloDrive access
tokens. A planned rotation keeps a bounded overlap so tokens issued before the
change remain verifiable until they expire. An emergency rotation may revoke
sessions faster when the old private key could be compromised.

The API signs with an approved RSA or elliptic-curve algorithm and identifies
the key with a unique `kid`. Verification services consume public keys through
JWKS. The private key never belongs in this repository, application logs,
screenshots, tickets, or a public runbook.

## Roles

| Role | Responsibility |
| --- | --- |
| Rotation lead | Owns change record, timing, stop/rollback decision, and evidence |
| Key custodian | Generates/imports protected material and controls private-key access |
| API operator | Deploys signing configuration and verifies every API node |
| Security reviewer | Confirms algorithm, key properties, access, overlap, and compromise response |
| Client/operator observer | Watches authentication, refresh, JWKS consumers, and user impact |

Use separation of duties where staffing permits. No one needs to paste the
private key into a chat to prove it exists.

## Planned versus emergency rotation

### Planned

Use the normal overlap sequence when the old key is trusted. Publish the new
public key before signing with it, retain the old public key for at least the
maximum accepted access-token lifetime plus clock/cache allowance, then remove
it.

### Emergency

Use the security-incident path when exposure is suspected, key access cannot be
accounted for, the algorithm is no longer approved, or an unauthorized token is
credible. The safety priority changes: rapid invalidation may be more important
than avoiding user sign-in prompts.

An emergency rotation can also require token-version/session-family revocation,
refresh-token invalidation, passkey/2FA review, and investigation of when the
key may have been used. Merely publishing a new key does not invalidate a token
already signed by a still-trusted old public key.

## Preconditions

- approved change or incident record with owner and window;
- exact deployed API version and node inventory;
- current token issuer, audience, algorithm, active `kid`, token lifetime, and
  accepted clock skew;
- current JWKS output and cache behavior of known consumers;
- protected key-storage mechanism, backup/escrow policy, and access review;
- tested rollback key/configuration that does not expose private material;
- readiness, login, refresh, JWKS, and protected-endpoint smoke tests;
- dashboards for authentication failure, token-validation reason, login/refresh
  rate, API health, and node/config drift; and
- communication plan if clients may need to sign in again.

Do not start a routine rotation during an authentication incident, incomplete
schema/deployment change, or when operators cannot identify all serving API
nodes.

## Stop conditions

Pause or roll back the planned change if:

- the new public key cannot be observed consistently before signing begins;
- any serving node lacks access to the approved new private key;
- nodes disagree on active `kid`, issuer, audience, or algorithm;
- newly issued tokens do not validate through the public JWKS path;
- old valid tokens fail before the approved overlap expires;
- authentication/refresh failures rise beyond the internal change threshold;
- the private key appears in logs, command output, artifacts, or an unintended
  ACL; or
- rollback identity/material is uncertain.

For suspected compromise, do not restore the exposed key merely to reduce user
impact. Escalate through the security-incident runbook.

## Planned rotation procedure

### 1. Generate or import the new key

Create the key with an approved algorithm, size or curve, and randomness in the
protected environment. Assign a globally unique, non-secret `kid` that does not
encode a hostname, account ID, operator name, or private path.

Apply least-privilege access to the application workload and key custodians.
Verify backup/escrow and recovery according to policy. Record only the public
fingerprint, `kid`, algorithm, creation/activation dates, custodian, and change
reference in evidence.

### 2. Stage the public key first

Add the new public key to the JWKS set while the old key remains active for
signing. Deploy this verification-only stage across all API nodes and other
approved token validators.

Verify:

- JWKS returns one entry per accepted `kid` with correct algorithm, use, and
  public-key parameters;
- private parameters never appear;
- cache headers and consumers permit the new key to propagate before use;
- duplicate `kid` values are rejected; and
- security/correlation headers remain present on success and sanitized errors.

Wait at least the approved JWKS propagation interval. A token signed by a key
that consumers have not fetched yet will look forged even when the key is
legitimate.

### 3. Switch signing to the new key

Update protected configuration so the new key becomes the only active signing
private key. Keep the old **public** key in the accepted previous-key set. Roll
API nodes through the normal deployment process and keep the mixed-signer window
controlled.

For each node, prove the exact configuration revision and issue a synthetic
test token through a supported non-user authentication flow. Decode only safe
headers/claims in controlled test tooling and confirm:

- header `alg` is the approved algorithm;
- header `kid` is the new identifier;
- issuer, audience, and time claims remain correct;
- JWKS validates the signature;
- a protected endpoint accepts the token; and
- a previous unexpired token remains accepted during overlap.

Do not log the complete token. A bearer token is a credential even when it was
created for a fixture.

### 4. Observe the overlap

Retain the previous public key until no normally issued access token signed by
it can remain valid, including clock-skew and cache allowance. Refresh tokens
are separate opaque/session credentials; a signing-key rotation does not
automatically revoke them.

Watch validation failures grouped by safe reason and `kid`, refresh/login rate,
401/403 rate, node readiness, and JWKS fetch/cache failures. Avoid metric labels
containing user, token, IP, or claims.

### 5. Retire the old public key

After the overlap and evidence review, remove the old public key from the
accepted JWKS set. Verify an expired/old-key synthetic token is rejected and a
new-key token remains accepted across every node and known consumer.

Destroy or archive old private material according to retention and incident
policy. “Delete the file” is not enough when copies may exist in backup, secret
versions, build artifacts, or operator workstations; follow the approved key
custody procedure.

## Emergency rotation procedure

1. Declare a security incident and record the suspected exposure window.
2. Preserve access, deployment, secret-store, and authentication evidence
   without copying the private key.
3. Generate or import a clean key through a separate trusted path.
4. Publish its public key and switch signing as quickly as safely possible.
5. Remove trust in the compromised public key according to the incident
   decision; do not keep normal overlap for convenience.
6. Revoke affected refresh-token families, increment token or security versions,
   or force broader sign-in according to exposure scope.
7. Search sanitized validation/audit evidence for unexpected use, issuer,
   audience, `kid`, account, geography, or privileged actions.
8. Reverify sensitive account changes, payouts, administrator activity, and
   provider configuration during the exposure window.
9. Notify users, partners, regulators, or insurers only through the approved
   incident and legal process.
10. Complete eradication, recovery, and lessons learned before closing.

If the active key is unavailable rather than exposed, use the availability and
backup recovery procedure. Do not label availability failure as compromise
without evidence, but do not dismiss unexplained key access as availability.

## Rollback

A planned rotation can roll signing back to the still-trusted prior key only
while:

- its private material remains protected and approved;
- its public key is still published and accepted;
- the rollback configuration has been validated; and
- no compromise concern exists.

Rollback order mirrors rollout: keep both public keys visible, switch active
signing, verify new tokens from every node, and investigate why the new key
failed. Do not reuse a `kid` for different key material.

If the new private key was exposed during rollout, generate another key; do not
rotate back and forth between two uncertain keys.

## Verification matrix

| Test | Expected result |
| --- | --- |
| JWKS read before switch | Old and staged new public keys, no private parameters |
| New login after switch | Token carries new `kid` and algorithm and validates |
| Old unexpired token during planned overlap | Accepted until natural or policy expiry |
| Old token after public-key retirement | Rejected with a sanitized stable response |
| Unknown `kid` | Rejected; no fallback to a symmetric or default secret |
| Algorithm substitution or downgrade | Rejected |
| Wrong issuer or audience | Rejected |
| Expired or not-yet-valid token | Rejected within documented skew policy |
| Refresh after switch | New access token uses new `kid`; family rules remain enforced |
| Logout or family revocation | Revoked session cannot obtain a token |
| API-node comparison | Every node accepts the reviewed set and uses one active signer |
| Error response | Correlation/security headers present; no token, key, or stack text |

## Evidence to retain

- approved change or incident reference and roles;
- source, deployment, and configuration revision;
- old and new public fingerprints, algorithms, and `kid` values;
- protected key-store and access-review outcome, not the key or secret path;
- stage, switch, overlap, and retirement timestamps;
- synthetic test correlation IDs and sanitized outcomes;
- node and JWKS consistency evidence;
- authentication metrics before, during, and after;
- rollback or forced-login decision; and
- old-key destruction or archive attestation.

## Common pitfalls

### Signing before publishing

Consumers cache JWKS and reject the new token. Stage the public key and allow
propagation first.

### Removing the old public key immediately

Every current access token fails at once. Keep bounded public-key overlap unless
the old private key is suspected compromised.

### Keeping overlap indefinitely

The rotation never completes and an old-key exposure remains useful. Set and
verify an explicit retirement time.

### Reusing a `kid`

Validators may cache the old public key under that identifier. Every key gets a
unique `kid`.

### Updating one API node

Tokens appear randomly valid as traffic moves between nodes. Prove the full
node inventory and shared configuration.

### Falling back to HS256

A shared secret makes every verifier a potential signer and cannot be published
through JWKS safely. An availability problem is not justification for changing
the trust model.

### Printing a test token

Tokens enter CI logs, tickets, or screenshots and remain usable until expiry.
Record a fingerprint, safe header fields, outcome, and correlation ID instead.

## Completion and escalation

The rotation is complete when the intended key signs on every node, public
verification is consistent, the previous key is retired according to policy,
authentication and refresh flows are healthy, old-key behavior matches the
planned or emergency decision, private material is accounted for, and evidence
is reviewed.

Any suspected disclosure follows the [security incident runbook](security-incident.md).
Deployment inconsistency follows [API deployment](api-deployment.md), and
authentication failures follow
[authentication and sessions](authentication-session.md).
