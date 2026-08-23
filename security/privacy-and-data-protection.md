# Privacy and Data Protection

## Data minimization

KiloDrive separates global identity, country operations, telemetry, audit,
provider attempts, and private artifacts. Each processor receives only the data
required for its function. Public identifiers and support references reduce the
need to disclose contact details.

## Location

Location is collected for user-requested route, matching, safety, trip, delivery,
and rental functions. Fresh high-frequency driver telemetry is short-lived in
Valkey and only the operational evidence required by policy is persisted.
Trip-sharing handles disclose bounded coarse data, expire, and can be revoked.

## Documents and recordings

Identity and vehicle documents are private, authorization-gated, scanned, and
audited. Call recording is configurable, consent-based, visibly indicated, and
subject to jurisdiction, retention, deletion, and legal-hold rules. Neither
document contents nor recordings enter operational logs.

## Retention and rights

Retention is defined by content class and legal/financial necessity. The global
privacy/deletion orchestrator coordinates country checkpoints, while country
cells perform local trip/financial anonymization or retention. Deletion does not
erase records that lawfully require retention; access is narrowed and data is
anonymized where appropriate.

## Tracking and analytics

Operational analytics are minimized and configured according to consent and
platform declarations. Data used only to provide KiloDrive functionality is not
represented as cross-company advertising tracking. Store privacy labels must
match actual code and provider use.
