# ADR 012: Native API v1 routes and generated wire contracts

- **Status:** Accepted
- **Date:** 2026-09-23

## Context

Path rewriting made endpoint selection, authorization metadata, Problem Details
instances, OpenAPI and metrics harder to reason about. Hand-written Flutter
wire parsing also allowed enum, timestamp, revision and money handling to drift
between features.

## Decision

ASP.NET Core registers canonical `/api/v1/...` selectors natively from the
reviewed route convention. Versioning middleware emits compatibility lifecycle
headers and telemetry but does not rewrite request paths. The unversioned
`/api/...` alias remains deprecated until 10 February 2027; doubled or malformed
versions are not repaired.

One reviewed OpenAPI v1 artifact and SHA-256 sidecar drive the generated private
Dart wire client. Hand-written feature repositories map wire contracts into
immutable domain/view models. Numeric-enum registries, 64-bit minor-unit money,
strict UTC timestamps, paging, revision fields, idempotency headers and Problem
Details normalization are centralized.

## Consequences

Endpoint metadata and telemetry describe the path actually served. Generated
wire drift fails CI. Unknown enums remain neutral and unsafe actions stay
disabled. Feature code retains meaningful domain models rather than exposing
generated transport objects directly.

Compatibility alias traffic must be measured and removed only after its sunset
gate passes. A breaking public change requires a new major API version.

## Validation

Tests cover canonical, alias, doubled-version, malformed, hub, health, webhook
and unknown paths; authorization/rate-limit metadata; OpenAPI hash drift;
null/missing fields; maximum 64-bit money; stale revisions; added properties;
strict timestamp parsing; and unknown numeric enums.
