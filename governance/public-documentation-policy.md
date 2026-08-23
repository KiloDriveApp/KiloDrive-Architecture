# Public Documentation Safety Policy

## Allowed

- component responsibilities and data-flow diagrams;
- technology families and public provider names;
- high-level security controls and failure behavior;
- public API conventions without private partner details;
- generic runbook decision flow; and
- direct dependency/third-party license summaries.

## Prohibited

- credentials, keys, tokens, hashes used as authenticators, or signed URLs;
- cloud account IDs, resource ARNs/names, private bucket/prefix names;
- internal/private IPs, exact host paths, database connection strings;
- customer, employee, fixture, or provider-destination personal data;
- exact firewall/security-group rules or exploitable defensive thresholds;
- console screenshots containing configuration or identifiers; and
- claims that optional/planned controls are deployed without evidence.

## Review

Every change receives architecture-owner and security/privacy review. Automated
secret and link scans are necessary but not sufficient. A reviewer compares the
text with the implemented code and labels it implemented, configurable,
operational policy, or planned.

If restricted information is committed, remove public access if needed, revoke
and rotate exposed material, preserve evidence, rewrite history only as part of a
coordinated response, and notify affected owners.
