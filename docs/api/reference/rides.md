# Rider requests, bidding and recurring rides

[Reference index](README.md) · [API guide](../README.md)

Access shown here describes bearer metadata only. Anonymous operations can still
require installation admission, application attestation, contact proof or country
context. A bearer token does not replace ownership, feature gates or role checks.

Each entry lists recorded schemas, parameters, status codes and mutation guards.
Response metadata is not a complete list of runtime business outcomes; read the
[contract limitations](../coverage-and-limitations.md).

## Operations on this page

- [GET `/api/v1/fare-splits/{planId}`](#get-apiv1fare-splitsplanid)
- [POST `/api/v1/fare-splits/{planId}/respond`](#post-apiv1fare-splitsplanidrespond)
- [GET `/api/v1/fares/quote`](#get-apiv1faresquote)
- [POST `/api/v1/fares/quote`](#post-apiv1faresquote)
- [GET `/api/v1/favorites`](#get-apiv1favorites)
- [POST `/api/v1/favorites`](#post-apiv1favorites)
- [DELETE `/api/v1/favorites/{favoriteId}`](#delete-apiv1favoritesfavoriteid)
- [GET `/api/v1/recurring-rides`](#get-apiv1recurring-rides)
- [POST `/api/v1/recurring-rides`](#post-apiv1recurring-rides)
- [POST `/api/v1/recurring-rides/recoverable`](#post-apiv1recurring-ridesrecoverable)
- [DELETE `/api/v1/recurring-rides/{recurringRideId}`](#delete-apiv1recurring-ridesrecurringrideid)
- [GET `/api/v1/recurring-rides/{recurringRideId}`](#get-apiv1recurring-ridesrecurringrideid)
- [PUT `/api/v1/recurring-rides/{recurringRideId}`](#put-apiv1recurring-ridesrecurringrideid)
- [GET `/api/v1/recurring-rides/{recurringRideId}/occurrences`](#get-apiv1recurring-ridesrecurringrideidoccurrences)
- [DELETE `/api/v1/recurring-rides/{recurringRideId}/revisioned`](#delete-apiv1recurring-ridesrecurringrideidrevisioned)
- [PUT `/api/v1/recurring-rides/{recurringRideId}/revisioned`](#put-apiv1recurring-ridesrecurringrideidrevisioned)
- [GET `/api/v1/rider/assistance-profile`](#get-apiv1riderassistance-profile)
- [PUT `/api/v1/rider/assistance-profile`](#put-apiv1riderassistance-profile)
- [GET `/api/v1/rider/membership`](#get-apiv1ridermembership)
- [GET `/api/v1/rider/membership/plans`](#get-apiv1ridermembershipplans)
- [GET `/api/v1/rides`](#get-apiv1rides)
- [POST `/api/v1/rides`](#post-apiv1rides)
- [POST `/api/v1/rides/fare-splits/{planId}/respond`](#post-apiv1ridesfare-splitsplanidrespond)
- [GET `/api/v1/rides/recent-locations`](#get-apiv1ridesrecent-locations)
- [GET `/api/v1/rides/{rideRequestId}`](#get-apiv1ridesriderequestid)
- [GET `/api/v1/rides/{rideRequestId}/bids`](#get-apiv1ridesriderequestidbids)
- [POST `/api/v1/rides/{rideRequestId}/bids/accept`](#post-apiv1ridesriderequestidbidsaccept)
- [GET `/api/v1/rides/{rideRequestId}/bids/{bidId}/avatar`](#get-apiv1ridesriderequestidbidsbididavatar)
- [POST `/api/v1/rides/{rideRequestId}/bids/{bidId}/reject`](#post-apiv1ridesriderequestidbidsbididreject)
- [POST `/api/v1/rides/{rideRequestId}/cancel`](#post-apiv1ridesriderequestidcancel)
- [PUT `/api/v1/rides/{rideRequestId}/fare`](#put-apiv1ridesriderequestidfare)
- [GET `/api/v1/rides/{rideRequestId}/fare-split`](#get-apiv1ridesriderequestidfare-split)
- [PUT `/api/v1/rides/{rideRequestId}/fare-split`](#put-apiv1ridesriderequestidfare-split)
- [GET `/api/v1/rides/{rideRequestId}/inquiries`](#get-apiv1ridesriderequestidinquiries)
- [GET `/api/v1/rides/{rideRequestId}/inquiries/{driverProfileId}`](#get-apiv1ridesriderequestidinquiriesdriverprofileid)
- [POST `/api/v1/rides/{rideRequestId}/inquiries/{driverProfileId}`](#post-apiv1ridesriderequestidinquiriesdriverprofileid)
- [POST `/api/v1/rides/{rideRequestId}/inquiries/{driverProfileId}/read`](#post-apiv1ridesriderequestidinquiriesdriverprofileidread)
- [GET `/api/v1/rides/{rideRequestId}/no-driver-recovery`](#get-apiv1ridesriderequestidno-driver-recovery)
- [GET `/api/v1/rides/{rideRequestId}/search-map`](#get-apiv1ridesriderequestidsearch-map)
- [POST `/api/v1/rides/{rideRequestId}/search/extend`](#post-apiv1ridesriderequestidsearchextend)

## GET `/api/v1/fare-splits/{planId}`

**What it does:** Read the permitted records/state for fare splits. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `planId` | path | Yes | `string (uuid)` | Membership catalog record; it does not itself prove a user entitlement. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [FareSplitPlanDto](../schemas/f.md#faresplitplandto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## POST `/api/v1/fare-splits/{planId}/respond`

**What it does:** Record the caller's response to the selected request/share in the fare splits / respond workflow. The request and returned models below define the exact submitted evidence and result.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

**Body:** [FareSplitResponseDto](../schemas/f.md#faresplitresponsedto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `planId` | path | Yes | `string (uuid)` | Membership catalog record; it does not itself prove a user entitlement. | No further constraint recorded |
| `If-Match` | header | Conditional or optional | `integer (int64)` | Strong resource ETag read before this logical edit; preserve the original value for uncertain-outcome replay. | No further constraint recorded |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [FareSplitPlanDto](../schemas/f.md#faresplitplandto) | `text/plain`, `application/json`, `text/json` | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes. Preserve the original revision during outcome recovery; refresh before a new logical edit.

## GET `/api/v1/fares/quote`

**What it does:** Read the permitted records/state for fares / quote. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `fromLatitude` | query | Yes | `number (double)` | Numeric from latitude for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `fromLongitude` | query | Yes | `number (double)` | Numeric from longitude for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `toLatitude` | query | Yes | `number (double)` | Numeric to latitude for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `toLongitude` | query | Yes | `number (double)` | Numeric to longitude for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `vehicleCategoryId` | query | Conditional or optional | `string (uuid)` | Identifier of the related vehicle category record in this model; ownership and scope are checked separately. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [FareQuoteResponseDto](../schemas/f.md#farequoteresponsedto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## POST `/api/v1/fares/quote`

**What it does:** Submit/create the documented record or action for fares / quote. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

**Body:** [FareQuoteRequestDto](../schemas/f.md#farequoterequestdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [FareQuoteResponseDto](../schemas/f.md#farequoteresponsedto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/favorites`

**What it does:** Read the permitted records/state for favorites. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | Array of [FavoriteDto](../schemas/f.md#favoritedto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## POST `/api/v1/favorites`

**What it does:** Submit/create the documented record or action for favorites. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

**Body:** [AddFavoriteDto](../schemas/a.md#addfavoritedto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [FavoriteDto](../schemas/f.md#favoritedto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## DELETE `/api/v1/favorites/{favoriteId}`

**What it does:** Request removal of the selected record for favorites. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `favoriteId` | path | Yes | `string (uuid)` | Identifier of the related favorite record in this model; ownership and scope are checked separately. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | No typed schema recorded | None recorded | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/recurring-rides`

**What it does:** Read the permitted records/state for recurring rides. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Passenger.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `page` | query | Conditional or optional | `integer (int32)` | Page-number context for this endpoint; not a universal zero-based offset. | No further constraint recorded |
| `pageSize` | query | Conditional or optional | `integer (int32)` | Requested or returned page size, subject to this endpoint's server bounds. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [RecurringRideDtoPagedResult](../schemas/r.md#recurringridedtopagedresult) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## POST `/api/v1/recurring-rides`

**What it does:** Submit/create the documented record or action for recurring rides. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Passenger.

**Body:** [UpsertRecurringRideDto](../schemas/u.md#upsertrecurringridedto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [RecurringRideDto](../schemas/r.md#recurringridedto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## POST `/api/v1/recurring-rides/recoverable`

**What it does:** Submit/create the documented record or action for recurring rides / recoverable. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Passenger.

**Body:** [UpsertRecurringRideDto](../schemas/u.md#upsertrecurringridedto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [RecurringRideDto](../schemas/r.md#recurringridedto) | `text/plain`, `application/json`, `text/json` | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.

## DELETE `/api/v1/recurring-rides/{recurringRideId}`

**What it does:** Request removal of the selected record for recurring rides. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Passenger.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `recurringRideId` | path | Yes | `string (uuid)` | Identifier of the related recurring ride record in this model; ownership and scope are checked separately. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | No typed schema recorded | None recorded | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/recurring-rides/{recurringRideId}`

**What it does:** Read the permitted records/state for recurring rides. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Passenger.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `recurringRideId` | path | Yes | `string (uuid)` | Identifier of the related recurring ride record in this model; ownership and scope are checked separately. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [RecurringRideDto](../schemas/r.md#recurringridedto) | `text/plain`, `application/json`, `text/json` | `ETag`, `X-Entity-Revision` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## PUT `/api/v1/recurring-rides/{recurringRideId}`

**What it does:** Update the permitted configuration/record for recurring rides. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Passenger.

**Body:** [UpsertRecurringRideDto](../schemas/u.md#upsertrecurringridedto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `recurringRideId` | path | Yes | `string (uuid)` | Identifier of the related recurring ride record in this model; ownership and scope are checked separately. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [RecurringRideDto](../schemas/r.md#recurringridedto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/recurring-rides/{recurringRideId}/occurrences`

**What it does:** Read the permitted records/state for recurring rides / occurrences. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Passenger.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `recurringRideId` | path | Yes | `string (uuid)` | Identifier of the related recurring ride record in this model; ownership and scope are checked separately. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | Array of [RecurringRideOccurrenceDto](../schemas/r.md#recurringrideoccurrencedto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## DELETE `/api/v1/recurring-rides/{recurringRideId}/revisioned`

**What it does:** Request removal of the selected record for recurring rides / revisioned. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Passenger.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `recurringRideId` | path | Yes | `string (uuid)` | Identifier of the related recurring ride record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |
| `If-Match` | header | Yes | `string` | Strong resource ETag read before this logical edit; preserve the original value for uncertain-outcome replay. | pattern: `^\"[1-9][0-9]*\"$` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | No typed schema recorded | None recorded | `ETag`, `X-Entity-Revision`, `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 428 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes. Preserve the original revision during outcome recovery; refresh before a new logical edit.

## PUT `/api/v1/recurring-rides/{recurringRideId}/revisioned`

**What it does:** Update the permitted configuration/record for recurring rides / revisioned. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Passenger.

**Body:** [UpsertRecurringRideDto](../schemas/u.md#upsertrecurringridedto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `recurringRideId` | path | Yes | `string (uuid)` | Identifier of the related recurring ride record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |
| `If-Match` | header | Yes | `string` | Strong resource ETag read before this logical edit; preserve the original value for uncertain-outcome replay. | pattern: `^\"[1-9][0-9]*\"$` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [RecurringRideDto](../schemas/r.md#recurringridedto) | `text/plain`, `application/json`, `text/json` | `ETag`, `X-Entity-Revision`, `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 428 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes. Preserve the original revision during outcome recovery; refresh before a new logical edit.

## GET `/api/v1/rider/assistance-profile`

**What it does:** Read the permitted records/state for rider / assistance profile. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Passenger.

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [RiderAssistanceProfileDto](../schemas/r.md#riderassistanceprofiledto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## PUT `/api/v1/rider/assistance-profile`

**What it does:** Update the permitted configuration/record for rider / assistance profile. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Passenger.

**Body:** [UpdateRiderAssistanceProfileDto](../schemas/u.md#updateriderassistanceprofiledto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [RiderAssistanceProfileDto](../schemas/r.md#riderassistanceprofiledto) | `text/plain`, `application/json`, `text/json` | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.

## GET `/api/v1/rider/membership`

**What it does:** Read the rider's membership state and benefits in the current account context.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required; declared roles: Passenger.

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [RiderEntitlementsDto](../schemas/r.md#riderentitlementsdto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/rider/membership/plans`

**What it does:** List membership plans for the rider audience; driver and rental plans are separate catalogs.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required; declared roles: Passenger.

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | Array of [MembershipPlanDto](../schemas/m.md#membershipplandto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/rides`

**What it does:** Read the permitted records/state for rides. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Passenger.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `page` | query | Conditional or optional | `integer (int32)` | Page-number context for this endpoint; not a universal zero-based offset. | No further constraint recorded |
| `pageSize` | query | Conditional or optional | `integer (int32)` | Requested or returned page size, subject to this endpoint's server bounds. | No further constraint recorded |
| `status` | query | Conditional or optional | [RideRequestStatus](../schemas/r.md#riderequeststatus) | Current domain status; use this model's enum or documented string vocabulary. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [RideRequestDtoPagedResult](../schemas/r.md#riderequestdtopagedresult) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## POST `/api/v1/rides`

**What it does:** Create a rider request with journey, proposed fare, category and applicable product options; this does not yet assign a driver.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required; declared roles: Passenger.

**Body:** [CreateRideRequestDto](../schemas/c.md#createriderequestdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `X-Quote-Id` | header | Conditional or optional | `string (uuid)` | Identifier of the related x quote record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `X-Quote-Version` | header | Conditional or optional | `integer (int64)` | X quote version for this model's state or policy; do not substitute a timestamp or mobile build. | No further constraint recorded |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [RideRequestDto](../schemas/r.md#riderequestdto) | `text/plain`, `application/json`, `text/json` | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.

## POST `/api/v1/rides/fare-splits/{planId}/respond`

**What it does:** Record the caller's response to the selected request/share in the rides / fare splits / respond workflow. The request and returned models below define the exact submitted evidence and result.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Passenger.

**Body:** [RespondFareSplitRequest](../schemas/r.md#respondfaresplitrequest); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `planId` | path | Yes | `string (uuid)` | Membership catalog record; it does not itself prove a user entitlement. | No further constraint recorded |
| `If-Match` | header | Conditional or optional | `string` | Strong resource ETag read before this logical edit; preserve the original value for uncertain-outcome replay. | No further constraint recorded |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [FareSplitPlanDto](../schemas/f.md#faresplitplandto) | `text/plain`, `application/json`, `text/json` | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes. Preserve the original revision during outcome recovery; refresh before a new logical edit.

## GET `/api/v1/rides/recent-locations`

**What it does:** Read the permitted records/state for rides / recent locations. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Passenger.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `limit` | query | Conditional or optional | `integer (int32)` | Numeric limit for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | Array of [RecentRideLocationDto](../schemas/r.md#recentridelocationdto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/rides/{rideRequestId}`

**What it does:** Read the permitted records/state for rides. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Passenger.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `rideRequestId` | path | Yes | `string (uuid)` | Rider request record, distinct from an accepted trip. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [RideRequestDto](../schemas/r.md#riderequestdto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/rides/{rideRequestId}/bids`

**What it does:** Read the permitted records/state for rides / bids. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Passenger.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `rideRequestId` | path | Yes | `string (uuid)` | Rider request record, distinct from an accepted trip. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | Array of [RideBidDto](../schemas/r.md#ridebiddto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## POST `/api/v1/rides/{rideRequestId}/bids/accept`

**What it does:** Accept an eligible current bid and establish the trip/financial state under server concurrency and readiness checks.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required; declared roles: Passenger.

**Body:** [AcceptBidDto](../schemas/a.md#acceptbiddto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `rideRequestId` | path | Yes | `string (uuid)` | Rider request record, distinct from an accepted trip. | No further constraint recorded |
| `If-Match` | header | Conditional or optional | `string` | Strong resource ETag read before this logical edit; preserve the original value for uncertain-outcome replay. | No further constraint recorded |
| `If-Match-Bid` | header | Conditional or optional | `string` | If match bid text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | No further constraint recorded |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [RideRequestDto](../schemas/r.md#riderequestdto) | `text/plain`, `application/json`, `text/json` | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes. Preserve the original revision during outcome recovery; refresh before a new logical edit.

## GET `/api/v1/rides/{rideRequestId}/bids/{bidId}/avatar`

**What it does:** Read the permitted records/state for rides / bids / avatar. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Passenger.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `rideRequestId` | path | Yes | `string (uuid)` | Rider request record, distinct from an accepted trip. | No further constraint recorded |
| `bidId` | path | Yes | `string (uuid)` | Identifier of the related bid record in this model; ownership and scope are checked separately. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | No typed schema recorded | None recorded | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## POST `/api/v1/rides/{rideRequestId}/bids/{bidId}/reject`

**What it does:** Reject the selected offer/request in the rides / bids / reject workflow. The request and returned models below define the exact submitted evidence and result.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Passenger.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `rideRequestId` | path | Yes | `string (uuid)` | Rider request record, distinct from an accepted trip. | No further constraint recorded |
| `bidId` | path | Yes | `string (uuid)` | Identifier of the related bid record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `If-Match` | header | Conditional or optional | `string` | Strong resource ETag read before this logical edit; preserve the original value for uncertain-outcome replay. | No further constraint recorded |
| `If-Match-Bid` | header | Conditional or optional | `string` | If match bid text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | No further constraint recorded |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | No typed schema recorded | None recorded | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes. Preserve the original revision during outcome recovery; refresh before a new logical edit.

## POST `/api/v1/rides/{rideRequestId}/cancel`

**What it does:** Cancel the selected pending or active workflow where permitted in the rides / cancel workflow. The request and returned models below define the exact submitted evidence and result.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Passenger.

**Body:** [CancelRequest](../schemas/c.md#cancelrequest); requiredness not asserted in metadata; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `rideRequestId` | path | Yes | `string (uuid)` | Rider request record, distinct from an accepted trip. | No further constraint recorded |
| `If-Match` | header | Conditional or optional | `string` | Strong resource ETag read before this logical edit; preserve the original value for uncertain-outcome replay. | No further constraint recorded |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | No typed schema recorded | None recorded | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes. Preserve the original revision during outcome recovery; refresh before a new logical edit.

## PUT `/api/v1/rides/{rideRequestId}/fare`

**What it does:** Update the permitted configuration/record for rides / fare. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Passenger.

**Body:** [UpdateRideFareDto](../schemas/u.md#updateridefaredto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `rideRequestId` | path | Yes | `string (uuid)` | Rider request record, distinct from an accepted trip. | No further constraint recorded |
| `If-Match` | header | Conditional or optional | `string` | Strong resource ETag read before this logical edit; preserve the original value for uncertain-outcome replay. | No further constraint recorded |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [RideRequestDto](../schemas/r.md#riderequestdto) | `text/plain`, `application/json`, `text/json` | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes. Preserve the original revision during outcome recovery; refresh before a new logical edit.

## GET `/api/v1/rides/{rideRequestId}/fare-split`

**What it does:** Read the permitted records/state for rides / fare split. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Passenger.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `rideRequestId` | path | Yes | `string (uuid)` | Rider request record, distinct from an accepted trip. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [FareSplitPlanDto](../schemas/f.md#faresplitplandto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## PUT `/api/v1/rides/{rideRequestId}/fare-split`

**What it does:** Update the permitted configuration/record for rides / fare split. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Passenger.

**Body:** [ConfigureFareSplitDto](../schemas/c.md#configurefaresplitdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `rideRequestId` | path | Yes | `string (uuid)` | Rider request record, distinct from an accepted trip. | No further constraint recorded |
| `If-Match` | header | Conditional or optional | `string` | Strong resource ETag read before this logical edit; preserve the original value for uncertain-outcome replay. | No further constraint recorded |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [FareSplitPlanDto](../schemas/f.md#faresplitplandto) | `text/plain`, `application/json`, `text/json` | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes. Preserve the original revision during outcome recovery; refresh before a new logical edit.

## GET `/api/v1/rides/{rideRequestId}/inquiries`

**What it does:** Read the permitted records/state for rides / inquiries. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Passenger.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `rideRequestId` | path | Yes | `string (uuid)` | Rider request record, distinct from an accepted trip. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | Array of [RideInquiryThreadDto](../schemas/r.md#rideinquirythreaddto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/rides/{rideRequestId}/inquiries/{driverProfileId}`

**What it does:** Read the permitted records/state for rides / inquiries. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Driver, Passenger.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `rideRequestId` | path | Yes | `string (uuid)` | Rider request record, distinct from an accepted trip. | No further constraint recorded |
| `driverProfileId` | path | Yes | `string (uuid)` | Driver-profile record associated with this operation or result. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | Array of [RideInquiryMessageDto](../schemas/r.md#rideinquirymessagedto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## POST `/api/v1/rides/{rideRequestId}/inquiries/{driverProfileId}`

**What it does:** Submit/create the documented record or action for rides / inquiries. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Driver, Passenger.

**Body:** [SendRideInquiryMessageDto](../schemas/s.md#sendrideinquirymessagedto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `rideRequestId` | path | Yes | `string (uuid)` | Rider request record, distinct from an accepted trip. | No further constraint recorded |
| `driverProfileId` | path | Yes | `string (uuid)` | Driver-profile record associated with this operation or result. | No further constraint recorded |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [RideInquiryMessageDto](../schemas/r.md#rideinquirymessagedto) | `text/plain`, `application/json`, `text/json` | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.

## POST `/api/v1/rides/{rideRequestId}/inquiries/{driverProfileId}/read`

**What it does:** Update the caller's read/seen state in the rides / inquiries / read workflow. The request and returned models below define the exact submitted evidence and result.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Driver, Passenger.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `rideRequestId` | path | Yes | `string (uuid)` | Rider request record, distinct from an accepted trip. | No further constraint recorded |
| `driverProfileId` | path | Yes | `string (uuid)` | Driver-profile record associated with this operation or result. | No further constraint recorded |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | No typed schema recorded | None recorded | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.

## GET `/api/v1/rides/{rideRequestId}/no-driver-recovery`

**What it does:** Read permitted recovery choices when a ride request has not obtained a driver.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required; declared roles: Passenger.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `rideRequestId` | path | Yes | `string (uuid)` | Rider request record, distinct from an accepted trip. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [RideNoDriverRecoveryProjection](../schemas/r.md#ridenodriverrecoveryprojection) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/rides/{rideRequestId}/search-map`

**What it does:** Read the permitted records/state for rides / search map. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Passenger.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `rideRequestId` | path | Yes | `string (uuid)` | Rider request record, distinct from an accepted trip. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [RideSearchMapDto](../schemas/r.md#ridesearchmapdto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## POST `/api/v1/rides/{rideRequestId}/search/extend`

**What it does:** Request an extension of the current ride search under marketplace policy; it does not guarantee a match.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required; declared roles: Passenger.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `rideRequestId` | path | Yes | `string (uuid)` | Rider request record, distinct from an accepted trip. | No further constraint recorded |
| `If-Match` | header | Conditional or optional | `string` | Strong resource ETag read before this logical edit; preserve the original value for uncertain-outcome replay. | No further constraint recorded |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [RideRequestDto](../schemas/r.md#riderequestdto) | `text/plain`, `application/json`, `text/json` | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes. Preserve the original revision during outcome recovery; refresh before a new logical edit.
