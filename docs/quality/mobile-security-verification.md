# Mobile security verification for both apps

This map translates the [OWASP Mobile Application Security Verification Standard](https://mas.owasp.org/MASVS/)
control groups into KiloDrive-specific questions for the consumer and System
Admin apps. It is an engineering test plan, **not** an OWASP certification,
penetration-test report or claim that every row has passed. The source apps
share an API but have different app identities, storage, audiences, notification
channels and release candidates. Each must be assessed on its own signed
Android and iOS artifacts.

## Evidence levels

| Level | Can show | Cannot by itself show |
| --- | --- | --- |
| Source/static review | Intended boundary, dangerous API use, generated contract and configuration | Runtime OS behavior or deployed provider policy |
| Unit/widget test | Deterministic state, denial presentation, redaction and formatting | Native keystore, App Check, OS notification or signed-store behavior |
| API/database test | Server authorization, session/revision/idempotency and owning transaction | Native app integrity or third-party acceptance |
| Signed-device test | Final binary, storage lifecycle, permissions, backgrounding and recipient isolation | Every provider failure or all production operating conditions |
| Provider/operational exercise | Configured integration, callback/retry and recovery | Permanent availability after the exercise window |

Report the lowest evidence level actually achieved. A mocked FCM send is not
a delivered push; a successful login widget is not device-bound session proof.
Associate each result with the exact app version, source revision, signed
artifact hash, OS/device class, country and fixture category. Keep sensitive
raw artifacts in protected evidence storage.

## Control-group map

| MASVS group | Consumer questions | System Admin questions | Required evidence before a stronger claim |
| --- | --- | --- | --- |
| Storage | Are tokens, app-lock material and pending operations account-bound, minimal and cleared on switch/logout? Are trip safety caches bounded? | Are Admin credentials and pending mutations isolated from consumer data and from another workspace? Do restricted document bytes expire? | Source and secure-storage tests; signed reinstall, backup/restore, logout and account-switch observations |
| Cryptography | Does local protection use platform-managed keys where intended, and do clients avoid storing server secrets? | Is the Admin pending-operation journal protected and free of passwords/step-up proofs? | Reviewed primitives/key ownership, corruption and key-loss behavior, artifact inspection |
| Authentication/authorization | Does consumer login grant only active rider/driver/rental workspaces? Do social links, reset and 2FA require server proof? | Does a dual-role person receive a separately scoped admin session? Are direct routes, target records and mutations denied without current grants? | Role matrix, cross-user/country/tenant denial, revoked-session and recent-auth/step-up tests |
| Network | Are sensitive calls protected in transit and scoped to the correct session? Are unknown mutation results reconciled? | Can a scope switch or refresh race deliver old-country data or re-send a financial decision? | Transport/config review, stale-response race, failure injection, API/read-back evidence |
| Platform | Are permission prompts contextual; are deep links, documents, store/call/push callbacks checked against current account? | Are app identity, App Check, installation proof, OS notifications and private views handled for both platforms? | Final merged manifests/entitlements, signed-device lifecycle and callback tests |
| Code | Do adapter results distinguish cancellation, failure and unknown? Are formatters and enum fallbacks safe? | Do unknown grants/statuses disable unsafe controls; are source-boundary and generated contract gates current? | Static analysis, deterministic tests, dependency and artifact review |
| Resilience | Does altered or stale client state fail server eligibility, billing and device checks? | Does changing a menu, app claim or local capability fail to grant admin access? | API authorization, tamper/old-client and negative role tests in approved environments |
| Privacy | Are OS previews, logs, analytics, location and account deletion minimized? | Are dossiers, call evidence, exports and alert hints purpose-limited and cleared across workspaces? | Redaction scans, data-flow review, signed-device preview and disclosure tests |

This mapping is intentionally phrased as review questions. Controls marked
implemented in source still need the applicable runtime proof. Cross-reference
[application security](../security/application-security.md),
[admin data handling](../security/admin-data-handling.md), and
[mobile sessions and installations](../architecture/mobile-session-and-device-lifecycle.md).

## Boundary cases with high release value

1. **Dual-role separation:** one global person with admin and rider membership
   signs into both apps. The consumer sees only consumer work; Admin sees only
   current allowed workspaces. Revoking one session or membership changes the
   corresponding access without leaking the other app's local data.
2. **Account switch and process death:** a private dossier, pending mutation,
   push route or cached avatar from one account cannot appear in another.
   Restart restores only current server-authorized state.
3. **Unknown financial outcome:** lose the HTTP response after the server may
   have committed. The original key and revision remain, the app shows a
   non-misleading state, and independent read-back decides the next action.
4. **Installation lifecycle:** reinstall or app-data reset creates a new
   installation relationship. A historical device association does not qualify
   an exact-recipient notification or authorize a request.
5. **Recipient isolation:** an admin alert or consumer push arrives during
   logout, account switch, permission change or session revocation. Generic OS
   text reveals no private detail, and opening rechecks the current target.
6. **Restricted evidence:** a document or call record changes authorization or
   retention state after a list loads. Detail open rechecks permission and does
   not reuse a stale private byte cache.
7. **Native billing:** cancellation, pending purchase, renewal, restore,
   refund and provider notification agree with server entitlement and ledger.
   A provider callback never mints access solely because it reached the app.
8. **Small and large presentations:** denial, confirmation, unknown outcome
   and privacy text remain understandable at narrow width, large text, high
   contrast, screen reader and keyboard focus.

## Test-design rules

Use deterministic barriers for asynchronous races: prove that a native or
server operation started before interrupting it. Avoid millisecond sleeps that
pass only on one scheduler. For each high-risk mutation, include an authorized
actor, a denied actor, wrong scope, stale precondition, duplicate key, lost
response, server 5xx after possible execution, and process restoration. For
provider adapters, classify explicit cancellation separately from unknown
completion. For data displays, test malformed timestamps, unknown enum values,
missing currency and partial API failures without inventing a success value.

Ordinary tests should use non-user fixtures and refuse real external origins.
Real-provider and signed-device jobs require an explicit owner, approved
environment, bounded run, cleanup and sanitized evidence. A public report
contains only safe references and conclusion; it never publishes token values,
private documents, messages, customer identities or precise defensive settings.

## Release report format

For each app/platform/candidate, record a small matrix:

| Field | Meaning |
| --- | --- |
| Control and journey | What promise and boundary were assessed |
| Implementation state | Implemented, partial, unavailable or planned in source |
| Evidence level | Static, host test, API/database, signed device or provider exercise |
| Result | Passed, failed, blocked or not run; no ambiguous green status |
| Artifact identity | Version, commit and signed hash kept in protected evidence |
| Scope | OS, country, store/provider environment, role and fixture class |
| Limit | What the evidence does not prove and the next owner/action |

The [two-app release runbook](../runbooks/two-app-release-and-compatibility.md)
uses this report to decide whether an exact candidate can be distributed.
