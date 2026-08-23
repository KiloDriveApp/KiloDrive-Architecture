# Runbook: security incident response

- **Owner:** Security incident response with affected service owners
- **Status:** Operational incident procedure
- **Last exercised:** Not yet recorded in this public repository
- **Related architecture:** [Threat boundaries](../security/threat-boundaries.md), [application security](../security/application-security.md), and [identity and access](../security/identity-and-access.md)

**Use when:** there is suspected account takeover, credential disclosure,
cross-tenant access, malicious upload, unauthorized financial change, signing-key
issue, provider compromise, or credible vulnerability report.

**Safety rule:** coordinate in restricted incident systems. Never place live
indicators, credentials, user documents, precise routes, or defensive details in
a public GitHub issue.

## Roles

- **Incident commander:** owns decisions and timeline.
- **Technical lead:** directs containment/eradication.
- **Evidence custodian:** preserves access-controlled evidence and provenance.
- **Communications/legal/privacy:** determines contractual, regulator, store,
  user, and law-enforcement obligations.
- **Service owner:** restores and verifies the affected capability.

One person may cover multiple roles in a small team, but name them explicitly.

## Severity guide

| Severity | Example | Initial posture |
| --- | --- | --- |
| SEV-1 | active signing/private credential misuse, cross-tenant disclosure, unauthorized money movement | immediate containment, executive/privacy involvement |
| SEV-2 | credible account takeover cluster or private-object exposure with bounded scope | urgent containment and scope analysis |
| SEV-3 | blocked exploit attempt or single-account issue with no confirmed exposure | investigate, targeted protection |
| SEV-4 | control weakness found internally with no exploitation evidence | track and remediate normally |

## 1. Triage

1. Validate the source without executing an exploit against production.
2. Record UTC/local timeline, reporter, affected capability/environment,
   correlation IDs, safe actor/resource surrogates, and observed impact.
3. Distinguish an application defect from a provider/edge/security-control alert.
4. Assign severity and owners; open restricted communication.
5. Protect the reporter and user data. Ask only for minimum reproduction detail.

Do not request passwords, OTPs, refresh/access tokens, biometric data, full bank
details, identity documents, or malware samples over ordinary email/chat.

## 2. Contain

Choose the narrowest action that stops harm:

- revoke affected refresh families/sessions and increment token version;
- disable a social/passkey credential pending recovery;
- rotate a disclosed provider/JWT credential;
- remove one node or provider route from service;
- disable a specific money/document/country feature;
- quarantine an object/prefix;
- force a compromised administrator account offline; or
- block an exploit pattern at edge and application boundaries.

Do not destroy evidence, delete audit/outbox rows, or restore an entire database
as first response. If JWT signing material is compromised, assume any token signed
by it may be forged: rotate, remove the compromised public key after policy-safe
transition, revoke sessions/token versions as needed, and review issuance/audit.

## 3. Preserve evidence

Capture immutable or access-controlled copies of:

- relevant security/domain audit records;
- sanitized application logs/traces and deployment version/hash;
- cloud audit/IAM/provider events;
- database metadata and affected rows through reviewed read-only queries;
- WAF/proxy request evidence after redaction; and
- object metadata/scan result without casually downloading content.

Record who collected what, when, from where, and the hash. Avoid broad exports
that increase exposure. Keep clocks/timezones explicit.

## 4. Determine scope and root cause

Ask:

- Which identities, tenants, countries, resources, and time range are affected?
- Was data read, changed, deleted, or merely reachable?
- Did the attacker obtain persistence (refresh family, passkey/social link,
  provider key, admin role)?
- Were logs or backups also exposed?
- Did money or entitlement state change, and do journals reconcile?
- Which preventive and detective controls succeeded or failed?

Never infer scope solely from absence of application logs. A logging gap is not
evidence of no access.

## 5. Eradicate

- Patch the ownership, validation, state, redaction, dependency, or configuration
  flaw.
- Rotate/revoke affected secrets and remove old trust.
- Remove unauthorized sessions, credentials, roles, objects, or persistence.
- Repair data through supported lifecycle/accounting operations where possible.
- Add regression tests for the exact attack and adjacent variants.
- Scan source history/artifacts if a secret was ever committed or printed.

## 6. Recover

1. Deploy to a controlled environment and run security/contract tests.
2. Restore production capability gradually.
3. Reconcile wallets, providers, objects, sessions, outbox, and schema as relevant.
4. Increase targeted monitoring for recurrence.
5. Confirm the user-facing recovery path works and does not reveal investigation
   details.

Rollback means restoring the last known secure compatible artifact or disabling
the narrow capability—not returning to a known vulnerable build.

## 7. Notify

Legal/privacy leadership determines notification content and timing from verified
facts and jurisdictional obligations. Separate preliminary operational updates
from formal breach conclusions. App stores, processors, insurers, regulators,
affected users, and law enforcement may each have different requirements.

Do not speculate, minimize, or overstate. Say what happened, what data/action was
in scope, what was done, and what the recipient should do.

## 8. Verify and close

- Exploit/regression tests now fail safely.
- All compromised credentials and sessions are revoked.
- IAM/object/tenant boundaries are restored.
- Wallet and provider reconciliation is clean.
- No secret/PII leaked into incident alerts or public records.
- Monitoring detects a safe synthetic recurrence.
- Required notifications and evidence retention are complete.
- Owners/dates exist for every corrective action.

Run a blameless review: focus on why the system allowed the path, not who made the
last edit. Update threat models, runbooks, tests, onboarding, and alerting. Repeat
tabletop exercises for crash, assault, route deviation, lost child, account
compromise, malicious upload, and false alarm scenarios.
