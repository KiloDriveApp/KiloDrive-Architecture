# Access, authentication and device admission

[API Guide](README.md) · [Identity endpoint reference](reference/identity.md)

## Three proofs with different jobs

A user session proves account identity. An installation credential proves the
admitted installation. Application attestation provides verified app evidence
where the configured policy requires it. None substitutes for the others.
Descriptive headers such as app build, platform or client name are useful
metadata; they are not independent proof of a trusted application.

The reviewed native client declares the consumer audience, binds authentication
to installation state and uses secure platform credential storage. The Admin
client has its own native identity and restricted channel. A local biometric
or PIN unlock protects the visible app; it is not server authorization for a
transfer, payout, password change or administrative action.

| Contract element | Purpose | Handling rule |
| --- | --- | --- |
| `Authorization: Bearer <access-token>` | Account session for protected operations | Never log it or place it in a shareable URL |
| `X-KiloDrive-Device` | Admitted installation credential | Keep it private; do not reuse another device's binding |
| App attestation | Provider-verified application evidence | Use the approved native integration; server policy owns acceptance |
| `X-KiloDrive-App` | Declared client audience | A declaration does not override verified app or session authority |
| `X-App-Platform`, `X-App-Build` | Compatibility and diagnostic metadata | Send accurate metadata; do not spoof admission or update policy |
| `X-KiloDrive-Recent-Authentication` where declared | Recent account proof for consequential work | Obtain through the secure ceremony and keep it out of logs |

Attestation and installation policy are configurable. This public guide does
not provide bypass tokens, debug exceptions, console settings or defensive
thresholds. Sideloaded testing must use an explicitly approved admission policy;
a failed attestation must not be silently converted into authenticated access.

## Registration and contact confirmation

`POST /api/v1/auth/register` accepts the documented registration model. Rider
and driver intent includes the chosen country and contact method; driver
account type and rental-organization choice must remain consistent across the
journey. The UI should preserve that intent rather than reconstructing it from
an old local workspace preference.

The schema's role enum describes the wider identity model. It is not authority
to register an administrator. Consumer registration and channel authorization
must enforce permitted roles on the server. Client-supplied preferences or
password-policy acknowledgement fields likewise do not replace server policy.

Contact verification uses server-issued, expiring challenges. Requesting a code,
receiving it and confirming it are distinct steps. Never return the code in
diagnostic UI, store it in release evidence or substitute an invented code.
Display the server's resend/expiry behavior rather than hard-coding a lifetime
from a historical build.

## Login and second factors

Password login uses `POST /api/v1/auth/login`. The response is a
`LoginResultDto`, which can require further verification rather than contain a
usable authenticated session. Email and phone login ceremonies have their own
request/confirmation routes. Second-factor, recovery and passkey endpoints
serve the corresponding established ceremony.

A client must branch on the returned state. A two-factor ticket is not an
access token. Store the final `AuthResponse` only after the ceremony completes.
Generic sign-in failures must not become a public account-existence lookup.
Respect throttling and avoid loops that resend codes or replay wrong passwords.

## Social sign-in and identity collisions

Social sign-in posts provider evidence to `POST /api/v1/auth/social`. Provider
tokens are validated by the server. Email equality alone is insufficient to
link accounts. A collision follows the protected pending-link review and
confirmation workflow, with explicit recent authentication and expiry.

The client must preserve the pending link and show the actual account-linking
decision. Do not automatically create a second identity, attach a provider to
an existing account or move between countries based on a display email.

## Session restoration and rotation

`POST /api/v1/auth/refresh` uses the documented refresh model. Refresh tokens
are sensitive rotating credentials. The source uses session-family and
installation binding so a restored token is not an unrestricted portable
credential. Central control identity owns this security state; country user
projections are not credential stores.

On cold launch, restore and validate the authenticated session before starting
protected trips, incoming-call, notification or wallet polling. Incomplete
onboarding should resume its saved journey. Serialize refresh operations and
secure-store writes. Logout must cancel old work and prevent a delayed rotation
write from restoring credentials that the user just removed.

On an expired or revoked session, stop protected work, reconcile account-bound
pending operations after legitimate reauthentication, and show a clear sign-in
state. Repeated 401s are not a reason to keep polling or invent a fresh mutation.

## Password and account security changes

Password reset uses the request/confirmation process under
`/api/v1/auth/password-reset/...`. The user proves control through the secure
reset workflow. Administrators can initiate an authorized reset; the Admin UI
must not expose, set or display a plaintext password.

Password changes, social disconnection, passkey changes, recovery-code work,
session revocation and contact changes follow their documented secure workflows.
Use recent authentication when required by the server. A confirmation dialog
protects user intent, but it does not prove account control.

Related: [identity and access](../security/identity-and-access.md),
[session/installation lifecycle](../architecture/mobile-session-and-device-lifecycle.md)
and [authentication recovery](../runbooks/authentication-session.md).
