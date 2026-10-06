# ADR 017: Separate installation reset from store-purchase recovery

- **Status:** Accepted/Incremental
- **Date:** 2026-10-06
- **Evidence:** [Committed build-196 checkpoint](../architecture/release-1.0.0-196.md)

## Context

iOS protected credentials can survive deletion and reinstallation. A phone may
be shared by different KiloDrive users, and a restored app-data backup can
contain historical account/navigation metadata. Firebase token lifetime and
Apple purchase history are independent of the KiloDrive installation. Resetting
one cannot prove that another was reset or that a purchase belongs to the newly
signed-in account. Store interruptions also leave transaction work that must
be resolved without charging again or transferring paid benefits.

## Decision

Use a non-backed-up app-data marker and durable preparation intent to identify
a true new installation. Before restoring private account state, clear only
KiloDrive-owned protected credential services and stale app preferences.
Temporary Keychain unavailability keeps preparation retryable. Existing
pre-marker upgrades migrate without silently discarding unresolved purchase
context; ordinary upgrades and offload are not a fresh-install reset.

Persist fresh-install push-reset intent separately. Serialize Firebase token
deletion and complete its marker before a new binding is read/registered. A
timed-out native deletion may still finish, so retry shares the existing flight
rather than deleting a subsequently issued token. Push provider availability
does not control the app's first frame or authorize device admission.

Keep Apple purchase history under Apple's authority. A KiloDrive reinstall,
logout or fixture identity reset does not delete that history. Recover a
purchase only after verification of exact signed transaction, application,
product, environment and account binding. An authenticated read-only review
may authorize finishing an exact verified expired queue item without granting
entitlement or writing a payment. An active foreign-account transaction remains
an ownership conflict; unknown evidence remains unresolved.

## Consequences

Deleting the entire Keychain would disturb unrelated SDK/device state and
would not remove Apple purchase history. Keeping all historical KiloDrive
credentials would make a new installation inherit a prior user's state.
Force-finishing every store transaction or creating a new checkout key after
a timeout would discard paid recovery evidence and risk a duplicate purchase.
These alternatives are rejected.

The chosen boundaries require separate reset and purchase journals, explicit
upgrade migration, scope/generation fences and truthful unavailable states.
They also require a retry path when protected storage or APNs registration is
late. A reset cannot erase server security restrictions, financial history,
provider ownership or the need for current API authorization.

## Validation

Host tests cover interrupted reset, delayed native completion, token-rotation
serialization, account switches, signed expiry and foreign-account rejection.
Exact signed iOS reinstall/upgrade, backup restore, APNs timing and StoreKit
purchase/restore scenarios remain required before broad native certification.
The [native matrix](../quality/native-platform-certification-matrix.md) tracks
those scenarios without relabeling host tests as device passes.

Rollback preserves server purchase/payment history and original operation
identity. It must not re-enable silent account inheritance or convert an
unknown purchase into a no-charge result. Continue with
[installation lifecycle](../architecture/mobile-session-and-device-lifecycle.md)
and [store reconciliation](../runbooks/store-entitlement-reconciliation.md).
