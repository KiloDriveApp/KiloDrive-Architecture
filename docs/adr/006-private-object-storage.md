# ADR 006: Private, quarantined, encrypted object storage

- **Status:** Accepted
- **Date:** 2026-08-23
- **Decision owners:** Security, Privacy, Platform Operations, and Document domains
- **Related systems:** S3, KMS, upload scanning/CDR, driver evidence, tickets, reports, thumbnails, LiveKit egress

## Context

KiloDrive accepts identity and driver-licence evidence, vehicle documents,
ticket attachments, profile/vehicle images, reports, and consented call
recordings. These objects differ in purpose and retention, but all can expose
people if stored under guessable public URLs or served before inspection.

File extensions and browser content types are untrusted. A scanner can be slow
or unavailable. A presigned URL is a bearer credential. Image metadata can leak
location/device information. Recording storage adds consent, legal hold, and
jurisdiction rules. The database also needs a stable audit and lifecycle record
that is not confused with the object bytes themselves.

## Decision drivers

- No user object is publicly readable.
- New untrusted content must remain unavailable until a trusted scan/policy
  result says it is safe.
- Authorization is checked when access is requested, not only when a URL was
  generated.
- Storage identities must be scoped by content class and prefix.
- Encryption, retention, deletion, and legal hold need explicit policy.
- The application must reconcile metadata/object mismatches and unknown egress
  results.
- Release artifacts and public documentation must not contain customer objects,
  signed URLs, bucket identities, or encryption-key identifiers.

## Decision

KiloDrive stores user-generated and generated artifacts in private S3 object
storage behind application authorization.

### Upload lifecycle

1. The API authenticates the actor and authorizes the target content class.
2. It enforces bounded size, declared type, filename policy, and magic-byte
   inspection before accepting content.
3. Bytes are stored under an opaque quarantine key. User filenames are metadata,
   never object paths.
4. The country database records ownership, class, storage key, content hash,
   scan/review state, revision, and retention metadata.
5. A fail-closed ClamAV/CDR or managed scanning adapter returns a signed/trusted
   result through an idempotent state transition.
6. `clean` content becomes eligible for its separately authorized workflow.
   Rejected content stays unavailable with a bounded safe reason. Timeout leaves
   it quarantined for retry.

### Delivery lifecycle

The API rechecks tenant, owner/participant/admin permission, object state,
content class, expiry, and legal hold. It then streams the object or issues a
very short-lived, response-constrained signed URL according to policy. Identity
documents use attachment or a controlled viewer and no public cache.

Display thumbnails are separately re-encoded, bounded, metadata-stripped
objects. The original is never treated as a safe thumbnail simply because it is
an image.

### Encryption and identities

Buckets block public access and use approved server-side encryption with a
customer-managed key where required. Application, scanner, thumbnail worker,
LiveKit egress, retention/deletion worker, and operator roles have separate
prefix/actions. KMS authorization is constrained by key policy, IAM, and
encryption context where supported.

### Recordings

Egress writes only after the required durable consent and jurisdiction policy
allow it. Output uses the recording-only prefix and write-only least privilege.
The database records safe provider ID, status, retention deadline, and legal
hold—not media, secret, token, or signed URL.

## Alternatives considered

### Public object URLs with random names

Randomness does not turn a public object into an authorized object. URLs leak
through logs, referrers, screenshots, and forwarding. This was rejected.

### Database BLOB storage

This simplifies transactional metadata/bytes but makes backups, replication,
large-file delivery, scanning, and retention expensive for the operational
country database. It was rejected for object content; MySQL remains the metadata
and lifecycle authority.

### Trust extension and client MIME type

These fields are user controlled and do not detect polyglots or active content.
They remain early validation hints, not safety proof.

### Scanner fail-open

This improves short-term upload availability during scanner failure but exposes
untrusted bytes. It was rejected. The user receives a clear quarantined/retry
state instead.

### Long-lived presigned links emailed to users

This avoids repeated API authorization but creates forwardable bearer access
and uncontrolled retention. It was rejected for sensitive content.

## Consequences

### Benefits

- Public exposure is denied by default.
- Untrusted and approved objects have explicit lifecycle states.
- Application authorization remains current after account/role/trip changes.
- Content classes can have different view, retention, deletion, and audit rules.
- Storage/egress/scanner compromise has a narrower IAM blast radius.
- Bounded thumbnails improve mobile memory use and remove metadata.

### Costs and risks

- Scanning and CDR introduce delay and an operational dependency.
- Quarantine needs retry, user-facing state, and administrator visibility.
- Signed URLs still require strict TTL and telemetry redaction.
- Object and metadata can drift after partial failures; reconciliation is
  required.
- KMS key policy mistakes can block otherwise valid IAM access.
- Legal hold and privacy deletion can conflict and need a governed decision.
- Egress timeout may leave an unknown recording job/object state.

## Security, privacy, and compliance

Content classes determine purpose, lawful handling, authorization, retention,
audit, and deletion. Identity evidence and recordings receive the strictest
controls. Every sensitive view/download/review is attributable. Logs and traces
exclude bytes, filenames where identifying, signed URLs, contact details,
document numbers, and provider payloads.

Presigned URLs are dropped from request telemetry at the earliest collection
boundary. Browser responses set safe content disposition/type and `nosniff`.
Objects are excluded from backups or included according to a documented restore
and retention policy; a database restore must not resurrect access to an object
whose deletion is authoritative.

## Reliability and operations

Operators monitor quarantine age/count, scanner latency/error, clean/reject
rates, object-write/read errors, missing-object/metadata mismatches, KMS denies,
egress unknown/partial states, retention backlog, and deletion/hold conflicts.

Scanner outage leaves uploads quarantined. Object storage outage leaves metadata
truth intact and approved content temporarily unavailable. Missing objects are
integrity incidents. Unknown egress is reconciled before restart. Deletion is
idempotent and legal hold fails closed.

See [storage architecture](../aws/storage.md), [documents/media/voice](../architecture/documents-media-voice.md),
[upload quarantine](../runbooks/upload-quarantine.md), and [LiveKit voice](../runbooks/livekit-voice.md).

## Validation

- Extension/MIME/magic mismatch and polyglot test corpus.
- Oversize, truncated, decompression-bomb, and archive policy tests.
- Clean, malware/reject, scanner timeout, retry, and duplicate callback tests.
- Cross-user, cross-tenant, expired, revoked-role, and closed-trip access tests.
- Bucket public-access/policy/KMS negative tests.
- Signed URL expiry, header constraint, and telemetry-redaction tests.
- Thumbnail size, re-encoding, metadata-removal, revision, and memory tests.
- Object-without-metadata and metadata-without-object reconciliation tests.
- Recording consent, egress duplicate/unknown, encryption, playback, retention,
  privacy deletion, and legal-hold exercises.
- Release-artifact scan proving no customer object or signed URL is packaged.

## Follow-up

- Maintain a content-class policy table with accountable owners.
- Exercise scanner and storage outage runbooks regularly.
- Review bucket/KMS/access-analyzer findings and retention jobs.
- Revisit direct-to-S3 upload only with signed upload policy, quarantine, content
  validation, and post-upload authorization intact.
