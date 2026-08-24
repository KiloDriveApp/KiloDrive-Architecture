# ADR 011: Argon2id by default with an explicit PBKDF2 FIPS profile

- **Status:** Accepted
- **Date:** 2026-08-24
- **Owners:** Identity, Security, and Platform Engineering
- **Related:** [Identity and access](../security/identity-and-access.md),
  [Application security](../security/application-security.md), and
  [Authentication runbook](../runbooks/authentication-session.md)

## Context

KiloDrive previously stored salted PBKDF2-HMAC-SHA256 password hashes with the
cost embedded in the representation. The construction was sound, but the older
work factor no longer matched the target guidance. Raising PBKDF2 everywhere
would improve cost while leaving it comparatively friendly to highly parallel
attack hardware. Adopting Argon2id makes memory part of the attack cost.

Some deployments may nevertheless have a contractual or regulatory requirement
to execute password derivation inside an approved FIPS cryptographic boundary.
Argon2id and the selected managed package must not be represented as FIPS
validated merely because they are strong password-hashing choices.

Password hash strings are attacker-controlled after a database compromise and
can also enter verification through corrupted data. Unbounded cost parameters
could turn verification into memory or CPU exhaustion. A production API also
needs enough headroom for legitimate login bursts.

## Decision

The normal profile uses Argon2id version 19 with:

- a random 16-byte salt;
- a 32-byte derived key;
- 19,456 KiB memory;
- two iterations; and
- one lane.

The exact `Konscious.Security.Cryptography.Argon2` dependency is security-
reviewed and pinned. The encoded representation records algorithm and cost so a
future policy can recognize and upgrade an older supported value.

An explicitly approved FIPS-only deployment selects PBKDF2-HMAC-SHA256 with at
least 600,000 iterations. Configuration fails startup when `FipsMode` is paired
with Argon2id or when PBKDF2 is selected outside the explicit FIPS profile.

Verification:

1. identifies only a supported tagged format or the bounded legacy format;
2. validates salt, output, memory, iteration and parallelism bounds before work;
3. enters a process-level concurrency gate sized to the reviewed memory budget;
4. derives and compares in constant time;
5. returns the ordinary coarse authentication result; and
6. after a correct password, replaces a supported weaker hash when policy says
   it needs rehashing.

The old hash is retained when verification fails or persistence of the upgraded
hash cannot complete. Passwords and derived material never enter telemetry.

## Alternatives considered

### PBKDF2 at a higher cost everywhere

This is compatible and is retained for the FIPS profile, but it does not make
memory a meaningful part of the attack cost. It remains a valid controlled
fallback, not the default.

### bcrypt or scrypt

Both have mature deployments. Argon2id provides a modern tunable memory-hard
design and aligns with the selected guidance. Adding several normal profiles
would increase migration and operational complexity without a current need.

### Rehash every account in a batch

The server cannot derive a new password hash without the plaintext password.
Resetting every password would harm users. Lazy rehash after successful proof
upgrades active accounts without weakening verification.

## Consequences

- Login consumes more bounded memory and needs capacity testing.
- Horizontal scale calculations include concurrent password operations, not
  only request count.
- A policy increase is backwards compatible because cost lives in the hash.
- Inactive accounts remain on an older supported format until successful login
  or a separate password-reset policy retires it.
- FIPS claims remain scoped to the approved deployment boundary and evidence.
- Dependency, SBOM, license, vulnerability and known-vector review include the
  Argon2 implementation.

## Validation

Tests cover a published Argon2id vector, normal and wrong-password verification,
legacy PBKDF2 migration, weaker Argon2 rehash, malformed and excessive cost
fields, invalid FIPS combinations, constant result semantics, and concurrency-
gate exhaustion. Capacity exercises measure authentication p95/p99, CPU,
working set and rejection behavior before increasing cost or concurrency.

The authentication runbook distinguishes a normal bad credential, a capacity-
gate event, invalid stored metadata, and configuration failure without exposing
the hash or password. Rollback may select a previously approved compatible
profile; it never converts stored hashes to plaintext or a fast digest.
