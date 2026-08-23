# AWS identity and access management

IAM is where a small configuration mistake can become either a complete outage
or an unnecessarily large security boundary. KiloDrive's rule is simple: one
workload should receive one capability-shaped permission set for one environment.
It should not inherit every permission the deployment account happens to have.

## People, workloads, and deployment automation are different actors

Keep these identities separate:

| Actor | Typical need | Must not inherit |
| --- | --- | --- |
| API runtime | publish dispatch events, send configured messages, access approved private prefixes, emit telemetry | deployment, account administration, broad object inspection |
| Dispatch consumer | receive/delete one queue and read domain state | event-bus administration or unrelated queues |
| LiveKit egress | write recordings to one private prefix | list/read all documents or delete recordings |
| Retention worker | inspect/delete expired recording objects under policy | start calls or read unrelated uploads |
| Deployment automation | replace signed artifacts and restart services | customer content or signing private key export |
| Observability collector | put approved log/metric/trace records | provider messaging or database administration |
| Human operator | narrowly scoped diagnosis and recovery | permanent runtime keys or routine administrator access |
| Break-glass operator | time-bounded emergency action | standing daily use |

## Prefer short-lived workload identity

On AWS compute, use an instance/task role or an assumed role through the standard
credential chain. Static keys create extra work: distribution, encryption,
rotation, inventory, leak response, and ownership transfer. They also tempt teams
to paste secrets into application settings while debugging.

When a third-party component needs AWS access, prefer an assumable role with a
purpose-specific external ID and trust policy. If a static credential is truly
unavoidable, give it the same narrow policy, store it in a protected secret
source, set an owner and expiry, and rotate it under a tested procedure.

## Designing a least-privilege policy

Start from an observed operation, not a broad managed policy:

1. Identify the exact SDK call, region, and resource type.
2. Read the service authorization reference to learn which actions support
   resource-level permissions and condition keys.
3. Grant only the actions required for the happy path and necessary
   reconciliation path.
4. Restrict resource ARN/prefix, source identity, encryption context, and source
   service where supported.
5. Add explicit guardrails for environment and public exposure.
6. Test the intended action and at least one action that should remain denied.
7. Record an owner, review date, health check, rollback, and incident runbook.

For S3, distinguish object actions from bucket-list actions and constrain list
permissions to a prefix. For KMS, remember that both IAM and key policy can
participate in authorization. For EventBridge-to-SQS, the queue resource policy
must trust the specific event rule. For SES or messaging, a successful API call
may still be blocked by sandbox, destination, origination, country, or protect
configuration rules.

## Understanding `AccessDenied`

An access-denied response proves that authentication reached AWS; it does not
mean the key is “bad.” Work through this order:

1. Determine the caller identity using a safe identity query. Do not print the
   secret, session token, or full application configuration.
2. Confirm account and region are the ones the resource belongs to.
3. Compare the exact action and resource in the exception with the identity
   policy.
4. Inspect resource policies, permission boundaries, session policies, service
   control policies, and explicit denies.
5. Check whether the application is unexpectedly choosing a static key before
   the instance role in its credential chain.
6. Make the smallest policy correction and test through a dedicated canary.

A hard-learned pitfall was responding to an EventBridge `PutEvents` denial as if
it were a connectivity problem. The API was authenticated and AWS was reachable;
the identity simply did not have the event-bus permission. Broadening the user to
administrator would have hidden the diagnosis and enlarged the blast radius.

## Rotation and revocation

Every credential needs a no-drama exit path:

- Use overlapping credentials only for the shortest verified transition.
- Deploy the new identity, observe canaries, then revoke the old one.
- Revoke immediately after accidental disclosure; do not wait to determine
  whether someone used it.
- Search source history, build artifacts, CI logs, command history, and tickets
  for copies, without reproducing the secret in the incident record.
- Review provider records and cloud audit trails for anomalous actions.
- Validate that the workload continues through its normal role after rotation.

## Human access

Require MFA, short sessions, named accounts, and role assumption. Use approval
for destructive data and security operations. Do not share an “operations” IAM
user across engineers; it destroys attribution. Break-glass access should be
sealed, monitored, time limited, and exercised before an emergency.

## Review checklist

- [ ] The policy has an accountable owner and review date.
- [ ] The principal is dedicated to one workload and environment.
- [ ] Static keys are absent or have a documented, time-bounded exception.
- [ ] Resources and prefixes are constrained where the service supports it.
- [ ] Trust/resource/key policies are reviewed along with identity policy.
- [ ] A non-user canary verifies the allowed path.
- [ ] A negative test verifies an unrelated resource/action is denied.
- [ ] Logs and traces never contain credentials or destination values.
- [ ] Rotation, revocation, and rollback have been rehearsed.

Exact identities, resource names, account numbers, and policies belong in the
restricted deployment repository, not this public guide.
