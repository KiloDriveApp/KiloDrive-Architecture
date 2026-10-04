# Field dictionary: G

[Dictionary index](README.md) · [API Guide](../README.md)

Requiredness and nullability below are schema metadata, not a replacement for
workflow validation. Monetary amounts use integer minor units; timestamp fields
use strict UTC parsing. Private tokens, passwords, document references and
personal fields must remain outside public logs and examples.

## GeneratedExportDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | No further constraint recorded |
| `status` | `string` | Yes | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | No further constraint recorded |
| `revision` | `integer (int64)` | Yes | Not declared nullable | Authoritative record revision used for applicable concurrency checks. | No further constraint recorded |
| `reportType` | `string` | Yes | Not declared nullable | Report type text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `format` | `string` | Yes | Not declared nullable | Output/file format selector; use the operation's supported media rather than guessing an extension. | No further constraint recorded |
| `requestedAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for requested at; parse strictly and localize only for display. | No further constraint recorded |
| `sourceAsOfUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for source as of; parse strictly and localize only for display. | No further constraint recorded |
| `availableAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for available at; parse strictly and localize only for display. | No further constraint recorded |
| `downloadExpiresAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for download expires at; parse strictly and localize only for display. | No further constraint recorded |
| `fileName` | `string` | No | Explicitly allowed | Document/file display name; it is not a storage authorization or approved-document status. | No further constraint recorded |
| `contentType` | `string` | No | Explicitly allowed | Content type text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `sizeBytes` | `integer (int64)` | No | Explicitly allowed | Numeric size bytes for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `previousActionCommitted` | `boolean` | Yes | Not declared nullable | Whether previous action committed applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `retryable` | `boolean` | Yes | Not declared nullable | Whether the error permits an applicable retry; it does not authorize a blind second mutation. | No further constraint recorded |
| `nextAction` | `string` | Yes | Not declared nullable | Suggested next workflow step returned by the server; it does not override authorization. | No further constraint recorded |
| `supportReference` | `string` | Yes | Not declared nullable | Support reference text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `downloadUrl` | `string` | No | Explicitly allowed | URL for download; validate the intended origin/access and never assume private links are public. | No further constraint recorded |
| `downloadUrlExpiresAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for download url expires at; parse strictly and localize only for display. | No further constraint recorded |
| `downloadToken` | `string` | No | Explicitly allowed | Private download token used by this specific ceremony; never log, publish or substitute it for another proof. | No further constraint recorded |
| `failureCode` | `string` | No | Explicitly allowed | Failure code text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `campaignId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related campaign record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `campaignRevisionId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related campaign revision record in this model; ownership and scope are checked separately. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## GlobalProductType

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | Membership | Membership state/choice in this specific enum. |
| `2` | DocumentVerification | Document verification state/choice in this specific enum. |
| `3` | Badge | Badge state/choice in this specific enum. |

## GoogleSubscriptionTransitionDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `previousPurchaseHash` | `string` | Yes | Not declared nullable | Previous purchase hash text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `previousProductId` | `string` | Yes | Not declared nullable | Identifier of the related previous product record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `previousBasePlanId` | `string` | Yes | Not declared nullable | Identifier of the related previous base plan record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `replacementMode` | `string` | Yes | Not declared nullable | Replacement mode text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `disclosureCode` | `string` | Yes | Not declared nullable | Disclosure code text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.
