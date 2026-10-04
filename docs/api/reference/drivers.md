# Driver onboarding, readiness and work

[Reference index](README.md) · [API guide](../README.md)

Access shown here describes bearer metadata only. Anonymous operations can still
require installation admission, application attestation, contact proof or country
context. A bearer token does not replace ownership, feature gates or role checks.

Each entry lists recorded schemas, parameters, status codes and mutation guards.
Response metadata is not a complete list of runtime business outcomes; read the
[contract limitations](../coverage-and-limitations.md).

## Operations on this page

- [GET `/api/v1/driver/assistance-capability`](#get-apiv1driverassistance-capability)
- [PUT `/api/v1/driver/assistance-capability`](#put-apiv1driverassistance-capability)
- [GET `/api/v1/driver/documents`](#get-apiv1driverdocuments)
- [POST `/api/v1/driver/documents`](#post-apiv1driverdocuments)
- [GET `/api/v1/driver/incentives/current`](#get-apiv1driverincentivescurrent)
- [GET `/api/v1/driver/profile`](#get-apiv1driverprofile)
- [GET `/api/v1/driver/profile/onboarding`](#get-apiv1driverprofileonboarding)
- [POST `/api/v1/driver/profile/onboarding/complete`](#post-apiv1driverprofileonboardingcomplete)
- [POST `/api/v1/driver/profile/onboarding/contact-proof`](#post-apiv1driverprofileonboardingcontact-proof)
- [POST `/api/v1/driver/profile/onboarding/progress`](#post-apiv1driverprofileonboardingprogress)
- [POST `/api/v1/driver/profile/onboarding/step`](#post-apiv1driverprofileonboardingstep)
- [GET `/api/v1/driver/profile/preferred-program`](#get-apiv1driverprofilepreferred-program)
- [POST `/api/v1/driver/profile/preferred-program/applications`](#post-apiv1driverprofilepreferred-programapplications)
- [POST `/api/v1/driver/profile/preferred-program/apply`](#post-apiv1driverprofilepreferred-programapply)
- [POST `/api/v1/driver/profile/rating/import`](#post-apiv1driverprofileratingimport)
- [GET `/api/v1/driver/profile/rating/imports`](#get-apiv1driverprofileratingimports)
- [GET `/api/v1/driver/profile/readiness`](#get-apiv1driverprofilereadiness)
- [GET `/api/v1/driver/profile/reviews`](#get-apiv1driverprofilereviews)
- [POST `/api/v1/driver/profile/reviews/{reviewId}/dispute`](#post-apiv1driverprofilereviewsreviewiddispute)
- [GET `/api/v1/driver/reports/earnings`](#get-apiv1driverreportsearnings)
- [GET `/api/v1/driver/rider-favorites`](#get-apiv1driverrider-favorites)
- [DELETE `/api/v1/driver/rider-favorites/{favoriteId}`](#delete-apiv1driverrider-favoritesfavoriteid)
- [POST `/api/v1/driver/rider-favorites/{riderUserId}`](#post-apiv1driverrider-favoritesrideruserid)
- [GET `/api/v1/driver/rides/alert-preferences`](#get-apiv1driverridesalert-preferences)
- [PUT `/api/v1/driver/rides/alert-preferences`](#put-apiv1driverridesalert-preferences)
- [GET `/api/v1/driver/rides/available`](#get-apiv1driverridesavailable)
- [GET `/api/v1/driver/rides/available/seek`](#get-apiv1driverridesavailableseek)
- [DELETE `/api/v1/driver/rides/bids/{bidId}`](#delete-apiv1driverridesbidsbidid)
- [POST `/api/v1/driver/rides/{rideRequestId}/bids`](#post-apiv1driverridesriderequestidbids)
- [GET `/api/v1/driver/rides/{rideRequestId}/inquiry`](#get-apiv1driverridesriderequestidinquiry)
- [POST `/api/v1/driver/rides/{rideRequestId}/inquiry`](#post-apiv1driverridesriderequestidinquiry)
- [POST `/api/v1/driver/rides/{rideRequestId}/inquiry/read`](#post-apiv1driverridesriderequestidinquiryread)
- [GET `/api/v1/driver/rides/{rideRequestId}/route-preview`](#get-apiv1driverridesriderequestidroute-preview)
- [POST `/api/v1/driver/rides/{rideRequestId}/view`](#post-apiv1driverridesriderequestidview)
- [GET `/api/v1/driver/status`](#get-apiv1driverstatus)
- [POST `/api/v1/driver/status`](#post-apiv1driverstatus)

## GET `/api/v1/driver/assistance-capability`

**What it does:** Read the permitted records/state for driver / assistance capability. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Driver.

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [DriverAssistanceCapabilityDto](../schemas/d.md#driverassistancecapabilitydto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## PUT `/api/v1/driver/assistance-capability`

**What it does:** Update the permitted configuration/record for driver / assistance capability. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Driver.

**Body:** [UpdateDriverAssistanceCapabilityDto](../schemas/u.md#updatedriverassistancecapabilitydto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [DriverAssistanceCapabilityDto](../schemas/d.md#driverassistancecapabilitydto) | `text/plain`, `application/json`, `text/json` | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
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

## GET `/api/v1/driver/documents`

**What it does:** List the driver's own submitted documents and their current review state.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required; declared roles: Driver.

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | Array of [DriverDocumentDto](../schemas/d.md#driverdocumentdto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## POST `/api/v1/driver/documents`

**What it does:** Submit a private upload as driver document evidence; submission does not approve it.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required; declared roles: Driver.

**Body:** [UploadDocumentDto](../schemas/u.md#uploaddocumentdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |
| `If-Match` | header | Yes | `string` | Strong resource ETag read before this logical edit; preserve the original value for uncertain-outcome replay. | pattern: `^\"[1-9][0-9]*\"$` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [DriverDocumentDto](../schemas/d.md#driverdocumentdto) | `text/plain`, `application/json`, `text/json` | `ETag`, `X-Entity-Revision`, `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 428 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes. Preserve the original revision during outcome recovery; refresh before a new logical edit.

## GET `/api/v1/driver/incentives/current`

**What it does:** Read the permitted records/state for driver / incentives / current. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | No typed schema recorded | None recorded | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/driver/profile`

**What it does:** Read the permitted records/state for driver / profile. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Driver.

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [DriverProfileDto](../schemas/d.md#driverprofiledto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/driver/profile/onboarding`

**What it does:** Read the driver's persisted setup/document checklist and remediation state.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required; declared roles: Driver.

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [DriverOnboardingDto](../schemas/d.md#driveronboardingdto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## POST `/api/v1/driver/profile/onboarding/complete`

**What it does:** Request completion of driver onboarding after required steps; this does not substitute for administrative readiness approval.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required; declared roles: Driver.

**Body:** [CompleteDriverOnboardingDto](../schemas/c.md#completedriveronboardingdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
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
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes. Preserve the original revision during outcome recovery; refresh before a new logical edit.

## POST `/api/v1/driver/profile/onboarding/contact-proof`

**What it does:** Submit proof of the applicable contact ceremony in the driver / profile / onboarding / contact proof workflow. The request and returned models below define the exact submitted evidence and result.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Driver.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |
| `X-KiloDrive-Recent-Authentication` | header | Conditional or optional | `string` | Private recent account proof when required by the server; local biometric/PIN unlock is insufficient. | minLength: `1`; maxLength: `256` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [TwoFactorStepUpDto](../schemas/t.md#twofactorstepupdto) | `text/plain`, `application/json`, `text/json` | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes. The server can require recent authentication; local app unlock is not proof.

## POST `/api/v1/driver/profile/onboarding/progress`

**What it does:** Persist the driver's onboarding progress for later resumption; progress is distinct from verified eligibility.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required; declared roles: Driver.

**Body:** [SaveDriverOnboardingProgressDto](../schemas/s.md#savedriveronboardingprogressdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
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
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes. Preserve the original revision during outcome recovery; refresh before a new logical edit.

## POST `/api/v1/driver/profile/onboarding/step`

**What it does:** Record a driver onboarding step through the server's step-validation workflow.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required; declared roles: Driver.

**Body:** [ConfirmDriverOnboardingStepDto](../schemas/c.md#confirmdriveronboardingstepdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
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
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes. Preserve the original revision during outcome recovery; refresh before a new logical edit.

## GET `/api/v1/driver/profile/preferred-program`

**What it does:** Read the permitted records/state for driver / profile / preferred program. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Driver.

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [PreferredDriverDto](../schemas/p.md#preferreddriverdto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## POST `/api/v1/driver/profile/preferred-program/applications`

**What it does:** Submit/create the documented record or action for driver / profile / preferred program / applications. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Driver.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [PreferredDriverDto](../schemas/p.md#preferreddriverdto) | `text/plain`, `application/json`, `text/json` | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.

## POST `/api/v1/driver/profile/preferred-program/apply`

**What it does:** Submit/create the documented record or action for driver / profile / preferred program / apply. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Driver.

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [PreferredDriverDto](../schemas/p.md#preferreddriverdto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## POST `/api/v1/driver/profile/rating/import`

**What it does:** Submit/create the documented record or action for driver / profile / rating / import. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Driver.

**Body:** [RequestRatingImportDto](../schemas/r.md#requestratingimportdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [RatingImportDto](../schemas/r.md#ratingimportdto) | `text/plain`, `application/json`, `text/json` | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
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

## GET `/api/v1/driver/profile/rating/imports`

**What it does:** Read the permitted records/state for driver / profile / rating / imports. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Driver.

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | Array of [RatingImportDto](../schemas/r.md#ratingimportdto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/driver/profile/readiness`

**What it does:** Read the authoritative assessment of whether this driver can go online or bid, including blocking reasons and next steps.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required; declared roles: Driver.

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [DriverReadinessDto](../schemas/d.md#driverreadinessdto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/driver/profile/reviews`

**What it does:** Read the permitted records/state for driver / profile / reviews. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Driver.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `page` | query | Conditional or optional | `integer (int32)` | Page-number context for this endpoint; not a universal zero-based offset. | No further constraint recorded |
| `pageSize` | query | Conditional or optional | `integer (int32)` | Requested or returned page size, subject to this endpoint's server bounds. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [DriverReviewsPageDto](../schemas/d.md#driverreviewspagedto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## POST `/api/v1/driver/profile/reviews/{reviewId}/dispute`

**What it does:** Submit/create the documented record or action for driver / profile / reviews / dispute. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Driver.

**Body:** [DisputeDriverReviewRequest](../schemas/d.md#disputedriverreviewrequest); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `reviewId` | path | Yes | `string (uuid)` | Identifier of the related review record in this model; ownership and scope are checked separately. | No further constraint recorded |
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

## GET `/api/v1/driver/reports/earnings`

**What it does:** Read the permitted records/state for driver / reports / earnings. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Driver.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `preset` | query | Conditional or optional | `string` | Named range/filter preset accepted by this endpoint; explicit date bounds have separate semantics. | No further constraint recorded |
| `fromUtc` | query | Conditional or optional | `string (date-time)` | UTC start of the requested range; apply this endpoint's inclusion/validation rules. | No further constraint recorded |
| `toUtc` | query | Conditional or optional | `string (date-time)` | UTC end of the requested range; apply this endpoint's inclusion/validation rules. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | No typed schema recorded | None recorded | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/driver/rider-favorites`

**What it does:** Read the permitted records/state for driver / rider favorites. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Driver.

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | Array of [DriverRiderFavoriteDto](../schemas/d.md#driverriderfavoritedto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## DELETE `/api/v1/driver/rider-favorites/{favoriteId}`

**What it does:** Request removal of the selected record for driver / rider favorites. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Driver.

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

## POST `/api/v1/driver/rider-favorites/{riderUserId}`

**What it does:** Submit/create the documented record or action for driver / rider favorites. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Driver.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `riderUserId` | path | Yes | `string (uuid)` | Identifier of the related rider user record in this model; ownership and scope are checked separately. | No further constraint recorded |

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

## GET `/api/v1/driver/rides/alert-preferences`

**What it does:** Read the permitted records/state for driver / rides / alert preferences. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Driver.

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [DriverRideAlertPreferencesDto](../schemas/d.md#driverridealertpreferencesdto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## PUT `/api/v1/driver/rides/alert-preferences`

**What it does:** Update the permitted configuration/record for driver / rides / alert preferences. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Driver.

**Body:** [UpdateDriverRideAlertPreferencesDto](../schemas/u.md#updatedriverridealertpreferencesdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [DriverRideAlertPreferencesDto](../schemas/d.md#driverridealertpreferencesdto) | `text/plain`, `application/json`, `text/json` | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
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

## GET `/api/v1/driver/rides/available`

**What it does:** Read the permitted records/state for driver / rides / available. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Driver.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `latitude` | query | Conditional or optional | `number (double)` | Latitude in degrees for the location represented by this model. | No further constraint recorded |
| `longitude` | query | Conditional or optional | `number (double)` | Longitude in degrees for the location represented by this model. | No further constraint recorded |
| `radiusMeters` | query | Conditional or optional | `integer (int32)` | Radius, measured in metres. | No further constraint recorded |
| `page` | query | Conditional or optional | `integer (int32)` | Page-number context for this endpoint; not a universal zero-based offset. | No further constraint recorded |
| `pageSize` | query | Conditional or optional | `integer (int32)` | Requested or returned page size, subject to this endpoint's server bounds. | No further constraint recorded |
| `dispatchMode` | query | Conditional or optional | [RideDispatchMode](../schemas/r.md#ridedispatchmode) | Dispatch mode represented by the `RideDispatchMode` model or enum; use that definition's fields/values. | No further constraint recorded |
| `minimumFareMinor` | query | Conditional or optional | `integer (int64)` | Minimum fare in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `minimumNetEarningsMinor` | query | Conditional or optional | `integer (int64)` | Minimum net earnings in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `paymentMethod` | query | Conditional or optional | [PaymentMethod](../schemas/p.md#paymentmethod) | Payment method enum; availability and settlement rules are checked separately. | No further constraint recorded |
| `schedule` | query | Conditional or optional | [DriverOfferScheduleFilter](../schemas/d.md#driverofferschedulefilter) | Schedule represented by the `DriverOfferScheduleFilter` model or enum; use that definition's fields/values. | No further constraint recorded |
| `accessibilityRequired` | query | Conditional or optional | `boolean` | Whether accessibility required applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `sort` | query | Conditional or optional | [DriverOfferSort](../schemas/d.md#driveroffersort) | Sort represented by the `DriverOfferSort` model or enum; use that definition's fields/values. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [DriverRideOfferDtoPagedResult](../schemas/d.md#driverrideofferdtopagedresult) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/driver/rides/available/seek`

**What it does:** Read a cursor-paged set of ride requests visible to this driver under current location, readiness and marketplace rules.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required; declared roles: Driver.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `latitude` | query | Conditional or optional | `number (double)` | Latitude in degrees for the location represented by this model. | No further constraint recorded |
| `longitude` | query | Conditional or optional | `number (double)` | Longitude in degrees for the location represented by this model. | No further constraint recorded |
| `radiusMeters` | query | Conditional or optional | `integer (int32)` | Radius, measured in metres. | No further constraint recorded |
| `pageSize` | query | Conditional or optional | `integer (int32)` | Requested or returned page size, subject to this endpoint's server bounds. | No further constraint recorded |
| `cursor` | query | Conditional or optional | `string` | Opaque scope-bound seek cursor from the previous page; do not modify it or reuse it under different filters. | No further constraint recorded |
| `dispatchMode` | query | Conditional or optional | [RideDispatchMode](../schemas/r.md#ridedispatchmode) | Dispatch mode represented by the `RideDispatchMode` model or enum; use that definition's fields/values. | No further constraint recorded |
| `minimumFareMinor` | query | Conditional or optional | `integer (int64)` | Minimum fare in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `minimumNetEarningsMinor` | query | Conditional or optional | `integer (int64)` | Minimum net earnings in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `paymentMethod` | query | Conditional or optional | [PaymentMethod](../schemas/p.md#paymentmethod) | Payment method enum; availability and settlement rules are checked separately. | No further constraint recorded |
| `schedule` | query | Conditional or optional | [DriverOfferScheduleFilter](../schemas/d.md#driverofferschedulefilter) | Schedule represented by the `DriverOfferScheduleFilter` model or enum; use that definition's fields/values. | No further constraint recorded |
| `accessibilityRequired` | query | Conditional or optional | `boolean` | Whether accessibility required applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [DriverRideOfferSeekPageDto](../schemas/d.md#driverrideofferseekpagedto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## DELETE `/api/v1/driver/rides/bids/{bidId}`

**What it does:** Request removal of the selected record for driver / rides / bids. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Driver.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `bidId` | path | Yes | `string (uuid)` | Identifier of the related bid record in this model; ownership and scope are checked separately. | No further constraint recorded |
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
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes. Preserve the original revision during outcome recovery; refresh before a new logical edit.

## POST `/api/v1/driver/rides/{rideRequestId}/bids`

**What it does:** Submit/create the documented record or action for driver / rides / bids. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Driver.

**Body:** [PlaceBidDto](../schemas/p.md#placebiddto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `rideRequestId` | path | Yes | `string (uuid)` | Rider request record, distinct from an accepted trip. | No further constraint recorded |
| `If-Match` | header | Conditional or optional | `string` | Strong resource ETag read before this logical edit; preserve the original value for uncertain-outcome replay. | No further constraint recorded |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [RideBidDto](../schemas/r.md#ridebiddto) | `text/plain`, `application/json`, `text/json` | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
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

## GET `/api/v1/driver/rides/{rideRequestId}/inquiry`

**What it does:** Read the permitted records/state for driver / rides / inquiry. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Driver.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `rideRequestId` | path | Yes | `string (uuid)` | Rider request record, distinct from an accepted trip. | No further constraint recorded |

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

## POST `/api/v1/driver/rides/{rideRequestId}/inquiry`

**What it does:** Submit/create the documented record or action for driver / rides / inquiry. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Driver.

**Body:** [SendRideInquiryMessageDto](../schemas/s.md#sendrideinquirymessagedto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `rideRequestId` | path | Yes | `string (uuid)` | Rider request record, distinct from an accepted trip. | No further constraint recorded |
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

## POST `/api/v1/driver/rides/{rideRequestId}/inquiry/read`

**What it does:** Update the caller's read/seen state in the driver / rides / inquiry / read workflow. The request and returned models below define the exact submitted evidence and result.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Driver.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `rideRequestId` | path | Yes | `string (uuid)` | Rider request record, distinct from an accepted trip. | No further constraint recorded |
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

## GET `/api/v1/driver/rides/{rideRequestId}/route-preview`

**What it does:** Read the permitted route preview for a ride request before deciding whether to bid.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required; declared roles: Driver.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `rideRequestId` | path | Yes | `string (uuid)` | Rider request record, distinct from an accepted trip. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [DriverRoutePreviewDto](../schemas/d.md#driverroutepreviewdto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## POST `/api/v1/driver/rides/{rideRequestId}/view`

**What it does:** Submit/create the documented record or action for driver / rides / view. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Driver.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `rideRequestId` | path | Yes | `string (uuid)` | Rider request record, distinct from an accepted trip. | No further constraint recorded |
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

## GET `/api/v1/driver/status`

**What it does:** Read the driver's current operational/online status.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required; declared roles: Driver.

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | No typed schema recorded | None recorded | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## POST `/api/v1/driver/status`

**What it does:** Request an online/status change subject to current readiness and operational rules.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required; declared roles: Driver.

**Body:** [DriverStatusRequest](../schemas/d.md#driverstatusrequest); required; media types: `application/json`, `text/json`, `application/*+json`.

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | No typed schema recorded | None recorded | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
