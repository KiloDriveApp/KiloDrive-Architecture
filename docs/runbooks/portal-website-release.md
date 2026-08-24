# Portal and corporate website release runbook

- **Owner:** Web release engineering, content operations, and application security
- **Status:** Operational browser-application release procedure
- **Last exercised:** Not yet recorded in this public repository
- **Related architecture:** [Portal and website](../architecture/portal-and-website.md), [API architecture](../architecture/api.md), and [application security](../security/application-security.md)

## Purpose and scope

Use this runbook to build, verify, and deploy the KiloDrive authenticated Portal
and public corporate Website. Both are ASP.NET Core applications that consume the
API, but their risk profiles differ:

- the **Portal** holds authenticated role-based administration and customer
  workflows; and
- the **Website** serves public content, tenant branding, legal/support pages,
  and calculators backed by reviewed API contracts.

This runbook covers immutable packaging, API compatibility, role and tenant
boundaries, strict CSP/security headers, CMS content, calculators, traffic
switching, smoke testing, and rollback. It does not authorize API or schema
changes; coordinate those through their own reviewed releases.

## Owners and decision rights

| Role | Responsibility |
| --- | --- |
| Web release lead | Owns change window, artifact identity, rollout, and final evidence |
| Portal owner | Verifies authentication, authorization, antiforgery, admin/user workflows |
| Website/content owner | Verifies public pages, locales, metadata, legal links, and calculators |
| API owner | Confirms routes/contracts, feature flags, and production compatibility |
| Security reviewer | Confirms CSP, headers, cookies, redirects, dependencies, and secret handling |
| Content/legal reviewer | Approves published content, privacy, terms, support, and claims |

## Preconditions

- The reviewed commit and exact release package are identifiable by hash.
- Release build/tests pass from a clean checkout using the pinned .NET SDK.
- The production API binary and OpenAPI contract support the release.
- Portal/Website `appsettings.json` shape matches code; protected values are
  referenced outside the package.
- Previous known-good immutable packages remain available.
- Database-driven content and calculator reference data are reviewed.
- Test accounts cover each supported role/permission without using real users.
- CSP and static assets are testable from the final package/host path.
- Traffic can be drained or switched one application at a time.

## Safety and stop conditions

Stop the release when:

- the package contains secrets, private settings, logs, uploads, fixture
  credentials, or build history;
- Portal role/tenant/country authorization tests fail;
- antiforgery is missing from a state-changing form;
- correlation/security headers disappear on redirects, validation errors, or
  exceptions;
- the CSP must be weakened with broad `unsafe-inline`, wildcard origins, or an
  undocumented exception to make the page render;
- a public content claim presents an aspirational feature as deployed fact;
- legal, privacy, support, or subscription links are broken;
- calculators disagree materially with the mobile source-of-truth contract; or
- the exact API version and target environment cannot be proven.

Never copy a development `appsettings` file over production. Never use a generic
configuration serializer that escapes policy strings into a different effective
value. Never disable CSP globally to make one helper/library work.

## Build and package

Build Portal and Website into separate isolated versioned directories. Do not
combine their output or publish over a live content root.

For each application:

1. restore with the pinned SDK/package graph;
2. run format/analyzer/build and relevant unit/integration/render tests;
3. publish release output to a clean staging directory;
4. exclude source, tests, `bin`/`obj` history, local settings, logs, uploads,
   dumps, keys, and fixture data;
5. inventory static assets and generate package hashes/SBOM/notices;
6. start the package against an isolated or controlled API endpoint with provider
   side effects disabled; and
7. run headers, routes, roles, content, and rendered browser checks.

Promote the tested package. A later rebuild is a different artifact and needs a
new evidence chain.

## Configuration and HTTP hardening gate

Verify configuration as the actual service identity:

- API base URL is HTTPS, expected, and cannot be changed by untrusted request
  input;
- tenant/country headers originate from validated user/domain context;
- authentication cookies are Secure, HttpOnly, appropriately SameSite, bounded,
  and protected by persistent encrypted Data Protection keys;
- forwarded headers are trusted only from approved proxy boundaries;
- correlation ID is validated/generated, echoed on every response, and forwarded
  to API calls;
- HSTS (where appropriate), `nosniff`, frame protection, Referrer Policy, and CSP
  survive success, redirect, validation, 404, and sanitized 500 paths;
- CSP for corporate/portal contains no `unsafe-inline` outside a separately
  documented Swagger scope; and
- logs redact cookies, authorization, tokens, form secrets, contact details,
  document links, and API payloads.

Prefer self-hosted version-pinned script/style assets. If a component tries to
inject inline styles, refactor or configure nonce/hash support narrowly. Do not
copy a CSP violation hash into policy without understanding whether the content
is stable and trusted.

## Portal certification

### Authentication and session

Test login, 2FA/step-up where required, logout revocation, session expiry, refresh
or reauthentication behavior, password/reset boundaries, lockout, and correlation
headers. A failed API session must route to a safe login/session-expired state,
not leave an authenticated-looking shell returning repeated errors.

### Authorization and tenancy

Use seeded non-production fixtures to verify menus and direct URLs for system
administrator, tenant administrator, rider, driver, rental owner, and rental team
permissions. Test cross-user IDOR and cross-tenant/country attempts. Hidden menu
items are not authorization; the API must deny the request.

System administrators must complete required step-up, select an authorized
country workspace, and see only that country's operational records. A global
administrator must not require a fake country `Users` projection.

### Forms and mutations

For every state-changing form:

- GET renders current values without mutation;
- POST action is distinct, authorized, and validates antiforgery;
- validation errors preserve safe input and field-specific messages;
- success uses Post/Redirect/Get where appropriate;
- API errors map to mature user states rather than raw JSON/status text;
- duplicate submissions are idempotent where the domain requires it; and
- audit/correlation evidence exists without form payloads.

At minimum cover system settings, calculator settings, drivers/riders/vehicles,
verification/documents, support tickets, memberships/plans, banks/branches,
wallet/cashout, rental organizations/teams, reports, notifications, and CMS.

### Detail and document views

Tabbed entity pages should load profile, audit, trips, finance, security,
documents, vehicles, membership, and support independently so one optional error
does not blank the page. Enum values render human names. Times use the viewer's
authorized timezone. Money uses row ISO currency and exact minor-unit formatting.

Private documents remain attachment-only, signed, audited, non-public, and
quarantine-aware. A pending/rejected scan should show a clear safe status rather
than exposing a raw `409` client exception.

## Corporate website certification

### Content and tenancy

Verify each public page loads published database content for the intended tenant
and locale. Missing translations follow the documented fallback; an untrusted
`X-Tenant` header must not provide a production security boundary. Confirm drafts
and unpublished content cannot be fetched publicly.

Review headings, grammar, link targets, navigation, footer, contact/support,
privacy, terms/EULA, data security, accessibility, metadata, canonical URL,
OpenGraph, and `hreflang`. Test English plus every published locale.

The reviewed navigation must expose Why KiloDrive, Safety & Trust, Pricing &
Plans, and Resources without hiding the direct Riders, Drivers, Rentals, Parcel,
Features, Membership, Safety, Data Security, calculators, blog, About, and
Support destinations. At 320 pixels, verify the menu opens, announces
“Navigation menu” (localized where published), reports expanded/collapsed state,
keeps every item reachable, closes predictably, and does not cover the primary
action.

Verify `WebsiteApi:PublicBaseUrl` is the approved HTTPS public origin. Then
inspect rendered—not source-only—SEO output:

- one absolute canonical URL for the current route;
- `x-default`, English, Spanish, and French alternates with the correct route;
- route-specific title and description plus Open Graph and Twitter summary
  metadata;
- valid WebSite/Organization data on the shell, Breadcrumb data on content
  pages, and BlogPosting author/date data on posts;
- `sitemap.xml` containing only approved public routes/variants; and
- `robots.txt` pointing to the canonical sitemap without disclosing private
  routes.

These controls improve discoverability; they do not justify analytics pixels,
cross-site tracking, unreviewed scripts, or a CSP exception.

### Contact and public forms

Email is optional where product policy says so. Validate field-specific errors,
Turnstile or approved abuse control, rate limiting, antiforgery where applicable,
correlation, successful clearing, and durable notification dispatch. Contact
emails may include a safe reference and authorized diagnostic browser/IP metadata
under policy; they must not block the HTTP response waiting for email delivery.

### Calculators

The mobile calculator contract is the source of truth unless a newer reviewed API
contract says otherwise. Test input labels, dropdowns, country/currency/unit
rules, period selection, optional/return/stops/diversions, validation, component
arithmetic, grand total, empty/unavailable behavior, and mobile/website parity.

For Jamaica tolls, use known public-landmark fixtures with expected plazas,
vehicle class, historical rate period, re-entry/return behavior, distance cost,
and exact grand-total sum. Zero matched tolls must not be presented as confidently
zero when the route/reference match failed.

## Rendered browser matrix

Use a supported browser automation suite with seeded accounts. Cover:

- narrow phone, tablet, and desktop widths;
- portrait/landscape where relevant;
- 1.0x, 1.3x, and higher supported text zoom;
- light/dark/high-contrast where offered;
- keyboard focus, tab order, visible focus, screen-reader landmarks, and 48 px
  targets for critical controls;
- every route, menu, modal, dropdown, tab, validation, and permission-specific
  menu; and
- screenshots plus console, network, CSP, mixed-content, and unhandled-promise
  assertions.

Screenshots must contain only fixtures and must not capture credentials or tokens.

## Deployment procedure

Deploy Portal and Website independently so a failure has a clear owner.

1. Record baseline package versions, traffic, latency/errors, API health, and CSP
   violation rate.
2. Freeze unrelated web/API/content deployments.
3. Drain one application/site or canary node.
4. stop it cleanly and place the new immutable package in a versioned directory;
5. attach only approved protected configuration/key references with correct ACLs;
6. switch one canary to the new package and prove reported version/content root;
7. test liveness/startup, root/login, security/correlation headers, static assets,
   and API connectivity;
8. run the production-safe Portal or Website smoke set;
9. restore traffic gradually and observe at least two normal windows; then
10. deploy the other application through the same independent sequence.

If an API release is also required, deploy and certify it first through the
[API deployment runbook](api-deployment.md), while preserving backward
compatibility for the currently serving web clients.

## Production-safe smoke set

### Portal

- unauthenticated redirect retains correlation and hardening headers;
- each fixture role logs in and sees only its allowed menu/routes;
- system admin selects an authorized country workspace;
- Settings GET renders current data; invalid POST returns field errors; valid
  POST includes antiforgery and audit;
- one representative entity list/detail/tab and one safe fixture mutation work;
- a quarantined document shows a safe state and an approved fixture document can
  be viewed through signed delivery; and
- logout revokes the session and direct navigation no longer succeeds.

### Website

- home, support/contact, privacy, terms, data security, and calculator pages load;
- tenant and locale content are correct with no draft leak;
- contact validation/success and Turnstile/rate-limit behavior work using a
  dedicated fixture;
- at least one known calculator route matches mobile/API component totals;
- canonical/metadata/`hreflang` and internal/external links are valid; and
- Twitter/Open Graph and structured data match the current content, sitemap and
  robots are canonical, and the narrow responsive menu remains keyboard- and
  screen-reader-operable; and
- no CSP, mixed-content, console, or uncaught browser error appears.

## Diagnosis guide

| Symptom | Likely cause | Safe action |
| --- | --- | --- |
| Portal page is blank | API auth/contract error, optional tab failure, JS/CSP exception | inspect correlation/console; keep successful core data visible |
| Inline style blocked | third-party helper or component mutation under strict CSP | refactor/self-host/nonce narrowly; do not add global `unsafe-inline` |
| Entity detail returns empty | route ID, role/country context, DTO mismatch, tab loader collapse | verify API response and independent tab states |
| Login loop after deploy | Data Protection/cookie key loss, callback URL, clock, API session | restore persistent keys/config; do not weaken cookie settings |
| Public page wrong tenant | host/header tenant resolution/cache key issue | contain content; verify trusted domain-to-tenant mapping |
| Calculator differs from mobile | duplicated formula/reference/DTO behavior | stop publishing wrong result; reconcile with source-of-truth contract |
| Static assets 404 | package path/base URL/cache/version mismatch | correct immutable package/reference; avoid editing live files |
| Canonical/structured data uses an internal host | missing or wrong public base URL | restore reviewed HTTPS `PublicBaseUrl`; do not derive authority from an untrusted Host header |
| Mobile navigation is empty or unlabelled | responsive-menu initialization/content fallback defect | verify fallback links, accessible name/expanded state and CSP-safe script execution |
| Security headers absent on errors | response clear/error middleware order | use shared hardening path and test 4xx/5xx |

## Rollback

1. Remove the affected canary/site from traffic.
2. Capture package hash, correlation IDs, sanitized browser/HTTP evidence, and
   first bad time.
3. Point the application to the prior immutable package.
4. Restore the prior compatible configuration contract if separately versioned;
   preserve Data Protection keys and content data.
5. Start one canary and verify package identity, login/public page, API calls,
   headers/CSP, static assets, and representative role/content flow.
6. Restore traffic gradually and observe two windows.

Do not roll back database content by overwriting it from a package. If a CMS edit
was wrong, publish an audited corrected revision. If the API contract is the
cause, coordinate an API rollback without breaking other clients.

## Verification criteria

- Every serving web node reports the intended package/commit.
- API contract/base URL and role/tenant/country boundaries pass.
- Correlation and security headers survive success, redirect, validation, 404,
  and sanitized 500 responses.
- Strict CSP produces no unexplained violation and contains no broad exception.
- Portal role routes/forms/tabs/documents/audit behave with fixtures.
- Website locales/content/legal/support/contact/calculators behave as reviewed.
- Browser matrix has no blockers, credential-bearing artifacts, or console error.
- Error/latency/CSP metrics remain within baseline for two windows.

## Evidence to retain

Retain change ID, roles, commit/package/static-asset hashes, SBOM/notices,
configuration-shape validation, API/OpenAPI compatibility, CSP/header results,
browser suite and sanitized screenshots, content/legal approval, calculator
fixtures, smoke correlation IDs, baseline/recovery metrics, rollout/rollback
timeline, and cleanup.

## Escalation

Escalate cross-role/tenant/country access, private document exposure, session/key
loss, wrong financial/calculator result, unpublished content leak, missing legal
notice, persistent CSP bypass, or inability to prove the package immediately to
security, privacy, financial, and incident owners as appropriate.

## Common pitfalls

- Deploying Portal and Website together and losing fault isolation.
- Copying appsettings through a serializer that rewrites CSP quotes.
- Adding `unsafe-inline` to silence one JavaScript helper.
- Verifying menus without testing direct unauthorized URLs.
- Treating a hidden tab as proof the API protects the data.
- Letting one failed optional tab blank an otherwise useful detail page.
- Publishing aspirational features as complete without code/test proof.
- Maintaining a second calculator formula that drifts from mobile/API behavior.
- Testing with an administrator's browser session rather than seeded role fixtures.
- Capturing credentials or private documents in screenshots.
