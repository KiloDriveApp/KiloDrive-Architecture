# Identity, Authentication, and Authorization

## Global identity

The control database is authoritative for user credentials and account security.
Country projections do not contain passwords, refresh tokens, 2FA secrets,
passkeys, or social tokens.

Supported authentication boundaries include password login, phone/email OTP,
social sign-in, passkeys, refresh rotation, and two-factor authentication.
Registration through any channel converges on a canonical validation and durable
projection saga.

## Token model

Access tokens are asymmetrically signed with a key identifier. Only public keys
are published through JWKS. Rotation accepts the current and approved previous
public keys during a bounded overlap. Private signing material is loaded from a
protected file or secret source and never published.

Refresh tokens are stored and rotated server-side. Reuse detection revokes the
compromised token family. Logout revokes the server token before the mobile app
wipes secure and account-bound local state.

## OTP and recovery

OTP challenges are short-lived, single purpose, user/challenge scoped, and
attempt limited independently of password lockout. Codes use a purpose-specific
peppered protection scheme rather than an enumerable unsalted hash. A provisional
registration does not become an active account until contact ownership is proven.

## 2FA and passkeys

TOTP secrets are protected at rest. Enrollment, confirmation, disable, recovery
regeneration, password/contact changes, and payout-related actions require a
recent step-up proof. Passkey create/delete also requires recent reauthentication.
Ceremonies use a single-use distributed store so recycling or API scale-out does
not invalidate a valid flow.

## Authorization

Authorization combines:

- authenticated global identity and active status;
- token version and authorized country/cell memberships;
- tenant resolution;
- role and explicit System Admin permission grants;
- resource ownership/participant membership;
- block, safety, compliance, membership, and lifecycle state; and
- recent step-up proof for elevated actions.

Foreign-resource access returns coarse responses so object existence is not
disclosed.
