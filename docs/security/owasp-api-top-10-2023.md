# KiloDrive and the OWASP API Security Top 10: 2023

This chapter maps KiloDrive's reviewed architecture to the ten categories in
the [OWASP API Security Top 10, 2023 edition](https://api-security.owasp.org/editions/2023/en/0x11-t10/).
OWASP supplies the risk taxonomy. The KiloDrive controls, examples and evidence
assessment below come from the product's source review; OWASP has not assessed,
endorsed or certified KiloDrive through this mapping.

The source baseline and evidence definitions are in
[security controls and assurance boundaries](security-control-model.md#scope-and-strength-of-evidence).
Evidence identifiers E01–E15 refer to that chapter's
[source index](security-control-model.md#representative-source-evidence).
No category is marked “passed” merely because a corresponding class or test
exists. Effective configuration, exact endpoint coverage and release evidence
remain separate questions.

## Coverage at a glance

| OWASP category | KiloDrive concern | Representative controls | Evidence still needed for an environment-wide claim |
| --- | --- | --- | --- |
| API1: Object authorization | Another person's trip, wallet, document or payout destination | Scoped queries, ownership/participant checks, current country membership | Negative coverage for every object path, including exports and nested records |
| API2: Authentication | Account takeover, stolen/replayed sessions, unsafe recovery | Password derivation, signed tokens, session revocation, recovery and step-up | Current protocol, legacy-session and signed-client exercises |
| API3: Property authorization | Reading or writing fields beyond the caller's authority | Explicit DTOs, validators and server-owned sensitive state | Response-field and forbidden-write review per role and lifecycle |
| API4: Resource consumption | Expensive queries, uploads, maps and messaging spend | Rate budgets, bounded work, timeouts and scanner limits | Aggregate multi-node limits, enforced modes and capacity/provider-cost evidence |
| API5: Function authorization | Consumer access to administrator actions | Separate app/session scope, role/capability checks and acting workspace | Full method/route/role matrix, including aliases and background execution |
| API6: Sensitive business flows | Valid commands used to abuse marketplace or financial workflows | Eligibility, lifecycle, financial risk rules and durable operation identity | Business-abuse scenarios across distinct commands and accounts |
| API7: Server-side request forgery | A supplied destination makes the server contact an unintended service | Webhook HTTPS/address policy, connection-time DNS validation, no redirects | Inventory and tests for every other URL-fetching adapter and network egress |
| API8: Misconfiguration | Unsafe production defaults, exposed secrets or permissive infrastructure | Production validator, response hardening, secret boundaries and safe errors | Effective deployed configuration, IAM, certificates, storage and key recovery |
| API9: Inventory | Forgotten routes, versions, hosts and undocumented providers | Canonical OpenAPI, route lifecycle, curated public inventory and CI | Full private runtime inventory and retirement evidence |
| API10: Consumed APIs | Incorrectly trusting provider responses or callbacks | Verified provider evidence, schema/business validation, quarantine and reconciliation | Adversarial adapter tests and provider-backed failure/recovery exercises |

## API1: Broken Object Level Authorization

[OWASP API1](https://api-security.owasp.org/editions/2023/en/0xa1-broken-object-level-authorization/)
concerns access to the wrong record even when the caller can legitimately use
the endpoint. For KiloDrive, viewing one's own payout destination must not imply
permission to view or delete somebody else's destination by substituting its ID.

KiloDrive uses tenant-scoped queries, current country membership and explicit
owner/participant/reviewer checks. A System Admin's global identity does not
eliminate selected-workspace or document-viewing boundaries. Private download
tests include foreign tenant/country cases; financial history and realtime
records need corresponding ownership checks. UUIDv7 values are identifiers,
not access secrets. Evidence: E02, E03 and E13.

Required verification: substitute a foreign record in list-detail, nested,
download, export and mutation paths; repeat with another tenant and country.
Confirm no side effect, no leaked response fields and no informative existence
oracle. Review every deliberate query-filter bypass. Representative tests do
not establish universal endpoint coverage.

Read [authorization dimensions](security-control-model.md#authorization-decide-who-may-do-what-to-which-record).

## API2: Broken Authentication

[OWASP API2](https://api-security.owasp.org/editions/2023/en/0xa2-broken-authentication/)
covers weaknesses in establishing and retaining identity, including recovery
flows. KiloDrive's relevant controls include salted password derivation,
asymmetric token validation, rotating refresh families, authoritative account
state, passkey ceremonies, explicit social linking and endpoint-specific recent
authentication/2FA. App Check is complementary application evidence, not a
replacement for human authentication. Evidence: E01–E05.

Required verification: reject invalid issuer/audience/signature/lifetime,
revoked families, cross-user recovery proofs and reused ceremonies; exercise
refresh rotation races, logout on one device, account switch and provider
outage. Check that social email equality cannot link an existing account.

The source retains compatibility for legacy tokens without a family claim.
Browser/native admission also has configuration boundaries. Their rollout and
retirement evidence must accompany any statement that all active sessions share
the newest binding guarantees. Source tests alone do not establish enrolled
MFA coverage, secure key custody or current provider configuration.

Read [authentication controls](security-control-model.md#authentication-prove-identity-and-preserve-it-safely).

## API3: Broken Object Property Level Authorization

[OWASP API3](https://api-security.owasp.org/editions/2023/en/0xa3-broken-object-property-level-authorization/)
concerns which properties a caller can read or change after reaching an object.
KiloDrive must separate editable contact/profile fields from server-owned role,
tenant, balance, document decision, provider state and entitlement fields.

Explicit DTOs and validators constrain commands; response projections should
expose only the fields needed for the authorized task. A readable audit detail
or dossier export still requires field minimization. Sensitive evidence must
not enter push bodies, broad realtime events or generic error payloads. E03,
E06 and E13 cover related boundaries, but no single generic DTO test proves
all field-level permissions.

Required verification: attempt unauthorized property changes and verify stored
state is unchanged, whether the parser rejects or ignores the extra input.
Compare response fields across consumer, driver and administrative roles,
including null/error/unknown-enum paths. Public schema sanitization protects
publication; it does not sanitize a live API response. The generated
[field coverage queue](../api/reference/coverage.md) remains an explicit semantic
documentation limitation, not proof of runtime exposure.

## API4: Unrestricted Resource Consumption

[OWASP API4](https://api-security.owasp.org/editions/2023/en/0xa4-unrestricted-resource-consumption/)
includes resource exhaustion and provider-cost abuse. KiloDrive's exposed work
includes password derivation, document scanning, map calls, exports, recovery
messages and provider diagnostics.

The implementation supplies route-specific budgets, request/input bounds,
password-work concurrency limits, provider timeouts and bounded scanner retries.
Rate-limit responses carry retry guidance; client session cleanup helps stop
accidental unauthorized polling storms. Evidence: E01, E11 and E13.

Two qualifications matter: the reviewed ASP.NET partitions are process-local,
and configurable endpoint budgets can observe without enforcing. Redis elsewhere
in the application does not turn these into cluster-wide request counters.

Required verification: oversized/paginated/bulk requests, cancellation, repeated
paid-provider calls, concurrent nodes and worker backlog. Establish aggregate
edge/distributed budgets, host resource bounds, provider spending controls and
normal-user capacity evidence. Those are operational requirements here, not
claims that every live limit was inspected. Keep defensive thresholds private.

Read [abuse and availability](security-control-model.md#abuse-controls-and-availability).

## API5: Broken Function Level Authorization

[OWASP API5](https://api-security.owasp.org/editions/2023/en/0xa5-broken-function-level-authorization/)
concerns access to an operation outside the caller's authority. In KiloDrive,
driver document decisions, wallet adjustments, catalog edits and operational
recovery belong to authorized administrative workflows.

The separate System Admin app presents those workflows. API role/capability,
country workspace and fresh-proof checks enforce them. Consumer-scoped sessions
remain consumer-scoped even when the global identity also has an administrator
role. Hiding navigation or excluding privileged endpoints from the public
OpenAPI is not access control. Evidence: E03, E08 and E15.

Required verification: direct calls from a consumer, insufficient administrator
permission, wrong workspace, changed HTTP method and compatibility alias.
Repeat for exports, batch actions and background handlers. Distinguish a
forbidden function from access to a foreign object inside an allowed function.

Independent approval defaults are domain-specific. Disabling a second reviewer
does not disable authorization or auditing, and enabling that policy is not
evidence that every unrelated admin action requires two people.

Read [the app and permission separation](security-control-model.md#consumer-and-system-admin-separation).

## API6: Unrestricted Access to Sensitive Business Flows

[OWASP API6](https://api-security.owasp.org/editions/2023/en/0xa6-unrestricted-access-to-sensitive-business-flows/)
addresses harmful use of legitimate workflows. A caller may be authenticated
and remain under transport limits while repeatedly creating reservations,
requesting verification messages or cycling financial actions.

KiloDrive's relevant defenses include driver readiness, bid/acceptance lifecycle
checks, plan rules, held-balance restrictions, cashout velocity/cooling rules,
audited administrative value actions and durable operation identity. Evidence:
E07–E09 and E15. The API recomputes eligibility; an old bid or a client screen is
not perpetual permission.

Idempotency stops duplicates of one command. It does not stop many distinct
commands with new keys. Required verification therefore includes concurrent
distinct intents, resource hoarding, repeat cancellation, promotional/value
abuse, notification amplification and re-upload/review loops. Check the business
outcome and downstream cost, not just status codes.

Automated detection coverage, cross-account correlation and operational response
remain evidence requirements. This chapter does not claim a universal bot/fraud
detection service merely because individual rules are implemented.

Read [financial safeguards](security-control-model.md#financial-safeguards).

## API7: Server Side Request Forgery

[OWASP API7](https://api-security.owasp.org/editions/2023/en/0xa7-server-side-request-forgery/)
concerns server requests directed to unintended destinations through supplied
URLs. Webhook subscriptions are one relevant KiloDrive boundary.

`WebhookDestinationPolicy` accepts permitted public HTTPS destinations, rejects
embedded credentials and unsuitable addresses, and revalidates DNS results at
connection time. The socket connects to an already validated address while
preserving normal hostname/certificate checks. Redirects and proxy use are
disabled for that handler. This avoids relying solely on validation when the
subscription was saved. Evidence: E12.

Required verification: prohibited address families, mixed DNS answers, changed
resolution and redirect behavior using controlled test infrastructure. Verify
the actual sending client uses the reviewed handler.

This control proves a bounded webhook design, not universal SSRF protection.
Inventory other provider URLs, document/media fetches, importers, health probes
and callbacks individually; assess egress restrictions separately. A destination
being administratively configured or HTTPS does not by itself establish that
it is safe. Private network details and live probing instructions are excluded
from this public guide.

## API8: Security Misconfiguration

[OWASP API8](https://api-security.owasp.org/editions/2023/en/0xa8-security-misconfiguration/)
covers unsafe configuration across application and infrastructure boundaries.
KiloDrive uses production prerequisite validation, protected secret sources,
security headers, sanitized Problem Details, trusted-proxy policy and private
upload handling. Evidence: E04, E13 and E14.

The deployment must still establish persistent Data Protection keys, signing-key
custody, restricted storage/IAM, trusted proxy addresses, appropriate CORS/CSP,
certificate validity, scanner health and provider settings. A successful startup
or schema fingerprint cannot prove all of these. WAF availability in an
architecture diagram is not evidence that a current rule is enforcing.

Required verification: effective settings for the deployed profile, protected
errors and cache headers, disabled development bypasses, secret scanning of
artifacts, restart/key recovery and narrowly scoped permissions. Verify alert
delivery as well as log generation. Rolling logs are supported; using CloudWatch
is optional. Source-only policy checks and live infrastructure assurance must
be reported separately.

Read [configuration and response responsibilities](security-control-model.md#auditing-configuration-and-response).

## API9: Improper Inventory Management

[OWASP API9](https://api-security.owasp.org/editions/2023/en/0xa9-improper-inventory-management/)
concerns forgotten interfaces and incomplete lifecycle knowledge. KiloDrive
maintains a canonical versioned contract, reviewed schema metadata and a curated
public endpoint/field reference.

At this baseline, the full private canonical artifact contains 996 paths and
1,123 operations. The public subset contains 459 paths and 528 operations;
administrative and provider-callback contracts are deliberately excluded.
Public absence does not mean an endpoint does not exist or lacks authorization.
See the [API manifest](../api/openapi/manifest.json) and
[coverage limitations](../api/coverage-and-limitations.md).

The canonical route family is `/api/v1/...`. Compatibility `/api/...` aliases
have a documented sunset of 2027-02-10; this is a lifecycle commitment, not proof
that a deployed alias has already disappeared.

Required verification: compare runtime methods/routes with the complete private
contract and policy inventory; track hosts, versions, workers, callbacks,
providers and retirement owners. Confirm old interfaces retain equivalent
controls until removal. Documentation CI proves reproducibility and structure,
not full semantic review or runtime route parity.

## API10: Unsafe Consumption of APIs

[OWASP API10](https://api-security.owasp.org/editions/2023/en/0xaa-unsafe-consumption-of-apis/)
addresses excessive trust in upstream services. KiloDrive consumes identity,
payment, store, maps, messaging, media and scanning providers through adapters.

Adapters must validate protocol identity, response shape and business binding.
For example, an authentic payment event still needs the correct server payment,
amount, currency and lifecycle; an unknown or contradictory event must not mint
wallet value. PayPal inbox/quarantine handling and distinct store purchase versus
restore contracts cover representative cases. Evidence: E04, E10, E12 and E13.

Timeouts, bounded retries, cancellation and circuit behavior limit failure
propagation. Generic retry of a value-changing request remains unsafe unless
provider idempotency and reconciliation preserve one logical operation. Provider
acceptance of a notification does not establish recipient delivery.

Required verification: malformed/truncated responses, stale/out-of-order events,
duplicates, wrong account/product/currency, provider downtime and response loss
after success. Validate environment and credential configuration separately.
An adapter interface or successful sandbox call does not certify the provider's
production behavior or every failure path.

## Prioritized assurance work

These are evidence and coverage priorities, not unverified declarations of
production vulnerabilities. Private findings should carry affected versions,
severity, owners and disclosure decisions in the restricted issue tracker.

| Priority | Owner role | Work | Completion evidence |
| --- | --- | --- | --- |
| First | API/security | Maintain the full function/object/property authorization matrix | Negative tests for current routes, aliases, exports and nested resources; reviewed exceptions |
| First | Identity/mobile/operations | Verify admission and session policy across supported client paths | Effective configuration and exact signed-artifact login, revoke, restart and account-switch results |
| First | Financial/provider | Verify interrupted and conflicting value operations | One durable outcome under races, lost responses, duplicate callbacks and provider reconciliation |
| Next | Operations/performance | Assess aggregate abuse budgets and expensive operations | Enforced-mode evidence, multi-node capacity results and provider-cost limits |
| Next | Integration/security | Extend outbound-request review beyond webhooks | Complete fetcher inventory and controlled DNS/redirect/destination regression evidence |
| Continuous | Release/platform | Retire obsolete interfaces and review supply-chain/configuration changes | Runtime inventory, sunset evidence, dependency assessment, secret and artifact checks |

## How to report assurance honestly

An assessment should identify its commit, signed build, environment, country,
provider mode, effective policy and exercise date. Record which tests used real
MySQL, real providers or test adapters and which were source inspections only.
Include untested routes, unavailable dependencies and accepted exceptions.

Do not turn a ten-row mapping into “100% OWASP compliant.” This taxonomy is a
review framework, not an exhaustive security specification. Mobile platform
security, privacy, legal compliance, supply-chain risk, insider misuse, incident
response and recovery also require assessment. Use the broader
[threat model](threat-boundaries.md), [testing guide](../quality/testing-and-verification.md)
and [security reporting policy](../../SECURITY.md) alongside this chapter.
