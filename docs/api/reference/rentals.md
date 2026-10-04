# Rental bookings and organization workflows

[Reference index](README.md) · [API guide](../README.md)

Access shown here describes bearer metadata only. Anonymous operations can still
require installation admission, application attestation, contact proof or country
context. A bearer token does not replace ownership, feature gates or role checks.

Each entry lists recorded schemas, parameters, status codes and mutation guards.
Response metadata is not a complete list of runtime business outcomes; read the
[contract limitations](../coverage-and-limitations.md).

## Operations on this page

- [GET `/api/v1/rental-partner/organizations`](#get-apiv1rental-partnerorganizations)
- [POST `/api/v1/rental-partner/organizations`](#post-apiv1rental-partnerorganizations)
- [DELETE `/api/v1/rental-partner/organizations/{organizationId}`](#delete-apiv1rental-partnerorganizationsorganizationid)
- [PUT `/api/v1/rental-partner/organizations/{organizationId}`](#put-apiv1rental-partnerorganizationsorganizationid)
- [GET `/api/v1/rental-partner/organizations/{organizationId}/analytics`](#get-apiv1rental-partnerorganizationsorganizationidanalytics)
- [POST `/api/v1/rental-partner/organizations/{organizationId}/availability-blocks`](#post-apiv1rental-partnerorganizationsorganizationidavailability-blocks)
- [DELETE `/api/v1/rental-partner/organizations/{organizationId}/availability-blocks/{blockId}`](#delete-apiv1rental-partnerorganizationsorganizationidavailability-blocksblockid)
- [GET `/api/v1/rental-partner/organizations/{organizationId}/billing`](#get-apiv1rental-partnerorganizationsorganizationidbilling)
- [POST `/api/v1/rental-partner/organizations/{organizationId}/billing/membership`](#post-apiv1rental-partnerorganizationsorganizationidbillingmembership)
- [PUT `/api/v1/rental-partner/organizations/{organizationId}/billing/membership/auto-renew`](#put-apiv1rental-partnerorganizationsorganizationidbillingmembershipauto-renew)
- [POST `/api/v1/rental-partner/organizations/{organizationId}/billing/membership/checkout`](#post-apiv1rental-partnerorganizationsorganizationidbillingmembershipcheckout)
- [PUT `/api/v1/rental-partner/organizations/{organizationId}/billing/mode`](#put-apiv1rental-partnerorganizationsorganizationidbillingmode)
- [GET `/api/v1/rental-partner/organizations/{organizationId}/bookings`](#get-apiv1rental-partnerorganizationsorganizationidbookings)
- [POST `/api/v1/rental-partner/organizations/{organizationId}/bookings/{bookingId}/agreement`](#post-apiv1rental-partnerorganizationsorganizationidbookingsbookingidagreement)
- [POST `/api/v1/rental-partner/organizations/{organizationId}/bookings/{bookingId}/agreement/sign`](#post-apiv1rental-partnerorganizationsorganizationidbookingsbookingidagreementsign)
- [POST `/api/v1/rental-partner/organizations/{organizationId}/bookings/{bookingId}/damage-claims`](#post-apiv1rental-partnerorganizationsorganizationidbookingsbookingiddamage-claims)
- [POST `/api/v1/rental-partner/organizations/{organizationId}/bookings/{bookingId}/deposit/settle`](#post-apiv1rental-partnerorganizationsorganizationidbookingsbookingiddepositsettle)
- [POST `/api/v1/rental-partner/organizations/{organizationId}/bookings/{bookingId}/inspections`](#post-apiv1rental-partnerorganizationsorganizationidbookingsbookingidinspections)
- [POST `/api/v1/rental-partner/organizations/{organizationId}/bookings/{bookingId}/late-return/assess`](#post-apiv1rental-partnerorganizationsorganizationidbookingsbookingidlate-returnassess)
- [PUT `/api/v1/rental-partner/organizations/{organizationId}/bookings/{bookingId}/status`](#put-apiv1rental-partnerorganizationsorganizationidbookingsbookingidstatus)
- [GET `/api/v1/rental-partner/organizations/{organizationId}/branches`](#get-apiv1rental-partnerorganizationsorganizationidbranches)
- [POST `/api/v1/rental-partner/organizations/{organizationId}/branches`](#post-apiv1rental-partnerorganizationsorganizationidbranches)
- [PUT `/api/v1/rental-partner/organizations/{organizationId}/extensions/{extensionId}`](#put-apiv1rental-partnerorganizationsorganizationidextensionsextensionid)
- [GET `/api/v1/rental-partner/organizations/{organizationId}/fleet/reminders`](#get-apiv1rental-partnerorganizationsorganizationidfleetreminders)
- [PUT `/api/v1/rental-partner/organizations/{organizationId}/profile-image`](#put-apiv1rental-partnerorganizationsorganizationidprofile-image)
- [GET `/api/v1/rental-partner/organizations/{organizationId}/team`](#get-apiv1rental-partnerorganizationsorganizationidteam)
- [POST `/api/v1/rental-partner/organizations/{organizationId}/team/invitations`](#post-apiv1rental-partnerorganizationsorganizationidteaminvitations)
- [DELETE `/api/v1/rental-partner/organizations/{organizationId}/team/invitations/{invitationId}`](#delete-apiv1rental-partnerorganizationsorganizationidteaminvitationsinvitationid)
- [PUT `/api/v1/rental-partner/organizations/{organizationId}/team/{userId}`](#put-apiv1rental-partnerorganizationsorganizationidteamuserid)
- [GET `/api/v1/rental-partner/organizations/{organizationId}/vehicles`](#get-apiv1rental-partnerorganizationsorganizationidvehicles)
- [POST `/api/v1/rental-partner/organizations/{organizationId}/vehicles`](#post-apiv1rental-partnerorganizationsorganizationidvehicles)
- [DELETE `/api/v1/rental-partner/organizations/{organizationId}/vehicles/{vehicleId}`](#delete-apiv1rental-partnerorganizationsorganizationidvehiclesvehicleid)
- [PUT `/api/v1/rental-partner/organizations/{organizationId}/vehicles/{vehicleId}`](#put-apiv1rental-partnerorganizationsorganizationidvehiclesvehicleid)
- [GET `/api/v1/rental-partner/organizations/{organizationId}/vehicles/{vehicleId}/availability`](#get-apiv1rental-partnerorganizationsorganizationidvehiclesvehicleidavailability)
- [DELETE `/api/v1/rental-partner/organizations/{organizationId}/vehicles/{vehicleId}/images/{imageId}`](#delete-apiv1rental-partnerorganizationsorganizationidvehiclesvehicleidimagesimageid)
- [PUT `/api/v1/rental-partner/organizations/{organizationId}/vehicles/{vehicleId}/images/{imageId}/primary`](#put-apiv1rental-partnerorganizationsorganizationidvehiclesvehicleidimagesimageidprimary)
- [PUT `/api/v1/rental-partner/organizations/{organizationId}/vehicles/{vehicleId}/protection`](#put-apiv1rental-partnerorganizationsorganizationidvehiclesvehicleidprotection)
- [POST `/api/v1/rental-partner/team/invitations/accept`](#post-apiv1rental-partnerteaminvitationsaccept)
- [POST `/api/v1/rental-partner/vehicles/{vehicleId}/images`](#post-apiv1rental-partnervehiclesvehicleidimages)
- [GET `/api/v1/rentals/booking-status-contract`](#get-apiv1rentalsbooking-status-contract)
- [POST `/api/v1/rentals/bookings`](#post-apiv1rentalsbookings)
- [GET `/api/v1/rentals/bookings/mine`](#get-apiv1rentalsbookingsmine)
- [POST `/api/v1/rentals/bookings/{bookingId}/agreement/sign`](#post-apiv1rentalsbookingsbookingidagreementsign)
- [POST `/api/v1/rentals/bookings/{bookingId}/cancel`](#post-apiv1rentalsbookingsbookingidcancel)
- [POST `/api/v1/rentals/bookings/{bookingId}/checkout`](#post-apiv1rentalsbookingsbookingidcheckout)
- [GET `/api/v1/rentals/bookings/{bookingId}/damage-evidence/{evidenceId}`](#get-apiv1rentalsbookingsbookingiddamage-evidenceevidenceid)
- [GET `/api/v1/rentals/bookings/{bookingId}/dispute-evidence/{evidenceId}`](#get-apiv1rentalsbookingsbookingiddispute-evidenceevidenceid)
- [POST `/api/v1/rentals/bookings/{bookingId}/disputes`](#post-apiv1rentalsbookingsbookingiddisputes)
- [POST `/api/v1/rentals/bookings/{bookingId}/extensions`](#post-apiv1rentalsbookingsbookingidextensions)
- [POST `/api/v1/rentals/bookings/{bookingId}/extensions/{extensionId}/checkout`](#post-apiv1rentalsbookingsbookingidextensionsextensionidcheckout)
- [GET `/api/v1/rentals/bookings/{bookingId}/inspection-evidence/{evidenceId}`](#get-apiv1rentalsbookingsbookingidinspection-evidenceevidenceid)
- [GET `/api/v1/rentals/bookings/{bookingId}/operations`](#get-apiv1rentalsbookingsbookingidoperations)
- [POST `/api/v1/rentals/bookings/{bookingId}/payment-authorized`](#post-apiv1rentalsbookingsbookingidpayment-authorized)
- [GET `/api/v1/rentals/bookings/{bookingId}/protection`](#get-apiv1rentalsbookingsbookingidprotection)
- [POST `/api/v1/rentals/bookings/{bookingId}/rating`](#post-apiv1rentalsbookingsbookingidrating)
- [DELETE `/api/v1/rentals/favorites/{vehicleId}`](#delete-apiv1rentalsfavoritesvehicleid)
- [PUT `/api/v1/rentals/favorites/{vehicleId}`](#put-apiv1rentalsfavoritesvehicleid)
- [GET `/api/v1/rentals/filters`](#get-apiv1rentalsfilters)
- [GET `/api/v1/rentals/organizations`](#get-apiv1rentalsorganizations)
- [GET `/api/v1/rentals/organizations/{organizationId}`](#get-apiv1rentalsorganizationsorganizationid)
- [GET `/api/v1/rentals/organizations/{organizationId}/profile-image`](#get-apiv1rentalsorganizationsorganizationidprofile-image)
- [GET `/api/v1/rentals/vehicles`](#get-apiv1rentalsvehicles)
- [GET `/api/v1/rentals/vehicles/{vehicleId}`](#get-apiv1rentalsvehiclesvehicleid)
- [GET `/api/v1/rentals/vehicles/{vehicleId}/availability`](#get-apiv1rentalsvehiclesvehicleidavailability)
- [GET `/api/v1/rentals/vehicles/{vehicleId}/images/{imageId}`](#get-apiv1rentalsvehiclesvehicleidimagesimageid)
- [GET `/api/v1/rentals/vehicles/{vehicleId}/protection`](#get-apiv1rentalsvehiclesvehicleidprotection)
- [GET `/api/v1/rentals/vehicles/{vehicleId}/quote`](#get-apiv1rentalsvehiclesvehicleidquote)

## GET `/api/v1/rental-partner/organizations`

**What it does:** Read the permitted records/state for rental partner / organizations. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | Array of [RentalOrganizationDto](../schemas/r.md#rentalorganizationdto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## POST `/api/v1/rental-partner/organizations`

**What it does:** Submit/create the documented record or action for rental partner / organizations. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

**Body:** [CreateRentalOrganizationDto](../schemas/c.md#createrentalorganizationdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [RentalOrganizationDto](../schemas/r.md#rentalorganizationdto) | `text/plain`, `application/json`, `text/json` | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
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

## DELETE `/api/v1/rental-partner/organizations/{organizationId}`

**What it does:** Request removal of the selected record for rental partner / organizations. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. | No further constraint recorded |
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

## PUT `/api/v1/rental-partner/organizations/{organizationId}`

**What it does:** Update the permitted configuration/record for rental partner / organizations. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

**Body:** [UpdateRentalOrganizationSettingsDto](../schemas/u.md#updaterentalorganizationsettingsdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [RentalOrganizationDto](../schemas/r.md#rentalorganizationdto) | `text/plain`, `application/json`, `text/json` | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
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

## GET `/api/v1/rental-partner/organizations/{organizationId}/analytics`

**What it does:** Read the permitted records/state for rental partner / organizations / analytics. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `from` | query | Yes | `string (date-time)` | From text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | No further constraint recorded |
| `to` | query | Yes | `string (date-time)` | To text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [RentalOwnerAnalyticsDto](../schemas/r.md#rentalowneranalyticsdto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## POST `/api/v1/rental-partner/organizations/{organizationId}/availability-blocks`

**What it does:** Submit/create the documented record or action for rental partner / organizations / availability blocks. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

**Body:** [CreateRentalAvailabilityBlockDto](../schemas/c.md#createrentalavailabilityblockdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [RentalAvailabilityBlockDto](../schemas/r.md#rentalavailabilityblockdto) | `text/plain`, `application/json`, `text/json` | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
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

## DELETE `/api/v1/rental-partner/organizations/{organizationId}/availability-blocks/{blockId}`

**What it does:** Request removal of the selected record for rental partner / organizations / availability blocks. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `blockId` | path | Yes | `string (uuid)` | Identifier of the related block record in this model; ownership and scope are checked separately. | No further constraint recorded |
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

## GET `/api/v1/rental-partner/organizations/{organizationId}/billing`

**What it does:** Read the permitted records/state for rental partner / organizations / billing. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [ProviderBillingDto](../schemas/p.md#providerbillingdto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## POST `/api/v1/rental-partner/organizations/{organizationId}/billing/membership`

**What it does:** Submit/create the documented record or action for rental partner / organizations / billing / membership. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

**Body:** [RentalMembershipPurchaseDto](../schemas/r.md#rentalmembershippurchasedto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [ProviderBillingDto](../schemas/p.md#providerbillingdto) | `text/plain`, `application/json`, `text/json` | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
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

## PUT `/api/v1/rental-partner/organizations/{organizationId}/billing/membership/auto-renew`

**What it does:** Update the permitted configuration/record for rental partner / organizations / billing / membership / auto renew. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

**Body:** [SetAutoRenewRequest](../schemas/s.md#setautorenewrequest); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |
| `X-KiloDrive-Step-Up` | header | Conditional or optional | `string` | X kilo drive step up text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | minLength: `1`; maxLength: `256` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [ProviderBillingDto](../schemas/p.md#providerbillingdto) | `text/plain`, `application/json`, `text/json` | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
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

## POST `/api/v1/rental-partner/organizations/{organizationId}/billing/membership/checkout`

**What it does:** Start the applicable payment checkout; checkout creation is not settlement in the rental partner / organizations / billing / membership / checkout workflow. The request and returned models below define the exact submitted evidence and result.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

**Body:** [MembershipCheckoutRequest](../schemas/m.md#membershipcheckoutrequest); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [MembershipCheckoutDto](../schemas/m.md#membershipcheckoutdto) | `text/plain`, `application/json`, `text/json` | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
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

## PUT `/api/v1/rental-partner/organizations/{organizationId}/billing/mode`

**What it does:** Update the permitted configuration/record for rental partner / organizations / billing / mode. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

**Body:** [BillingModeDto](../schemas/b.md#billingmodedto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [ProviderBillingDto](../schemas/p.md#providerbillingdto) | `text/plain`, `application/json`, `text/json` | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
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

## GET `/api/v1/rental-partner/organizations/{organizationId}/bookings`

**What it does:** Read the permitted records/state for rental partner / organizations / bookings. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | Array of [RentalPartnerBookingDto](../schemas/r.md#rentalpartnerbookingdto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## POST `/api/v1/rental-partner/organizations/{organizationId}/bookings/{bookingId}/agreement`

**What it does:** Submit/create the documented record or action for rental partner / organizations / bookings / agreement. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

**Body:** [IssueRentalAgreementDto](../schemas/i.md#issuerentalagreementdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `bookingId` | path | Yes | `string (uuid)` | Identifier of the related booking record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [RentalAgreementDto](../schemas/r.md#rentalagreementdto) | `text/plain`, `application/json`, `text/json` | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
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

## POST `/api/v1/rental-partner/organizations/{organizationId}/bookings/{bookingId}/agreement/sign`

**What it does:** Submit signature/acceptance evidence for the selected agreement in the rental partner / organizations / bookings / agreement / sign workflow. The request and returned models below define the exact submitted evidence and result.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

**Body:** [SignRentalAgreementDto](../schemas/s.md#signrentalagreementdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `bookingId` | path | Yes | `string (uuid)` | Identifier of the related booking record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [RentalAgreementDto](../schemas/r.md#rentalagreementdto) | `text/plain`, `application/json`, `text/json` | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
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

## POST `/api/v1/rental-partner/organizations/{organizationId}/bookings/{bookingId}/damage-claims`

**What it does:** Submit/create the documented record or action for rental partner / organizations / bookings / damage claims. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

**Body:** [CreateRentalDamageClaimDto](../schemas/c.md#createrentaldamageclaimdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `bookingId` | path | Yes | `string (uuid)` | Identifier of the related booking record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [RentalDamageClaimDto](../schemas/r.md#rentaldamageclaimdto) | `text/plain`, `application/json`, `text/json` | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
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

## POST `/api/v1/rental-partner/organizations/{organizationId}/bookings/{bookingId}/deposit/settle`

**What it does:** Request the applicable settlement under the current financial state in the rental partner / organizations / bookings / deposit / settle workflow. The request and returned models below define the exact submitted evidence and result.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

**Body:** [SettleRentalDepositDto](../schemas/s.md#settlerentaldepositdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `bookingId` | path | Yes | `string (uuid)` | Identifier of the related booking record in this model; ownership and scope are checked separately. | No further constraint recorded |
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

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.

## POST `/api/v1/rental-partner/organizations/{organizationId}/bookings/{bookingId}/inspections`

**What it does:** Submit/create the documented record or action for rental partner / organizations / bookings / inspections. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

**Body:** [CreateRentalInspectionDto](../schemas/c.md#createrentalinspectiondto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `bookingId` | path | Yes | `string (uuid)` | Identifier of the related booking record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [RentalInspectionDto](../schemas/r.md#rentalinspectiondto) | `text/plain`, `application/json`, `text/json` | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
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

## POST `/api/v1/rental-partner/organizations/{organizationId}/bookings/{bookingId}/late-return/assess`

**What it does:** Submit/create the documented record or action for rental partner / organizations / bookings / late return / assess. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

**Body:** [RentalExpectedVersionDto](../schemas/r.md#rentalexpectedversiondto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `bookingId` | path | Yes | `string (uuid)` | Identifier of the related booking record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | `integer (int64)` | `text/plain`, `application/json`, `text/json` | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
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

## PUT `/api/v1/rental-partner/organizations/{organizationId}/bookings/{bookingId}/status`

**What it does:** Update the permitted configuration/record for rental partner / organizations / bookings / status. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

**Body:** [UpdateRentalBookingStatusDto](../schemas/u.md#updaterentalbookingstatusdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `bookingId` | path | Yes | `string (uuid)` | Identifier of the related booking record in this model; ownership and scope are checked separately. | No further constraint recorded |
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

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.

## GET `/api/v1/rental-partner/organizations/{organizationId}/branches`

**What it does:** Read the permitted records/state for rental partner / organizations / branches. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | Array of [RentalPartnerBranchDto](../schemas/r.md#rentalpartnerbranchdto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## POST `/api/v1/rental-partner/organizations/{organizationId}/branches`

**What it does:** Submit/create the documented record or action for rental partner / organizations / branches. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

**Body:** [CreateRentalBranchDto](../schemas/c.md#createrentalbranchdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | `string (uuid)` | `text/plain`, `application/json`, `text/json` | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
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

## PUT `/api/v1/rental-partner/organizations/{organizationId}/extensions/{extensionId}`

**What it does:** Update the permitted configuration/record for rental partner / organizations / extensions. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

**Body:** [ReviewRentalExtensionDto](../schemas/r.md#reviewrentalextensiondto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `extensionId` | path | Yes | `string (uuid)` | Identifier of the related extension record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [RentalExtensionDto](../schemas/r.md#rentalextensiondto) | `text/plain`, `application/json`, `text/json` | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
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

## GET `/api/v1/rental-partner/organizations/{organizationId}/fleet/reminders`

**What it does:** Read the permitted records/state for rental partner / organizations / fleet / reminders. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `from` | query | Conditional or optional | `string (date-time)` | From text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | No further constraint recorded |
| `to` | query | Conditional or optional | `string (date-time)` | To text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | Array of [RentalFleetReminderDto](../schemas/r.md#rentalfleetreminderdto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## PUT `/api/v1/rental-partner/organizations/{organizationId}/profile-image`

**What it does:** Update the permitted configuration/record for rental partner / organizations / profile image. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

**Body:** [UpdateRentalOrganizationProfileImageDto](../schemas/u.md#updaterentalorganizationprofileimagedto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. | No further constraint recorded |
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

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.

## GET `/api/v1/rental-partner/organizations/{organizationId}/team`

**What it does:** Read the permitted records/state for rental partner / organizations / team. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [RentalTeamDto](../schemas/r.md#rentalteamdto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## POST `/api/v1/rental-partner/organizations/{organizationId}/team/invitations`

**What it does:** Submit/create the documented record or action for rental partner / organizations / team / invitations. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

**Body:** [InviteRentalTeamMemberDto](../schemas/i.md#inviterentalteammemberdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [RentalTeamInvitationDto](../schemas/r.md#rentalteaminvitationdto) | `text/plain`, `application/json`, `text/json` | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
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

## DELETE `/api/v1/rental-partner/organizations/{organizationId}/team/invitations/{invitationId}`

**What it does:** Request removal of the selected record for rental partner / organizations / team / invitations. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `invitationId` | path | Yes | `string (uuid)` | Identifier of the related invitation record in this model; ownership and scope are checked separately. | No further constraint recorded |
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

## PUT `/api/v1/rental-partner/organizations/{organizationId}/team/{userId}`

**What it does:** Update the permitted configuration/record for rental partner / organizations / team. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

**Body:** [UpdateRentalTeamMemberDto](../schemas/u.md#updaterentalteammemberdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `userId` | path | Yes | `string (uuid)` | Related account identity; the server still proves the caller's ownership or permitted relationship. | No further constraint recorded |
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

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.

## GET `/api/v1/rental-partner/organizations/{organizationId}/vehicles`

**What it does:** Read the permitted records/state for rental partner / organizations / vehicles. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | Array of [RentalPartnerVehicleDto](../schemas/r.md#rentalpartnervehicledto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## POST `/api/v1/rental-partner/organizations/{organizationId}/vehicles`

**What it does:** Submit/create the documented record or action for rental partner / organizations / vehicles. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

**Body:** [CreateRentalVehicleDto](../schemas/c.md#createrentalvehicledto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | `string (uuid)` | `text/plain`, `application/json`, `text/json` | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
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

## DELETE `/api/v1/rental-partner/organizations/{organizationId}/vehicles/{vehicleId}`

**What it does:** Request removal of the selected record for rental partner / organizations / vehicles. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `vehicleId` | path | Yes | `string (uuid)` | Account vehicle record associated with this operation or result. | No further constraint recorded |
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

## PUT `/api/v1/rental-partner/organizations/{organizationId}/vehicles/{vehicleId}`

**What it does:** Update the permitted configuration/record for rental partner / organizations / vehicles. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

**Body:** [UpdateRentalVehicleDto](../schemas/u.md#updaterentalvehicledto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `vehicleId` | path | Yes | `string (uuid)` | Account vehicle record associated with this operation or result. | No further constraint recorded |
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

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.

## GET `/api/v1/rental-partner/organizations/{organizationId}/vehicles/{vehicleId}/availability`

**What it does:** Read the permitted records/state for rental partner / organizations / vehicles / availability. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `vehicleId` | path | Yes | `string (uuid)` | Account vehicle record associated with this operation or result. | No further constraint recorded |
| `from` | query | Yes | `string (date-time)` | From text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | No further constraint recorded |
| `to` | query | Yes | `string (date-time)` | To text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [RentalAvailabilityCalendarDto](../schemas/r.md#rentalavailabilitycalendardto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## DELETE `/api/v1/rental-partner/organizations/{organizationId}/vehicles/{vehicleId}/images/{imageId}`

**What it does:** Request removal of the selected record for rental partner / organizations / vehicles / images. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `vehicleId` | path | Yes | `string (uuid)` | Account vehicle record associated with this operation or result. | No further constraint recorded |
| `imageId` | path | Yes | `string (uuid)` | Identifier of the related image record in this model; ownership and scope are checked separately. | No further constraint recorded |
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

## PUT `/api/v1/rental-partner/organizations/{organizationId}/vehicles/{vehicleId}/images/{imageId}/primary`

**What it does:** Update the permitted configuration/record for rental partner / organizations / vehicles / images / primary. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `vehicleId` | path | Yes | `string (uuid)` | Account vehicle record associated with this operation or result. | No further constraint recorded |
| `imageId` | path | Yes | `string (uuid)` | Identifier of the related image record in this model; ownership and scope are checked separately. | No further constraint recorded |
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

## PUT `/api/v1/rental-partner/organizations/{organizationId}/vehicles/{vehicleId}/protection`

**What it does:** Update the permitted configuration/record for rental partner / organizations / vehicles / protection. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

**Body:** [SetRentalProviderProtectionDto](../schemas/s.md#setrentalproviderprotectiondto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `vehicleId` | path | Yes | `string (uuid)` | Account vehicle record associated with this operation or result. | No further constraint recorded |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | `integer (int32)` | `text/plain`, `application/json`, `text/json` | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
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

## POST `/api/v1/rental-partner/team/invitations/accept`

**What it does:** Accept the selected offer/request in the rental partner / team / invitations / accept workflow. The request and returned models below define the exact submitted evidence and result.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

**Body:** [AcceptRentalTeamInvitationDto](../schemas/a.md#acceptrentalteaminvitationdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | No typed schema recorded | None recorded | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
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

## POST `/api/v1/rental-partner/vehicles/{vehicleId}/images`

**What it does:** Submit/create the documented record or action for rental partner / vehicles / images. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

**Body:** [AddRentalVehicleImageDto](../schemas/a.md#addrentalvehicleimagedto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `vehicleId` | path | Yes | `string (uuid)` | Account vehicle record associated with this operation or result. | No further constraint recorded |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | `string (uuid)` | `text/plain`, `application/json`, `text/json` | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
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

## GET `/api/v1/rentals/booking-status-contract`

**What it does:** Read the rental booking state contract used to render supported states and transitions consistently.

**Explanation basis:** Operation-specific explanation.

**Access:** Anonymous bearer metadata.

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [RentalBookingStatusContractDto](../schemas/r.md#rentalbookingstatuscontractdto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## POST `/api/v1/rentals/bookings`

**What it does:** Submit/create the documented record or action for rentals / bookings. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Passenger.

**Body:** [CreateRentalBookingDto](../schemas/c.md#createrentalbookingdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [RentalBookingDto](../schemas/r.md#rentalbookingdto) | `text/plain`, `application/json`, `text/json` | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
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

## GET `/api/v1/rentals/bookings/mine`

**What it does:** Read the permitted records/state for rentals / bookings / mine. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | Array of [RentalBookingDto](../schemas/r.md#rentalbookingdto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## POST `/api/v1/rentals/bookings/{bookingId}/agreement/sign`

**What it does:** Submit signature/acceptance evidence for the selected agreement in the rentals / bookings / agreement / sign workflow. The request and returned models below define the exact submitted evidence and result.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Passenger.

**Body:** [SignRentalAgreementDto](../schemas/s.md#signrentalagreementdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `bookingId` | path | Yes | `string (uuid)` | Identifier of the related booking record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [RentalAgreementDto](../schemas/r.md#rentalagreementdto) | `text/plain`, `application/json`, `text/json` | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
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

## POST `/api/v1/rentals/bookings/{bookingId}/cancel`

**What it does:** Cancel the selected pending or active workflow where permitted in the rentals / bookings / cancel workflow. The request and returned models below define the exact submitted evidence and result.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

**Body:** [CancelRentalBookingDto](../schemas/c.md#cancelrentalbookingdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `bookingId` | path | Yes | `string (uuid)` | Identifier of the related booking record in this model; ownership and scope are checked separately. | No further constraint recorded |
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

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.

## POST `/api/v1/rentals/bookings/{bookingId}/checkout`

**What it does:** Start the applicable payment checkout; checkout creation is not settlement in the rentals / bookings / checkout workflow. The request and returned models below define the exact submitted evidence and result.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Passenger.

**Body:** [CreateRentalCheckoutDto](../schemas/c.md#createrentalcheckoutdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `bookingId` | path | Yes | `string (uuid)` | Identifier of the related booking record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [RentalCheckoutDto](../schemas/r.md#rentalcheckoutdto) | `text/plain`, `application/json`, `text/json` | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
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

## GET `/api/v1/rentals/bookings/{bookingId}/damage-evidence/{evidenceId}`

**What it does:** Read the permitted records/state for rentals / bookings / damage evidence. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `bookingId` | path | Yes | `string (uuid)` | Identifier of the related booking record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `evidenceId` | path | Yes | `string (uuid)` | Identifier of the related evidence record in this model; ownership and scope are checked separately. | No further constraint recorded |

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

## GET `/api/v1/rentals/bookings/{bookingId}/dispute-evidence/{evidenceId}`

**What it does:** Read the permitted records/state for rentals / bookings / dispute evidence. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `bookingId` | path | Yes | `string (uuid)` | Identifier of the related booking record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `evidenceId` | path | Yes | `string (uuid)` | Identifier of the related evidence record in this model; ownership and scope are checked separately. | No further constraint recorded |

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

## POST `/api/v1/rentals/bookings/{bookingId}/disputes`

**What it does:** Submit/create the documented record or action for rentals / bookings / disputes. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Passenger.

**Body:** [OpenRentalDisputeDto](../schemas/o.md#openrentaldisputedto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `bookingId` | path | Yes | `string (uuid)` | Identifier of the related booking record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [RentalDisputeDto](../schemas/r.md#rentaldisputedto) | `text/plain`, `application/json`, `text/json` | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
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

## POST `/api/v1/rentals/bookings/{bookingId}/extensions`

**What it does:** Submit/create the documented record or action for rentals / bookings / extensions. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Passenger.

**Body:** [RequestRentalExtensionDto](../schemas/r.md#requestrentalextensiondto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `bookingId` | path | Yes | `string (uuid)` | Identifier of the related booking record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [RentalExtensionDto](../schemas/r.md#rentalextensiondto) | `text/plain`, `application/json`, `text/json` | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
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

## POST `/api/v1/rentals/bookings/{bookingId}/extensions/{extensionId}/checkout`

**What it does:** Start the applicable payment checkout; checkout creation is not settlement in the rentals / bookings / extensions / checkout workflow. The request and returned models below define the exact submitted evidence and result.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Passenger.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `bookingId` | path | Yes | `string (uuid)` | Identifier of the related booking record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `extensionId` | path | Yes | `string (uuid)` | Identifier of the related extension record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [RentalCheckoutDto](../schemas/r.md#rentalcheckoutdto) | `text/plain`, `application/json`, `text/json` | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
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

## GET `/api/v1/rentals/bookings/{bookingId}/inspection-evidence/{evidenceId}`

**What it does:** Read the permitted records/state for rentals / bookings / inspection evidence. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `bookingId` | path | Yes | `string (uuid)` | Identifier of the related booking record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `evidenceId` | path | Yes | `string (uuid)` | Identifier of the related evidence record in this model; ownership and scope are checked separately. | No further constraint recorded |

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

## GET `/api/v1/rentals/bookings/{bookingId}/operations`

**What it does:** Read operation/recovery facts for an authorized rental booking before continuing an interrupted booking or payment workflow.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `bookingId` | path | Yes | `string (uuid)` | Identifier of the related booking record in this model; ownership and scope are checked separately. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [RentalBookingOperationsDto](../schemas/r.md#rentalbookingoperationsdto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## POST `/api/v1/rentals/bookings/{bookingId}/payment-authorized`

**What it does:** Submit/create the documented record or action for rentals / bookings / payment authorized. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Passenger.

**Body:** [AuthorizeRentalBookingPaymentDto](../schemas/a.md#authorizerentalbookingpaymentdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `bookingId` | path | Yes | `string (uuid)` | Identifier of the related booking record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [RentalBookingDto](../schemas/r.md#rentalbookingdto) | `text/plain`, `application/json`, `text/json` | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
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

## GET `/api/v1/rentals/bookings/{bookingId}/protection`

**What it does:** Read the permitted records/state for rentals / bookings / protection. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `bookingId` | path | Yes | `string (uuid)` | Identifier of the related booking record in this model; ownership and scope are checked separately. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [RentalProviderProtectionDto](../schemas/r.md#rentalproviderprotectiondto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## POST `/api/v1/rentals/bookings/{bookingId}/rating`

**What it does:** Submit the caller's permitted rating for the selected completed service in the rentals / bookings / rating workflow. The request and returned models below define the exact submitted evidence and result.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Passenger.

**Body:** [CreateRentalRatingDto](../schemas/c.md#createrentalratingdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `bookingId` | path | Yes | `string (uuid)` | Identifier of the related booking record in this model; ownership and scope are checked separately. | No further constraint recorded |
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

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.

## DELETE `/api/v1/rentals/favorites/{vehicleId}`

**What it does:** Request removal of the selected record for rentals / favorites. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `vehicleId` | path | Yes | `string (uuid)` | Account vehicle record associated with this operation or result. | No further constraint recorded |

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

## PUT `/api/v1/rentals/favorites/{vehicleId}`

**What it does:** Update the permitted configuration/record for rentals / favorites. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `vehicleId` | path | Yes | `string (uuid)` | Account vehicle record associated with this operation or result. | No further constraint recorded |

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

## GET `/api/v1/rentals/filters`

**What it does:** Read the permitted records/state for rentals / filters. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Anonymous bearer metadata.

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [RentalMarketplaceFiltersDto](../schemas/r.md#rentalmarketplacefiltersdto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/rentals/organizations`

**What it does:** Read the permitted records/state for rentals / organizations. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Anonymous bearer metadata.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Search` | query | Conditional or optional | `string` | Search text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | No further constraint recorded |
| `Page` | query | Conditional or optional | `integer (int32)` | Numeric page for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `PageSize` | query | Conditional or optional | `integer (int32)` | Numeric page size for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [RentalOrganizationCardDtoPagedResult](../schemas/r.md#rentalorganizationcarddtopagedresult) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/rentals/organizations/{organizationId}`

**What it does:** Read the permitted records/state for rentals / organizations. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Anonymous bearer metadata.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [RentalOrganizationPublicDto](../schemas/r.md#rentalorganizationpublicdto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/rentals/organizations/{organizationId}/profile-image`

**What it does:** Read the permitted records/state for rentals / organizations / profile image. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Anonymous bearer metadata.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | No typed schema recorded | None recorded | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/rentals/vehicles`

**What it does:** Read the permitted records/state for rentals / vehicles. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Anonymous bearer metadata.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Category` | query | Conditional or optional | `string` | Category text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | No further constraint recorded |
| `PickupAt` | query | Conditional or optional | `string (date-time)` | Pickup at text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | No further constraint recorded |
| `ReturnAt` | query | Conditional or optional | `string (date-time)` | Return at text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | No further constraint recorded |
| `Latitude` | query | Conditional or optional | `number (double)` | Numeric latitude for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `Longitude` | query | Conditional or optional | `number (double)` | Numeric longitude for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `Page` | query | Conditional or optional | `integer (int32)` | Numeric page for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `PageSize` | query | Conditional or optional | `integer (int32)` | Numeric page size for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `Search` | query | Conditional or optional | `string` | Search text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | No further constraint recorded |
| `OrganizationId` | query | Conditional or optional | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `Make` | query | Conditional or optional | `string` | Make text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | No further constraint recorded |
| `Model` | query | Conditional or optional | `string` | Model text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | No further constraint recorded |
| `MinYear` | query | Conditional or optional | `integer (int32)` | Numeric min year for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `MaxYear` | query | Conditional or optional | `integer (int32)` | Numeric max year for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `VehicleType` | query | Conditional or optional | `string` | Vehicle type text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | No further constraint recorded |
| `Transmission` | query | Conditional or optional | `string` | Transmission text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | No further constraint recorded |
| `MinimumSeats` | query | Conditional or optional | `integer (int32)` | Numeric minimum seats for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `BookingMode` | query | Conditional or optional | [RentalBookingMode](../schemas/r.md#rentalbookingmode) | Booking mode represented by the `RentalBookingMode` model or enum; use that definition's fields/values. | No further constraint recorded |
| `Sort` | query | Conditional or optional | `string` | Sort text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | No further constraint recorded |
| `RadiusKilometers` | query | Conditional or optional | `number (double)` | Numeric radius kilometers for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [RentalVehicleCardDtoPagedResult](../schemas/r.md#rentalvehiclecarddtopagedresult) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/rentals/vehicles/{vehicleId}`

**What it does:** Read the permitted records/state for rentals / vehicles. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Anonymous bearer metadata.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `vehicleId` | path | Yes | `string (uuid)` | Account vehicle record associated with this operation or result. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [RentalVehicleDetailDto](../schemas/r.md#rentalvehicledetaildto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/rentals/vehicles/{vehicleId}/availability`

**What it does:** Read the permitted records/state for rentals / vehicles / availability. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Anonymous bearer metadata.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `vehicleId` | path | Yes | `string (uuid)` | Account vehicle record associated with this operation or result. | No further constraint recorded |
| `from` | query | Yes | `string (date-time)` | From text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | No further constraint recorded |
| `to` | query | Yes | `string (date-time)` | To text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [RentalAvailabilityCalendarDto](../schemas/r.md#rentalavailabilitycalendardto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/rentals/vehicles/{vehicleId}/images/{imageId}`

**What it does:** Read the permitted records/state for rentals / vehicles / images. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Anonymous bearer metadata.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `vehicleId` | path | Yes | `string (uuid)` | Account vehicle record associated with this operation or result. | No further constraint recorded |
| `imageId` | path | Yes | `string (uuid)` | Identifier of the related image record in this model; ownership and scope are checked separately. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | No typed schema recorded | None recorded | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/rentals/vehicles/{vehicleId}/protection`

**What it does:** Read the permitted records/state for rentals / vehicles / protection. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Anonymous bearer metadata.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `vehicleId` | path | Yes | `string (uuid)` | Account vehicle record associated with this operation or result. | No further constraint recorded |
| `pickupAt` | query | Yes | `string (date-time)` | Pickup at text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | No further constraint recorded |
| `returnAt` | query | Yes | `string (date-time)` | Return at text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [RentalProviderProtectionDto](../schemas/r.md#rentalproviderprotectiondto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/rentals/vehicles/{vehicleId}/quote`

**What it does:** Read a rental quote for the selected vehicle and booking context; quoted availability is not a confirmed reservation.

**Explanation basis:** Operation-specific explanation.

**Access:** Anonymous bearer metadata.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `vehicleId` | path | Yes | `string (uuid)` | Account vehicle record associated with this operation or result. | No further constraint recorded |
| `PickupAt` | query | Conditional or optional | `string (date-time)` | Pickup at text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | No further constraint recorded |
| `ReturnAt` | query | Conditional or optional | `string (date-time)` | Return at text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | No further constraint recorded |
| `HandoverMode` | query | Conditional or optional | [RentalVehicleHandoverMode](../schemas/r.md#rentalvehiclehandovermode) | Handover mode represented by the `RentalVehicleHandoverMode` model or enum; use that definition's fields/values. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [RentalQuoteDto](../schemas/r.md#rentalquotedto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
