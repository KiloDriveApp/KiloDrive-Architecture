# Entity Identification

## Identifier classes

KiloDrive separates machine identifiers from human support references.

| Identifier | Use | Disclosure |
| --- | --- | --- |
| UUIDv7 | Security-sensitive and transactional entities | May appear in authorized API contracts |
| Stable catalogue code | Countries, currencies, vehicle/reference catalogues | Public where appropriate |
| Friendly user ID | Human support lookup without sharing an email or phone | User and authorized support staff |
| Ticket reference | Short, uppercase, human-readable support reference | Ticket participants and support staff |
| Provider ID | Reconciliation with an external provider | Restricted operations data |
| Correlation ID | Trace a request safely across components | May be returned to the caller |
| Idempotency key | De-duplicate one caller's mutation | Confidential request metadata |

## UUIDv7 policy

New externally exposed, security-sensitive, and transactional records use RFC
9562 UUIDv7 values. Their time ordering improves index locality, but IDs are not
authorization tokens and possession never grants access. Static catalogues may
retain reviewed business codes.

## Human references

Friendly identifiers improve support usability while reducing dependence on
personal contact data. They are generated, unique in their intended scope,
immutable after publication, and resolved only through authorized endpoints.
Short references are not used as secrets; lookup endpoints are rate limited and
return coarse errors.

## Entity versioning

Realtime-capable entities use persisted monotonic versions. Clients merge an
event only when its version is newer than the local entity. Wall-clock time is
metadata, not an ordering primitive.

## Audit identity

Audit records distinguish actor, subject, owner type, action, outcome, device,
network metadata, country/tenant context, and correlation ID. Public runbooks do
not publish the exact audit schema or customer values.
