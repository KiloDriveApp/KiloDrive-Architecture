# ADR 002: RFC 9562 UUIDv7 for transactional identifiers

- **Status:** Accepted
- **Date:** 2026-08-23
- **Decision owners:** Architecture and Database
- **Related systems:** API domain entities, MySQL indexes, public contracts, fixtures

## Context

KiloDrive needs identifiers that can be generated independently on multiple API
nodes, remain unique across country cells, travel safely through JSON and URLs,
and avoid the predictable enumeration of integer primary keys.

Random UUIDv4 meets distribution and opacity goals, but sustained random inserts
scatter across B-tree pages. Auto-increment integers have excellent locality but
are database-bound, easy to enumerate, and awkward when fixtures or distributed
producers need to allocate an ID before insertion.

Support staff also need a readable account/ticket reference. A 36-character UUID
is poor human interface, so machine and human identifiers must remain separate.

## Decision drivers

- Multi-node ID generation without a central sequence call.
- Better insertion locality than UUIDv4.
- Standards-based support in the .NET runtime.
- Stable JSON/database representation across cells.
- No reliance on an identifier as authorization.
- Human support references that do not expose contact details.
- Safe idempotent creation and fixture generation.

## Decision

New externally exposed, security-sensitive, and transactional KiloDrive entities
use RFC 9562 UUID version 7, generated through `Uuid7.NewGuid()`, which delegates
to .NET's `Guid.CreateVersion7()`.

The reviewed MySQL mapping stores canonical UUID text in `char(36)` with an ASCII
collation. The leading millisecond timestamp keeps canonical UUIDv7 values
roughly creation-ordered and improves B-tree insertion locality compared with
UUIDv4.

Static catalogues may use stable reviewed business codes. Existing identifiers
are not rewritten merely to achieve uniformity.

Human lookup uses separate values:

- friendly user IDs have `KD-` plus ten unambiguous uppercase characters; and
- support tickets have a five-character uppercase reference in their intended
  uniqueness scope.

The database UUID remains the authoritative identity and foreign key.

## Alternatives considered

### Auto-increment `bigint`

Excellent index locality and compact storage. Rejected as the platform-wide
identifier because allocation depends on one database, values reveal rough
cardinality/order, and merging fixture/cell data is harder. It remains suitable
for purely internal sequence numbers where those concerns do not apply.

### UUIDv4

Well supported and highly random, but produces random B-tree insertion patterns.
Existing UUIDv4 values remain valid; new transactional creation follows v7.

### ULID

Readable, sortable, and widely used. Not chosen because UUIDv7 is now an RFC,
has direct .NET runtime support, and fits existing GUID contracts and EF
mappings without introducing another identifier type.

### Snowflake-style 64-bit IDs

Compact and ordered, but require careful worker-ID/time coordination and expose
more structure. Clock rollback and worker configuration become availability
concerns. The extra operational component is not justified here.

### Database-generated `UUID()`

Keeps generation in MySQL but makes the application unable to reference related
new entities before insertion and does not guarantee the required v7 policy.
Database scripts for static legacy seeds may still contain reviewed stable IDs;
application transactional paths use the wrapper.

## Consequences

### Benefits

- Independent ID generation across nodes and cells.
- Improved B-tree locality under time-progressing writes.
- Existing GUID API and EF tooling remain usable.
- IDs remain opaque enough to avoid simple integer enumeration.
- One architecture test can flag new `Guid.NewGuid()` creation sites.
- Friendly support references can evolve without changing foreign keys.

### Costs and risks

- `char(36)` indexes are wider than `binary(16)` or `bigint`.
- UUIDv7 leaks approximate creation time. Sensitive APIs must not expose IDs
  unnecessarily.
- Values created in the same millisecond are not a causal event sequence.
- Clock behavior affects ordering; explicit UTC timestamps and entity versions
  remain required.
- Friendly IDs and short ticket references need unique constraints and collision
  handling.

## Security, privacy, and compliance

UUIDv7 is not an access-control mechanism. Every lookup includes tenant,
participant/owner, role, and relevant state. Ownership-sensitive endpoints
return a coarse not-found response for missing and foreign IDs.

The timestamp portion can reveal approximate record age, so public responses
include only identifiers needed by the workflow. IDs are still personal data
when they single out a user and are not used as advertising/tracking IDs.

Friendly IDs contain no email or phone number and are safe to read to authorized
support. Short references are rate-limited and never authorize access.

## Reliability and operations

- Keep database unique constraints as the final collision guard.
- Retry only the specific friendly-reference allocation on a collision; do not
  blindly replay a larger committed operation.
- Preserve IDs during idempotent retry and event replay.
- Use `CreatedAtUtc` for retention/audit and persisted versions for realtime
  merge ordering.
- Monitor primary/index growth and page behavior before proposing `binary(16)`.

A future binary-storage migration would use expand/contract with dual
representation/backfill and byte-order tests. Feature code must not invent a
database-specific byte shuffle.

## Validation

- Tests assert generated GUIDs are version 7 and progress in expected temporal
  order across ordinary calls.
- Architecture/static tests reject new transactional `Guid.NewGuid()` sites.
- MySQL clone tests verify collation, length, unique/FK behavior, and canonical
  round trip.
- Idempotency tests prove retry returns the same entity ID.
- Cross-user authorization tests prove a known UUID grants no access.
- Friendly user/ticket allocation tests cover format, ambiguous characters, and
  uniqueness conflict.

## Follow-up

- Keep [entity identification](../architecture/entity-identification.md)
  examples aligned with the implementation.
- Benchmark storage/index cost before considering `binary(16)`.
- Document any justified catalogue or legacy exception at its creation site.
