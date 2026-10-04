# Wire conventions: identifiers, money, dates and enums

[API Guide](README.md)

## JSON and typed models

The curated OpenAPI uses OpenAPI 3.0.1. Required fields, nullable fields,
formats, arrays and referenced DTOs come from the reviewed source artifact.
Do not treat an omitted optional property, `null`, an empty string, zero and an
empty array as interchangeable. An omitted update field can mean something
different from explicitly clearing it.

Object schemas frequently declare `additionalProperties: false`. Send the
defined model, not an arbitrary dictionary of guessed fields. Validation and
business requirements can be stricter than generated schema metadata. The
[limitations chapter](coverage-and-limitations.md) explains this distinction.

## IDs and references

Resource IDs generally use canonical UUID strings, with externally exposed
transactional IDs generated as UUIDv7. Treat them as opaque and preserve them
exactly. Static catalog business codes, trace numbers, cursors, storage
references and provider product IDs have their own formats; they are not
interchangeable UUIDs.

An operation reference identifies durable command evidence. An idempotency key
identifies the client's logical request. A payment ID identifies a payment.
A trace number supports a customer-facing investigation. Keep these fields
distinct and never substitute one merely because it looks similar.

## Money remains integer minor units

Amounts such as `balanceMinor`, `amountMinor`, fees and fares are signed 64-bit
integers in the accompanying currency's minor units. Use integer or decimal-safe
conversion; never perform a wallet calculation in binary floating point.
JavaScript clients must also guard values beyond the language's safe integer
range. A documented `int64` must not silently become an imprecise `Number`.

For a two-decimal currency, an illustrative `100000` minor-unit amount displays
as `1,000.00`. A whole-unit display such as `1,000` is a presentation choice,
not a different stored amount. The currency code must remain visible when the
symbol could be ambiguous. Never assume `$` means USD.

| Layer | Example | Rule |
| --- | --- | --- |
| Wire amount | `100000` plus `USD` | Integer minor units |
| US-style display | `USD 1,000.00` | Locale/user separator style |
| Alternative separator display | `USD 1.000,00` | Same value, different presentation |
| Editing field | User types digits; grouping appears automatically | Parse through one currency-aware formatter, preserving cursor and decimals |
| Financial export | Amount plus explicit ISO currency | Do not drop currency or change authoritative precision |

The app's money-format preference changes grouping and decimal presentation.
It does not change the wallet currency, quoted amount, FX source or settlement
rules. Apply it consistently to fares, top-ups, transfers, withdrawals, tips,
membership prices, receipts and aggregate metrics. Keep display strings out of
mutation DTOs.

FX rates can appear as JSON numeric reference fields in current DTOs. They are
not monetary amounts. Use server-owned quotes and the returned amount/fee
snapshots, rather than multiplying displayed rates with floating-point math.
See [money and memberships](money-and-memberships.md).

## Timestamps and calendar dates

Timestamp fields such as `createdAtUtc` are UTC instants; date-only fields such
as a licence expiry have calendar-date semantics. Do not turn a date-only
document expiry into a UTC midnight that displays on the previous day.

Parse timestamps with centralized strict/nullable UTC helpers. Missing or
malformed input means unknown/unavailable. Never substitute the current time,
trim an ISO substring or label a localized time as UTC.

The consumer app uses its centralized locale/date/time preferences for display.
Administrative views and country-bound exports use the documented affected-user
or selected IANA timezone. A country-bound export uses the user's country
timezone and the established 12-hour AM/PM presentation. Label timezone context
where it matters; include an offset or zone in investigation evidence.

Day boundaries used for filters and membership usage must follow the endpoint's
documented semantics. A device's visual date preference cannot redefine a
server settlement period, expiry instant or report range.

## Numeric enums

API enums serialize as numbers. Convert them with a domain-specific exhaustive
mapping; never display a bare number or borrow another enum's labels.

Small verified examples from this source snapshot are:

| Enum | Verified values | Caution |
| --- | --- | --- |
| Consumer registration role | Passenger = 1; Driver = 2 | Wider identity roles in the schema do not authorize administrative registration |
| Payment method | Cash = 1; Wallet = 2; Card = 3; External = 4 | A numeric option does not prove that provider is enabled |
| Push platform | iOS = 1; Android = 2; Web = 3 | App/channel authority comes from verified evidence, not this number |

A future unknown enum value renders **Unknown or unavailable**, disables unsafe
actions and produces a sanitized diagnostic. It must not crash a list, become
the first enum entry, or default to an approved/paid/active state.

Some explicitly defined permission/weekday types are flag sets. Their named
constants describe bits and aggregate choices; use the corresponding source
registry and permitted-bit validation. Do not combine ordinary trip/payment
status numbers as flags. Generated enum metadata can list named constants
without expressing every valid combination, so compare that model with the
owning workflow before generating a strict validator.

## Response headers

The endpoint pages list headers recorded in their response metadata. Their
cross-cutting meanings are:

| Header | Meaning | Client handling |
| --- | --- | --- |
| `Retry-After` | Server-directed backoff for throttling or applicable pending work | Honor it rather than starting parallel retries |
| `Idempotent-Replayed` | The response came from the existing operation's replay path | Do not count it as a second transaction |
| `X-Operation-Reference` | Durable reference for the logical operation where supplied | Keep it with the original pending operation for outcome discovery |
| `X-Recovery-Operation-Reference` | Reference exposed for the supported recovery boundary | Use owner-scoped recovery; it is not authorization by itself |
| `ETag` | Strong authoritative resource revision where published | Use it as the declared `If-Match` precondition for a new edit |
| `X-Entity-Revision` | Authoritative revision value where published | Do not substitute a display timestamp or app build |
| `X-KiloDrive-Support-Code` | Sanitized support code from applicable failure enrichment | Retain with safe correlation context for troubleshooting |
| `X-KiloDrive-Warning-Codes` | Applicable successful-response warning references | Show relevant degraded/pending behavior rather than assuming complete success |

The last two describe reviewed result-filter behavior and may not appear in
each operation's generated header metadata. Header omission is not evidence
that a mutation was never executed.

## Headers and transport

Use HTTPS and the canonical path. Do not forward account, installation or
attestation credentials to another origin following an unexpected redirect.
Respect `Content-Type`, declared binary response media and server cache policy.
Record safe correlation/support identifiers for diagnostics rather than raw
request bodies.

`Idempotency-Key` and applicable `If-Match` headers are mutation controls.
`ETag` and `X-Entity-Revision` identify an authoritative revision where exposed.
`Retry-After` controls backoff. A field's presence in JSON is not a substitute
for a required HTTP precondition header.
