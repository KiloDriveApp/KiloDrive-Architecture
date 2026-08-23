# Glossary

This glossary uses KiloDrive's meaning of each term. Some words have broader
meanings in other systems.

| Term | Meaning |
| --- | --- |
| AAB | Android App Bundle: the publishing artifact uploaded to Google Play. Google Play uses it to generate optimized APKs for supported devices. |
| ABI | Application Binary Interface: the native machine-code contract for a processor family, such as `arm64-v8a` or `armeabi-v7a`. A package can build successfully yet fail on a device if the required ABI is absent. |
| ADR | Architecture Decision Record: a short, durable explanation of an important design choice, the alternatives considered, and the consequences the team accepts. |
| ADOT | AWS Distro for OpenTelemetry: AWS-supported components for collecting and exporting OpenTelemetry traces and metrics. It is an observability path, not the source of business truth. |
| Aggregate | A cluster of domain state protected by one consistency boundary and version, such as a ride request and its actionable assignment state. |
| AML | Anti-Money Laundering controls: rules and review processes intended to detect or restrict suspicious movement of funds. A feature flag is not a substitute for an approved country operating model. |
| API | Application Programming Interface. In KiloDrive, the authenticated ASP.NET Core API is the server-side security and business-rule boundary shared by mobile, Portal, Website, and provider callbacks. |
| APK | Android Package: an installable Android application artifact. KiloDrive inspects release APKs as well as AABs because native libraries and merged permissions can differ from source declarations. |
| APNs | Apple Push Notification service, used to deliver permitted notifications to Apple devices. |
| App attestation | Platform-signed evidence intended to make unauthorized or automated clients harder to use. It supplements authentication and authorization; it never grants access by itself. |
| AsyncNotifier | Riverpod state owner for asynchronous Flutter features. It coordinates user intent, loading/refresh/mutation states, cancellation, and disposal without putting transport logic in widgets. |
| At-least-once delivery | A message-delivery model in which retries can deliver the same message more than once; consumers therefore need idempotency. |
| Audit event | An append-oriented, sanitized record of a security, administrative, or important user action. It is evidence, not a debug-payload dump. |
| Backplane | Shared transport used by multiple API nodes to distribute realtime messages and coordinate SignalR clients. KiloDrive uses Valkey where configured. |
| Breadcrumb | A sampled, durable location observation retained for authorized trip reconstruction, safety, and distance evidence. |
| B-tree locality | The storage/index benefit gained when newly generated keys are roughly time ordered instead of randomly scattered across index pages. |
| Canary | A scheduled non-user probe sent to a dedicated test destination to verify a provider path without involving customer data. |
| Capacity envelope | The tested combination of workload, throughput, latency, errors, saturation, and recovery headroom within which customer objectives remain satisfied. It is not a permanent “maximum users” claim. |
| CDR | Content Disarm and Reconstruction: sanitizing a document by rebuilding safe content rather than trusting the original binary. |
| Cell fingerprint | Deterministic hash of normalized country-cell table, column, index, and foreign-key metadata. |
| Circuit breaker | A resilience control that temporarily stops calls to a failing dependency so the application can recover instead of amplifying failure. |
| ClamAV | Open-source malware-scanning engine used by a configured upload-scanning adapter. A timeout or unavailable scanner is not a clean result; protected uploads remain quarantined. |
| Cloud edge | Public TLS, WAF, request filtering, and proxy boundary in front of the application. It supplements but never replaces application authorization. |
| Compliance evidence | Version-bound proof that a required control operated for a particular country, release, provider, and time window. A configuration field without a test or review record is not compliance evidence. |
| Compliance register | Controlled country-by-country record of applicable obligations, legal sources, control owners, evidence, review dates, exceptions, and launch decisions. The public architecture describes its shape but does not publish privileged legal advice. |
| Control plane | Global identity, country routing, support/privacy orchestration, and other cross-cell coordination data. |
| Correlation ID | A validated or generated request identifier propagated through responses, traces, logs, outbox work, and safe audit evidence. |
| CQRS | Command Query Responsibility Segregation: separating state-changing commands from read-only queries so validation, transaction, audit, and caching expectations are explicit. It does not require separate services or databases. |
| CSRF | Cross-Site Request Forgery: tricking an authenticated browser into submitting an unwanted request. The Portal uses anti-forgery protection because cookies can be sent automatically by the browser. |
| CSP | Content Security Policy, a browser response header that limits which script, style, frame, image, and connection sources a page may use. |
| Country cell | A country-scoped MySQL database containing operational, tenant, and financial domain data. |
| Country activation gate | Fail-closed decision that permits signup or operations only after the country shard, schema contract, rules, providers, legal approvals, runbooks, and accountable owners are ready. |
| Data plane | Country-local operational state used to run rides, deliveries, rentals, wallets, and related workflows. It is distinct from the global identity control plane. |
| Data controller | Organization that determines why and how personal data is processed under the applicable privacy framework. The legal role depends on the processing relationship and must be determined by counsel, not inferred from a database name. |
| Data processor | Organization that handles personal data on a controller's instructions. Provider contracts, subprocessor review, security obligations, and cross-border transfer rules remain part of the compliance boundary. |
| Data Protection | ASP.NET Core facility for purpose-scoped encryption and integrity protection of application secrets such as protected fields. Its key ring must be persistent, protected, and shared correctly across API nodes. |
| Dead-letter queue | A queue that isolates messages that could not be processed after the allowed attempts, preserving them for investigation and controlled redrive. |
| Distributed transaction | One atomic transaction spanning independent systems or databases. KiloDrive avoids it across control/country boundaries and uses durable orchestration instead. |
| Durable state | Business state that must survive process, cache, and connection loss and can explain the outcome later. |
| DTO | Data Transfer Object: the intentionally shaped request or response sent across an API or application boundary. A DTO is not automatically the database entity behind it. |
| EF Core | Entity Framework Core, the .NET object-relational mapper used to model and query KiloDrive's MySQL data. Its model metadata participates in schema-contract verification. |
| Egress | LiveKit service that exports or records an authorized media room under consent, retention, and storage policy. |
| Entity version | Persisted monotonic number changed with an entity and used to reject stale commands/events deterministically. |
| Ephemeral state | Replaceable short-lived data such as presence, websocket connections, and fresh location indexes. |
| Escrow hold | Funds reserved for an accepted marketplace obligation; held funds are not spendable until settlement or release. |
| EventBridge | AWS event-bus service used as a configurable dispatch-acceleration path. Event publication does not replace the SQL outbox's durable recovery evidence. |
| FCM | Firebase Cloud Messaging, used for permitted Android and cross-platform push delivery. |
| Geofence corridor | A bounded area around an expected route used as one signal for route-deviation analysis; it is not proof without map matching and uncertainty handling. |
| H3 | A hierarchical hexagonal geospatial indexing system useful for bucketing and neighborhood queries. Use is documented as implemented or planned per feature. |
| Haversine distance | Straight-line great-circle distance between coordinates. Useful as a bounded approximation, not a substitute for road distance or traversal evidence. |
| HMAC | Keyed cryptographic message authentication code used to create a non-reversible, secret-dependent fingerprint for values such as voucher codes. |
| Headroom | Deliberately unused capacity reserved for bursts, failover, queue draining, and recovery rather than ordinary steady-state load. |
| IAP | In-App Purchase: a digital product or subscription purchased through an app store. The store receipt/token must be verified server-side before entitlement is granted. |
| IAM | Identity and Access Management: cloud policies, roles, and credentials that grant the smallest required actions and resources. |
| IANA timezone | Named timezone such as `America/Jamaica`, used for local calendar/business rules rather than fixed numeric offsets. |
| Idempotency key | Caller-supplied identifier bound to a mutation and payload so uncertain retries do not produce a second business effect. |
| Idempotency lease | Temporary claim that prevents concurrent requests with the same idempotency key from executing together. |
| Immutable journal | Accounting entry that cannot be edited or deleted after posting; corrections use linked reversing entries. |
| IPA | iOS App Store package containing the signed application and embedded frameworks. Release review inspects the actual IPA, not only Dart or Swift source. |
| JWT | JSON Web Token: compact signed claims used for KiloDrive access tokens and some provider integrations. A JWT is readable by its holder unless its contents are separately encrypted. |
| JWKS | JSON Web Key Set publishing public verification keys for asymmetrically signed tokens. |
| Jurisdiction | Country, state, province, territory, municipality, or other legal authority whose rules may apply to an operation. A country code is a routing key, not a complete legal conclusion. |
| KMS | Cloud key-management service used to protect encryption keys and enforce audited key-use policy. |
| KYC | Know Your Customer controls: identity and eligibility checks appropriate to a financial or marketplace action. Required evidence and limits are country- and risk-specific. |
| Lawful basis | Documented legal ground for processing personal data. Consent is only one possible basis and must not be used as a generic substitute when another basis or prohibition applies. |
| Legal hold | Authorized suspension of ordinary deletion or retention expiry for defined evidence. Holds are scoped, audited, reviewed, and released deliberately; they do not justify indefinite collection of unrelated data. |
| Map matching | Matching noisy GPS observations to plausible road-network segments, often through OSRM `/match` or an equivalent engine. |
| MediatR | In-process .NET request dispatcher used to route commands and queries to handlers. It organizes application flow; it is not an external message broker. |
| Minor unit | Integer representation of money at the ISO currency exponent; for a two-decimal currency, `12345` represents `123.45`. |
| Monotonic version | Version that only increases for one entity, independent of wall-clock movement or clock skew between nodes. |
| OAuth 2.0 | Authorization framework commonly used to obtain delegated provider tokens. Receiving a provider token does not by itself prove that it belongs to the intended KiloDrive account. |
| OIDC | OpenID Connect: identity layer built on OAuth 2.0 that adds signed identity claims. The server still validates issuer, audience, signature, expiry, nonce where applicable, and verified-email policy. |
| OpenAPI | Machine-readable description of the HTTP contract, including paths, parameters, security, schemas, and responses. KiloDrive reviews and hashes the v1 artifact to detect drift. |
| OpenTelemetry | Vendor-neutral APIs and formats for traces, metrics, and related telemetry. |
| ORM | Object-Relational Mapper: software that maps application objects and queries to relational tables and SQL. An ORM reduces routine mapping work but does not remove the need to understand indexes, locks, transactions, and generated SQL. |
| OSRM | Open Source Routing Machine: road-network routing service used for operations such as route/table calculation and map matching. Its result quality depends on the regional data build and request evidence. |
| OTLP | OpenTelemetry Protocol: the wire format used to export telemetry to a collector over transports such as gRPC or HTTP. OTLP must not carry tokens, payloads, or precise user data. |
| Outbox | Durable database records committed with business state and later claimed by workers to perform side effects. |
| p50 / p95 / p99 | Latency percentiles: the values at or below which 50%, 95%, or 99% of observations complete. Tail percentiles reveal slow experiences hidden by an average. |
| Passkey | WebAuthn/FIDO credential using public-key authentication and an authenticator such as device biometrics or hardware key. |
| PBKDF2 | Password-Based Key Derivation Function 2: a salted, deliberately expensive derivation function used with a reviewed work factor. It must not be confused with a fast hash used only for a lookup protocol. |
| PII | Personally identifiable information, including combinations of data that can identify or locate a person. |
| ProblemDetails | Structured HTTP error representation with stable public fields; production responses must not expose stack traces or sensitive payloads. |
| Projection | Credential-free country-local representation of a global user, retained for local domain relationships. |
| Provider reconciliation | Querying signed webhook or provider state to settle a request whose outcome became unknown after a timeout or crash. |
| Presigned URL | Time-bounded, scoped URL granting a specific object operation without making the object public. Treat it as a temporary bearer credential. |
| Query filter | EF Core rule automatically applying tenant or archival scope. Administrative bypass requires explicit proof and review. |
| Rate-limit partition | Key—such as trusted client IP, authenticated user, tenant, or policy—whose request budget is tracked independently. |
| Realtime hint | Fast notification that state may have changed. The authorized API/database remains the source of truth after reconnect or gaps. |
| Reverse geocoding | Converting coordinates into a human-readable address. It can fail or be slow, so coordinates remain the immediate fallback. |
| RPO/RTO | Recovery point and recovery time objectives. Exact production targets are restricted operational data. |
| RS256 / ES256 | JWT signature algorithms using RSA or elliptic-curve private keys respectively and SHA-256. Verifiers use public keys; algorithm selection must be pinned rather than trusted from an unvalidated token header. |
| S3 | Amazon Simple Storage Service, used for private object storage such as approved documents and consented recordings. Bucket privacy, authorization, encryption, retention, and malware disposition are separate controls. |
| Saga | Durable multi-step orchestration across independent transaction boundaries, with idempotent steps and compensating behavior. |
| Safety case | Versioned, auditable response record with severity, owner, SLA, escalation channel, evidence, acknowledgement, transitions, and closure reason. It coordinates human response; it is not merely a notification. |
| Saturation | The degree to which a constrained resource—such as CPU, connections, locks, memory, IO, bandwidth, or provider quota—has no safe capacity left for more work. |
| SBOM | Software Bill of Materials: machine-readable inventory of components, versions, relationships, and available licence/provenance data. |
| Schema contract | Versioned expectation for relational metadata that the application verifies before serving incompatible work. |
| SDK | Software Development Kit: libraries and tools supplied for a platform or provider. Adding an SDK can change native permissions, privacy declarations, transitive packages, and license obligations. |
| SES | Amazon Simple Email Service, a configurable provider for transactional email. Successful API acceptance is tracked separately from delivery, bounce, complaint, or open evidence. |
| Side effect | Work outside the core state transition, such as publish, email, webhook, object processing, or provider call. |
| SignalR | ASP.NET Core realtime framework used to deliver authorized live updates to connected clients. |
| SLO | Service Level Objective: an internal, measurable reliability or performance target for a customer-relevant service over a defined window. |
| SNS | Amazon Simple Notification Service, commonly used to fan alarms or events to approved operator destinations. A topic without a confirmed human subscription cannot page anyone. |
| SQS | Amazon Simple Queue Service, used for buffered at-least-once work delivery and dead-letter isolation. Consumers must tolerate redelivery. |
| Spatial index | Database index optimized for geometric data and predicates such as proximity/intersection. |
| SRID | Spatial Reference System Identifier. KiloDrive's geographic points use SRID 4326 so the database interprets longitude and latitude in the intended Earth coordinate system. |
| Step-up proof | Recent stronger authentication required before a sensitive boundary change such as payout, password, contact, passkey, or 2FA mutation. |
| StoreKit | Apple's framework for App Store purchases and subscriptions. StoreKit client state is reconciled with server-verified signed transaction evidence before membership authority changes. |
| Subledger | Detailed operational history for a specific balance or domain, such as `WalletTransactions`. It complements the general journal. |
| Tenant | Logical marketplace/organization authorization boundary inside an approved country cell. |
| TLS | Transport Layer Security, which protects network traffic in transit and authenticates the server endpoint. TLS does not replace application authorization or encrypt data after it reaches an endpoint. |
| TOTP | Time-based one-time password generated from a shared secret, commonly used for authenticator-app 2FA. |
| Trusted contact | User-selected person eligible to receive a time-bounded live-trip share under the active trip and privacy policy. A trusted contact is not automatically an emergency responder or account administrator. |
| TTL | Time to live: the bounded period after which cached, ephemeral, or privacy-sensitive state expires. A TTL is not a substitute for explicit revocation when immediate removal is required. |
| TURN | Relay protocol/server used when direct WebRTC media paths cannot traverse NAT or firewalls. |
| UUIDv7 | RFC 9562 time-ordered universally unique identifier used for new transactional and externally exposed entities. |
| Valkey | Redis-protocol distributed data service used for cache, realtime scale-out, fresh geospatial state, and short-lived coordination. |
| WAF | Web Application Firewall: an edge control that filters known hostile patterns, probes, and abusive request rates. It reduces noise but cannot enforce entity ownership or business state. |
| Webhook | Provider-to-API callback authenticated by a provider-specific signature and handled idempotently. |
| WebRTC | Real-time media technology used underneath LiveKit client connections. Signalling, media, TURN relay, platform permissions, and recording are distinct paths that must be tested separately. |
| Worker heartbeat | Periodic evidence that a background processor is alive; it must be interpreted alongside backlog age and failures. |

If a chapter uses a term differently, the chapter should say so explicitly.
