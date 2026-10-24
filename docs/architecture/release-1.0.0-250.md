# Consumer 1.0.0+250 — trip sharing, rental journeys and release history

Reviewed 24 October 2026 against product source revision
`33acdf7e54348f4b3bdf5bb2e06ee0c06f38b4e9`. The consumer source version is
`1.0.0+250`, the separate System Admin source version is `0.1.0+49`, and the
schema contract is `2026.10.24.1`. These are source observations, not claims
that a store has approved the build or that every country and provider is live.

## What the combined customer notes cover

This chapter brings together the distinct, reviewed release themes of builds
244, 248 and 250. It does not redate or erase their original records. Build
248 had already incorporated the history of builds 247 and 224; those
improvements should be represented once, with their original provenance, when
the public changelog is consolidated into 250.

| Source build | Customer-facing improvement | Important boundary |
| --- | --- | --- |
| 244 | Provider workspaces explain documents, membership allowance and account access separately. Plan comparison shows store currency and term-specific benefits. Registration retains the selected journey; Back returns to the previous task. Rental dates retain their times, and booking acknowledgements and provider-confirmed payment receipts can be emailed or downloaded by an authorized user. | Membership does not by itself approve a provider. Store pricing and receipts come from the relevant provider and authoritative booking record. |
| 248 | The app links to the consolidated End User and Transportation Provider manuals. Rental booking, payment, receipt, collection and return screens make status and next actions clearer. Delivery drafts and open requests are easier to recover. Identity and service readiness identify the missing requirement; interrupted financial actions retain their original operation for reconciliation. | This build already includes retained 247/224 release history; it is not a new certificate for those earlier journeys. |
| 250 | Shared trips show live journey updates and the assigned driver and vehicle safety details. Ride search and map interactions give clearer feedback and recover after interruption. Rental browsing, booking decisions, documents and provider tasks present more useful next steps; delivery and account navigation remain available after interruptions. | A share exposes only its approved public projection. Private account, contact, chat and payment data remain outside it. Live movement requires an active authorized trip and fresh location evidence. |

## Operating interpretation

The API remains authoritative for trip state, assignment, membership benefits,
booking and financial outcomes. A mobile screen must not turn an interrupted
response into a second purchase, settlement or booking. Public trip sharing
and short links are separate from authenticated account access: the link's
scope, expiry, revocation and privacy projection govern what a viewer sees.
Device location and realtime delivery can be delayed; a stale observation is
not presented as current movement or manufactured into a precise route.

Rental collection and return remain distinct from booking agreement and
payment confirmation. Provider identity or driving readiness is evaluated
separately from membership access. Published country features and store
products are effective only where the corresponding policy, provider mapping
and operational prerequisites have been verified.

## Source and publication evidence

The source release descriptions are the build-244, build-248 and build-250
blocks in `database/seed-app-release-changelog.sql` in the product repository.
The three-locale Google Play copy for build 250 is in
`docs/releases/play-store-1.0.0-250.txt`. The earlier
[build-248 chapter](release-1.0.0-248.md) preserves its 23 October policy,
manual and consolidation evidence; it is not rewritten as a build-250 test.

On 24 October 2026, the production release catalogue published build 250 with
312 retained improvement cards and archived the 244 and 248 source entries.
The public [build-250 changelog](https://kilodrive.com/changelog/1.0.0/build/250)
returned HTTP 200 with the merged summary. The old build-244 and build-248
changelog URLs returned HTTP 301 directly to build 250; the previously folded
224 and 247 links did likewise. The website deployment also passed its public
manual, support-code, architecture and blog route probes. This is evidence of
release-note publication, not of a newly approved store binary or physical
journey certification.

Signed artifacts, store review, production API/schema state and physical-device
journeys each need their own verification. Use the [current baseline](../current-baseline.md),
[mobile release runbook](../runbooks/mobile-release.md) and
[portal/website release runbook](../runbooks/portal-website-release.md) to
check the corresponding evidence.
