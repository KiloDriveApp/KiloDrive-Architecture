# Field dictionary: O

[Dictionary index](README.md) · [API Guide](../README.md)

Requiredness and nullability below are schema metadata, not a replacement for
workflow validation. Monetary amounts use integer minor units; timestamp fields
use strict UTC parsing. Private tokens, passwords, document references and
personal fields must remain outside public logs and examples.

## OnboardingStepDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `code` | `string` | Yes | Not declared nullable | Code in this model's vocabulary; distinguish business/error/catalog codes from confidential verification codes. | No further constraint recorded |
| `documentType` | [DocumentType](d.md#documenttype) | No | Not declared nullable | Document type represented by the `DocumentType` model or enum; use that definition's fields/values. | No further constraint recorded |
| `status` | `string` | Yes | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | No further constraint recorded |
| `reviewNote` | `string` | No | Explicitly allowed | Human-readable reviewer explanation, including remediation where applicable. | No further constraint recorded |
| `updatedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for updated at; parse strictly and localize only for display. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## OpenRentalDisputeDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `reasonCode` | `string` | Yes | Not declared nullable | Stable reason code; map through the applicable reason catalog instead of displaying an unrelated enum. | No further constraint recorded |
| `detail` | `string` | Yes | Not declared nullable | Detail text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `evidence` | [RentalEvidenceInput](r.md#rentalevidenceinput)[] | Yes | Not declared nullable | Collection of evidence for this model; interpret each item through the declared item type. | No further constraint recorded |
| `expectedBookingVersion` | `integer (int32)` | Yes | Not declared nullable | Expected booking version for this model's state or policy; do not substitute a timestamp or mobile build. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## OpenTripDisputeRequest

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `reason` | `string` | Yes | Not declared nullable | Reason supplied or returned for this workflow; follow any catalog/required validation rules. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## OutOfBandStepUpChallengeDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `channel` | `string` | Yes | Not declared nullable | Channel text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `expiresAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for expires at; parse strictly and localize only for display. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.
