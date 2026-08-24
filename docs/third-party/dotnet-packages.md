# .NET Package Inventory

## Verified baseline

The source targets .NET 9 and uses central package management with transitive
pinning. The API has the broad dependency surface; the Portal and Website are
thin server-rendered API clients. Tests use one xUnit project plus integration
infrastructure. Versions below are the reviewed source baseline, not a promise
that every future release keeps them.

## Direct API dependencies

| Area | Direct package/family | Baseline | Why it exists |
| --- | --- | --- | --- |
| AWS | EventBridge, Pinpoint SMS/Voice v1+v2, S3, Secrets Manager, STS, SES v2, Social Messaging, SQS SDKs | AWS SDK v3 packages, centrally pinned | Dispatch, messaging, object storage, secret/identity access, email, WhatsApp, queues |
| Data | EF Core + Relational | 9.0.16 | Unit of work, model metadata, relational queries |
| MySQL | Pomelo EF MySQL; MySqlConnector | 9.0.0; 2.4.0 | MySQL 8 provider and direct operational/test access |
| Auth | JwtBearer; Fido2; Google APIs Auth; FirebaseAdmin | 9.0.16; 4.0.1; 1.70.0; 3.0.0 | JWT validation, passkeys, social token validation, FCM administration |
| Password hashing | Konscious.Security.Cryptography.Argon2 | 1.3.1 (exact reviewed pin) | Argon2id password derivation for the normal non-FIPS profile |
| Application | MediatR; FluentValidation.AspNetCore | 12.5.0; 11.3.1 | CQRS dispatch and request validation |
| Realtime/cache | SignalR Redis; Extensions Redis; StackExchange.Redis | 9.0.16; 9.0.8; 2.8.31 | Hub backplane, distributed cache, Valkey protocol operations |
| Observability | OpenTelemetry hosting/exporter/instrumentation family | 1.17.0 | Traces, metrics, OTLP export, ASP.NET/HTTP/runtime instrumentation |
| Logging | Serilog.AspNetCore; CloudWatch sink | 9.0.0; 4.3.37 | Structured local/cloud logs |
| Payments | Stripe.net | 52.2.0 | Stripe API/webhook adapter |
| Reports | ClosedXML; QuestPDF | 0.105.1; 2026.7.2 | XLSX and PDF output |
| Images | SixLabors.ImageSharp | 3.1.12 | Safe server-side image processing/re-encoding |
| Contract | Swashbuckle.AspNetCore | 7.2.0 | OpenAPI generation and filters |

The exact AWS patch numbers are in central package management and should be
upgraded as a reviewed family where adapters share `AWSSDK.Core`.

### AWS SDK direct-version snapshot

The reviewed central-package snapshot pins these direct AWS packages. Keeping
the values visible helps a junior engineer understand that “AWS SDK” is a family
of service clients, not one package that can be upgraded independently without
checking `AWSSDK.Core` compatibility.

| Package | Reviewed version | Capability |
| --- | --- | --- |
| `AWSSDK.PinpointSMSVoiceV2` | 3.7.505.37 | End User Messaging SMS APIs |
| `AWSSDK.PinpointSMSVoice` | 3.7.502.63 | Voice messaging APIs used by the adapter |
| `AWSSDK.SimpleEmailV2` | 3.7.509.10 | SES email and raw-message delivery |
| `AWSSDK.SocialMessaging` | 3.7.503.29 | AWS WhatsApp/Social Messaging path |
| `AWSSDK.S3` | 3.7.415.3 | Private object storage |
| `AWSSDK.SecurityToken` | 3.7.401 | STS/workload identity support |
| `AWSSDK.SecretsManager` | 3.7.400.185 | Protected configuration material |
| `AWSSDK.EventBridge` | 3.7.502.62 | Dispatch event publication |
| `AWSSDK.SQS` | 3.7.502.57 | Queue consumption and dead-letter recovery |

The family remains on the v3 line while selected service adapters share that
compatible core. A v4 migration is a coordinated batch with compile,
serialization, credential-chain, timeout, retry, fake, and deployed IAM tests,
not a blind version bump.

## Other projects and test-only dependencies

Portal directly references Serilog.AspNetCore and the CloudWatch sink. Website
directly references Serilog.AspNetCore. The test project directly references the
.NET test SDK, xUnit, coverlet, ASP.NET Core MVC testing, EF Core InMemory,
MySqlConnector, and Testcontainers for MySQL.

Test-only packages do not ship in a production publish, but CI workers still
execute them. They remain in the security/license inventory and must not receive
production credentials.

The Argon2 package is deliberately exact-version pinned. Updating it requires
known-vector, hash-compatibility, malformed-input, memory/concurrency and lazy-
rehash tests. Environments with an approved FIPS-only boundary select the
platform PBKDF2-HMAC-SHA256 profile instead; package presence does not make
Argon2 a FIPS-validated primitive.

## Resolved transitive examples

The verified restore contains transitive components such as:

- `AWSSDK.Core` and CloudWatch Logs SDK support;
- ClosedXML parser and Open XML document libraries;
- Fido2 model/helpers and cryptographic libraries;
- FluentValidation core;
- Google API, GAX, auth, and HTTP helpers;
- IdentityModel/JWT support;
- OpenTelemetry core/exporter/instrumentation packages;
- Serilog core and sinks;
- serialization, fonts, spatial/index helpers, and framework support packages;
- test-only Docker/Testcontainers, SSH, and cryptography helpers.

This is illustrative. Generate the SBOM from `--include-transitive` after the
exact release restore; never hand-maintain a supposedly complete transitive list.

The [SBOM contract](sbom.md) explains artifact binding and completeness checks.

## Package update workflow

1. Restore/build/test the current baseline.
2. Update one coherent family, not unrelated major packages.
3. Compare direct and transitive graphs and package advisories.
4. Run API, authorization, provider-contract, OpenAPI, MySQL fixture, and publish
   tests.
5. Validate trimming/publish output and ensure test packages are absent.
6. Regenerate SBOM and notices; review new or changed licenses.
7. Deploy to a disposable/staging environment and test rollback.

Central pinning prevents projects resolving incompatible families, but it does
not prove runtime compatibility. Database providers, authentication libraries,
AWS SDK families, OpenTelemetry, and document renderers deserve focused tests.

## Security and license notes

Package versions are monitored for CVEs and unmaintained dependencies. ImageSharp
and QuestPDF have license models that require organization/use-case eligibility
review, not just preservation of an MIT notice. Cloud/provider SDK use also
depends on service terms and data-processing agreements.
