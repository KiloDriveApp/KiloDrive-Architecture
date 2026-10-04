# Field dictionary: N

[Dictionary index](README.md) · [API Guide](../README.md)

Requiredness and nullability below are schema metadata, not a replacement for
workflow validation. Monetary amounts use integer minor units; timestamp fields
use strict UTC parsing. Private tokens, passwords, document references and
personal fields must remain outside public logs and examples.

The explanation basis distinguishes model-specific meaning, shared conventions,
name-derived units and type-only entries awaiting semantic review. See the
[coverage report](../reference/coverage.md); field presence is not semantic completeness.

## Models on this page

- [NameChangeRequestDto](#namechangerequestdto)
- [NearbyDriverDto](#nearbydriverdto)
- [NotificationCenterItemDto](#notificationcenteritemdto)
- [NotificationCenterPageDto](#notificationcenterpagedto)
- [NotificationCenterSeekPageDto](#notificationcenterseekpagedto)
- [NotificationPreferencesDto](#notificationpreferencesdto)

## NameChangeRequestDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `userId` | `string (uuid)` | Yes | Not declared nullable | Related account identity; the server still proves the caller's ownership or permitted relationship. | Shared convention | No further constraint recorded |
| `supportTicketId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related support ticket record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `currentFirstName` | `string` | Yes | Not declared nullable | Current first name text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `currentLastName` | `string` | Yes | Not declared nullable | Current last name text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `requestedFirstName` | `string` | Yes | Not declared nullable | Requested first name text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `requestedLastName` | `string` | Yes | Not declared nullable | Requested last name text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `identityFileRef` | `string` | Yes | Not declared nullable | Identity file ref text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `reason` | `string` | Yes | Not declared nullable | Reason supplied or returned for this workflow; follow any catalog/required validation rules. | Shared convention | No further constraint recorded |
| `status` | `string` | Yes | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | Shared convention | No further constraint recorded |
| `reviewNote` | `string` | No | Explicitly allowed | Human-readable reviewer explanation, including remediation where applicable. | Shared convention | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for created at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `revision` | `integer (int64)` | No | Not declared nullable | Authoritative record revision used for applicable concurrency checks. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## NearbyDriverDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `driverProfileId` | `string (uuid)` | Yes | Not declared nullable | Driver-profile record associated with this operation or result. | Shared convention | No further constraint recorded |
| `latitude` | `number (double)` | Yes | Not declared nullable | Latitude in degrees for the location represented by this model. | Shared convention | No further constraint recorded |
| `longitude` | `number (double)` | Yes | Not declared nullable | Longitude in degrees for the location represented by this model. | Shared convention | No further constraint recorded |
| `rating` | `number (double)` | Yes | Not declared nullable | Numeric rating for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `distanceMeters` | `number (double)` | Yes | Not declared nullable | Distance represented by this model, in metres; its source/assessment depends on the operation. | Shared convention | No further constraint recorded |
| `locationVersion` | `integer (int64)` | No | Not declared nullable | Location version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |
| `locationSource` | `string` | No | Explicitly allowed | Location source text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `sampledAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for sampled at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `locationAgeSeconds` | `integer (int32)` | No | Explicitly allowed | Location age, measured in seconds. | Naming convention | No further constraint recorded |
| `locationAccuracyMeters` | `number (double)` | No | Explicitly allowed | Location accuracy, measured in metres. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## NotificationCenterItemDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `title` | `string` | Yes | Not declared nullable | Human-readable title for the record/content, distinct from its ID. | Shared convention | No further constraint recorded |
| `message` | `string` | Yes | Not declared nullable | Message text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `templateKey` | `string` | Yes | Not declared nullable | Template key text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `actionType` | `string` | Yes | Not declared nullable | Action type text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `actionTarget` | `string` | No | Explicitly allowed | Action target text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `metadata` | `schema` | Yes | Not declared nullable | Metadata text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `isRead` | `boolean` | Yes | Not declared nullable | Whether is read applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `readAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for read at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for created at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `category` | `string` | No | Explicitly allowed | Category text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `priority` | `string` | No | Explicitly allowed | Priority text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `threadKey` | `string` | No | Explicitly allowed | Thread key text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `expiresAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for expires at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `deliveryState` | `string` | No | Explicitly allowed | Delivery state text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## NotificationCenterPageDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `items` | [NotificationCenterItemDto](n.md#notificationcenteritemdto)[] | Yes | Not declared nullable | Records returned in this collection/page, each using the referenced item model. | Shared convention | No further constraint recorded |
| `page` | `integer (int32)` | Yes | Not declared nullable | Page-number context for this endpoint; not a universal zero-based offset. | Shared convention | No further constraint recorded |
| `pageSize` | `integer (int32)` | Yes | Not declared nullable | Requested or returned page size, subject to this endpoint's server bounds. | Shared convention | No further constraint recorded |
| `totalCount` | `integer (int64)` | Yes | Not declared nullable | Total count defined by this page model; not automatically a live aggregate. | Shared convention | No further constraint recorded |
| `unreadCount` | `integer (int64)` | Yes | Not declared nullable | Current unread count in the applicable notification/chat model. | Shared convention | No further constraint recorded |
| `totalPages` | `integer (int32)` | No | Not declared nullable | Number of pages represented by this page-number model. | Shared convention | readOnly: `True` |
| `hasPreviousPage` | `boolean` | No | Not declared nullable | Whether has previous page applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | readOnly: `True` |
| `hasNextPage` | `boolean` | No | Not declared nullable | Whether has next page applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | readOnly: `True` |

**Additional object properties:** not allowed by the schema.

## NotificationCenterSeekPageDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `items` | [NotificationCenterItemDto](n.md#notificationcenteritemdto)[] | Yes | Not declared nullable | Records returned in this collection/page, each using the referenced item model. | Shared convention | No further constraint recorded |
| `pageSize` | `integer (int32)` | Yes | Not declared nullable | Requested or returned page size, subject to this endpoint's server bounds. | Shared convention | No further constraint recorded |
| `hasMore` | `boolean` | Yes | Not declared nullable | Whether the seek-paged result indicates more records after this page. | Shared convention | No further constraint recorded |
| `nextCursor` | `string` | No | Explicitly allowed | Opaque, scope-bound continuation token; preserve it unchanged and reset it when filters/context change. | Shared convention | No further constraint recorded |
| `unreadCount` | `integer (int64)` | Yes | Not declared nullable | Current unread count in the applicable notification/chat model. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## NotificationPreferencesDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `rides` | `boolean` | Yes | Not declared nullable | Whether rides applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `driverBidAlerts` | `boolean` | Yes | Not declared nullable | Whether driver bid alerts applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `deliveries` | `boolean` | Yes | Not declared nullable | Whether deliveries applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `wallet` | `boolean` | Yes | Not declared nullable | Whether wallet applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `promotions` | `boolean` | Yes | Not declared nullable | Whether promotions applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.
