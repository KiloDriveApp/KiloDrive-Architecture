# Release 1.0.0 Build 97 Architecture Update

This note records the architecture changes that are part of the synchronized
1.0.0+97 release. It is intentionally public-safe: deployment credentials,
customer data, provider payloads and private infrastructure addresses are not
included. The application repository, the API and the country cells are
released from one reviewed source set; `/health/ready` remains the authority
for live schema readiness.

## What changed

### Vehicle and driver onboarding

Vehicle registration and insurance are collected in the vehicle portion of the
driver onboarding journey. A driver with an already compliant registered
vehicle is not sent through a duplicate add-vehicle step. The API validates the
year as a friendly, typed value and limits chassis/VIN input to 19 characters.
Registration and insurance artifacts are stored as private, quarantined
documents and are reviewed independently of upload success. Editing a verified
vehicle resets the relevant verification state and produces a durable review
event.

The mobile client renders vehicle maintenance and compliance as independent
sections. A slow or failed optional maintenance section no longer erases a
successful vehicle list: the last good section remains visible with a partial
error and retry action. Superseded make/model reads are generation-fenced so a
late response cannot replace a newer selection.

### Contract and state discipline

The API continues to expose the existing routes and DTO wire shapes. Validation
errors are stable ProblemDetails responses, OpenAPI is regenerated from the
reviewed contract, and the canonical artifact is checked by SHA-256 in CI.
Flutter uses typed view state for the affected vehicle and onboarding slices,
including loading, empty, ready, partial failure and stale-data states. No
presentation code needs to interpret storage keys or raw JSON maps to render a
vehicle status.

### Schema and release alignment

The MySQL contract for this release is `2026.09.06.3`. The canonical scripts
remain `database/schema.sql` for a fresh install and
`database/full-schema-alignment.sql` for an idempotent upgrade. EF migrations
are not used. Production deployment backs up the database, applies the reviewed
alignment package, verifies the control and country-cell fingerprints, and
checks API readiness before traffic is considered healthy.

## Operational guidance

1. Treat a successful upload as **Submitted**, never **Approved**. Approval is
   an administrator review decision with an audit record.
2. Keep vehicle, registration, fitness and insurance evidence in the country
   cell that owns the operational decision; global identity stores only the
   identity and membership needed to route the request.
3. Use the existing idempotency key and entity revision for retryable vehicle
   mutations. A lost response is reconciled before another mutation is sent.
4. Keep the release APK for device QA and upload only the signed AAB to Google
   Play. Private Dart symbols remain in the release system and are never
   published.
5. If readiness fails after deployment, stop rollout and follow the schema
   alignment and API deployment runbooks. Do not repair a production cell with
   ad-hoc row edits.

## Evidence boundaries

Source tests, OpenAPI verification, manual certification and the deployment
manifest are maintained in the application repository. This architecture
repository records the design and operating rationale; it does not claim that
an external provider, store review or country launch is certified merely
because the code path exists.
