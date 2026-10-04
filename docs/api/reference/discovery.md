# Public information and capability discovery

[Reference index](README.md) · [API guide](../README.md)

Access shown here describes bearer metadata only. Anonymous operations can still
require installation admission, application attestation, contact proof or country
context. A bearer token does not replace ownership, feature gates or role checks.

Each entry lists recorded schemas, parameters, status codes and mutation guards.
Response metadata is not a complete list of runtime business outcomes; read the
[contract limitations](../coverage-and-limitations.md).

## GET `/api/v1/app-releases`

**What it does:** Read the permitted records/state for app releases. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Anonymous bearer metadata.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `surface` | query | Conditional or optional | `string` | Surface text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |
| `platform` | query | Conditional or optional | `string` | Platform selector in this contract; numeric enums and string selectors are not interchangeable. |
| `language` | query | Conditional or optional | `string` | Language selector/content language; use the endpoint's supported values and fallback rules. |
| `page` | query | Conditional or optional | `integer (int32)` | Page-number context for this endpoint; not a universal zero-based offset. |
| `pageSize` | query | Conditional or optional | `integer (int32)` | Requested or returned page size, subject to this endpoint's server bounds. |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [AppReleaseListDto](../schemas/a.md#appreleaselistdto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `text/plain`, `application/json`, `text/json`, `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/app-releases/current`

**What it does:** Read the permitted records/state for app releases → current. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Anonymous bearer metadata.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `surface` | query | Conditional or optional | `string` | Surface text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |
| `platform` | query | Conditional or optional | `string` | Platform selector in this contract; numeric enums and string selectors are not interchangeable. |
| `language` | query | Conditional or optional | `string` | Language selector/content language; use the endpoint's supported values and fallback rules. |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [AppReleaseDetailDto](../schemas/a.md#appreleasedetaildto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/app-releases/{version}`

**What it does:** Read the permitted records/state for app releases. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Anonymous bearer metadata.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `version` | path | Yes | `string` | Version in this model's domain; not automatically an API major version. |
| `surface` | query | Conditional or optional | `string` | Surface text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |
| `platform` | query | Conditional or optional | `string` | Platform selector in this contract; numeric enums and string selectors are not interchangeable. |
| `language` | query | Conditional or optional | `string` | Language selector/content language; use the endpoint's supported values and fallback rules. |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [AppReleaseDetailDto](../schemas/a.md#appreleasedetaildto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `text/plain`, `application/json`, `text/json`, `application/problem+json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/app-releases/{version}/build/{build}`

**What it does:** Read the permitted records/state for app releases → build. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Anonymous bearer metadata.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `version` | path | Yes | `string` | Version in this model's domain; not automatically an API major version. |
| `build` | path | Yes | `integer (int32)` | Numeric build for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. |
| `surface` | query | Conditional or optional | `string` | Surface text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |
| `platform` | query | Conditional or optional | `string` | Platform selector in this contract; numeric enums and string selectors are not interchangeable. |
| `language` | query | Conditional or optional | `string` | Language selector/content language; use the endpoint's supported values and fallback rules. |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [AppReleaseDetailDto](../schemas/a.md#appreleasedetaildto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `text/plain`, `application/json`, `text/json`, `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `text/plain`, `application/json`, `text/json`, `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/app-version-policy`

**What it does:** Read app-version compatibility/update policy for the requested platform/version/build context.

**Access:** Anonymous bearer metadata.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `platform` | query | Yes | `string` | Platform selector in this contract; numeric enums and string selectors are not interchangeable. |
| `version` | query | Yes | `string` | Version in this model's domain; not automatically an API major version. |
| `build` | query | Conditional or optional | `integer (int32)` | Numeric build for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. |
| `language` | query | Conditional or optional | `string` | Language selector/content language; use the endpoint's supported values and fallback rules. |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [AppVersionPolicyDto](../schemas/a.md#appversionpolicydto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `text/plain`, `application/json`, `text/json`, `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/blog`

**What it does:** Read the permitted records/state for blog. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Anonymous bearer metadata.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `language` | query | Conditional or optional | `string` | Language selector/content language; use the endpoint's supported values and fallback rules. |
| `category` | query | Conditional or optional | `string` | Category text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |
| `tag` | query | Conditional or optional | `string` | Tag text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |
| `q` | query | Conditional or optional | `string` | Q text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |
| `page` | query | Conditional or optional | `integer (int32)` | Page-number context for this endpoint; not a universal zero-based offset. |
| `pageSize` | query | Conditional or optional | `integer (int32)` | Requested or returned page size, subject to this endpoint's server bounds. |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [BlogCatalogDto](../schemas/b.md#blogcatalogdto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/blog/{slug}`

**What it does:** Read the permitted records/state for blog. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Anonymous bearer metadata.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `slug` | path | Yes | `string` | Slug text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |
| `language` | query | Conditional or optional | `string` | Language selector/content language; use the endpoint's supported values and fallback rules. |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [BlogPostDto](../schemas/b.md#blogpostdto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/content`

**What it does:** Read the permitted records/state for content. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Anonymous bearer metadata.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `language` | query | Conditional or optional | `string` | Language selector/content language; use the endpoint's supported values and fallback rules. |
| `countryCode` | query | Conditional or optional | `string` | Country ISO code for this model/context; it cannot override authenticated country authority. |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [ContentPageDto](../schemas/c.md#contentpagedto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## POST `/api/v1/content/contact`

**What it does:** Submit/create the documented record or action for content → contact. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

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

**What it does:** Read the permitted records/state for content → legal catalogue. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Anonymous bearer metadata.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `language` | query | Yes | `string` | Language selector/content language; use the endpoint's supported values and fallback rules. |
| `countryCode` | query | Yes | `string` | Country ISO code for this model/context; it cannot override authenticated country authority. |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [LegalDocumentCatalogueDto](../schemas/l.md#legaldocumentcataloguedto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `text/plain`, `application/json`, `text/json`, `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/content/{slug}`

**What it does:** Read the permitted records/state for content. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Anonymous bearer metadata.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `slug` | path | Yes | `string` | Slug text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |
| `language` | query | Conditional or optional | `string` | Language selector/content language; use the endpoint's supported values and fallback rules. |
| `countryCode` | query | Conditional or optional | `string` | Country ISO code for this model/context; it cannot override authenticated country authority. |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [ContentPageDto](../schemas/c.md#contentpagedto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/content/{slug}/versions`

**What it does:** Read the permitted records/state for content → versions. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Anonymous bearer metadata.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `slug` | path | Yes | `string` | Slug text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |
| `language` | query | Conditional or optional | `string` | Language selector/content language; use the endpoint's supported values and fallback rules. |
| `countryCode` | query | Conditional or optional | `string` | Country ISO code for this model/context; it cannot override authenticated country authority. |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [LegalDocumentVersionSummaryDto](../schemas/l.md#legaldocumentversionsummarydto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/content/{slug}/versions/{version}`

**What it does:** Read the permitted records/state for content → versions. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Anonymous bearer metadata.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `slug` | path | Yes | `string` | Slug text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |
| `version` | path | Yes | `string` | Version in this model's domain; not automatically an API major version. |
| `language` | query | Conditional or optional | `string` | Language selector/content language; use the endpoint's supported values and fallback rules. |
| `countryCode` | query | Conditional or optional | `string` | Country ISO code for this model/context; it cannot override authenticated country authority. |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [LegalDocumentVersionDto](../schemas/l.md#legaldocumentversiondto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/content/{slug}/versions/{version}/pdf`

**What it does:** Read the permitted records/state for content → versions → pdf. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Anonymous bearer metadata.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `slug` | path | Yes | `string` | Slug text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |
| `version` | path | Yes | `string` | Version in this model's domain; not automatically an API major version. |
| `language` | query | Conditional or optional | `string` | Language selector/content language; use the endpoint's supported values and fallback rules. |
| `countryCode` | query | Conditional or optional | `string` | Country ISO code for this model/context; it cannot override authenticated country authority. |

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

**What it does:** Submit/create the documented record or action for legal acceptances. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

**Body:** [AcceptLegalDocumentDto](../schemas/a.md#acceptlegaldocumentdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |

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

**What it does:** Read the permitted records/state for legal acceptances → catalogue. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `language` | query | Yes | `string` | Language selector/content language; use the endpoint's supported values and fallback rules. |
| `countryCode` | query | Yes | `string` | Country ISO code for this model/context; it cannot override authenticated country authority. |

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

**Access:** Anonymous bearer metadata.

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | No typed schema recorded | None recorded | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/public/country-sites`

**What it does:** List published country-site information for discovery and public navigation.

**Access:** Anonymous bearer metadata.

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [PublicCountrySiteDto](../schemas/p.md#publiccountrysitedto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/public/membership-prices`

**What it does:** Read informational membership prices in the selected country's currency; this does not create an executable purchase.

**Access:** Anonymous bearer metadata.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `countryCode` | query | Yes | `string` | Country ISO code for this model/context; it cannot override authenticated country authority. |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [PublicMembershipPricesDto](../schemas/p.md#publicmembershippricesdto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/reference-data/banks`

**What it does:** Read the permitted records/state for reference data → banks. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Anonymous bearer metadata.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `countryCode` | query | Yes | `string` | Country ISO code for this model/context; it cannot override authenticated country authority. |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [BankReferenceDto](../schemas/b.md#bankreferencedto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/reference-data/countries`

**What it does:** Read the permitted records/state for reference data → countries. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Anonymous bearer metadata.

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [CountryReferenceDto](../schemas/c.md#countryreferencedto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/reference-data/vehicle-insurers`

**What it does:** Read the permitted records/state for reference data → vehicle insurers. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Anonymous bearer metadata.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `countryCode` | query | Yes | `string` | Country ISO code for this model/context; it cannot override authenticated country authority. |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [VehicleInsurerReferenceDto](../schemas/v.md#vehicleinsurerreferencedto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/resources/manuals`

**What it does:** Read the permitted records/state for resources → manuals. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

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

**What it does:** Read the permitted records/state for vehicle catalog → makes. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | `string[]` | `text/plain`, `application/json`, `text/json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/vehicle-catalog/models`

**What it does:** Read the permitted records/state for vehicle catalog → models. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `make` | query | Yes | `string` | Vehicle manufacturer name/catalog selection. |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | `string[]` | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/vehicle-catalog/years`

**What it does:** Read the permitted records/state for vehicle catalog → years. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | `integer (int32)[]` | `text/plain`, `application/json`, `text/json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/vehicle-categories`

**What it does:** Read the permitted records/state for vehicle categories. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Anonymous bearer metadata.

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [PublicVehicleCategoryDto](../schemas/p.md#publicvehiclecategorydto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
