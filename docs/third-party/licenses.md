# Third-Party Licenses and Notices

## Scope and responsibility

This is engineering guidance, not legal advice and not a substitute for the exact
license texts associated with a release. The release SBOM, upstream source/package
metadata, signed artifact, service terms, and counsel-approved obligations are
authoritative.

## Common license and terms families

| Component family | Common upstream model | Engineering obligation |
| --- | --- | --- |
| .NET/ASP.NET/EF/Microsoft extensions | MIT | Preserve copyright and license text |
| AWS SDK and OpenTelemetry | Apache-2.0 | Preserve license/NOTICE and comply with terms |
| Firebase/Google libraries | Apache-2.0 or package-specific | Verify metadata plus service/privacy terms |
| Serilog, MediatR, Redis/MySQL clients, ClosedXML, Swashbuckle, Stripe.net | Commonly MIT/Apache-style | Preserve each exact resolved notice; do not infer from the family |
| Flutter SDK and plugins | BSD-3-Clause, MIT, Apache-2.0, or package-specific | Generate notices from resolved Dart and native graphs |
| ImageSharp | Six Labors Split License | Confirm commercial eligibility and current terms |
| QuestPDF | Community/commercial terms | Confirm organization eligibility for each release |
| Cloud/provider services | Commercial/service terms | Maintain account, DPA, branding, data-location, and acceptable-use compliance |

“Common” is intentionally not “guaranteed.” A fork, transitive component, or new
major version may use different terms.

## Review by distribution surface

License obligations follow the delivered artifact, not the repository folder. A
server library may stay on an operator-controlled host, while a Dart plugin,
AAR, framework, font, sound, or map attribution is redistributed in a store
binary. The reviewer asks:

- Is the component compiled, dynamically linked, copied as a resource, used only
  during build/test, or consumed as a remote service?
- Is the application distributed to customers, run as a hosted service, or both?
- Did a plugin add native code under a different license than its Dart wrapper?
- Are modifications, NOTICE content, source offers, attribution placement, or
  relinking requirements triggered?
- Does a commercial/community grant depend on organization size, revenue,
  deployment count, or use case?

The answer is captured per resolved version. A repository license badge is not
the legal text, and a wrapper's MIT license does not automatically cover the SDK
it downloads.

## Obligations beyond a notice file

- Attribution may need to appear inside the app, documentation, or map UI.
- Apache-2.0 NOTICE content must be preserved when applicable.
- Source-available, dual-license, copyleft, codec, font, media, and commercial
  packages require explicit review.
- Google Maps/OpenStreetMap and other geodata have attribution and use limits.
- Apple, Google Play, Firebase, payment, messaging, cloud, and social identity
  services impose contractual and privacy requirements independent of SDK code.
- Assets, vehicle photographs, icons, fonts, and manuals need their own provenance
  even when no package manager is involved.

## Release notice procedure

1. Restore the exact commit with the pinned toolchains.
2. Export direct and transitive .NET, Dart, Gradle, CocoaPods, and embedded native
   dependency graphs.
3. Generate an SPDX/CycloneDX SBOM with versions, hashes, supplier, license
   expressions, and package URLs where available.
4. Resolve `UNKNOWN`, `NOASSERTION`, copyleft, source-available, commercial, and
   dual-license entries manually.
5. Preserve upstream license and NOTICE text verbatim in the release notice
   bundle.
6. Compare store data-safety/privacy labels and permissions with the actual SDK
   graph.
7. Sign/archive the SBOM, notice bundle, scanner results, approvals, and artifact
   hashes together.

## Vulnerability is separate from license

A permissive package may be vulnerable; a secure package may be commercially
ineligible. Run both reviews. A vulnerability exception records affected
versions, exploitability, exposed code path, compensating controls, owner,
expiry, and upgrade/removal plan. A license exception records the actual grant
and approval; it is not hidden in a vulnerability waiver.

## Attribution in the product

Mobile releases expose an accessible third-party notices surface generated from
the resolved graph. Server distributions retain the notice bundle beside the
artifact evidence. Map screens display attribution required by the selected
map/data source. Documentation and marketing assets preserve attribution
required by fonts, images, icons, or datasets.

Generation may deduplicate identical texts but must not drop copyright holders.
It preserves verbatim license/NOTICE content: this guide may summarize
obligations, but a summary never replaces upstream legal text.

## Removal and replacement

Deleting a package reference is only the first step. Verify the signed
binary/publish no longer contains its assembly, framework, native library,
resource, font, or generated code. Remove platform registrations, permissions,
entitlements, privacy labels, rules, notices, provider configuration, and unused
transitive pins. Regenerate the SBOM and compare the artifact graph.

Keep historical notices with historical releases. A current release no longer
using a package does not erase obligations attached to binaries already
distributed.

## Developer rules

- Do not paste unlicensed snippets, images, fonts, or proprietary API examples
  into source.
- Do not remove copyright headers required by an upstream license.
- Do not guess a license from a repository homepage.
- Do not publish internal SBOM fields containing private repository URLs,
  credentials, build paths, or operator identities.
- Escalate uncertainty before release, not after store submission.
