# Notice

Copyright © 2026 Eprecus LLC. All rights reserved.

## What this repository publishes

This repository publishes KiloDrive architecture, operational principles,
security explanations, a curated API reference, documentation tooling and a
sanitized direct-dependency inventory. It describes the consumer app and the
separate restricted System Admin app, their shared API, and the boundaries among
identity, country data, money, documents and external providers.

It is not the application source distribution, a production access package or
a complete private operations manual. Public API descriptions explain reviewed
contracts; they do not grant API credentials, partner access, administrative
privileges or permission to test production. See the
[API publication limits](docs/api/coverage-and-limitations.md) and
[security reporting policy](SECURITY.md).

## Rights and third-party material

The copyright notice above remains unchanged. This update adds no new license
grant over KiloDrive code, documentation, branding or confidential material.
Public visibility must not be interpreted as permission to use production data,
trademarks, private implementation details or third-party services.

KiloDrive uses open-source packages and commercial/cloud services. Their
respective licenses, copyright notices, attribution requirements and service
terms remain applicable. Naming a package or provider here does not replace
its exact license text, convey its trademarks, or imply its endorsement of
KiloDrive. A vendored or modified package must retain its own reviewed origin
and notices rather than being presented as an unmodified upstream release.

The [license guide](docs/third-party/licenses.md) explains engineering review
responsibilities. It is not the complete set of notices for an APK, AAB, IPA or
server deployment. Exact resolved packages, native libraries, fonts, media,
maps and other distributed assets require release-specific review and notices.

## Dependency inventory limits

The [readable direct-package inventory](docs/third-party/direct-packages.md) and
[public CycloneDX baseline](docs/third-party/kilodrive-public-direct.cdx.json)
cover the reviewed direct dependencies and explicit overrides for both mobile
apps and the tracked .NET projects. They identify source provenance and package
ownership; the [SBOM guide](docs/third-party/sbom.md) defines their scope.

This public baseline is not a complete transitive/native release SBOM, a
vulnerability clearance, a license audit or proof that every listed component
ships in every artifact. A matching checksum establishes artifact consistency,
not security, suitability or license compliance.

## Standards, security and assurance statements

The [OWASP mapping](docs/security/owasp-api-top-10-2023.md) references the
[OWASP API Security Top 10, 2023 edition](https://api-security.owasp.org/editions/2023/en/0x11-t10/).
OWASP supplies the risk taxonomy; the KiloDrive analysis is this repository's
source-based assessment. It does not indicate an OWASP audit, endorsement or
certification. Third-party standards and project names identify their respective
work and do not imply an affiliation.

The [current baseline](docs/current-baseline.md) records the source snapshot
behind published claims. Source presence, a schema fingerprint, a generated
contract, a green documentation job and a successful device/provider exercise
are different evidence. None should be substituted for another. Historical
chapters retain their original scope and do not certify newer releases.

Security chapters explain implemented controls, configurable policies and
operating requirements. They are not a penetration-test report, regulatory
approval, promise of availability or guarantee that every feature/provider is
active in every country. No response-time commitment, bounty or legal safe
harbor is created by publishing this documentation.

## Product information and privacy

Current user-facing commitments and product information are published on the
[KiloDrive website](https://kilodrive.com/), including the
[Privacy Policy](https://kilodrive.com/privacy),
[Terms of Service](https://kilodrive.com/terms),
[user manuals](https://kilodrive.com/manuals) and
[public release page](https://kilodrive.com/changelog). Architecture examples
do not replace those documents or establish current local pricing and availability.
For ordinary questions, use [Contact KiloDrive](https://kilodrive.com/contact).

## Restricted information and corrections

Credentials, signing material, private infrastructure identifiers, production
connection details and personal records must not be committed here. Examples
must remain synthetic and must not confer real identity, eligibility or
financial authority.

If restricted material or a security weakness is discovered, follow
[SECURITY.md](SECURITY.md). Do not copy it into a public issue, commit, fork,
screenshot or support attachment. Ordinary non-sensitive documentation
corrections follow [CONTRIBUTING.md](CONTRIBUTING.md).
