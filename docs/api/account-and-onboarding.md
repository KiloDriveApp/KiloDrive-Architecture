# Account setup and driver readiness

[API Guide](README.md) · [Driver reference](reference/drivers.md)

## Preserve one registration journey

First-run selection records audience, country, contact method, driver account
type and rental-organization intent. Registration, social signup, contact proof
and setup progress must carry the same intent. A stale local preference must
not turn a rider into a driver or create an unintended rental organization.

Account setup reads expose actual persisted progress. The contact-detail
change routes use request/confirm ceremonies; ordinary profile editing must
not directly mark a new email or phone as verified. Identity conflicts should
produce an actionable result without exposing another person's account.

Legal acceptance is server-persisted evidence tied to the applicable version,
language and context. Showing a document is different from recording consent.
After a restart, restore the authoritative state rather than treating a local
checkbox as completed acceptance.

## Driver onboarding is a checklist, not one flag

`GET /api/v1/driver/profile/onboarding` describes document/setup requirements.
The workflow includes identity documents and required vehicle documents. A
registered vehicle, uploaded file, reviewed document, verified vehicle, active
membership and ready driver are different facts.

The reviewed `DriverReadinessDto` reports profile and contact verification,
licence status/expiry, vehicle assignment/verification, registration, insurance,
fitness, membership entitlement, duty eligibility, location freshness and
blocking reasons. Fields such as `canBid`, `canGoOnline`, `bidGateCode`,
`onlineGateCode` and `nextAction` describe the server's current assessment.
Do not rebuild a competing readiness algorithm by counting green UI checkmarks.

## Document lifecycle

1. The owner uploads a genuine supported file through the private upload boundary.
2. The owner submits the resulting reference in the applicable document model.
3. The document remains pending until an authorized review decides its state.
4. The reviewer inspects the actual protected document and its relevant metadata.
5. Approval/rejection updates audit, readiness projections and durable
   notification intent.
6. A rejected owner can submit a replacement; the current checklist reflects
   the latest applicable upload and review state.

Typical checklist states are `missing`, `pending`, `approved` and `rejected`.
Rejection needs a readable reason and remediation guidance. A replacement is
new evidence, not permission to erase the previous rejection's audit history.
Expired documents and changed vehicles can invalidate a previously ready state.

## Reviewer authority belongs to the Admin app

The separate System Admin dossier supports authorized review and readiness
decisions. The consumer app lets the driver see requirements, submit evidence,
read outcomes and remediate rejection. It does not approve its own documents
or provide system-administrator controls.

Single- or dual-approval requirements are configurable API policy for the
applicable area. UI state must follow the server's policy; hiding a second
reviewer step locally does not change authorization. This public guide does
not expose administrative routes or policy override procedures.

## Online and bidding eligibility

Going online, seeing work, placing a bid and accepting an assignment have
different lifecycle checks. The server assesses readiness and must recheck
current eligibility where the action requires it. A plan purchase alone does
not make a driver licensed, insured, vehicle-compliant or available.

Account-owned vehicle storage and maintenance are available without a driver
membership. Legacy `MaxRegisteredVehicles` plan metadata is not a storage cap
for the Maintenance Center. Work eligibility still depends on vehicle
assignment, verification, compatibility and critical-defect rules.

After a reviewer decision, replacement document, expiry, membership change or
vehicle edit, refresh authoritative readiness. Show the reason and next step.
Do not leave a permanently disabled button with no explanation.

## Test the journey, including restarts

Verify intent preservation through social login, contact confirmation and cold
restart. Test pending and rejected evidence, readable private preview, replacement
upload, expired documents, driver status changes and a previously ready driver
becoming blocked. Confirm that notification history describes the actual review
outcome and that a failed provider delivery does not reverse the review decision.

Read [documents and privacy](documents-and-privacy.md),
[mobile architecture](../architecture/mobile.md) and
[System Admin workflow contracts](../architecture/admin-workflow-contracts.md).
