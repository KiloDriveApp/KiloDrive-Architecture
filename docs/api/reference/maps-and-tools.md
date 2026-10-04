# Maps, fare tools and saved calculations

[Reference index](README.md) · [API guide](../README.md)

Access shown here describes bearer metadata only. Anonymous operations can still
require installation admission, application attestation, contact proof or country
context. A bearer token does not replace ownership, feature gates or role checks.

Each entry lists recorded schemas, parameters, status codes and mutation guards.
Response metadata is not a complete list of runtime business outcomes; read the
[contract limitations](../coverage-and-limitations.md).

## Operations on this page

- [GET `/api/v1/calculations`](#get-apiv1calculations)
- [POST `/api/v1/calculations`](#post-apiv1calculations)
- [DELETE `/api/v1/calculations/{id}`](#delete-apiv1calculationsid)
- [PUT `/api/v1/calculations/{id}/title`](#put-apiv1calculationsidtitle)
- [GET `/api/v1/maps/autocomplete`](#get-apiv1mapsautocomplete)
- [GET `/api/v1/maps/geocode`](#get-apiv1mapsgeocode)
- [GET `/api/v1/maps/place`](#get-apiv1mapsplace)
- [GET `/api/v1/maps/reverse-geocode`](#get-apiv1mapsreverse-geocode)
- [GET `/api/v1/maps/route`](#get-apiv1mapsroute)
- [GET `/api/v1/maps/traffic-routes`](#get-apiv1mapstraffic-routes)
- [POST `/api/v1/tools/calculators/export/pdf`](#post-apiv1toolscalculatorsexportpdf)
- [GET `/api/v1/tools/tolls/estimate`](#get-apiv1toolstollsestimate)
- [GET `/api/v1/tools/tolls/options`](#get-apiv1toolstollsoptions)
- [GET `/api/v1/tools/tolls/periods`](#get-apiv1toolstollsperiods)
- [GET `/api/v1/tools/tolls/plazas`](#get-apiv1toolstollsplazas)
- [POST `/api/v1/tools/tolls/route-estimate`](#post-apiv1toolstollsroute-estimate)

## GET `/api/v1/calculations`

**What it does:** Read the permitted records/state for calculations. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | Array of [SavedCalculationDto](../schemas/s.md#savedcalculationdto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## POST `/api/v1/calculations`

**What it does:** Submit/create the documented record or action for calculations. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

**Body:** [SaveCalculationDto](../schemas/s.md#savecalculationdto); requiredness not asserted in metadata; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [SavedCalculationDto](../schemas/s.md#savedcalculationdto) | `text/plain`, `application/json`, `text/json` | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
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

## DELETE `/api/v1/calculations/{id}`

**What it does:** Request removal of the selected record for calculations. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | path | Yes | `string (uuid)` | Opaque identifier of this model's record; knowing it does not grant access. | No further constraint recorded |
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

## PUT `/api/v1/calculations/{id}/title`

**What it does:** Update the permitted configuration/record for calculations / title. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

**Body:** [RenameSavedCalculationDto](../schemas/r.md#renamesavedcalculationdto); requiredness not asserted in metadata; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | path | Yes | `string (uuid)` | Opaque identifier of this model's record; knowing it does not grant access. | No further constraint recorded |
| `If-Match` | header | Conditional or optional | `integer (int32)` | Strong resource ETag read before this logical edit; preserve the original value for uncertain-outcome replay. | No further constraint recorded |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [SavedCalculationDto](../schemas/s.md#savedcalculationdto) | `text/plain`, `application/json`, `text/json` | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
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

## GET `/api/v1/maps/autocomplete`

**What it does:** Read the permitted records/state for maps / autocomplete. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Anonymous bearer metadata.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `input` | query | Yes | `string` | Input text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | No further constraint recorded |
| `latitude` | query | Conditional or optional | `number (double)` | Latitude in degrees for the location represented by this model. | No further constraint recorded |
| `longitude` | query | Conditional or optional | `number (double)` | Longitude in degrees for the location represented by this model. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | No typed schema recorded | None recorded | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/maps/geocode`

**What it does:** Read the permitted records/state for maps / geocode. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Anonymous bearer metadata.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `address` | query | Yes | `string` | Address text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | No typed schema recorded | None recorded | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/maps/place`

**What it does:** Read the permitted records/state for maps / place. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Anonymous bearer metadata.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `placeId` | query | Yes | `string` | Identifier of the related place record in this model; ownership and scope are checked separately. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | No typed schema recorded | None recorded | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/maps/reverse-geocode`

**What it does:** Read the permitted records/state for maps / reverse geocode. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Anonymous bearer metadata.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `latitude` | query | Yes | `number (double)` | Latitude in degrees for the location represented by this model. | No further constraint recorded |
| `longitude` | query | Yes | `number (double)` | Longitude in degrees for the location represented by this model. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | No typed schema recorded | None recorded | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/maps/route`

**What it does:** Read the permitted records/state for maps / route. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Anonymous bearer metadata.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `fromLatitude` | query | Yes | `number (double)` | Numeric from latitude for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `fromLongitude` | query | Yes | `number (double)` | Numeric from longitude for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `toLatitude` | query | Yes | `number (double)` | Numeric to latitude for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `toLongitude` | query | Yes | `number (double)` | Numeric to longitude for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | No typed schema recorded | None recorded | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/maps/traffic-routes`

**What it does:** Read the permitted records/state for maps / traffic routes. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Anonymous bearer metadata.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `fromLatitude` | query | Yes | `number (double)` | Numeric from latitude for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `fromLongitude` | query | Yes | `number (double)` | Numeric from longitude for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `toLatitude` | query | Yes | `number (double)` | Numeric to latitude for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `toLongitude` | query | Yes | `number (double)` | Numeric to longitude for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | No typed schema recorded | None recorded | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## POST `/api/v1/tools/calculators/export/pdf`

**What it does:** Submit/create the documented record or action for tools / calculators / export / pdf. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Anonymous bearer metadata.

**Body:** [CalculatorPdfRequest](../schemas/c.md#calculatorpdfrequest); required; media types: `application/json`, `text/json`, `application/*+json`.

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | No typed schema recorded | None recorded | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/tools/tolls/estimate`

**What it does:** Read the permitted records/state for tools / tolls / estimate. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Anonymous bearer metadata.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `corridor` | query | Yes | `string` | Corridor text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | No further constraint recorded |
| `origin` | query | Yes | `string` | Origin text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | No further constraint recorded |
| `destination` | query | Yes | `string` | Destination text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | No further constraint recorded |
| `vehicleClass` | query | Yes | `integer (int32)` | Numeric vehicle class for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `returnTrip` | query | Conditional or optional | `boolean` | Whether return trip applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `onDate` | query | Conditional or optional | `string (date)` | Calendar date for on date; preserve date-only semantics rather than shifting it through a timezone. | No further constraint recorded |
| `costPerKilometerMinor` | query | Conditional or optional | `integer (int64)` | Cost per kilometer in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [TollEstimateDto](../schemas/t.md#tollestimatedto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/tools/tolls/options`

**What it does:** Read the permitted records/state for tools / tolls / options. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Anonymous bearer metadata.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `countryCode` | query | Conditional or optional | `string` | Country ISO code for this model/context; it cannot override authenticated country authority. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | Array of [TollJourneyOptionDto](../schemas/t.md#tolljourneyoptiondto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/tools/tolls/periods`

**What it does:** Read the permitted records/state for tools / tolls / periods. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Anonymous bearer metadata.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `countryCode` | query | Conditional or optional | `string` | Country ISO code for this model/context; it cannot override authenticated country authority. | No further constraint recorded |
| `vehicleClass` | query | Conditional or optional | `integer (int32)` | Numeric vehicle class for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | Array of [TollPricingPeriodDto](../schemas/t.md#tollpricingperioddto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/tools/tolls/plazas`

**What it does:** Read the permitted records/state for tools / tolls / plazas. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Anonymous bearer metadata.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `countryCode` | query | Conditional or optional | `string` | Country ISO code for this model/context; it cannot override authenticated country authority. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | Array of [TollPlazaDto](../schemas/t.md#tollplazadto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## POST `/api/v1/tools/tolls/route-estimate`

**What it does:** Submit/create the documented record or action for tools / tolls / route estimate. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Anonymous bearer metadata.

**Body:** [TollRouteEstimateRequest](../schemas/t.md#tollrouteestimaterequest); required; media types: `application/json`, `text/json`, `application/*+json`.

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [TollRouteEstimateDto](../schemas/t.md#tollrouteestimatedto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
