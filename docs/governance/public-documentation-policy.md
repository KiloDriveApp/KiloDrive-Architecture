# Public Documentation Safety Policy

Public architecture documentation should be useful enough to teach and review,
without becoming an access guide or a second store of sensitive operational
data. This policy explains that line.

## Safe to publish

- component responsibilities and data-flow/state diagrams;
- technology families and public provider names;
- high-level security controls and failure behavior;
- public API conventions and sanitized example contracts;
- generic runbook decision flow;
- direct dependency and licence summaries;
- synthetic identifiers, addresses, and payloads that are clearly fictional;
- design tradeoffs and lessons that do not expose an active weakness; and
- capability status: implemented, configurable, operational policy, or planned.

## Keep restricted

- credentials, keys, tokens, OTPs, hashes usable as authenticators, recovery
  codes, cookies, or signed URLs;
- cloud account IDs, private resource names, complete ARNs, internal addresses,
  database connection strings, or filesystem layouts that reveal deployment;
- customer, employee, fixture, or provider-destination personal data;
- exact firewall/security-group rules or defensive thresholds that would help
  bypass controls;
- console screenshots or logs containing configuration or identifiers;
- raw request/response bodies from production;
- private documents, call media, chat content, or precise trip locations;
- unannounced incidents, vulnerabilities, or legal assessments; and
- operational commands that mutate named production resources.

## The “could this be combined?” test

A single fact may look harmless while several facts together reveal too much.
Before publishing, ask whether the text can be combined with another public
source to identify an account, host, bucket, user, route, or defensive control.

Prefer role and purpose over names. “Private object storage with a quarantine
prefix” teaches the architecture. The exact bucket and prefix do not.

## Safe examples

Use obviously synthetic values:

```text
Correlation ID: 00000000-0000-7000-8000-000000000001
Country: Example country (EX)
Currency: XYZ
Provider request ID: provider-example-001
```

Do not create examples that resemble live access keys, bearer tokens, phone
numbers, emails, or signed URLs. Secret scanners cannot reliably understand
author intent, and readers may copy examples into real configuration.

## Claims and status

Security language must be specific and supportable. Say “the API validates an
asymmetrically signed access token and publishes public verification keys”
instead of “unhackable enterprise-grade security.”

Do not state that an optional provider, scanner, egress service, canary, or
country operation is active merely because code exists. Label it configurable
until deployment evidence proves otherwise.

## Review

Automated link/secret scans are necessary but not sufficient. A reviewer
compares claims with code, schema, tests, and approved policy. Security/privacy
review is required for identity, money, location, communications, documents,
retention, provider, and incident material.

## If restricted information is committed

Treat the event as a security incident:

1. restrict public access when appropriate;
2. preserve evidence without spreading the value further;
3. revoke and rotate exposed credentials or links;
4. assess logs, forks, caches, and package artifacts;
5. coordinate history rewriting when required; and
6. document the root cause and prevention control.

Deleting the latest commit alone does not remove a secret from Git history.
