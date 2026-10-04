# Field dictionary: H

[Dictionary index](README.md) · [API Guide](../README.md)

Requiredness and nullability below are schema metadata, not a replacement for
workflow validation. Monetary amounts use integer minor units; timestamp fields
use strict UTC parsing. Private tokens, passwords, document references and
personal fields must remain outside public logs and examples.

## HouseholdAccountDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | No further constraint recorded |
| `name` | `string` | Yes | Not declared nullable | Name of the record described by this model; distinct from its opaque ID. | No further constraint recorded |
| `countryCode` | `string` | Yes | Not declared nullable | Country ISO code for this model/context; it cannot override authenticated country authority. | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | No further constraint recorded |
| `status` | [HouseholdStatus](h.md#householdstatus) | Yes | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | No further constraint recorded |
| `availableBalanceMinor` | `integer (int64)` | Yes | Not declared nullable | Available balance in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `heldBalanceMinor` | `integer (int64)` | Yes | Not declared nullable | Funds reserved by applicable holds/escrow; they are not freely spendable. | No further constraint recorded |
| `version` | `integer (int64)` | Yes | Not declared nullable | Version in this model's domain; not automatically an API major version. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## HouseholdConsentState

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`, `4`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | Pending | Pending state/choice in this specific enum. |
| `2` | Accepted | Accepted state/choice in this specific enum. |
| `3` | Revoked | Revoked state/choice in this specific enum. |
| `4` | NotApplicable | Not applicable state/choice in this specific enum. |

## HouseholdMemberRole

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`, `4`, `5`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | Owner | Owner state/choice in this specific enum. |
| `2` | Guardian | Guardian state/choice in this specific enum. |
| `3` | Adult | Adult state/choice in this specific enum. |
| `4` | Dependent | Dependent state/choice in this specific enum. |
| `5` | Delegate | Delegate state/choice in this specific enum. |

## HouseholdStatus

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`, `4`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | PendingConsent | Pending consent state/choice in this specific enum. |
| `2` | Active | Active state/choice in this specific enum. |
| `3` | Suspended | Suspended state/choice in this specific enum. |
| `4` | Closed | Closed state/choice in this specific enum. |
