# ADR 015: Account, membership and notification authority

- **Status:** Accepted
- **Date:** 2026-09-23

## Context

Password recovery, native subscriptions and notifications cross devices and
providers. A UI callback, purchase sheet, push receipt or email send cannot be
authoritative business state. Treating them as authority causes enumeration,
lost access, duplicate purchase handling and invisible notification failures.

## Decision

The control database owns credentials, recovery ceremonies, session revocation
and global security audit. The country-cell membership state machine owns paid
access, periods, pending changes and lifecycle history. Verified Apple/Google
history is evidence into that machine; device callbacks and RTDN/notification
arrival are not entitlement authority.

The country-cell notification row is the durable inbox projection. Push, email,
SMS and WhatsApp are delivery channels with append-only, payload-minimized
attempt evidence. Account/security and safety notifications remain mandatory;
other categories respect reviewed preferences.

## Consequences

Cancellation can preserve paid access through the current period. A deferred
downgrade is visible and cancellable without replacing the current plan early.
Notification history remains available when OS push is denied. Provider and
device certification remains separate from source implementation.

## Validation

Model-based tests cover membership state/event pairs, duplicate/out-of-order
provider events, renewal, retry, grace, cancellation, expiry, refund, revoke,
restore, upgrade and downgrade. Account tests cover anti-enumeration, expired
codes, session revocation and cross-device recovery. Notification tests cover
dedupe, channel preference, mandatory classes, token rebind, failed delivery,
timezone formatting and privacy-safe attempts.
