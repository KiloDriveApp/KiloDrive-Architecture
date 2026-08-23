# Security and Vulnerability Reporting

KiloDrive welcomes responsible reports that help protect riders, drivers,
rental organizations, administrators, and the public. Please do not disclose a
suspected vulnerability, credential, private endpoint, customer record, or
working exploit in a public GitHub issue.

## Report privately

Email [support@kilodrive.com](mailto:support@kilodrive.com) with a subject that
begins `Security report`.
Include only the information needed to triage safely:

- affected product and high-level component;
- observed behavior and expected safe behavior;
- impact you believe is possible;
- safe reproduction steps using your own account or synthetic data;
- approximate UTC time and a sanitized correlation ID, if available;
- device/browser and released application version; and
- a contact method for coordinated follow-up.

Do not email passwords, access/refresh tokens, OTPs, private keys, full payment
details, identity documents, call recordings, precise trip histories, or data
belonging to another user. If sensitive evidence is essential, first ask for an
approved secure transfer method.

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

## What happens after a report

KiloDrive will acknowledge and triage the report, preserve relevant evidence,
assign an owner and severity, and assess security, privacy, safety, financial,
and availability impact. Remediation may include containment, credential
rotation, data correction through supported workflows, regression tests,
monitoring, and coordinated notification or disclosure.

Response time depends on impact and report quality. Duplicate or already-known
reports may be closed with limited detail when sharing more would expose an
active defensive control.

## Public repository findings

For ordinary documentation defects—broken links, grammar, an outdated package
version, or an inaccurate non-sensitive diagram—a public issue or pull request
is appropriate.

If this repository accidentally contains restricted information, do not quote
it in an issue. Report it privately. Removing the latest line is not enough for
a credential in Git history; KiloDrive will coordinate access restriction,
rotation, cache/fork assessment, and history repair.

## No production access is granted

Publication of architecture and runbook principles does not grant permission
to test KiloDrive production, third-party providers, cloud resources, mobile
store accounts, or users. Obtain explicit written authorization for any testing
beyond normal use of your own account.
