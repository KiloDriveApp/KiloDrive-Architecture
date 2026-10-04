# Private documents, evidence and exports

[API Guide](README.md) · [Upload reference](reference/uploads.md)

## Uploading is not approving

An upload receipt establishes that supported bytes were accepted at the private
storage boundary. Submitting that reference as a driver/vehicle document creates
domain evidence. Reviewing and approving it creates a later authorized decision.
Do not confuse those steps or mark a licence valid merely because a camera
photo was uploaded.

The reviewed upload boundary accepts genuine JPG/JPEG, PNG and PDF files up to
the documented 10 MB application limit. Extension, content class and magic-byte
checks must agree. Antivirus scanning is configurable; its presence in source
does not certify an active scanner deployment.

Use multipart fields from the operation's inline schema. The ordinary and
recoverable upload routes have distinct contracts. Where the recoverable flow
supplies an operation receipt, preserve it through an interrupted response.
Do not repeatedly upload the same evidence just because the final UI refresh
failed.

## References remain private

A `fileRef` or upload record ID is not a permanent public download URL.
`GET /api/v1/uploads/{fileRef}` goes through authorized retrieval. Owner,
participant or authorized reviewer access depends on the domain and current
scope. Never publish storage keys, presigned URLs, document contents or review
screenshots in this repository.

The consumer and Admin clients must fetch documents through the authenticated
media boundary. Cache keys include the relevant authorization context. Logout,
account switch, device denial, replacement and permission changes must stop
private media reuse. Opening a document from a dossier should show loading,
readable preview and an actionable error instead of a silent tap.

## Replacement and audit evidence

Rejected documents carry the reviewer reason and an owner remediation path.
Replacement uploads preserve the earlier review trail. The checklist/readiness
assessment follows the latest applicable evidence and current expiry/compliance
state. An old approved thumbnail must not remain the apparent current document
after a replacement or expiry.

Administrative decisions are audit-recorded in readable terms. The affected
user's timestamps use the applicable timezone. Full administrative audit detail
and export contracts stay private; public architecture explains the accountability
model without publishing personal data or investigator payloads.

## Support, trip and rental evidence

Support attachments, trip chat/call records, delivery custody and rental
inspection/damage evidence require the relevant owner/participant/organization
relationship. A URL-shaped field does not authorize public sharing. Evidence
views should mask unrelated identities and retain only what the workflow needs.

Trip sharing is an explicit consent/capability boundary, not a substitute for
the private trip contract. Public sharing-token routes are excluded from this
curated export. Do not put real share tokens in examples or treat a link as
permanent access.

## Reports and account export

Personal report/export routes require the signed-in user's authority. Report
types have different eligibility; driver earnings/commission data require the
corresponding driver relationship. Date ranges, timezone semantics and file
formats follow the endpoint model.

Download, render and share actions must handle cancellation and avoid leaking
private files into a shared cache. Scheduled reports are separate durable work:
creating a schedule is not proof that an email attachment reached the recipient.
Account export, deactivation and deletion likewise have their own security,
recovery and retention behavior.

## Public versus private information

Published website pages, legal versions and public catalogs can be documented
and linked here. Identity records, account exports, wallets, conversations,
support cases and uploaded evidence remain protected even when their route
names and schema fields are documented publicly.

Use the [Privacy Policy](https://kilodrive.com/privacy) and
[Terms of Service](https://kilodrive.com/terms) for product disclosures.
Architectural documentation is not a replacement for jurisdiction-specific
legal commitments or a promise that every protected record is immediately
erasable.

Related: [private storage decision](../adr/006-private-object-storage.md),
[onboarding](account-and-onboarding.md) and
[security reporting](../../SECURITY.md).
