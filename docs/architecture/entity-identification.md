# Entity Identification

## Why KiloDrive has more than one kind of identifier

An identifier has a job. The ID that makes a database index behave well is not
necessarily the ID a rider should read over the phone to support. A payment
provider's transaction reference is not an authorization token. A correlation
ID should help trace one request without exposing the user's email.

KiloDrive separates those jobs instead of forcing one identifier to do all of
them.

| Identifier | Main purpose | Typical visibility | Security meaning |
| --- | --- | --- | --- |
| UUIDv7 | Authoritative entity identity | Authorized API payloads and internal links | None by itself; ownership is checked separately |
| Friendly user ID (`KD-XXXXXXXXXX`) | Human support lookup | User and authorized support staff | Public-ish reference, never a login secret |
| Five-character ticket reference | Readable support conversation reference | Ticket participants and support staff | Not proof of ticket access |
| Stable catalogue code | Country, currency, vehicle class, or reference data | Public where appropriate | None |
| Entity version | Order concurrent/realtime changes | API contract for mutable entities | Prevents stale update, not caller authentication |
| Idempotency key | Identify one caller's mutation attempt | Request metadata and protected operational records | Scoped replay control; treat as confidential metadata |
| Correlation ID | Trace one request across components | Response header and sanitized telemetry | Diagnostic only |
| Provider reference | Reconcile an external operation | Restricted operations and accounting | Must be validated against provider evidence |

## UUIDv7 in plain language

RFC 9562 UUID version 7 puts a Unix-epoch millisecond timestamp in the most
significant portion of the UUID and keeps the remaining bits for the version,
variant, and randomness. It still looks like an ordinary UUID:

```text
0195f4aa-6d2e-7abc-8def-0123456789ab
```

The `7` at the start of the third group identifies version 7. The example is
illustrative and does not identify a KiloDrive record.

KiloDrive creates new externally exposed, transactional, and security-sensitive
records with .NET's `Guid.CreateVersion7()` through the small `Uuid7.NewGuid()`
wrapper. The wrapper also gives architecture tests one policy point to inspect.

### Why time ordering helps MySQL

A B-tree index stores keys in sorted pages. Random UUIDv4 inserts land all over
the tree. Under sustained writes, that tends to cause page splits, cache churn,
fragmentation, and less predictable write latency.

UUIDv7 values generated around the same time share a leading timestamp. New
keys therefore arrive near the growing edge of a sorted index more often. The
benefits are especially useful for outbox messages, audit events, bids,
transactions, and telemetry samples that are created continuously.

KiloDrive currently maps GUID keys as canonical `char(36)` values with an ASCII
collation in MySQL. UUIDv7's canonical text form preserves timestamp-first
sorting, so it still improves locality compared with UUIDv4. A future move to
`binary(16)` could reduce storage and index width, but it would be a measured,
expand/contract migration—not a reason to hand-convert bytes in feature code.

### What UUIDv7 does not provide

- It is not fully monotonic within the same millisecond across every process.
- Its timestamp is not an audited `CreatedAtUtc` value.
- Its random portion does not grant access.
- It does not replace a unique business reference.
- It does not order events from machines whose operations have different
  causal histories.

Use the explicit timestamp for display and retention, a persisted entity version
for realtime merge ordering, and authorization predicates for access.

## A worked B-tree example

Imagine a ride-alert table receiving five inserts:

```text
UUIDv4:  f2..., 18..., a9..., 4c..., d1...
UUIDv7:  0195...01, 0195...02, 0195...03, 0195...04, 0195...05
```

The UUIDv4 keys are likely to touch unrelated leaf pages. The UUIDv7 keys are
likely to cluster. This does not make an inefficient query fast: an index such
as `(TenantId, Status, CreatedAtUtc)` may still be the correct access path.
UUIDv7 improves the primary and foreign-key insertion shape; it is not an excuse
to omit query-specific indexes.

## When not to generate a new UUID

Stable catalogues may use a reviewed business code. A country code should remain
`JM`; generating a UUID every time a seed runs would make foreign references
unusable. The same principle applies to deterministic product and reference
codes.

For transactional rows, never call a fresh generator during an idempotent retry
unless the operation has proved no row already exists. The idempotency record or
business reference should lead back to the original entity.

## Friendly user IDs

People should not have to read a 36-character UUID to support. New KiloDrive
users receive a display ID shaped like:

```text
KD-7M4Q2R9X3A
```

The ten-character body uses an uppercase, unambiguous alphabet. Characters that
are easy to confuse over a phone call—such as `I`, `L`, `O`, and `U`—are
excluded. The database applies a unique index, which is the final authority on
uniqueness.

Friendly IDs follow four rules:

1. They are immutable once published.
2. They are never accepted as proof that the caller owns the account.
3. Support lookup is authenticated, permission-checked, rate-limited, and
   audited.
4. The UUIDv7 remains the foreign-key and API identity.

Friendly IDs are nullable in some storage mappings for rolling compatibility
with older rows, but all new creation paths assign one. A data-quality check
should find and backfill legacy gaps through a reviewed process.

### Collision handling

Randomness makes a collision unlikely; “unlikely” is not the same as
“impossible.” Keep the unique constraint. A creation workflow that encounters
that specific unique-key conflict should generate a new friendly value and
retry the small identity write, not relax the constraint or retry the whole
business operation blindly.

## Ticket references

Support tickets use a five-character, uppercase reference designed for a short
conversation. A process-local monotonic sequence starts at a random point and
the database-level uniqueness boundary protects cross-process allocation. The
allocator checks the intended tenant scope before returning a candidate.

Five characters are convenient but much smaller than UUID space. Consequently:

- references are scoped by tenant where the schema defines that scope;
- the UUID remains the authoritative ticket ID;
- ticket lookup returns coarse errors;
- repeated lookup attempts are rate-limited and anomaly-monitored; and
- a reference never authorizes reading messages or attachments.

The common mistake is to treat “hard for a normal person to guess” as “secret.”
Short support codes are designed to be readable, so build authorization as if
the code were already known.

## Correlation IDs

A correlation ID follows a request through the edge, API, portal, outbox, and
provider attempt metadata. Middleware accepts only a validated value or creates
a new one, returns it in the response, and preserves it even when an exception
handler clears a partial response.

A good correlation record says:

```text
operation=ride.accept
outcome=conflict
correlation=<validated opaque value>
country=<authorized context>
```

A bad record includes the bearer token, chat message, document path, phone
number, or full request body. Correlation is useful precisely because engineers
can join safe metadata without logging customer content.

Correlation IDs also have limits. A client can reuse one, so they are not unique
business references and cannot prove causality on their own.

## Idempotency keys

Mobile networks fail in awkward places. A rider can submit a transfer, lose the
response, and tap again. An idempotency key tells the server that both HTTP
attempts represent one logical mutation.

KiloDrive scopes an idempotency record to the tenant and caller, stores a payload
fingerprint, leases execution, and records the completed response. The expected
outcomes are:

- same key and same payload after completion: replay the result;
- same key while another execution is active: return a controlled conflict;
- same key with a different payload: reject it;
- server exception before a safe completion: release or expire the claim under
  the idempotency policy.

Idempotency does not prevent two users from accepting the same ride. That is the
job of a conditional state/version update inside a transaction. Mature mutation
handlers frequently need both controls:

```text
idempotency key  -> “did this caller already make this request?”
entity version   -> “is the business state still the one they acted on?”
```

## Persisted entity versions

Realtime messages may arrive twice or out of order. Mutable realtime entities
therefore use a persisted, monotonic version. A client merges an event only when
its entity version is newer than the local version.

Do not derive an entity version from wall-clock ticks. Clocks can move, API nodes
can disagree, and two writes can occur at the same apparent time. Increment the
version as part of the same conditional database update that changes state.

A typical write shape is:

```sql
UPDATE SomeEntity
SET Status = @nextStatus,
    Version = Version + 1
WHERE Id = @id
  AND TenantId = @tenantId
  AND Version = @expectedVersion
  AND Status = @expectedStatus;
```

Zero affected rows becomes a stable conflict response. It should not silently
overwrite a newer decision.

## Provider references

Payment, store, messaging, and voice providers return their own identifiers.
KiloDrive stores only the identifiers needed for status, reconciliation, and
support. A provider reference is mapped to a local payment or attempt under an
explicit provider and tenant/country context.

Never assume two providers use the same namespace. A unique constraint should
usually include provider plus provider reference, or point through a local
payment ID. Webhook handling verifies the provider signature before trusting the
reference and remains idempotent if the provider sends events again or out of
order.

## Identifiers and privacy

An opaque ID can still be personal data when it consistently singles out a
person. KiloDrive therefore follows these practices:

- do not use user IDs as analytics advertising identifiers;
- do not place access or refresh tokens in query strings;
- do not embed emails or phone numbers in object keys, queue names, or
  correlation IDs;
- use coarse, authorized support lookup responses;
- expire public sharing handles and provide explicit revocation;
- redact or hash destinations used for fraud correlation; and
- avoid publishing real IDs in documentation, screenshots, or fixture evidence.

## Common mistakes

### Using `Guid.NewGuid()` in a new entity path

It quietly reintroduces random UUIDv4 write patterns and bypasses the policy
tests. Use `Uuid7.NewGuid()` for new transactional and exposed entities.

### Parsing creation time from the UUID

The timestamp portion is useful for ordering, not a replacement for the row's
UTC audit timestamp. Import, restoration, or regenerated IDs can tell a
different story from the business event.

### Returning a different error for a foreign ID

“Exists but forbidden” tells an attacker the record exists. Ownership-sensitive
lookups generally include the owner in the query and return the same coarse
not-found result for missing and foreign records.

### Displaying UUIDs to support staff by default

It increases transcription errors and encourages staff to paste internal IDs
into chat. Show the friendly user or ticket reference, with the UUID available
only in a protected diagnostic view when genuinely needed.

### Reusing the idempotency key for an edited form

The server correctly rejects a changed payload under an old key. The client
should create the key for one logical submission, retain it across transport
retry, and replace it when the user makes a materially new decision.

## Review checklist

- Is this a transactional entity, stable catalogue, human reference, provider
  reference, or diagnostic identifier?
- Does it use UUIDv7 when required?
- Is there a separate `CreatedAtUtc` and, for mutable realtime state, a version?
- What is the database uniqueness scope?
- How does a collision or duplicate webhook behave?
- Does lookup include tenant and owner, not only the ID?
- Is a short code being mistaken for a secret?
- Can this value enter logs, URLs, screenshots, or public documentation safely?
- Does retry return the original entity rather than generate a second ID?

## Related reading

- [UUIDv7 decision record](../adr/002-uuidv7-identifiers.md)
- [Tenancy and country cells](tenancy-and-country-cells.md)
- [Schema lifecycle](../database/schema-lifecycle.md)
- [System context](system-context.md)
