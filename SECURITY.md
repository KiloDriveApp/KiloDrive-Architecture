# Security and Vulnerability Reporting

KiloDrive welcomes responsible reports that help protect riders, drivers,
rental organizations, administrators, and the public. Please do not disclose a
suspected vulnerability, credential, private endpoint, customer record, or
working exploit in a public GitHub issue.

For the technical security design, read the
[security control model](docs/security/security-control-model.md),
[OWASP API Security Top 10 mapping](docs/security/owasp-api-top-10-2023.md) and
[threat boundaries](docs/security/threat-boundaries.md). This file explains
reporting and research boundaries; it is not a security certification or an
authorization to conduct testing.

## Report privately

Email [support@kilodrive.com](mailto:support@kilodrive.com) with a subject that
begins `Security report`.
Use that private channel for suspected application vulnerabilities, exposed
secrets and sensitive repository mistakes. Do not use a public issue or pull
request for initial disclosure. An ordinary product problem without suspected
security impact can use [Contact KiloDrive](https://kilodrive.com/contact).

Include only the information needed to triage safely:

- affected surface: consumer app, System Admin app, API, Portal, Website or this
  documentation repository;
- release/build number or source commit when known, plus platform and distribution
  channel where relevant; report an unknown version as unknown;
- observed behavior and expected safe behavior;
- impact you believe is possible;
- safe reproduction steps using your own account or synthetic data;
- approximate UTC time, or local time with its timezone, and a sanitized
  correlation ID if available;
- affected country/workspace and role category without personal identifiers;
- whether the observation came from source inspection, a test environment or
  ordinary use of a deployed application; and
- a contact method for coordinated follow-up.

Do not email passwords, access/refresh tokens, OTPs, private keys, full payment
details, identity documents, call recordings, precise trip histories, or data
belonging to another user. Also remove installation credentials, push tokens,
presigned URLs and sensitive query strings from screenshots, HAR files, crash
reports and copied commands. If restricted evidence is essential, first ask
for an approved secure transfer method. A correlation ID can help locate private
server evidence without sending the underlying payload.

### Suggested report structure

```text
Subject: Security report - brief component and issue summary
Affected surface and version:
Source or environment observed:
Country/workspace and role category:
Observation time and timezone:
Expected behavior:
Observed behavior:
Minimal authorized reproduction:
Potential impact:
Sanitized correlation or documentation reference:
What testing was stopped:
Follow-up contact:
```

Distinguish observed facts from suspected impact. A theoretical source concern
can be reported without trying to reproduce it in production. An OWASP/CWE
classification is helpful if known, but it is not required.

## Scope and version information

| Surface | Examples of relevant concerns |
| --- | --- |
| Consumer app and account API | Login/recovery, social linking, session reuse, unauthorized account or trip access |
| System Admin app and privileged API | Consumer-to-admin escalation, missing capability checks, wrong-country access, unauthorized document viewing or approval |
| Device and notification workflows | Admission bypass, installation/session confusion, cross-account or cross-app push delivery |
| Financial and membership workflows | Unauthorized value changes, duplicate settlement, unsafe unknown-outcome retry, incorrect provider/account binding |
| Portal and Website | Authentication, authorization, browser protections, private-data exposure and unsafe trusted-content handling |
| Integration boundaries | Unsafe outbound destinations, forged/replayed provider evidence, exposed provider credentials |
| This repository and its tooling | Accidental sensitive publication, unsafe build tooling, misleading security claims with actionable impact |

This is a reporting scope, not a grant of testing access. The separate System
Admin app is restricted; a consumer account, public contract or documented
route does not grant administrative access. Third-party providers, cloud and
store accounts remain outside any testing authorization unless expressly named
in a separate written scope.

The [documentation baseline](docs/current-baseline.md) identifies reviewed
source, not a list of supported production versions or a patch-service promise.
Build-numbered chapters are historical evidence. Include the version actually
observed; a relevant report about an older or unknown version can still be
submitted for triage. Deployment and release evidence determine applicability.

## Testing boundaries

Good-faith research must remain controlled. Do not:

- access, alter, download, or retain data that is not yours;
- impersonate another user or contact KiloDrive users;
- perform denial of service, uncontrolled load, or resource-exhaustion tests;
- interfere with active rides, deliveries, calls, safety cases, or payments;
- send unsolicited SMS, email, WhatsApp, push, or voice messages;
- upload malware to production or evade document quarantine;
- attempt social engineering, physical intrusion, or employee targeting;
- publish a vulnerability before coordinated review; or
- use a discovered weakness to move money or establish persistence.

Use dedicated non-production fixtures when KiloDrive has authorized them. Stop
testing as soon as you confirm the minimum evidence needed to explain the issue.

If a request unexpectedly exposes another person's data, stop and report the
minimum sanitized observation without enumerating more records. If a payment
or membership action has an uncertain outcome, do not repeat it under a new
operation key to investigate. Preserve the safe reference and let authorized
operators reconcile it. Synthetic documents and test accounts are not real
identity evidence and must not be used to gain real-world eligibility.

## What happens after a report

KiloDrive will acknowledge and triage the report, preserve relevant evidence,
assign an owner and severity, and assess security, privacy, safety, financial,
and availability impact. Remediation may include containment, credential
rotation, data correction through supported workflows, regression tests,
monitoring, and coordinated notification or disclosure.

Response time depends on impact and report quality. Duplicate or already-known
reports may be closed with limited detail when sharing more would expose an
active defensive control.

The intended sequence is receipt and clarification, impact assessment,
containment where necessary, remediation with regression evidence, and
coordinated communication. A fix may require configuration, provider action or
a mobile release in addition to a code change. Maintain separate evidence for
what was corrected in source and what was verified in the affected deployment.

This policy does not announce a bounty, fixed response deadline, guaranteed
reward, legal safe harbor or blanket permission to test. Coordinate any
disclosure using the private reporting channel. Public remediation notes should
omit secrets, affected people and details that would compromise an unresolved
defensive boundary.

## Public repository findings

For ordinary documentation defects—broken links, grammar, an outdated package
reference without suspected vulnerability, or an inaccurate non-sensitive
diagram—a public issue or pull request is appropriate. Cite the page, section
and supporting non-sensitive evidence; follow [CONTRIBUTING.md](CONTRIBUTING.md).

If this repository accidentally contains restricted information, do not quote
it in an issue. Report it privately. Removing the latest line is not enough for
a credential in Git history; KiloDrive will coordinate access restriction,
rotation, cache/fork assessment, and history repair.

Security/privacy and release owners should retain the affected commit/artifact,
impact scope, containment, correction and verification evidence in restricted
records. A public documentation check cannot certify the incident is resolved.

## No production access is granted

Publication of architecture and runbook principles does not grant permission
to test KiloDrive production, third-party providers, cloud resources, mobile
store accounts, or users. Obtain explicit written authorization for any testing
beyond normal use of your own account.

Related documents: [security posture](docs/security/README.md),
[administrative data handling](docs/security/admin-data-handling.md),
[security incident runbook](docs/runbooks/security-incident.md) and
[publication notice](NOTICE.md).
