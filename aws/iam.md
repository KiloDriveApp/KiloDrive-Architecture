# AWS Identity and Access Management

## Principles

- Prefer workload identity over static access keys.
- Give each application/provider adapter its own role or policy boundary.
- Scope actions to the smallest feasible resources and prefixes.
- Separate runtime, deployment, monitoring, backup, and break-glass duties.
- Require MFA and short sessions for human administration.
- Record configuration changes through AWS audit services and KiloDrive release
  evidence.

## Workload separation

The API runtime may need narrowly scoped permissions for messaging, private
objects, dispatch publication/consumption, telemetry, and secret retrieval.
LiveKit egress receives write-only access to its recording prefix; a separate
retention role can inspect/delete according to policy. Deployment automation may
replace binaries but does not need access to customer object contents.

## Credential lifecycle

1. Create a role/policy for one capability.
2. Validate it with a non-user canary destination or disposable object.
3. Enable production use only after sanitized evidence passes.
4. Monitor denied actions and unusual use.
5. Rotate or revoke immediately after exposure or ownership change.

Policy documents, role names, account IDs, and resource ARNs are intentionally
excluded from this public repository.
