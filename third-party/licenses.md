# Third-Party Licenses and Notices

This page is a compliance guide, not a substitute for the exact release SBOM and
license files shipped with a binary.

## Common license families in the current direct graph

| Component family | Typical upstream license/terms | Required treatment |
| --- | --- | --- |
| .NET, ASP.NET Core, EF Core, Microsoft extensions | MIT | Preserve copyright/license notice |
| AWS SDK for .NET | Apache-2.0 | Preserve notice/license and comply with terms |
| OpenTelemetry | Apache-2.0 | Preserve notice/license |
| Firebase/Google API libraries | Apache-2.0 or package-specific terms | Verify package metadata and service terms |
| Serilog, MediatR, StackExchange.Redis, MySqlConnector, Pomelo, ClosedXML, Swashbuckle, Stripe.net | Commonly permissive MIT/Apache-style licenses | Preserve exact upstream notices |
| Flutter SDK/plugins | BSD-3-Clause, MIT, Apache-2.0, or package-specific | Generate notices from resolved pub graph |
| SixLabors.ImageSharp | Six Labors Split License | Confirm commercial eligibility and preserve required terms |
| QuestPDF | QuestPDF community/commercial license terms | Confirm organization eligibility for each release |
| Google Maps, Firebase, Apple services, Google Play, Stripe, PayPal, Twilio, Cloudflare, AWS, LiveKit hosting | Service/commercial terms | Maintain account, data-processing, branding, and usage compliance |

## Release process

1. Generate package and license inventory from the exact restored build.
2. Include transitive packages and native frameworks.
3. Flag unknown, copyleft, source-available, dual, or commercial terms for legal
   review.
4. Generate app/server third-party notices and preserve upstream text verbatim.
5. Verify store declarations, SDK data use, permissions, and privacy labels.
6. Archive the SBOM, notices, scanner output, and approval with release evidence.

Do not infer a package's license solely from this summary. Upstream package
metadata and the resolved source archive are authoritative.
