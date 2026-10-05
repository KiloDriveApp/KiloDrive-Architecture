# KiloDrive glossary

This glossary explains terminology used in the architecture, API, security and
operations guides. Definitions describe the reviewed design or a general
concept; an entry does not prove a feature is deployed, enabled or certified.
Use the [current baseline](docs/current-baseline.md) for source provenance and
[NOTICE.md](NOTICE.md) for publication and dependency limits.

[Common distinctions](#common-distinctions) · [A to C](#a-to-c) ·
[D to I](#d-to-i) · [J to R](#j-to-r) · [S to Z](#s-to-z) ·
[Reading paths](#reading-paths)

## Common distinctions

| Terms often confused | Difference that matters |
| --- | --- |
| Authentication / authorization / admission | Identity proof, permission for a specific action, and permission for an installation/client path are separate decisions |
| Application identity / installation / user / session | The verified app, one installation, the person/account and its renewable session are different records and trust boundaries |
| Object / property / function authorization | Which record, which fields and which operation the caller may access require separate checks |
| Recent authentication / step-up / app lock | Fresh identity proof, an action's additional server ceremony and local device privacy are not interchangeable |
| Idempotency / concurrency / reconciliation | One logical operation, current entity preconditions and authoritative outcome recovery solve different problems |
| Missing / failed / outcome unknown | Absence of evidence, an authoritative failure and an unconfirmed effect require different recovery decisions |
| Plan catalog / store product / entitlement | Editable definitions, provider sales configuration and a user's verified benefits are separate authorities |
| Scan clean / document approved / driver ready | Malware disposition, human/domain review and complete trip eligibility are separate states |
| Queued / provider accepted / delivered | A durable send request, provider processing acceptance and observed delivery are separate evidence |
| Source / configuration / deployment / certification | Existing code, effective settings, shipped artifacts and exercised scenarios must not be substituted for one another |

## A to C

| Term | Meaning |
| --- | --- |
| AAB | Android App Bundle: the publishing artifact uploaded to Google Play. Google Play uses it to generate optimized APKs for supported devices. |
| ABI | Application Binary Interface: the native machine-code contract for a processor family, such as `arm64-v8a` or `armeabi-v7a`. A package can build successfully yet fail on a device if the required ABI is absent. |
| Acting workspace | An explicitly selected and server-authorized administrative country/tenant context. A header or saved UI choice alone does not grant cross-tenant access. See [System Admin architecture](docs/architecture/system-admin-mobile-app.md). |
| Adapter | A boundary translating platform/provider protocols into typed application results. It isolates SDK behavior, timeouts and callbacks without making client observations authoritative. See [native adapters](docs/architecture/native-adapters-and-store-billing.md). |
| Adapter observation | Typed OS or provider evidence such as product discovery, a picker result or a GPS fix. The API must still decide the corresponding account, money, document or trip transition. See the [native platform handbook](docs/architecture/native-platform-handbook.md). |
| ADOT | AWS Distro for OpenTelemetry: AWS-supported components for collecting and exporting OpenTelemetry traces and metrics. It is an observability path, not the source of business truth. |
| ADR | Architecture Decision Record: a short, durable explanation of an important design choice, the alternatives considered, and the consequences the team accepts. |
| Aggregate | A cluster of domain state protected by one consistency boundary and version, such as a ride request and its actionable assignment state. |
| AML | Anti-Money Laundering controls: rules and review processes intended to detect or restrict suspicious movement of funds. A feature flag is not a substitute for an approved country operating model. |
| API | Application Programming Interface. KiloDrive's ASP.NET Core API owns server-side authentication, authorization and business rules for both apps, the Portal, Website and provider callbacks. Individual routes can be authenticated or explicitly anonymous. |
| APK | Android Package: an installable Android application artifact. KiloDrive inspects release APKs as well as AABs because native libraries and merged permissions can differ from source declarations. |
| APNs | Apple Push Notification service, used to deliver permitted notifications to Apple devices. |
| App attestation | Provider-verified evidence about an application under the configured platform policy. It supplements user authentication, installation admission and authorization; it does not prove the human's identity or grant a role. |
| App channel | The consumer or System Admin application context used in admission and notification binding. A caller-supplied label is descriptive; the verified application identity and authorized session establish the permitted channel. |
| App Check | Firebase service issuing application-attestation tokens that the API verifies for signature, issuer, audience, lifetime and permitted app identity. Protected routes and device bootstrap have distinct enforcement policies. See [device admission](docs/security/security-control-model.md#device-admission-and-identification). |
| Argon2id | Memory-hard password derivation algorithm used by KiloDrive's normal password-storage profile. Its memory, iteration, parallelism, salt, output and concurrency policy are versioned and bounded; package use does not imply FIPS validation. |
| AsyncNotifier | Riverpod state owner for asynchronous Flutter features. It coordinates user intent, loading/refresh/mutation states, cancellation, and disposal without putting transport logic in widgets. |
| At-least-once delivery | A message-delivery model in which retries can deliver the same message more than once; consumers therefore need idempotency. |
| Audit event | A durable record of an action, actor, affected party, result and time, with appropriate correlation. Readable summaries and restricted evidence serve different audiences. An audit table alone is not a tamper-proof archive. |
| Authentication | Establishing who presented valid identity proof and whether the account/session remains valid. It does not decide permission to every function, object or property. |
| Authorization | Deciding whether the current principal may perform this action on this resource in this country and lifecycle state. KiloDrive combines role, capability, ownership, tenant, country and freshness checks. |
| B-tree locality | The storage/index benefit gained when newly generated keys are roughly time ordered instead of randomly scattered across index pages. |
| Backplane | Shared transport used by multiple API nodes to distribute realtime messages and coordinate SignalR clients. KiloDrive uses Valkey where configured. |
| Bearer credential | A credential whose possession can authorize its defined use. Access tokens and presigned URLs must be protected against disclosure; their scope and lifetime still constrain what they permit. |
| BFF | Backend for Frontend: a trusted server component serving a particular browser client. Secrets used to prove that component's identity must remain server-side, not in browser JavaScript. |
| BFLA | Broken Function Level Authorization, OWASP API5:2023. A caller invokes an operation outside their role/capability, such as consumer access to an administrative decision. |
| BOLA | Broken Object Level Authorization, OWASP API1:2023. A caller accesses another person's record through an otherwise usable function. Identifiers and tenant filters alone do not establish object ownership. |
| BOPLA | Broken Object Property Level Authorization, OWASP API3:2023. An allowed object operation exposes or changes fields beyond the caller's authority; both response disclosure and writable-field checks matter. |
| Breadcrumb | A sampled, durable location observation retained for authorized trip reconstruction, safety, and distance evidence. |
| Browser-audience proof | A signed, short-lived proof supplied by an approved server-side browser component and bound to method, target and body. When enabled, a distributed nonce claim prevents replay. It supplements user/session authorization. |
| Callback fencing | Rejecting late asynchronous results when their captured account, session, workspace or operation generation no longer matches the active context. It prevents a previous user's callback from changing current state. |
| Certification row | One exact capability, platform, lifecycle, signed artifact and provider environment with an observed result and evidence link. A host test cannot fill a physical-device row. See the [native matrix](docs/quality/native-platform-certification-matrix.md). |
| Canary | A scheduled non-user probe sent to a dedicated test destination to verify a provider path without involving customer data. |
| Canonical route | The reviewed versioned HTTP route, currently `/api/v1/...`. A compatibility alias is a separate lifecycle concern and must not weaken the same authorization rules. |
| Capability | An explicitly supported administrative function with associated UI, contract and permission requirements. A navigation entry or registry row is not proof that its entire operator workflow is certified. |
| Capacity envelope | The tested combination of workload, throughput, latency, errors, saturation, and recovery headroom within which customer objectives remain satisfied. It is not a permanent “maximum users” claim. |
| CDR | Content Disarm and Reconstruction: sanitizing a document by rebuilding safe content rather than trusting the original binary. |
| Cell fingerprint | Deterministic hash of normalized country-cell table, column, index, and foreign-key metadata. |
| Circuit breaker | A resilience control that temporarily stops calls to a failing dependency so the application can recover instead of amplifying failure. |
| Claim | A statement carried in an authenticated identity/token, such as subject or session family. Claims are trusted only after token validation and applicable authoritative-state checks. |
| ClamAV | Open-source malware-scanning engine used by a configured upload-scanning adapter. A timeout or unavailable scanner is not a clean result; protected uploads remain quarantined. |
| Cloud edge | Public TLS, WAF, request filtering, and proxy boundary in front of the application. It supplements but never replaces application authorization. |
| Compatibility alias | An older route retained temporarily while clients migrate. KiloDrive's unversioned API aliases have a documented sunset; that date alone does not prove live removal. |
| Compensating entry | A linked financial entry correcting or reversing the effect of an earlier posting while retaining the original accounting evidence. It avoids editing immutable history. |
| Compliance evidence | Version-bound proof that a required control operated for a particular country, release, provider, and time window. A configuration field without a test or review record is not compliance evidence. |
| Compliance register | Controlled country-by-country record of applicable obligations, legal sources, control owners, evidence, review dates, exceptions, and launch decisions. The public architecture describes its shape but does not publish privileged legal advice. |
| Consumer-scoped session | A session restricted to consumer roles and country membership, even if the same global identity also holds a System Admin role. Refresh or a client header must not elevate it. |
| Contract parity | Agreement between reviewed source contracts and derived client/public artifacts. Wire-shape parity verifies fields and constraints, not every business rule, deployed endpoint or semantic explanation. |
| Control plane | Global identity, country routing, support/privacy orchestration, and other cross-cell coordination data. |
| Correlation ID | A validated or generated request identifier propagated through responses, traces, logs, outbox work, and safe audit evidence. |
| CORS | Cross-Origin Resource Sharing: browser rules controlling which origins may read permitted cross-origin responses. CORS is not API authorization and does not stop a non-browser HTTP client. |
| Country activation gate | Fail-closed decision that permits signup or operations only after the country shard, schema contract, rules, providers, legal approvals, runbooks, and accountable owners are ready. |
| Country cell | A country-scoped MySQL database containing operational, tenant, and financial domain data. |
| CQRS | Command Query Responsibility Segregation: separating state-changing commands from read-only queries so validation, transaction, audit, and caching expectations are explicit. It does not require separate services or databases. |
| Credential-free projection | A country user row containing operational identity/profile context but no password, refresh-token, 2FA or passkey authority. See [identity and access](docs/security/identity-and-access.md). |
| CSP | Content Security Policy, a browser response header that limits which script, style, frame, image, and connection sources a page may use. |
| CSRF | Cross-Site Request Forgery: tricking an authenticated browser into submitting an unwanted request. The Portal uses anti-forgery protection because cookies can be sent automatically by the browser. |
| Curated public contract | The reviewed subset of the complete private API permitted for public documentation. Excluded admin, operational and provider-callback contracts still require full private inventory and enforcement. |
| Cursor pagination | Returning a bounded page and continuation position instead of assuming all results fit in one response. Ordering, filtering and authorization must remain consistent across pages. |

## D to I

| Term | Meaning |
| --- | --- |
| Data controller | Organization that determines why and how personal data is processed under the applicable privacy framework. The legal role depends on the processing relationship and must be determined by counsel, not inferred from a database name. |
| Data plane | Country-local operational state used to run rides, deliveries, rentals, wallets, and related workflows. It is distinct from the global identity control plane. |
| Data processor | Organization that handles personal data on a controller's instructions. Provider contracts, subprocessor review, security obligations, and cross-border transfer rules remain part of the compliance boundary. |
| Data Protection | ASP.NET Core facility for purpose-scoped encryption and integrity protection of application secrets such as protected fields. Its key ring must be persistent, protected, and shared correctly across API nodes. |
| Dead-letter queue | A queue that isolates messages that could not be processed after the allowed attempts, preserving them for investigation and controlled redrive. |
| Device admission | Server decision about whether an installation may use the applicable client path. It is separate from user authentication and resource authorization; see [the control model](docs/security/security-control-model.md). |
| Device ban | Server-controlled restriction on an installation or associated policy scope. It must not be described as permanent physical-hardware identification simply because a record has a device ID. |
| Distributed transaction | One atomic transaction spanning independent systems or databases. KiloDrive avoids it across control/country boundaries and uses durable orchestration instead. |
| Document quarantine | Private disposition while a file lacks trusted clean scan evidence or has been rejected by scanning. An outage is not a clean result; clean scanning is not document authenticity or driver approval. |
| Dossier | The authorized Admin view joining a person's details, security, vehicles, financials, readiness, rides, activity and actions. Every tab and export remains scoped to current permission and workspace. |
| Driver readiness | The API's computed eligibility from applicable profile, contact, identity, vehicle and other requirements. Uploading one file or purchasing a plan alone does not prove trip eligibility. |
| DTO | Data Transfer Object: the intentionally shaped request or response sent across an API or application boundary. A DTO is not automatically the database entity behind it. |
| Dual approval | A policy requiring a distinct authorized reviewer for a covered proposal. KiloDrive supports domain-specific independent-approval flags with disabled source defaults; effective deployment policy must be checked. |
| Durable state | Business state that must survive process, cache, and connection loss and can explain the outcome later. |
| EF Core | Entity Framework Core, the .NET object-relational mapper used to model and query KiloDrive's MySQL data. Its model metadata participates in schema-contract verification. |
| Egress | Outbound network traffic from a system. In a media-specific chapter, LiveKit Egress names the service that exports or records an authorized room. Network destination controls and recording consent are different concerns. |
| Entitlement | Server-recognized right to a membership benefit for the relevant account, product and period. A local purchase callback, displayed plan card or catalog edit does not by itself grant it. |
| Entity version | Persisted monotonic number changed with an entity and used to reject stale commands/events deterministically. |
| Ephemeral state | Replaceable short-lived data such as presence, websocket connections, and fresh location indexes. |
| Escrow hold | Funds reserved for an accepted marketplace obligation; held funds are not spendable until settlement or release. |
| EventBridge | AWS event-bus service used as a configurable dispatch-acceleration path. Event publication does not replace the SQL outbox's durable recovery evidence. |
| Evidence scope | The commit/artifact, environment, country, provider mode, policy and scenario to which an observation applies. A historical passing test must not be relabeled as proof of a newer release. |
| Fail closed | Refusing the protected operation when required authorization or safety evidence is absent or unavailable. The response should distinguish a temporary dependency failure from a proven denial. |
| FCM | Firebase Cloud Messaging, used for permitted Android and cross-platform push delivery. |
| Field dictionary | Human-readable explanations of API model properties, types, constraints and meaning. KiloDrive labels model-specific, shared, inferred and type-only descriptions in its [coverage report](docs/api/reference/coverage.md). |
| Financial hold | A restriction on spendable funds or on progression of a risky action. A wallet escrow amount and a review-required action are different forms of hold and should be labelled explicitly. |
| FIPS profile | Explicit deployment profile that keeps required cryptographic work inside an approved FIPS boundary. For KiloDrive password hashing it selects PBKDF2-HMAC-SHA256 with the reviewed work factor instead of Argon2id; it is not a generic claim that the entire application is certified. |
| FX quote | A server-owned foreign-exchange/pricing result with currency, rate, validity and transaction context. A stored quote/snapshot prevents later display or rate changes from silently rewriting a committed amount. |
| Geofence corridor | A bounded area around an expected route used as one signal for route-deviation analysis; it is not proof without map matching and uncertainty handling. |
| Global identity | The central user and credential authority shared across authorized country memberships. It is distinct from the operational projections used by each country cell. |
| H3 | A hierarchical hexagonal geospatial indexing system useful for bucketing and neighborhood queries. Use is documented as implemented or planned per feature. |
| Haversine distance | Straight-line great-circle distance between coordinates. Useful as a bounded approximation, not a substitute for road distance or traversal evidence. |
| Headroom | Deliberately unused capacity reserved for bursts, failover, queue draining, and recovery rather than ordinary steady-state load. |
| HMAC | Hash-based Message Authentication Code: a secret-key mechanism for verifying message integrity/authenticity or deriving a keyed lookup fingerprint. It is not encryption and does not hide the message it authenticates. |
| IAM | Identity and Access Management: cloud policies, roles, and credentials that grant the smallest required actions and resources. |
| IANA timezone | Named timezone such as `America/Jamaica`, used for local calendar/business rules rather than fixed numeric offsets. |
| IAP | In-App Purchase: a digital product or subscription purchased through an app store. The store receipt/token must be verified server-side before entitlement is granted. |
| Idempotency key | Identifier for one logical command, bound to actor, tenant, route, payload and required revision. Preserve the original key and intent during uncertain recovery; the key is not authentication or proof that execution succeeded. |
| Idempotency lease | Temporary execution claim preventing concurrent work under one operation key. Lease expiry alone does not prove that a prior domain/provider mutation failed or authorize blind re-execution. |
| Immutable journal | Accounting entry that cannot be edited or deleted after posting; corrections use linked reversing entries. |
| Independent approval | The distinct-reviewer rule when enabled for a supported administrative area. It supplements permission, revision and audit checks; see also dual approval. |
| Installation credential | A secret plus server registration context representing one app installation. Model, IP and claimed device identifiers cannot substitute for it, and reinstalling may create another installation. |
| Installation generation | The current server/client binding generation used when tokens or installation state rotate. Stale callbacks must not revive a prior account or push destination. |
| IPA | iOS App Store package containing the signed application and embedded frameworks. Release review inspects the actual IPA, not only Dart or Swift source. |

## J to R

| Term | Meaning |
| --- | --- |
| Jurisdiction | Country, state, province, territory, municipality, or other legal authority whose rules may apply to an operation. A country code is a routing key, not a complete legal conclusion. |
| JWKS | JSON Web Key Set publishing public verification keys for asymmetrically signed tokens. |
| JWT | JSON Web Token: compact signed claims used for KiloDrive access tokens and some provider integrations. A JWT is readable by its holder unless its contents are separately encrypted. |
| Key ID (kid) | A token-header identifier selecting the intended verification key from a reviewed key set. It is not a private signing key and must not override algorithm or issuer policy. |
| KMS | Cloud key-management service used to protect encryption keys and enforce audited key-use policy. |
| KYC | Know Your Customer controls: identity and eligibility checks appropriate to a financial or marketplace action. Required evidence and limits are country- and risk-specific. |
| Lawful basis | Documented legal ground for processing personal data. Consent is only one possible basis and must not be used as a generic substitute when another basis or prohibition applies. |
| Least privilege | Granting only the permissions, country scope, resources and time necessary for an actor or service to perform its authorized task. |
| Legal hold | Authorized suspension of ordinary deletion or retention expiry for defined evidence. Holds are scoped, audited, reviewed, and released deliberately; they do not justify indefinite collection of unrelated data. |
| Map matching | Matching noisy GPS observations to plausible road-network segments, often through OSRM `/match` or an equivalent engine. |
| MediatR | In-process .NET request dispatcher used to route commands and queries to handlers. It organizes application flow; it is not an external message broker. |
| Membership Center | The Admin workspace for plan catalogs, benefit/term-price editing, active-member drill-down and permitted membership actions. New paid-plan drafts still need store and country setup. |
| Minor unit | Integer representation of money at the applicable currency exponent; for a two-decimal currency, `12345` represents `123.45`. Carry the currency explicitly and never assume every currency has two decimal places. |
| Monotonic version | Version that only increases for one entity, independent of wall-clock movement or clock skew between nodes. |
| Mutation | A state-changing operation. Retryable commands need their prescribed authorization, validation, operation identity and version/lifecycle checks before durable effects. |
| Native viewing lease | An optional bounded Admin viewing session governed by API policy. Disabling that lease must not remove document authorization, required access proof or private-content handling. |
| No-mutation evidence | An authoritative witness that the original command performed no relevant domain/provider mutation. It is stronger than a timeout, absent UI update or missing recovery record. |
| Nonce | A value used once within a defined protocol scope to prevent replay. Its uniqueness matters only with expiry, binding and an authoritative atomic claim or consumption mechanism. |
| Nullable field | A contract property whose value may be JSON null. Nullability is different from whether the property may be omitted; clients must respect both aspects of the schema. |
| Numeric enum | An API enumeration serialized as a number. Clients map it through the correct exhaustive domain registry; unknown values use a neutral state and disable unsafe actions. |
| OAuth 2.0 | Authorization framework commonly used to obtain delegated provider tokens. Receiving a provider token does not by itself prove that it belongs to the intended KiloDrive account. |
| Observation mode | A policy mode that records would-reject decisions without enforcing them. Metrics from observation cannot be described as active traffic blocking. |
| OIDC | OpenID Connect: identity layer built on OAuth 2.0 that adds signed identity claims. The server still validates issuer, audience, signature, expiry, nonce where applicable, and verified-email policy. |
| OpenAPI | Machine-readable description of the HTTP contract, including paths, parameters, security, schemas, and responses. KiloDrive reviews and hashes the v1 artifact to detect drift. |
| OpenTelemetry | Vendor-neutral APIs and formats for traces, metrics, and related telemetry. |
| Operation envelope | Durable identity and intent for a command, including the scoped key and original request/preconditions needed for safe recovery. It is not simply the latest visible entity state. |
| Optimistic concurrency | Rejecting a mutation whose expected entity version no longer matches current state, so stale edits cannot silently overwrite newer decisions. |
| ORM | Object-Relational Mapper: software that maps application objects and queries to relational tables and SQL. An ORM reduces routine mapping work but does not remove the need to understand indexes, locks, transactions, and generated SQL. |
| OSRM | Open Source Routing Machine: road-network routing service used for operations such as route/table calculation and map matching. Its result quality depends on the regional data build and request evidence. |
| OTLP | OpenTelemetry Protocol: the wire format used to export telemetry to a collector over transports such as gRPC or HTTP. OTLP must not carry tokens, payloads, or precise user data. |
| OTP | One-Time Password or verification code used in a specific expiring challenge. Its purpose, contact/account binding, attempt limit and single-use consumption are separate from password-login lockout. |
| Outbox | Durable database records committed with business state and later claimed by workers to perform side effects. |
| Outcome unknown | A command may have changed domain or provider state but its result is unconfirmed. Retain the original key, payload and revision, then reconcile before any further mutation. |
| OWASP API Security Top 10 | The 2023 API risk taxonomy used by this repository's [KiloDrive mapping](docs/security/owasp-api-top-10-2023.md). Mapping controls to categories is not OWASP endorsement or certification. |
| p50 / p95 / p99 | Latency percentiles: the values at or below which 50%, 95%, or 99% of observations complete. Tail percentiles reveal slow experiences hidden by an average. |
| Passkey | WebAuthn/FIDO credential using public-key authentication and an authenticator such as device biometrics or hardware key. |
| PBKDF2 | Password-Based Key Derivation Function 2: a salted, deliberately expensive derivation function used by KiloDrive only under the explicit FIPS password profile or to verify supported legacy hashes. It must not be confused with a fast hash used only for a lookup protocol. |
| Permission grant | Authoritative assignment of capabilities to an account. Possessing the Admin app or selecting a country in its UI does not create a grant. |
| PII | Personally identifiable information, including combinations of data that can identify or locate a person. |
| Plan draft | An inactive membership-catalog entry awaiting required benefit, pricing, product and country setup. Creating it is not equivalent to publishing an Apple or Google product. |
| Presigned URL | Time-bounded, scoped URL granting a specific object operation without making the object public. Treat it as a temporary bearer credential. |
| ProblemDetails | Structured HTTP error representation with stable public fields; production responses must not expose stack traces or sensitive payloads. |
| Process-local limit | A rate/work counter maintained by one running process. Multiple API nodes require an assessed aggregate control; a shared cache used for other purposes does not change this property. |
| Projection | A derived representation for a particular read or operational purpose. KiloDrive's country user projection is credential-free and supports local relationships; the global identity remains the credential authority. |
| Provider acceptance | The provider accepted a request for processing. This does not establish eventual recipient delivery, final payment settlement or agreement with the server's business state. |
| Provider reconciliation | Comparing authoritative provider evidence with the server-owned operation, account, amount, currency and lifecycle to establish a durable outcome. It is a read/decision process before any justified retry, not permission to repeat a charge. |
| Push-token binding | Association of a push token with the verified app channel, account, country, installation and session. Rotation, logout, revocation and explicit opt-out must preserve ownership boundaries. |
| Query filter | EF Core rule automatically applying tenant or archival scope. Administrative bypass requires explicit proof and review. |
| Rate-limit partition | The identity of a request-budget bucket, such as trusted client IP, authenticated user or policy. The reviewed ASP.NET counters are process-local; Redis use elsewhere does not make their budget cluster-wide. |
| Realtime hint | Fast notification that state may have changed. The authorized API/database remains the source of truth after reconnect or gaps. |
| Recent authentication | Fresh server-recognized proof of the user's identity, from the applicable authentication time or supported reauthentication ceremony. It is not identical to action-bound 2FA step-up. |
| Refresh-token family | The persisted chain of session tokens produced by rotation. Family liveness and reuse detection support revocation; legacy tokens without the additive family claim have an explicitly different compatibility scope. |
| Replay | Repeating a prior message or command. A protected mutation may return its stored response without executing again; malicious replay of an expired or consumed authentication proof must fail. |
| Residual risk | Risk remaining after implemented controls and operating measures. Record its owner, scope, review date and closure evidence rather than hiding it behind a generic secure label. |
| Reverse geocoding | Converting coordinates into a human-readable address. It can fail or be slow, so coordinates remain the immediate fallback. |
| RPO/RTO | Recovery point and recovery time objectives. Exact production targets are restricted operational data. |
| RS256 / ES256 | JWT signature algorithms using RSA or elliptic-curve private keys respectively and SHA-256. Verifiers use public keys; algorithm selection must be pinned rather than trusted from an unvalidated token header. |

## S to Z

| Term | Meaning |
| --- | --- |
| S3 | Amazon Simple Storage Service, used for private object storage such as approved documents and consented recordings. Bucket privacy, authorization, encryption, retention, and malware disposition are separate controls. |
| Safety case | Versioned, auditable response record with severity, owner, SLA, escalation channel, evidence, acknowledgement, transitions, and closure reason. It coordinates human response; it is not merely a notification. |
| Saga | Durable multi-step orchestration across independent transaction boundaries, with idempotent steps and compensating behavior. |
| Saturation | The degree to which a constrained resource—such as CPU, connections, locks, memory, IO, bandwidth, or provider quota—has no safe capacity left for more work. |
| SBOM | Software Bill of Materials: an inventory of components and available version, origin, relationship and license evidence. KiloDrive's public direct/override baseline is narrower than the complete signed-release dependency graph. |
| Schema contract | Versioned expectation for relational metadata that the application verifies before serving incompatible work. |
| SDK | Software Development Kit: libraries and tools supplied for a platform or provider. Adding an SDK can change native permissions, privacy declarations, transitive packages, and license obligations. |
| Semantic coverage | How much of a contract has a reviewed explanation of purpose, units, lifecycle and field meaning. A complete type listing or successful regeneration does not establish complete semantic coverage. |
| SES | Amazon Simple Email Service, a configurable provider for transactional email. Successful API acceptance is tracked separately from delivery, bounce, complaint, or open evidence. |
| Session family | See refresh-token family. A family is bound to a user and tenant and may bind an installation; it is not the physical device identifier or a reusable authentication secret. |
| SHA-256 sidecar | A companion file recording the expected SHA-256 of an artifact. Matching it detects inconsistency with that recorded baseline but does not prove the artifact is safe or independently reviewed. |
| Side effect | Work outside the core state transition, such as publish, email, webhook, object processing, or provider call. |
| SignalR | ASP.NET Core realtime framework used to deliver authorized live updates to connected clients. |
| Signed-artifact evidence | Observations tied to the exact signed APK/AAB/IPA, platform, device, provider mode and scenario. Source analysis cannot replace native distribution and runtime behavior checks. |
| Single-flight refresh | Coordinating concurrent expired-session requests behind one refresh attempt so parallel callers do not independently rotate the same refresh credential. |
| SLO | Service Level Objective: an internal, measurable reliability or performance target for a customer-relevant service over a defined window. |
| SNS | Amazon Simple Notification Service, commonly used to fan alarms or events to approved operator destinations. A topic without a confirmed human subscription cannot page anyone. |
| Spatial index | Database index optimized for geometric data and predicates such as proximity/intersection. |
| SQS | Amazon Simple Queue Service, used for buffered at-least-once work delivery and dead-letter isolation. Consumers must tolerate redelivery. |
| SRID | Spatial Reference System Identifier. KiloDrive's geographic points use SRID 4326 so the database interprets longitude and latitude in the intended Earth coordinate system. |
| SSRF | Server-Side Request Forgery: supplied destinations cause the server to contact an unintended resource. URL validation, connection-time address checks and egress policy address different parts of this risk. |
| Step-up proof | Additional server-validated authentication evidence required by a particular protected action. KiloDrive's enrolled 2FA proof is action-, user- and tenant-bound and single-use. Requirements are endpoint-specific; local biometrics and a generic recent-auth proof are not interchangeable. |
| StoreKit | Apple's framework for App Store purchases and subscriptions. StoreKit client state is reconciled with server-verified signed transaction evidence before membership authority changes. |
| Subledger | Detailed operational history for a specific balance or domain, such as `WalletTransactions`. It complements the general journal. |
| System Admin app | The separate restricted Android/iOS operator client for privileged KiloDrive tasks. The API remains authoritative for permissions, readiness, financial mutations and audit. |
| Tenant | Logical marketplace/organization authorization boundary inside an approved country cell. |
| TLS | Transport Layer Security, which protects network traffic in transit and authenticates the server endpoint. TLS does not replace application authorization or encrypt data after it reaches an endpoint. |
| Token version | Authoritative identity/session revision used when deciding whether previously issued claims remain valid. It is distinct from API version, mobile build number and entity revision. |
| TOTP | Time-based one-time password generated from a shared secret, commonly used for authenticator-app 2FA. |
| Trusted contact | User-selected person eligible to receive a time-bounded live-trip share under the active trip and privacy policy. A trusted contact is not automatically an emergency responder or account administrator. |
| Trusted proxy | An explicitly configured intermediary permitted to supply original client-address or routing context. Arbitrary forwarded headers from a requester must not gain that authority. |
| TTL | Time to live: the bounded period after which cached, ephemeral, or privacy-sensitive state expires. A TTL is not a substitute for explicit revocation when immediate removal is required. |
| TURN | Relay protocol/server used when direct WebRTC media paths cannot traverse NAT or firewalls. |
| UUIDv7 | RFC 9562 time-ordered universally unique identifier used for new transactional and externally exposed entities. It identifies a record; possession of its value does not grant access. |
| Valkey | Redis-protocol distributed data service used for cache, realtime scale-out, fresh geospatial state, and short-lived coordination. |
| Viewing proof | Server-validated evidence required by a protected document-viewing contract. It must not be conflated with the optional native viewing lease or treated as permanent authorization. |
| WAF | Web Application Firewall: an edge control that filters known hostile patterns, probes, and abusive request rates. It reduces noise but cannot enforce entity ownership or business state. |
| Webhook | An HTTP event delivery across systems. Inbound provider callbacks require provider-specific authenticity and business binding; outbound KiloDrive deliveries require authorized subscriptions, safe destinations, signing and idempotent handling. |
| WebRTC | Real-time media technology used underneath LiveKit client connections. Signalling, media, TURN relay, platform permissions, and recording are distinct paths that must be tested separately. |
| Wire shape | The serialized API contract: property names, types, nullability, requiredness, constraints, parameters and response structure. It does not fully describe business semantics. |
| Worker heartbeat | Periodic evidence that a background processor is alive; it must be interpreted alongside backlog age and failures. |
| Zero trust assumption | A review assumption that clients, headers, network location and prior authorization cannot be blindly trusted for the next action. Use of this principle is not a claim of a certified zero-trust architecture. |

## Reading paths

- [API guide](docs/api/README.md), [field dictionary](docs/api/schemas/README.md)
  and [coverage queue](docs/api/reference/coverage.md) explain wire contracts
  and the limits of generated descriptions.
- [Security controls](docs/security/security-control-model.md) and
  [OWASP mapping](docs/security/owasp-api-top-10-2023.md) connect terms to
  source evidence, configuration and negative test expectations.
- [System Admin app](docs/architecture/system-admin-mobile-app.md),
  [session/device lifecycle](docs/architecture/mobile-session-and-device-lifecycle.md)
  and [notification delivery](docs/architecture/notification-delivery-lifecycle.md)
  explain cross-screen and cross-app responsibilities.
- [Financial systems](docs/architecture/financial-systems.md),
  [authoritative FX](docs/architecture/authoritative-foreign-exchange.md) and
  [safe recovery](docs/api/errors-and-recovery.md) explain monetary invariants.
- [Testing and verification](docs/quality/testing-and-verification.md) and
  [SBOM scope](docs/third-party/sbom.md) explain evidence and release boundaries.

If a chapter uses a term differently, it should define that meaning explicitly
and link here. Prefer the exact domain contract over a generic glossary meaning
when interpreting a request field or lifecycle state. Report ordinary corrections
through [CONTRIBUTING.md](CONTRIBUTING.md) and sensitive concerns through
[SECURITY.md](SECURITY.md).
