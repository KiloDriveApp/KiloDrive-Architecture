# Documents, Media, and Voice

## Private uploads

Identity, licence, vehicle, ticket, and financial evidence are private objects.
The API validates authorization, size, declared type, and magic bytes, then keeps
new objects quarantined until a fail-closed malware scanner returns a signed or
trusted clean result. Rejected, timed-out, or unavailable scans never publish the
object.

S3 objects use private ACL/policy, encryption at rest, non-public keys, and
least-privilege roles. Downloads use short-lived authorized delivery or streamed
responses. Thumbnails are re-encoded and do not expose the original object key.

## Document lifecycle

Metadata tracks owner, content class, type, review state, upload and expiry time,
reviewer, notes, and audit history. Vehicle and driver eligibility is revoked or
returned to review when required evidence expires or is rejected.

## Avatars and images

The mobile client requests authenticated, revision-aware thumbnails and decodes
them to bounded dimensions. In-flight requests are deduplicated; account-bound
caches have a strict budget and are evicted on revision change or logout.

## In-app voice

LiveKit provides rider/driver rooms authorized to a specific trip and role.
Tokens are short-lived and scoped. Call invitation, join, decline, timeout,
reconnect, completion, and cleanup are audited with safe metadata.

Recording is configurable and requires explicit consent and a visible recording
state. Egress writes encrypted objects to private S3 storage under jurisdiction,
retention, deletion, and legal-hold rules. Audit events contain identifiers,
participants, timestamps, status, consent and retention metadata—not audio or
tokens.

Free-plan and paid-plan call entitlements are server-enforced. A permitted GSM
fallback invokes the platform dialer rather than exposing a reusable in-app
channel after the trip closes.
