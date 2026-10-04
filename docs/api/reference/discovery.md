# Public information and capability discovery

[Reference index](README.md) · [API guide](../README.md)

Access shown here describes bearer metadata only. Anonymous operations can still
require installation admission, application attestation, contact proof or country
context. A bearer token does not replace ownership, feature gates or role checks.

Each entry lists recorded schemas, parameters, status codes and mutation guards.
Response metadata is not a complete list of runtime business outcomes; read the
[contract limitations](../coverage-and-limitations.md).

## Operations on this page

- [GET `/api/v1/app-releases`](#get-apiv1app-releases)
- [GET `/api/v1/app-releases/current`](#get-apiv1app-releasescurrent)
- [GET `/api/v1/app-releases/{version}`](#get-apiv1app-releasesversion)
- [GET `/api/v1/app-releases/{version}/build/{build}`](#get-apiv1app-releasesversionbuildbuild)
- [GET `/api/v1/app-version-policy`](#get-apiv1app-version-policy)
- [GET `/api/v1/blog`](#get-apiv1blog)
- [GET `/api/v1/blog/{slug}`](#get-apiv1blogslug)
- [GET `/api/v1/content`](#get-apiv1content)
- [POST `/api/v1/content/contact`](#post-apiv1contentcontact)
- [GET `/api/v1/content/legal-catalogue`](#get-apiv1contentlegal-catalogue)
- [GET `/api/v1/content/{slug}`](#get-apiv1contentslug)
- [GET `/api/v1/content/{slug}/versions`](#get-apiv1contentslugversions)
- [GET `/api/v1/content/{slug}/versions/{version}`](#get-apiv1contentslugversionsversion)
- [GET `/api/v1/content/{slug}/versions/{version}/pdf`](#get-apiv1contentslugversionsversionpdf)
- [GET `/api/v1/features`](#get-apiv1features)
- [POST `/api/v1/legal-acceptances`](#post-apiv1legal-acceptances)
- [GET `/api/v1/legal-acceptances/catalogue`](#get-apiv1legal-acceptancescatalogue)
- [GET `/api/v1/public/capabilities`](#get-apiv1publiccapabilities)
- [GET `/api/v1/public/country-sites`](#get-apiv1publiccountry-sites)
- [GET `/api/v1/public/membership-prices`](#get-apiv1publicmembership-prices)
- [GET `/api/v1/reference-data/banks`](#get-apiv1reference-databanks)
- [GET `/api/v1/reference-data/countries`](#get-apiv1reference-datacountries)
- [GET `/api/v1/reference-data/vehicle-insurers`](#get-apiv1reference-datavehicle-insurers)
- [GET `/api/v1/resources/manuals`](#get-apiv1resourcesmanuals)
- [GET `/api/v1/vehicle-catalog/makes`](#get-apiv1vehicle-catalogmakes)
- [GET `/api/v1/vehicle-catalog/models`](#get-apiv1vehicle-catalogmodels)
- [GET `/api/v1/vehicle-catalog/years`](#get-apiv1vehicle-catalogyears)
- [GET `/api/v1/vehicle-categories`](#get-apiv1vehicle-categories)

## GET `/api/v1/app-releases`

**What it does:** Read the permitted records/state for app releases. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Anonymous bearer metadata.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `surface` | query | Conditional or optional | `string` | Surface text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | No further constraint recorded |
| `platform` | query | Conditional or optional | `string` | Platform selector in this contract; numeric enums and string selectors are not interchangeable. | No further constraint recorded |
| `language` | query | Conditional or optional | `string` | Language selector/content language; use the endpoint's supported values and fallback rules. | No further constraint recorded |
| `page` | query | Conditional or optional | `integer (int32)` | Page-number context for this endpoint; not a universal zero-based offset. | No further constraint recorded |
| `pageSize` | query | Conditional or optional | `integer (int32)` | Requested or returned page size, subject to this endpoint's server bounds. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [AppReleaseListDto](../schemas/a.md#appreleaselistdto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `text/plain`, `application/json`, `text/json`, `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/app-releases/current`

**What it does:** Read the permitted records/state for app releases / current. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Anonymous bearer metadata.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `surface` | query | Conditional or optional | `string` | Surface text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | No further constraint recorded |
| `platform` | query | Conditional or optional | `string` | Platform selector in this contract; numeric enums and string selectors are not interchangeable. | No further constraint recorded |
| `language` | query | Conditional or optional | `string` | Language selector/content language; use the endpoint's supported values and fallback rules. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [AppReleaseDetailDto](../schemas/a.md#appreleasedetaildto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/app-releases/{version}`

**What it does:** Read the permitted records/state for app releases. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Anonymous bearer metadata.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `version` | path | Yes | `string` | Version in this model's domain; not automatically an API major version. | No further constraint recorded |
| `surface` | query | Conditional or optional | `string` | Surface text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | No further constraint recorded |
| `platform` | query | Conditional or optional | `string` | Platform selector in this contract; numeric enums and string selectors are not interchangeable. | No further constraint recorded |
| `language` | query | Conditional or optional | `string` | Language selector/content language; use the endpoint's supported values and fallback rules. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [AppReleaseDetailDto](../schemas/a.md#appreleasedetaildto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `text/plain`, `application/json`, `text/json`, `application/problem+json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/app-releases/{version}/build/{build}`

**What it does:** Read the permitted records/state for app releases / build. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Anonymous bearer metadata.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `version` | path | Yes | `string` | Version in this model's domain; not automatically an API major version. | No further constraint recorded |
| `build` | path | Yes | `integer (int32)` | Numeric build for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | minimum: `1` |
| `surface` | query | Conditional or optional | `string` | Surface text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | No further constraint recorded |
| `platform` | query | Conditional or optional | `string` | Platform selector in this contract; numeric enums and string selectors are not interchangeable. | No further constraint recorded |
| `language` | query | Conditional or optional | `string` | Language selector/content language; use the endpoint's supported values and fallback rules. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [AppReleaseDetailDto](../schemas/a.md#appreleasedetaildto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `text/plain`, `application/json`, `text/json`, `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `text/plain`, `application/json`, `text/json`, `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/app-version-policy`

**What it does:** Read app-version compatibility/update policy for the requested platform/version/build context.

**Explanation basis:** Operation-specific explanation.

**Access:** Anonymous bearer metadata.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `platform` | query | Yes | `string` | Platform selector in this contract; numeric enums and string selectors are not interchangeable. | No further constraint recorded |
| `version` | query | Yes | `string` | Version in this model's domain; not automatically an API major version. | No further constraint recorded |
| `build` | query | Conditional or optional | `integer (int32)` | Numeric build for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `language` | query | Conditional or optional | `string` | Language selector/content language; use the endpoint's supported values and fallback rules. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [AppVersionPolicyDto](../schemas/a.md#appversionpolicydto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `text/plain`, `application/json`, `text/json`, `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/blog`

**What it does:** Read the permitted records/state for blog. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Anonymous bearer metadata.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `language` | query | Conditional or optional | `string` | Language selector/content language; use the endpoint's supported values and fallback rules. | No further constraint recorded |
| `category` | query | Conditional or optional | `string` | Category text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | No further constraint recorded |
| `tag` | query | Conditional or optional | `string` | Tag text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | No further constraint recorded |
| `q` | query | Conditional or optional | `string` | Q text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | No further constraint recorded |
| `page` | query | Conditional or optional | `integer (int32)` | Page-number context for this endpoint; not a universal zero-based offset. | No further constraint recorded |
| `pageSize` | query | Conditional or optional | `integer (int32)` | Requested or returned page size, subject to this endpoint's server bounds. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [BlogCatalogDto](../schemas/b.md#blogcatalogdto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/blog/{slug}`

**What it does:** Read the permitted records/state for blog. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Anonymous bearer metadata.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `slug` | path | Yes | `string` | Slug text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | No further constraint recorded |
| `language` | query | Conditional or optional | `string` | Language selector/content language; use the endpoint's supported values and fallback rules. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [BlogPostDto](../schemas/b.md#blogpostdto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/content`

**What it does:** Read the permitted records/state for content. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Anonymous bearer metadata.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `language` | query | Conditional or optional | `string` | Language selector/content language; use the endpoint's supported values and fallback rules. | No further constraint recorded |
| `countryCode` | query | Conditional or optional | `string` | Country ISO code for this model/context; it cannot override authenticated country authority. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | Array of [ContentPageDto](../schemas/c.md#contentpagedto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## POST `/api/v1/content/contact`

**What it does:** Submit/create the documented record or action for content / contact. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Anonymous bearer metadata.

**Body:** [SubmitWebsiteContactDto](../schemas/s.md#submitwebsitecontactdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | `string (uuid)` | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/content/legal-catalogue`

**What it does:** Read the permitted records/state for content / legal catalogue. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Anonymous bearer metadata.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `language` | query | Yes | `string` | Language selector/content language; use the endpoint's supported values and fallback rules. | No further constraint recorded |
| `countryCode` | query | Yes | `string` | Country ISO code for this model/context; it cannot override authenticated country authority. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [LegalDocumentCatalogueDto](../schemas/l.md#legaldocumentcataloguedto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `text/plain`, `application/json`, `text/json`, `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/content/{slug}`

**What it does:** Read the permitted records/state for content. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Anonymous bearer metadata.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `slug` | path | Yes | `string` | Slug text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | No further constraint recorded |
| `language` | query | Conditional or optional | `string` | Language selector/content language; use the endpoint's supported values and fallback rules. | No further constraint recorded |
| `countryCode` | query | Conditional or optional | `string` | Country ISO code for this model/context; it cannot override authenticated country authority. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [ContentPageDto](../schemas/c.md#contentpagedto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/content/{slug}/versions`

**What it does:** Read the permitted records/state for content / versions. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Anonymous bearer metadata.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `slug` | path | Yes | `string` | Slug text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | No further constraint recorded |
| `language` | query | Conditional or optional | `string` | Language selector/content language; use the endpoint's supported values and fallback rules. | No further constraint recorded |
| `countryCode` | query | Conditional or optional | `string` | Country ISO code for this model/context; it cannot override authenticated country authority. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | Array of [LegalDocumentVersionSummaryDto](../schemas/l.md#legaldocumentversionsummarydto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/content/{slug}/versions/{version}`

**What it does:** Read the permitted records/state for content / versions. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Anonymous bearer metadata.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `slug` | path | Yes | `string` | Slug text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | No further constraint recorded |
| `version` | path | Yes | `string` | Version in this model's domain; not automatically an API major version. | No further constraint recorded |
| `language` | query | Conditional or optional | `string` | Language selector/content language; use the endpoint's supported values and fallback rules. | No further constraint recorded |
| `countryCode` | query | Conditional or optional | `string` | Country ISO code for this model/context; it cannot override authenticated country authority. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [LegalDocumentVersionDto](../schemas/l.md#legaldocumentversiondto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/content/{slug}/versions/{version}/pdf`

**What it does:** Read the permitted records/state for content / versions / pdf. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Anonymous bearer metadata.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `slug` | path | Yes | `string` | Slug text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | No further constraint recorded |
| `version` | path | Yes | `string` | Version in this model's domain; not automatically an API major version. | No further constraint recorded |
| `language` | query | Conditional or optional | `string` | Language selector/content language; use the endpoint's supported values and fallback rules. | No further constraint recorded |
| `countryCode` | query | Conditional or optional | `string` | Country ISO code for this model/context; it cannot override authenticated country authority. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | `string (binary)` | `application/pdf` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/features`

**What it does:** Read applicable feature enablement for the current authenticated context.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required.

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [FeaturePolicyEnvelopeDto](../schemas/f.md#featurepolicyenvelopedto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## POST `/api/v1/legal-acceptances`

**What it does:** Submit/create the documented record or action for legal acceptances. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

**Body:** [AcceptLegalDocumentDto](../schemas/a.md#acceptlegaldocumentdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [LegalDocumentAcceptanceDto](../schemas/l.md#legaldocumentacceptancedto) | `text/plain`, `application/json`, `text/json` | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
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

## GET `/api/v1/legal-acceptances/catalogue`

**What it does:** Read the permitted records/state for legal acceptances / catalogue. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `language` | query | Yes | `string` | Language selector/content language; use the endpoint's supported values and fallback rules. | No further constraint recorded |
| `countryCode` | query | Yes | `string` | Country ISO code for this model/context; it cannot override authenticated country authority. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [LegalDocumentCatalogueDto](../schemas/l.md#legaldocumentcataloguedto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `text/plain`, `application/json`, `text/json`, `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `text/plain`, `application/json`, `text/json`, `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/public/capabilities`

**What it does:** Read public capability/availability information; individual actions still require their own authorization and readiness.

**Explanation basis:** Operation-specific explanation.

**Access:** Anonymous bearer metadata.

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | No typed schema recorded | None recorded | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/public/country-sites`

**What it does:** List published country-site information for discovery and public navigation.

**Explanation basis:** Operation-specific explanation.

**Access:** Anonymous bearer metadata.

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | Array of [PublicCountrySiteDto](../schemas/p.md#publiccountrysitedto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/public/membership-prices`

**What it does:** Read informational membership prices in the selected country's currency; this does not create an executable purchase.

**Explanation basis:** Operation-specific explanation.

**Access:** Anonymous bearer metadata.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `countryCode` | query | Yes | `string` | Country ISO code for this model/context; it cannot override authenticated country authority. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [PublicMembershipPricesDto](../schemas/p.md#publicmembershippricesdto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/reference-data/banks`

**What it does:** Read the permitted records/state for reference data / banks. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Anonymous bearer metadata.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `countryCode` | query | Yes | `string` | Country ISO code for this model/context; it cannot override authenticated country authority. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | Array of [BankReferenceDto](../schemas/b.md#bankreferencedto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/reference-data/countries`

**What it does:** Read the permitted records/state for reference data / countries. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Anonymous bearer metadata.

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | Array of [CountryReferenceDto](../schemas/c.md#countryreferencedto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/reference-data/vehicle-insurers`

**What it does:** Read the permitted records/state for reference data / vehicle insurers. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Anonymous bearer metadata.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `countryCode` | query | Yes | `string` | Country ISO code for this model/context; it cannot override authenticated country authority. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | Array of [VehicleInsurerReferenceDto](../schemas/v.md#vehicleinsurerreferencedto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/resources/manuals`

**What it does:** Read the permitted records/state for resources / manuals. This route-derived summary does not establish additional lifecycle rules.

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

## GET `/api/v1/vehicle-catalog/makes`

**What it does:** Read the permitted records/state for vehicle catalog / makes. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | Array of `string` | `text/plain`, `application/json`, `text/json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/vehicle-catalog/models`

**What it does:** Read the permitted records/state for vehicle catalog / models. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `make` | query | Yes | `string` | Vehicle manufacturer name/catalog selection. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | Array of `string` | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/vehicle-catalog/years`

**What it does:** Read the permitted records/state for vehicle catalog / years. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | Array of `integer (int32)` | `text/plain`, `application/json`, `text/json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/vehicle-categories`

**What it does:** Read the permitted records/state for vehicle categories. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Anonymous bearer metadata.

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | Array of [PublicVehicleCategoryDto](../schemas/p.md#publicvehiclecategorydto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
