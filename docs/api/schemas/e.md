# Field dictionary: E

[Dictionary index](README.md) · [API Guide](../README.md)

Requiredness and nullability below are schema metadata, not a replacement for
workflow validation. Monetary amounts use integer minor units; timestamp fields
use strict UTC parsing. Private tokens, passwords, document references and
personal fields must remain outside public logs and examples.

## EffectiveNotificationPreferencesDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `tripCalls` | `boolean` | Yes | Not declared nullable | Whether trip calls applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `bidsAndAssignments` | `boolean` | Yes | Not declared nullable | Whether bids and assignments applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `tripStatus` | `boolean` | Yes | Not declared nullable | Whether trip status applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `chat` | `boolean` | Yes | Not declared nullable | Whether chat applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `deliveries` | `boolean` | Yes | Not declared nullable | Whether deliveries applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `walletAndMembership` | `boolean` | Yes | Not declared nullable | Whether wallet and membership applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `safety` | `boolean` | Yes | Not declared nullable | Whether safety applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `security` | `boolean` | Yes | Not declared nullable | Whether security applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `promotions` | `boolean` | Yes | Not declared nullable | Whether promotions applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `vibration` | `boolean` | Yes | Not declared nullable | Whether vibration applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `readAloud` | `boolean` | Yes | Not declared nullable | Whether read aloud applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `quietHoursStartMinutes` | `integer (int32)` | No | Explicitly allowed | Quiet hours start, measured in minutes. | No further constraint recorded |
| `quietHoursEndMinutes` | `integer (int32)` | No | Explicitly allowed | Quiet hours end, measured in minutes. | No further constraint recorded |
| `quietHoursTimeZone` | `string` | No | Explicitly allowed | Quiet hours time zone text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `presentationControlsAvailable` | `boolean` | Yes | Not declared nullable | Whether presentation controls available applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `mandatoryCategories` | `string[]` | Yes | Not declared nullable | Collection of mandatory categories for this model; interpret each item through the declared item type. | No further constraint recorded |
| `updatedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for updated at; parse strictly and localize only for display. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## EmailTripReceiptDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `emailAddress` | `string` | Yes | Not declared nullable | Email address text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## EmergencyNumberDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `countryCode` | `string` | Yes | Not declared nullable | Country ISO code for this model/context; it cannot override authenticated country authority. | No further constraint recorded |
| `number` | `string` | Yes | Not declared nullable | Number text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## EndVoiceCallRequest

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `tripId` | `string (uuid)` | Yes | Not declared nullable | Accepted trip record, distinct from the originating ride request. | No further constraint recorded |
| `callId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related call record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `reason` | `string` | No | Explicitly allowed | Reason supplied or returned for this workflow; follow any catalog/required validation rules. | No further constraint recorded |
| `providerEventId` | `string` | No | Explicitly allowed | Identifier of the related provider event record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `realtimeEventId` | `string` | No | Explicitly allowed | Identifier of the related realtime event record in this model; ownership and scope are checked separately. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## EscalateSupervisedTripDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `reason` | `string` | Yes | Not declared nullable | Reason supplied or returned for this workflow; follow any catalog/required validation rules. | No further constraint recorded |
| `expectedRevision` | `integer (int64)` | Yes | Not declared nullable | Revision the caller read for this logical update; retain the original during uncertain-outcome recovery. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## ExternalEvidenceConfidenceLevel

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | Low | Low state/choice in this specific enum. |
| `2` | Medium | Medium state/choice in this specific enum. |
| `3` | High | High state/choice in this specific enum. |
