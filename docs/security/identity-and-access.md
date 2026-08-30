# Identity, authentication, and authorization

Authentication answers *who presented this proof?* Authorization answers *may
that identity perform this action on this resource, in this country, right now?*
KiloDrive keeps those questions separate because a valid access token is not
permission to inspect every driver, join every call, or change every wallet.

## Global identity and country projections

`kilodrive_control` is authoritative for:

- password hashes and password policy state;
- refresh tokens, sessions, token families, and token version;
- email/phone ownership and verification;
- TOTP secret state and recovery codes;
- passkey credentials and single-use ceremonies;
- social identities and linking state;
- global role/permission grants and country-cell memberships; and
- global security audit events.

A country `Users` row is an operational projection for local foreign keys. It
contains the local profile context required by rides, wallets, documents, and
rentals, but no password, refresh token, TOTP secret, or passkey. This avoids the
dangerous situation where two databases disagree about whether an account is
locked or which password is current.

Registration spans control and cell databases, so it cannot rely on one ACID
transaction. The mature design uses a durable, idempotent registration saga:
prove contact ownership, create the global identity, project the country user,
create required local records, and reconcile incomplete steps. Never create an
active placeholder account merely because somebody requested an OTP for an email
or number.

### One registration intent

The reviewed client carries one immutable registration intent from first-run
choice through password or social registration and final review. It contains
the intended role, country, contact method, driver account type, and whether a
rental organization should be created. Dependent request fields are derived
from that object, never from an older app-mode preference.

The API validates the same combinations before identity creation. A passenger
intent cannot carry driver/company fields, and a rental-organization request
must carry the matching company-driver intent. Interrupted signup can restore
the reviewed intent, but successful authentication clears it so it cannot
overwrite an authorized workspace later.

## Passwords

Passwords are processed through a canonical policy regardless of whether signup
began with email, phone, social, or a workspace choice. The server always owns
the local minimum-strength rules, supported-country validation, and lockout. An
optional breached-password check is implemented, but its presence in source
does not prove that a particular deployment has enabled it. The client provides
clear field errors but is not the enforcement boundary.

When breached-password checking is configured, the server performs a
k-anonymity range lookup. It hashes the candidate password for the lookup, sends
only the first five hexadecimal characters of that hash to the range service,
and compares the remaining suffix locally against the returned candidates. The
complete password, complete lookup hash, and suffix are not sent to that
service. Prefix-range responses may be cached for the configured bounded period;
passwords and suffixes must never enter that cache or application telemetry.

The SHA-1 operation used by this protocol is only a compatibility step for the
breach-corpus lookup. It is not KiloDrive's password-storage algorithm. If the
lookup is disabled, no remote breach query is made. If the service is
unavailable, the deployment's explicit fail-open or fail-closed policy decides
whether a new password is accepted. Operators must document that choice,
monitor sanitized lookup availability, and verify it with an approved test
before describing breached-password rejection as active.

Password hashes use a slow, salted password derivation function with a reviewed
work factor. Store neither plaintext nor reversible passwords. Rehash on a
successful login when the configured work factor changes.

### Argon2id and the explicit FIPS profile

The normal KiloDrive password-storage profile is **Argon2id** with a random
16-byte salt, 32-byte derived key, RFC 9106 version 19 encoding, 19,456 KiB of
memory, two iterations, and one lane. Those values are a reviewed baseline, not
a timeless optimum. Capacity tests and current password-hashing guidance decide
when the policy changes.

An approved environment that must keep password derivation inside a validated
FIPS cryptographic boundary uses the separate PBKDF2-HMAC-SHA256 profile with at
least 600,000 iterations. Configuration rejects Argon2id with `FipsMode=true`
and rejects the PBKDF2 profile outside that explicit mode. Engineers must not
describe the Argon2 library itself as FIPS validated.

Each stored representation identifies its algorithm and cost. Verification
parses untrusted hash metadata through strict upper and lower bounds before it
allocates memory or performs expensive work, compares derived bytes in constant
time, and limits concurrent operations so login bursts cannot consume the
process memory envelope. A supported older PBKDF2 or weaker Argon2id hash is
verified once and replaced after a successful login. A failed login never
rewrites the record.

The release gate includes known Argon2 vectors, malformed/oversized encodings,
wrong-password behavior, legacy migration, FIPS configuration rejection, and
concurrency-capacity tests. A work-factor increase is therefore a controlled
security and capacity change, not a string edit in production configuration.

Password failure counters are independent of OTP challenge attempts. We learned
why this matters: if an invalid OTP increments the global password lockout, an
attacker who knows a victim's email can deliberately lock the account without
knowing the password.

## Access tokens: RS256/ES256 and JWKS

Production access tokens use asymmetric signing. The private RSA or EC key signs
tokens; API nodes and external verifiers receive only public material through
`/.well-known/jwks.json`.

Each token header includes a `kid` derived from the public key. Verification
selects the matching public key rather than trying an ambiguous list. Access
tokens are intentionally short-lived, which limits exposure after theft and
bounds key-rotation overlap.

### Safe rollover

1. Generate the new private key in a protected environment.
2. Load the new private key as current and keep the old **public** key in the
   approved previous-key list.
3. Deploy and verify that JWKS publishes both keys and new tokens carry the new
   `kid`.
4. Wait longer than the maximum lifetime of tokens signed by the old key, with a
   small operational margin.
5. Remove the old public key and verify it no longer validates new requests.

Never place a previous private key in the public-key list. Never publish private
parameters in JWKS. A symmetric HS256 secret cannot be safely exposed through
JWKS and should not be represented as equivalent to asymmetric production
signing.

The private key can come from a protected file, environment source, or approved
secret manager. An ephemeral key is for development: restarting would invalidate
every token and prevent stable rollover.

## Refresh tokens, sessions, and logout

Access-token expiry is not enough. Refresh tokens are server-side records grouped
into a token family. Every refresh rotates the token. If an already used token is
presented again, the server treats the family as compromised and revokes the
replacement chain.

Logout calls the server first to revoke the refresh token/session, then the app
disconnects realtime services and wipes secure tokens, identity metadata,
workspace choice, and account-bound caches. Deleting only local storage leaves a
copied refresh token usable.

When refresh fails, the HTTP client emits a typed session-expired event. Session
cleanup is atomic from the user's perspective: credentials disappear, hubs
disconnect, caches wipe, and navigation returns to login. Leaving the shell
visible while every request returns 401 is both confusing and risky.

## Recent authentication and 2FA step-up

These controls answer different questions and must not be described as one
token. A recent-authentication boundary accepts either the current access
session's validated `auth_time` when it is no more than ten minutes old or a
generic, single-use proof bound to the same user and tenant. The proof is issued
after password or supported linked-social reauthentication. It is deliberately
not bound to one action, but it is consumed once and cannot become a second
access token.

An enrolled 2FA step-up proof is stricter: it is bound to the named protected
action, user, and tenant and is consumed atomically. Reusing it, presenting it
for another action, or presenting it after expiry fails with the same coarse
error. Accounts without enrolled 2FA follow the endpoint's explicit policy;
ordinary accounts are not silently locked out merely because 2FA is optional,
while selected System Administrator security/settings mutations require
enrollment before they proceed.

The KiloDrive app lock is only a local privacy boundary. A biometric unlock or
the app's own four-digit PIN never satisfies recent authentication or 2FA for a
wallet, payout, passkey, contact, password, or administrator mutation.

## OTP and recovery challenges

A safe OTP challenge is:

- short lived (normally minutes, not an hour);
- purpose-specific (login, contact verification, or recovery);
- bound to the intended user/contact and challenge ID;
- single use and invalidated by a newer challenge;
- attempt limited independently from password lockout;
- rate limited by trusted IP, account/contact surrogate, and abuse signals; and
- protected at rest with a purpose-specific peppered HMAC or protected-token
  mechanism so a database leak cannot cheaply enumerate six-digit codes.

Errors stay coarse. Cross-user challenge reuse and an unknown challenge should
not reveal which user or contact exists. Authenticated phone-verification routes
must run authorization before model validation, rate-limit work, database
lookups, or notification enqueueing.

## TOTP 2FA and step-up

TOTP secrets are encrypted at rest with persistent Data Protection/KMS-backed
material. Enrollment is not complete until the user confirms a valid code.
Recovery codes are one-way protected, shown once, and regenerated only after a
recent proof.

Step-up is required for changes that cross a security or money boundary,
including 2FA enrollment/disable, recovery regeneration, password and contact
mutations, payout destination changes, cashout, and destructive account actions.
A bearer token alone may be stolen and must not be enough.

Local biometric unlock is convenience access to a device-bound secret; it is not
a substitute for server step-up on a wallet or account-security request. The API
cannot trust a client boolean that says “biometrics passed.”

## Passkeys

WebAuthn verifies a challenge, relying-party ID, origin, credential, signature,
and user-presence/verification flags according to policy. Create/delete requires
recent reauthentication.

Challenges are single use and live in a distributed store. Process-local memory
breaks when IIS recycles or a load balancer sends completion to another API node.
If Valkey is unavailable, the ceremony fails closed and the user can choose
another approved authentication method.

## Social account linking

Provider tokens are verified server-side. Tokens do not belong in outbound query
strings because proxies and telemetry often record URLs. Use provider-supported
authorization headers or POST bodies and redact outbound request metadata.

Never link a social identity to an existing account solely because an email
string matches. Require a verified provider email claim and an explicit,
authenticated linking ceremony or a confirmation challenge sent through the
existing account. Apple flows also bind a client-generated nonce to prevent token
replay/substitution.

When social signup discovers that the provider belongs with an existing
KiloDrive account, the server creates an expiring pending-link record and gives
the client a protected opaque intent. The user signs in to the existing account,
performs recent authentication, reviews the existing and provider identities,
and explicitly confirms or cancels. The record is user-bound, provider-bound,
single use, replay protected, and invalid after expiry.

This ceremony also protects hidden or relay emails: the provider subject and
verified claims—not a guessed display name or matching email string—identify
the external account. Provider display text such as “social” is never accepted
as a person's real name when a reviewed name claim is available; missing names
are requested from the user rather than invented.

## Authorization decision stack

For a protected resource, evaluate:

1. Is the global identity authenticated, active, and at the current token version?
2. Is the selected workspace/role present in authenticated claims/profile?
3. Is the country membership valid and the country provisioned/active?
4. Has tenant resolution produced the same authorized tenant as the resource?
5. Does the role have the explicit permission?
6. Does the caller own, participate in, or have a documented administrator path
   to this entity?
7. Do block, safety, compliance, membership, and lifecycle rules allow it?
8. Does this action require recent step-up?
9. Does the expected entity version/state still match inside the locked
   transaction?

System Administrators choose an authorized country workspace; a global admin
does not need a fake local user row to operate. Cross-tenant admin paths carry an
explicit acting-tenant proof and are audited.

Foreign-resource access returns the same coarse `404`/domain error as a missing
resource where possible. This avoids turning authorization endpoints into UUID
existence oracles.

## Data Protection keys must persist

ASP.NET Core Data Protection protects TOTP secrets and other application tokens.
If the process logs that it is using an ephemeral in-memory repository, values
may become undecryptable on restart and API nodes will disagree. Production uses
a persistent, access-controlled key ring and appropriate at-rest protection.
Back up and restore it as security material, not as an ordinary public artifact.

## Regression suite expectations

Test logout revocation, refresh reuse and family revocation, failed-refresh
sign-out, OTP denial-of-service separation, cross-database partial registration,
social-email takeover prevention, 2FA boundary mutations, cross-node passkeys,
role/workspace restore, and cross-user object access. Include negative tests;
happy-path login alone proves very little.

Also test contradictory registration intents, interrupted-signup restoration,
pending-social-link expiry/replay/account mismatch, recent-authentication
expiry, linked-provider reauthentication, last-login-method protection, and
account-switch cleanup.

See [ADR 007](../adr/007-asymmetric-jwt-signing.md) and the
[authentication/session runbook](../runbooks/authentication-session.md).
