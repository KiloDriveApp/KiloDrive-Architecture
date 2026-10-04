"""Reviewed public wording for endpoint purposes and contract field semantics.

Exact wire definitions remain source-derived. Generic descriptions deliberately
explain the contract's field name/type without inventing a hidden business rule.
"""

from __future__ import annotations

import re
from api_context import MODEL_FIELDS, OPERATIONS

PURPOSES = {
    ("post", "/api/v1/auth/register"): "Create a consumer account and begin its country/contact/onboarding journey; this does not grant administrator authority.",
    ("post", "/api/v1/auth/login"): "Authenticate an identifier and password; return either the next security step or the final authenticated session.",
    ("post", "/api/v1/auth/refresh"): "Rotate an eligible refresh credential and obtain the current session; installation and session-family checks still apply.",
    ("post", "/api/v1/auth/logout"): "End the applicable authenticated session through the server logout workflow.",
    ("get", "/api/v1/auth/session"): "Read the current session's authoritative account/security state before resuming protected work.",
    ("get", "/api/v1/auth/me"): "Read the authenticated identity's user model.",
    ("post", "/api/v1/auth/social"): "Validate provider sign-in evidence and return a session or the protected pending-link/verification ceremony.",
    ("post", "/api/v1/auth/password-reset/request"): "Request the secure password-reset ceremony; the response must not expose a password or account-existence proof.",
    ("post", "/api/v1/auth/password-reset/confirm"): "Confirm valid reset evidence and set the new password through the established identity workflow.",
    ("post", "/api/v1/auth/recent-authentication"): "Obtain server-validated recent account proof for consequential operations that require it.",
    ("post", "/api/v1/devices/register"): "Register/admit an installation and return its private credential and access state; anonymous bearer metadata does not bypass app admission.",
    ("get", "/api/v1/devices/status"): "Read the current installation's allowed/restricted access state.",
    ("post", "/api/v1/devices/heartbeat"): "Update the current installation's reported metadata and return access state.",
    ("get", "/api/v1/public/country-sites"): "List published country-site information for discovery and public navigation.",
    ("get", "/api/v1/public/membership-prices"): "Read informational membership prices in the selected country's currency; this does not create an executable purchase.",
    ("get", "/api/v1/public/capabilities"): "Read public capability/availability information; individual actions still require their own authorization and readiness.",
    ("get", "/api/v1/features"): "Read applicable feature enablement for the current authenticated context.",
    ("get", "/api/v1/app-version-policy"): "Read app-version compatibility/update policy for the requested platform/version/build context.",
    ("get", "/api/v1/driver/profile/onboarding"): "Read the driver's persisted setup/document checklist and remediation state.",
    ("get", "/api/v1/driver/profile/readiness"): "Read the authoritative assessment of whether this driver can go online or bid, including blocking reasons and next steps.",
    ("get", "/api/v1/driver/documents"): "List the driver's own submitted documents and their current review state.",
    ("post", "/api/v1/driver/documents"): "Submit a private upload as driver document evidence; submission does not approve it.",
    ("get", "/api/v1/driver/status"): "Read the driver's current operational/online status.",
    ("post", "/api/v1/driver/status"): "Request an online/status change subject to current readiness and operational rules.",
    ("get", "/api/v1/wallet"): "Read the current user's authoritative wallet, currency, held/available breakdown and revision.",
    ("get", "/api/v1/wallet/transactions/history"): "Read owner-scoped seek-paged ledger history; its row-set cutoff is separate from the live wallet balance.",
    ("post", "/api/v1/wallet/topup"): "Start an owner-scoped top-up/payment intent; provider reconciliation, not checkout navigation, establishes wallet credit.",
    ("post", "/api/v1/wallet/transfers"): "Execute the authorized value transfer to the documented saved recipient, with fees/FX and durable recovery where applicable.",
    ("post", "/api/v1/wallet/cashout"): "Request a withdrawal and applicable hold; approval, provider dispatch and settlement are subsequent states.",
    ("get", "/api/v1/operations/status"): "Read the caller's durable command outcome using its original key/reference; this read never executes the command.",
    ("get", "/api/v1/wallet/command-recovery"): "Read the compatibility command-recovery state; new clients prefer /api/v1/operations/status.",
    ("get", "/api/v1/driver/membership/store-status"): "Read the single authoritative driver membership workspace snapshot, including entitlement and billing/recovery state.",
    ("post", "/api/v1/driver/membership"): "Purchase an eligible driver plan through the wallet workflow with server-owned pricing/proration and revision checks.",
    ("get", "/api/v1/store-billing/products"): "Read the reviewed platform/audience product mapping for comparison with actual native localized offers.",
    ("post", "/api/v1/store-billing/quote"): "Validate the exact mapped plan and native offer and create the applicable server-owned purchase quote.",
    ("post", "/api/v1/store-billing/prepare"): "Persist the applicable purchase preparation before native checkout; preparation does not grant entitlement.",
    ("post", "/api/v1/store-billing/verify"): "Validate store transaction evidence on the server and reconcile/grant the mapped entitlement once.",
    ("post", "/api/v1/store-billing/restore"): "Reconcile eligible existing store purchases with the authenticated account; restoration is not a new sale.",
    ("get", "/api/v1/notifications/history"): "Read the owner's persisted notification inbox using a scope-bound seek cursor and filters.",
    ("post", "/api/v1/notifications/push-token"): "Bind a current provider token to verified app, installation, session, account and country authority with guarded state updates.",
    ("delete", "/api/v1/notifications/push-token"): "Deactivate the current owner's applicable push binding without transferring another account's authority.",
    ("get", "/api/v1/notifications/push-token/installation-state"): "Read current installation push enablement/revision without revealing provider tokens or another owner's identity.",
    ("post", "/api/v1/rides"): "Create a rider request with journey, proposed fare, category and applicable product options; this does not yet assign a driver.",
    ("post", "/api/v1/rides/{rideRequestId}/bids/accept"): "Accept an eligible current bid and establish the trip/financial state under server concurrency and readiness checks.",
    ("get", "/api/v1/trips/active"): "Read the current user's active trip state for restoration and navigation.",
    ("post", "/api/v1/trips/{tripId}/start"): "Start the assigned trip after the applicable pickup and lifecycle checks.",
    ("post", "/api/v1/trips/{tripId}/complete"): "Complete an eligible trip and record its authoritative payment/settlement effects.",
    ("post", "/api/v1/trips/{tripId}/chat"): "Commit a participant chat message using its stable client/mutation identity; a realtime echo is not another message.",
    ("get", "/api/v1/trips/{tripId}/chat"): "Read authorized participant chat history using the documented pagination/reconciliation bounds.",
    ("post", "/api/v1/trips/{tripId}/tip"): "Record an authorized trip tip as a distinct value-moving operation.",
    ("post", "/api/v1/uploads"): "Accept a genuine supported file into private storage and return upload evidence; it is neither public sharing nor document approval.",
    ("get", "/api/v1/uploads/{fileRef}"): "Retrieve private bytes only through authorized owner/reviewer access to this file reference.",
    ("post", "/api/v1/uploads/recoverable"): "Create an upload with durable recovery identity so an interrupted response can be reconciled.",
    ("get", "/api/v1/uploads/operations/{operationId}"): "Read an authorized recoverable upload's result instead of blindly submitting a second upload.",
}

FIELDS = {
    "id": "Opaque identifier of this model's record; knowing it does not grant access.",
    "userId": "Related account identity; the server still proves the caller's ownership or permitted relationship.",
    "tenantId": "Tenant associated with this record; it is not caller authority to switch tenants.",
    "driverProfileId": "Driver-profile record associated with this operation or result.",
    "vehicleId": "Account vehicle record associated with this operation or result.",
    "tripId": "Accepted trip record, distinct from the originating ride request.",
    "rideRequestId": "Rider request record, distinct from an accepted trip.",
    "planId": "Membership catalog record; it does not itself prove a user entitlement.",
    "paymentId": "Server-owned payment record used for state/reconciliation.",
    "recipientFavoriteId": "Saved recipient reference used by this transfer; not an arbitrary target user ID.",
    "fileRef": "Private storage reference; not a permanent public URL or approval decision.",
    "uploadRecordId": "Private upload inventory record associated with the stored evidence.",
    "token": "Token for this specific contract, such as push registration; sensitive values must not be logged or reused in another ceremony.",
    "accessToken": "Sensitive bearer access credential for the issued session.",
    "refreshToken": "Sensitive rotating refresh credential; preserve secure-store and session-family rules.",
    "deviceToken": "Private admitted-installation credential; not a user password or portable account authority.",
    "password": "Secret password input for the established secure identity ceremony; never echo or log it.",
    "allowWeakPassword": "Client acknowledgement field for a password-policy choice; it does not override server validation.",
    "identifier": "Sign-in identifier accepted by this identity contract; validation and privacy rules still apply.",
    "firstName": "Person's given name as provided through the applicable profile/identity workflow.",
    "lastName": "Person's family name as provided through the applicable profile/identity workflow.",
    "email": "Email address for this model's person/destination; its presence does not prove verification.",
    "phoneNumber": "Country-aware contact number; its presence does not prove verification or provider provisioning.",
    "name": "Name of the record described by this model; distinct from its opaque ID.",
    "displayName": "Human-readable display label; do not use it as a stable identifier.",
    "currency": "ISO currency code for the accompanying monetary amounts.",
    "currencyCode": "ISO currency code; do not infer it from a dollar symbol.",
    "countryCode": "Country ISO code for this model/context; it cannot override authenticated country authority.",
    "timezone": "Timezone context used by this contract; apply documented IANA/display semantics.",
    "language": "Language selector/content language; use the endpoint's supported values and fallback rules.",
    "amountMinor": "Monetary amount in the accompanying currency's integer minor units.",
    "balanceMinor": "Wallet balance in integer minor units; use the full wallet breakdown to interpret spendable funds.",
    "heldBalanceMinor": "Funds reserved by applicable holds/escrow; they are not freely spendable.",
    "revision": "Authoritative record revision used for applicable concurrency checks.",
    "expectedRevision": "Revision the caller read for this logical update; retain the original during uncertain-outcome recovery.",
    "stateRevision": "Revision of the returned state snapshot, distinct from a display timestamp.",
    "policyVersion": "Policy revision used for this assessment; not the mobile app build number.",
    "version": "Version in this model's domain; not automatically an API major version.",
    "clientOperationId": "Client's stable identity for this logical operation; preserve it through interrupted responses.",
    "mutationId": "Stable identity of a logical state mutation; do not generate a replacement merely because the response was lost.",
    "operationId": "Durable operation reference used for applicable outcome discovery.",
    "traceNumber": "Human/support trace reference for the transaction, distinct from its resource ID.",
    "Idempotency-Key": "Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response.",
    "If-Match": "Strong resource ETag read before this logical edit; preserve the original value for uncertain-outcome replay.",
    "X-KiloDrive-Recent-Authentication": "Private recent account proof when required by the server; local biometric/PIN unlock is insufficient.",
    "cursor": "Opaque scope-bound seek cursor from the previous page; do not modify it or reuse it under different filters.",
    "continuation": "Endpoint-specific continuation value from the previous response; preserve its scope and ordering.",
    "search": "Search text applied within this endpoint's authorized collection; it does not widen account/tenant scope.",
    "preset": "Named range/filter preset accepted by this endpoint; explicit date bounds have separate semantics.",
    "beforeUtc": "UTC upper pagination bound for older records, interpreted by this endpoint's ordering rules.",
    "beforeSequence": "Sequence upper bound for older chat/events; use persisted sequence ordering rather than display time.",
    "clientMessageId": "Stable client message identity used for deduplication or reconciliation after a lost chat response.",
    "fromUtc": "UTC start of the requested range; apply this endpoint's inclusion/validation rules.",
    "toUtc": "UTC end of the requested range; apply this endpoint's inclusion/validation rules.",
    "format": "Output/file format selector; use the operation's supported media rather than guessing an extension.",
    "documentKey": "Stable key of the legal/document definition whose version is being accepted or read.",
    "expectedAuthorizationFingerprint": "Fingerprint of the authorization/quote the caller reviewed; used to detect a changed financial precondition.",
    "promoCode": "Promotion code supplied for server validation; it is not a guaranteed discount or credit.",
    "status": "Current domain status; use this model's enum or documented string vocabulary.",
    "state": "State in this model's workflow; do not map it with another domain's status registry.",
    "outcome": "Result/recovery state of this operation; unknown or pending is not failed or successful.",
    "noMutation": "Explicit server evidence that no domain/provider mutation occurred; absence is not equivalent proof.",
    "responseStatusCode": "Recorded HTTP result status for the operation when available.",
    "requiresTwoFactor": "Whether login needs its next second-factor step before a final authenticated session exists.",
    "twoFactorTicket": "Sensitive temporary ceremony ticket; it is not a bearer access token.",
    "auth": "Final authentication/session model when the ceremony actually completes.",
    "pendingSocialLink": "Protected pending account-link decision; email equality alone must not finalize it.",
    "maskedDestination": "Privacy-reduced contact display for the ceremony; not the raw credential or full destination.",
    "canBid": "Server's current assessment of bidding eligibility, not a client-computed approval.",
    "canGoOnline": "Server's current assessment of online eligibility.",
    "blockingReasons": "Readable or coded reasons that currently block the assessed workflow.",
    "checklist": "Requirement-by-requirement setup/readiness state.",
    "nextAction": "Suggested next workflow step returned by the server; it does not override authorization.",
    "membershipEntitled": "Whether current membership evidence supplies the applicable entitlement.",
    "complianceProjectionCurrent": "Whether the projected compliance state agrees with the authoritative assessed version.",
    "reviewNote": "Human-readable reviewer explanation, including remediation where applicable.",
    "reason": "Reason supplied or returned for this workflow; follow any catalog/required validation rules.",
    "reasonCode": "Stable reason code; map through the applicable reason catalog instead of displaying an unrelated enum.",
    "items": "Records returned in this collection/page, each using the referenced item model.",
    "page": "Page-number context for this endpoint; not a universal zero-based offset.",
    "pageSize": "Requested or returned page size, subject to this endpoint's server bounds.",
    "totalCount": "Total count defined by this page model; not automatically a live aggregate.",
    "totalPages": "Number of pages represented by this page-number model.",
    "hasMore": "Whether the seek-paged result indicates more records after this page.",
    "nextCursor": "Opaque, scope-bound continuation token; preserve it unchanged and reset it when filters/context change.",
    "unreadCount": "Current unread count in the applicable notification/chat model.",
    "isActive": "Whether this record is marked active; other permission/provider/readiness checks still apply.",
    "platform": "Platform selector in this contract; numeric enums and string selectors are not interchangeable.",
    "audience": "Applicable product/client audience, distinct from verified security authority.",
    "provider": "Configured provider selector for this operation; a named provider is not proof of readiness.",
    "notificationPermission": "Reported native notification permission state.",
    "channelCapabilities": "Reported native delivery capabilities for applicable notification behavior.",
    "explicitOptIn": "Explicit user intent where the binding workflow requires consent to enable delivery.",
    "code": "Code in this model's vocabulary; distinguish business/error/catalog codes from confidential verification codes.",
    "supportCode": "Sanitized support reference for a failure/warning; suitable for protected troubleshooting context.",
    "correlationId": "Safe request correlation reference; not an access token or proof of success.",
    "safeAction": "Server guidance for safe recovery; preserve operation evidence before retrying.",
    "retryable": "Whether the error permits an applicable retry; it does not authorize a blind second mutation.",
    "paymentMethod": "Payment method enum; availability and settlement rules are checked separately.",
    "quoteToken": "Server-owned quote evidence; preserve currency/amount/expiry binding and treat it as private.",
    "fxQuoteToken": "Private FX quote evidence for the current transfer, distinct from a display rate.",
    "exchangeRate": "Reference FX rate for this result; use server amount snapshots instead of floating-point monetary recalculation.",
    "termDays": "Requested/applicable membership term in days; only configured valid terms are allowed.",
    "periodDays": "Duration of this catalog plan's default period, expressed in days.",
    "feeMinor": "Fee for the applicable default product/plan period, in the stated currency's integer minor units.",
    "weeklyFeeMinor": "Catalog price for the weekly term in currency minor units; availability still depends on the configured offer.",
    "monthlyFeeMinor": "Catalog price for the monthly term in currency minor units.",
    "threeMonthFeeMinor": "Catalog price for the three-month term in currency minor units.",
    "sixMonthFeeMinor": "Catalog price for the six-month term in currency minor units.",
    "annualFeeMinor": "Catalog price for the annual term in currency minor units.",
    "maxBidsPerDay": "Plan allotment for new bids in the server-defined daily usage period; re-bid rules are separate.",
    "maxVehicleChangesPerPeriod": "Plan's vehicle-change allotment for its usage period; assignment and verification checks still apply.",
    "maxRegisteredVehicles": "Legacy plan metadata; it must not cap account-owned vehicle storage or Maintenance Center access.",
    "maxFavorites": "Plan's applicable saved-favorite allotment; ownership and feature policy still apply.",
    "maxAcceptedRidesPerMonth": "Catalog allotment for accepted rides in the applicable monthly period; use authoritative usage/readiness checks.",
    "maxAcceptedTripsPerWeek": "Catalog allotment for accepted trips in the applicable weekly period; use authoritative usage/readiness checks.",
    "minWithdrawalMinor": "Applicable lower withdrawal bound in currency minor units; read current cashout limits before requesting.",
    "maxWithdrawalMinor": "Applicable upper withdrawal bound in currency minor units; current server limits remain authoritative.",
    "baseCurrency": "Currency of the catalog/quote's base amount, distinct from the displayed local currency.",
    "fxRateFromBase": "Reference conversion rate from the base currency; executable prices come from the server's reviewed quote.",
    "usage": "Current benefit consumption/allotment model; plan definition and consumed usage are different facts.",
    "autoRenew": "Membership renewal preference/state for this model; it does not itself prove the next charge will succeed.",
    "upgradeCreditMinor": "Server-calculated unused-value upgrade credit in currency minor units.",
    "currentPeriod": "Current authoritative membership usage/entitlement period model.",
    "pendingChange": "Scheduled or pending membership change, distinct from the currently effective entitlement.",
    "nextReset": "Next benefit-usage reset information; it is not automatically membership expiry.",
    "priceTermEvidence": "Evidence of the accepted price/term mapping used by the membership lifecycle.",
    "lifecycleReasonCode": "Reason for the current membership lifecycle state; render through its contract vocabulary.",
    "fileName": "Document/file display name; it is not a storage authorization or approved-document status.",
    "driverRevision": "Driver aggregate revision associated with the document/readiness state.",
    "make": "Vehicle manufacturer name/catalog selection.",
    "model": "Model in the owning domain; for vehicle contracts, the vehicle model associated with the manufacturer.",
    "plateNumber": "Country-specific vehicle registration plate; validate through the applicable country workflow.",
    "vinChassis": "Vehicle VIN/chassis identification data; keep the actual value private and within authorized views.",
    "verificationStatus": "Current vehicle verification enum; a saved vehicle is not automatically approved for work.",
    "verificationNote": "Human-readable verification decision/reason for the vehicle.",
    "insuranceStatus": "Insurance review/status enum; an uploaded policy is not automatically current confirmed coverage.",
    "insurancePolicyNumberLast4": "Masked last-four insurance policy identifier; not the full policy number.",
    "isPrimary": "Whether the vehicle is designated primary in this account context; work eligibility is assessed separately.",
    "planName": "Human plan name; use plan/entitlement records for identity and authority.",
    "stops": "Ordered journey/delivery stops in the referenced stop model.",
    "distanceMeters": "Distance represented by this model, in metres; its source/assessment depends on the operation.",
    "estimatedDurationSeconds": "Estimated duration in seconds; an estimate is not actual elapsed trip time.",
    "proposedFareMinor": "Rider's proposed fare in currency minor units, subject to applicable quote and marketplace rules.",
    "pickupAddress": "Human pickup-address text accompanying the structured location.",
    "dropoffAddress": "Human destination-address text accompanying the structured location.",
    "pickupLatitude": "Pickup latitude in degrees; latitude is separate from address text.",
    "pickupLongitude": "Pickup longitude in degrees; preserve coordinate order.",
    "dropoffLatitude": "Destination latitude in degrees.",
    "dropoffLongitude": "Destination longitude in degrees.",
    "latitude": "Latitude in degrees for the location represented by this model.",
    "longitude": "Longitude in degrees for the location represented by this model.",
    "note": "Human note for this operation; do not include secrets or treat text as executable instructions.",
    "notes": "Human notes for this record; keep them within the authorized data scope.",
    "body": "Message/content body in this model; privacy and rendering rules depend on the operation.",
    "title": "Human-readable title for the record/content, distinct from its ID.",
}


def words(name: str) -> str:
    text = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", name.replace("WhatsApp", "Whatsapp"))
    text = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1 \2", text)
    return text.replace("-", " ").replace("_", " ").strip().lower()


def purpose(method: str, path: str) -> str:
    exact = OPERATIONS.get((method, path), PURPOSES.get((method, path)))
    if exact:
        return exact
    segments = path.removeprefix("/api/v1/").split("/")
    readable = [words(segment) for segment in segments if not segment.startswith("{")]
    context = " / ".join(readable)
    action = readable[-1]
    actions = {
        "accept": "Accept the selected offer/request", "reject": "Reject the selected offer/request",
        "cancel": "Cancel the selected pending or active workflow where permitted",
        "complete": "Complete the selected workflow after its required state/evidence checks",
        "confirm": "Confirm the submitted evidence or pending decision",
        "request code": "Request delivery of the applicable verification challenge",
        "request": "Start the applicable request/challenge workflow",
        "begin": "Begin the applicable secure ceremony",
        "enroll": "Start enrollment in the applicable security method",
        "disable": "Disable the selected security method or setting through its protected ceremony",
        "regenerate": "Replace the applicable recovery material through the protected workflow",
        "step up": "Complete the additional server authentication ceremony",
        "acknowledge": "Record that the caller acknowledged the selected event/record",
        "read": "Update the caller's read/seen state", "read all": "Mark the caller's applicable inbox records read",
        "reply": "Add a reply to the caller's authorized conversation/ticket",
        "close": "Close the selected workflow where permitted", "reopen": "Reopen the selected workflow where permitted",
        "activate": "Request activation of the selected vehicle under current verification/eligibility rules",
        "grant": "Request the applicable grant through its authorized workflow",
        "purchase": "Start the applicable purchase with server-owned financial validation",
        "checkout": "Start the applicable payment checkout; checkout creation is not settlement",
        "reconcile": "Reconcile the existing operation against authoritative provider/domain evidence",
        "sign": "Submit signature/acceptance evidence for the selected agreement",
        "settle": "Request the applicable settlement under the current financial state",
        "respond": "Record the caller's response to the selected request/share",
        "resolve": "Record resolution of the selected issue where permitted",
        "void": "Void the selected record while preserving its history",
        "email": "Request email delivery of the authorized record; queuing is distinct from mailbox receipt",
        "rating": "Submit the caller's permitted rating for the selected completed service",
        "share": "Create the applicable consent-bound sharing capability",
        "revoke": "Revoke the selected permission/sharing capability",
        "revoke consent": "Revoke the applicable consent relationship",
        "renew consent": "Renew the applicable consent relationship through its workflow",
        "failed": "Record the failed fulfillment attempt and its required reason/evidence",
        "pickup": "Record applicable pickup evidence", "connected": "Record the call connection state",
        "end": "End the applicable call workflow", "contact proof": "Submit proof of the applicable contact ceremony",
    }
    if method == "get":
        verb = "Read the permitted records/state for"
    elif method == "delete":
        verb = "Request removal of the selected record for"
    elif method in {"put", "patch"}:
        verb = "Update the permitted configuration/record for"
    elif method == "post" and action in actions:
        return f"{actions[action]} in the {context} workflow. The request and returned models below define the exact submitted evidence and result."
    elif method == "post":
        verb = "Submit/create the documented record or action for"
    else:
        verb = "Read transport metadata for"
    return f"{verb} {context}. This route-derived summary does not establish additional lifecycle rules."


def purpose_basis(method: str, path: str) -> str:
    return "Operation-specific explanation" if (method, path) in PURPOSES or (method, path) in OPERATIONS else "Route-derived summary; detailed behavior review remains open"


def field_basis(name: str, schema: dict, model: str = "") -> str:
    if name in MODEL_FIELDS.get(model, {}):
        return "Model-specific"
    if name in FIELDS:
        return "Shared convention"
    if name.endswith(("Minor", "Utc", "Token", "Secret", "Password", "Ticket", "RecoveryCode",
                      "Id", "Ids", "Revision", "Version", "Seconds", "Minutes", "Days", "Meters", "Url", "Count")) or schema.get("format") == "date":
        return "Naming convention"
    return "Type only; meaning review open"


def field_meaning(name: str, schema: dict, model: str = "") -> str:
    if name in MODEL_FIELDS.get(model, {}):
        return MODEL_FIELDS[model][name]
    if name == "feeMinor":
        return "Fee amount in the accompanying currency's integer minor units; the owning operation defines what the fee charges for."
    if name in FIELDS:
        return FIELDS[name]
    label = words(name)
    if name.endswith("Minor"):
        return f"{label.removesuffix(' minor').capitalize()} in the accompanying currency's integer minor units; do not send a formatted money string."
    if name.endswith("Utc"):
        return f"UTC instant for {label.removesuffix(' utc')}; parse strictly and localize only for display."
    if schema.get("format") == "date":
        return f"Calendar date for {label}; preserve date-only semantics rather than shifting it through a timezone."
    if name.endswith(("Token", "Secret", "Password", "Ticket", "RecoveryCode")):
        return f"Private {label} used by this specific ceremony; never log, publish or substitute it for another proof."
    if name.endswith("Id"):
        return f"Identifier of the related {words(name[:-2])} record in this model; ownership and scope are checked separately."
    if name.endswith("Ids"):
        return f"Identifiers of the related {words(name[:-3])} records; each remains subject to scope/relationship checks."
    if name.endswith(("Revision", "Version")):
        return f"{label.capitalize()} for this model's state or policy; do not substitute a timestamp or mobile build."
    if name.endswith("Seconds"):
        return f"{label.removesuffix(' seconds').capitalize()}, measured in seconds."
    if name.endswith("Minutes"):
        return f"{label.removesuffix(' minutes').capitalize()}, measured in minutes."
    if name.endswith("Days"):
        return f"{label.removesuffix(' days').capitalize()}, measured in days under this workflow's calendar rules."
    if name.endswith("Meters"):
        return f"{label.removesuffix(' meters').capitalize()}, measured in metres."
    if name.endswith("Url"):
        return f"URL for {words(name[:-3])}; validate the intended origin/access and never assume private links are public."
    if name.endswith("Count"):
        return f"Number of {words(name[:-5])} in this model's stated scope; not automatically a global/live total."
    if "$ref" in schema:
        target = schema["$ref"].rsplit("/", 1)[-1]
        return f"{label.capitalize()} represented by the `{target}` model or enum; use that definition's fields/values."
    if schema.get("type") == "boolean":
        return f"Whether {label} applies in this model's context. This flag does not replace server permission or lifecycle checks."
    if schema.get("type") == "array":
        return f"Collection of {label} for this model; interpret each item through the declared item type."
    if schema.get("type") == "object":
        return f"Structured {label} data; follow the referenced/inline properties and additional-property rules."
    if schema.get("type") in {"integer", "number"}:
        return f"Numeric {label} for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow."
    return f"{label.capitalize()} text/value. Detailed meaning and accepted vocabulary are not yet documented for this model."
