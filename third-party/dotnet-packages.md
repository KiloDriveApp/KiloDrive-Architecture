# Direct .NET Package Inventory

Baseline: .NET 9 central package management, reviewed 2026-08-23. Transitive
packages are captured by the release SBOM and may change after a lock update.

| Area | Direct packages |
| --- | --- |
| AWS | AWSSDK.EventBridge, PinpointSMSVoice, PinpointSMSVoiceV2, S3, SecretsManager, SecurityToken, SimpleEmailV2, SocialMessaging, SQS |
| Data | Microsoft.EntityFrameworkCore, Relational, Pomelo.EntityFrameworkCore.MySql, MySqlConnector |
| Authentication | Microsoft.AspNetCore.Authentication.JwtBearer, Fido2, Google.Apis.Auth, FirebaseAdmin |
| Application | MediatR, FluentValidation.AspNetCore |
| Distributed/realtime | StackExchange.Redis, Microsoft.Extensions.Caching.StackExchangeRedis, Microsoft.AspNetCore.SignalR.StackExchangeRedis |
| Observability | OpenTelemetry hosting/exporter/instrumentation, Serilog.AspNetCore, Serilog.Sinks.AwsCloudWatch |
| Payments | Stripe.net |
| Reports/media | ClosedXML, QuestPDF, SixLabors.ImageSharp |
| API contract | Swashbuckle.AspNetCore |
| Test | xUnit, Microsoft test host/MVC testing, coverlet, Testcontainers.MySql, EF Core InMemory |

## Selected pinned versions

| Package family | Baseline version |
| --- | --- |
| EF Core / JwtBearer / SignalR Redis | 9.0.16 |
| Pomelo EF MySQL | 9.0.0 |
| MySqlConnector | 2.4.0 |
| MediatR | 12.5.0 |
| FluentValidation.AspNetCore | 11.3.1 |
| StackExchange.Redis | 2.8.31 |
| OpenTelemetry | 1.17.0 |
| FirebaseAdmin | 3.0.0 |
| Stripe.net | 52.2.0 |
| ClosedXML | 0.105.1 |
| QuestPDF | 2026.7.2 |
| ImageSharp | 3.1.12 |
| Swashbuckle | 7.2.0 |

Exact AWS SDK patch versions are centrally pinned together on the v3 SDK family
until all adapters can migrate consistently. Consult the release SBOM rather than
copying this table into an automated compliance decision.
