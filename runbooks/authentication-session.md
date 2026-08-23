# Runbook: Authentication and Session Incident

## Scope

Failed login/OTP/social/passkey flows, suspected token theft, unexpected session
persistence, 2FA bypass reports, or abnormal lockouts.

## Procedure

1. Identify the stable error code, correlation ID, authentication method, user
   surrogate, and affected country/tenant without collecting credentials.
2. Confirm global identity status, token version, refresh family, session, 2FA,
   passkey, social link, and relevant security audit state.
3. For suspected compromise, revoke the token family/sessions, increment token
   version as required, disable affected social/passkey credentials, and require
   a verified recovery ceremony.
4. For OTP abuse, inspect challenge-scoped attempts and rate limits; do not alter
   password lockout counters to make OTP work.
5. For multi-node passkey failures, validate Valkey single-use ceremony state and
   clock consistency.
6. Restore only after password, OTP, social, passkey, refresh, logout, and step-up
   regression tests pass.

Never request a user's password, OTP, recovery code, access token, or biometric
data for troubleshooting.
