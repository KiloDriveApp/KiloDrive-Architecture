# Release 1.0.0 build 116 architecture update

Owner: KiloDrive Engineering, Safety Operations and Privacy Engineering.
Last source review: 13 September 2026.
Environment: reviewed source and production API/schema, verified 13 September 2026.
Evidence: [authoritative source facts](https://github.com/KiloDriveApp/KiloDrive/blob/main/docs/generated/repository-facts.md),
[evidence implementation](https://github.com/KiloDriveApp/KiloDrive/blob/main/src/server/KiloDrive.Api/Services/Voice/TripCallEvidenceService.cs)
and [operational runbook](https://github.com/KiloDriveApp/KiloDrive/blob/main/docs/trip-call-evidence-runbook.md).
Implementation: [reviewed release commit](https://github.com/KiloDriveApp/KiloDrive/commit/b82b7920d354040ef38a3a4fc7ae236dc2a9324d).
Deployment evidence: [owned production verification](https://github.com/KiloDriveApp/KiloDrive/blob/main/docs/releases/release-116-production-verification.md).

| Fact | Value | Authority |
| --- | --- | --- |
| Mobile release | 1.0.0+116 | Flutter pubspec.yaml |
| Schema contract | 2026.09.13.1 | SchemaContract.CurrentVersion |
| Public REST | /api/v1 | Reviewed OpenAPI v1 |
| API inventory | 723 paths, 814 operations | Source-generated repository facts |
| OpenAPI SHA-256 | 66b68b440668f4f0f31092cf1cdfff5334c81227ff1195316d64dbfa85129d46 | Reviewed artifact and sidecar |
| Mobile languages | English, Spanish, French, Japanese, Simplified Chinese, Traditional Chinese | ARB configuration |

## Trip-call evidence owns a separate retention boundary

Each call snapshots caller and callee user IDs and roles, the trip, tenant,
country and provider session. Lifecycle transitions append ring, consent,
connected and explicit terminal events in the country-cell transaction.
Server timestamps, duration, provider/realtime event references and policy
versions travel with the evidence. EF save guards reject participant identity
changes and updates or deletes of evidence events.

Each event stores a canonical payload hash, the preceding event hash, a
sequence number, the event hash and an HMAC signature with its key ID.
Timestamp canonicalization uses UTC and MySQL microsecond precision so a
database round trip cannot invalidate an otherwise intact chain. Retained
verification keys support rotation without invalidating older evidence.
An empty, truncated or altered chain is never reported as intact.

Investigators need a SystemAdmin role, the required capability, the selected
tenant boundary, recent two-factor verification and a documented purpose.
The action-specific proof is mandatory on reads and mutations, regardless of
whether the account has enrolled an authenticator; no enrollment fallback grants
unverified access. Generated OpenAPI and Dart clients mark that header required.
Every read records access. Decisions reload state after acquiring the trip
lock so concurrent investigators cannot publish competing decisions. The
requester cannot approve the request; a separate investigator records
fulfilment while preserving the approval reason. Fulfilment records an
operational action; an authorized export process performs the actual transfer.

Routine evidence follows the approved one-month metadata schedule, independently
of recording retention. A country-cell worker checks expiry hourly and removes
eligible evidence, access history and completed disclosure rows atomically.
It rechecks evidence and recording holds and unresolved disclosures under the
same trip lock. The minimized erasure audit retains the final chain hash and
removed-row count. Ordinary call history keeps its own operational policy.
Audio recording remains disabled; this release adds no audio transcript.

SOS and suspected-collision events can reference an originating call. The
server proves participant ownership and the shared trip/tenant before appending
an emergency escalation event in the safety transaction. Notification delivery
and human emergency response retain their separate operational responsibilities.

## Release-history consolidation preserves source descriptions

Builds 111, 113, 114 and 115 are consolidated into build 116. Build 110 is
consolidated into build 109. Each source locale retains its original summary
and description as an improvement entry. Existing improvement and governance
references move before source parents are deleted. Display dates converge on
the destination build's most recent release date. Transactional scripts and
deterministic markers make canonical seed replay converge on the same result.

## Verification and operating limits

Production readiness returned Healthy with the reviewed schema contract valid.
Admin, driver and rider sign-in and the safety/incoming-call read routes passed
smoke checks. An authenticated investigator request without its fresh proof
returned Forbidden. Release 116 and 109 are published; consolidated source build
detail routes are absent. The corporate build 116 changelog is published.
The final server suite passed 4,730 tests with no failures; 74 integration cases
requiring dedicated environments were skipped, not certified by this release.

Verification includes hash tampering, MySQL timestamp materialization, rotated
keys, immutable role snapshots, retention holds, open disclosures and explicit
terminal-event mappings. Runtime composition keeps the evidence expiry worker
inside the country-cell worker profile. Source verification and signed Android
artifacts do not imply store approval or physical two-device certification.

Production signing material belongs in the secret manager and restricted
deployment configuration. It is never included in source, documentation,
release packages or investigator responses. Operators must preserve retained
keys while any signed evidence or legal hold still depends on them.
