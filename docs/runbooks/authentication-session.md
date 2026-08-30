# Runbook: authentication and session incidents

- **Owner:** Identity and application security
- **Status:** Operational incident procedure
- **Last exercised:** Not yet recorded in this public repository
- **Related architecture:** [Identity and access](../security/identity-and-access.md) and [application security](../security/application-security.md)

**Use when:** login/OTP/social/passkey fails unexpectedly, users remain in the app
after refresh expiry, logout appears ineffective, 2FA is bypassed/locked, or
there is suspected token theft.

**Never ask for:** password, OTP, recovery code, access/refresh token, TOTP
secret, passkey material, or biometric data.

## Establish scope

Collect only:

- stable error code and HTTP status;
- correlation ID and timestamp/timezone;
- authentication method and app/browser version;
- safe user/session surrogate;
- selected country/workspace; and
- whether the behavior affects one identity, one node, one method, or everyone.

Do not screenshot credential fields or enable verbose body logging.

## Symptom map

| Symptom | Likely areas |
| --- | --- |
| Correct login returns workspace error | claims/profile role reconciliation, country membership, session persistence ordering |
| App shell remains after repeated 401 | refresh failure did not emit atomic session-expired cleanup |
| Logout then refresh still works | server refresh token was not revoked |
| OTP failures lock password login | challenge attempts incorrectly share password counters |
| Passkey begin works, completion fails on another node | process-local ceremony state or RP/origin mismatch |
| 2FA secret stops working after restart | ephemeral/mismatched Data Protection key ring or clock issue |
| Social login links wrong account | email-only automatic linking or unverified claim |
| Tokens fail after deployment | signing key/JWKS rotation mismatch, issuer/audience/clock |

## Safe diagnosis

### Global identity and account state

Confirm active/locked status, token version, verified contact state, authorized
country memberships, role/workspace claims, and recent security audit events in
the control plane. Do not query a country projection for credentials.

### Refresh family and logout

Inspect session and refresh-family state using safe IDs. A rotated token should
be revoked, its replacement linked, and reuse should revoke the family. Logout
should revoke server state before local cleanup.

If refresh fails, verify the app clears secure tokens, identity/workspace
metadata and account-bound caches, disconnects SignalR/voice, and navigates to
login. It must not keep an apparently authenticated shell.

### OTP

Check challenge purpose, owner/contact binding, expiry, attempt count, newer-
challenge invalidation, and rate-limit decision. Confirm password lockout counters
were not changed by OTP failures. Do not extend OTP lifetime broadly to resolve a
delivery incident; fix provider latency and preserve a short security window.

### Recent authentication, 2FA, and Data Protection

Distinguish recent authentication from action-bound 2FA step-up. Recent
authentication accepts the current session's validated `auth_time` within ten
minutes or one generic, single-use proof bound to the user and tenant. Enrolled
2FA step-up is bound to one named action and is consumed atomically. Check the
endpoint's enrollment policy, proof user/tenant/action, consumption, expiry,
TOTP clock skew, enrollment confirmation, recovery state, and persistent Data
Protection key-ring availability across nodes. Warnings about an ephemeral key
repository are production defects: encrypted secrets may become unreadable
after restart.

### Passkeys

Check relying-party ID, exact allowed origin, challenge expiry/one-time consume,
credential status, sign counter/policy, server clocks, and distributed Valkey
state. If the store is unavailable, fail closed and offer password/OTP recovery.

### Social login

Confirm token issuer/audience/signature/expiry/nonce and verified email claim.
Review whether linking was an explicit signed-in ceremony. Ensure outbound token
verification did not place credentials in query logs.

### JWT and JWKS

Inspect token header `kid` using a synthetic or affected-token metadata tool that
does not log the full token. Confirm JWKS contains current and approved previous
public keys, issuer/audience are consistent, private key is readable by every API
node, and clocks are synchronized.

## Containment

For suspected compromise:

1. Revoke affected refresh family/all sessions.
2. Increment token version if broad access-token invalidation is required.
3. Disable suspicious passkey/social credentials.
4. Require verified recovery and the endpoint's recent-authentication/2FA policy
   before re-enabling.
5. Rotate signing/provider material if exposure is credible.
6. Add a narrow WAF/rate-limit rule only if it does not block legitimate recovery.

For widespread configuration failure, keep a known secure alternate login method
available. Do not disable 2FA globally or accept a local mobile PIN as server
proof.

## Recovery

- Correct code/configuration and test with dedicated accounts.
- Restore persistent shared key rings/distributed ceremony state.
- Perform JWT rollover rather than abruptly replacing public trust when possible.
- Re-enable the affected authentication method gradually.
- Notify affected users according to verified impact without revealing account
  existence to an unauthenticated reporter.

## Verification matrix

- Password login success/failure/lockout and breached-password policy.
- Public phone/email OTP login plus authenticated contact verification.
- Per-challenge OTP attempts and cross-user challenge reuse.
- 2FA enroll/confirm/login/step-up/disable/recovery.
- Passkey begin/complete across two API nodes, replay, wrong origin, and expiry.
- Social login and explicit link/unlink with unverified/mismatched email cases.
- Refresh rotation, replay family revocation, logout revocation, killed-app restore.
- Rider, driver, rental owner, and System Admin workspace reconciliation.
- JWT current/previous rollover and unknown `kid` rejection.
- Logs/traces contain no token, OTP, contact, or secret.

## Closeout lessons

Authentication bugs often hide in transitions: valid login followed by failed
workspace discovery, committed social link followed by provider timeout, or
logout that wipes only the phone. Add tests around those boundaries, not just a
single successful login request.
