# Runbook: Service or Failure Mode

- **Owner:** Named team or operational role
- **Status:** Implemented / Configurable / Operational policy / Planned
- **Last exercised:** YYYY-MM-DD or “not yet exercised”
- **Related architecture:** Link to the relevant chapter and ADR

## Purpose and safety boundary

Explain what this runbook restores and what it must never compromise.

## Trigger and customer symptoms

List alerts, health states, and user-visible symptoms. Do not equate one alert
with a root cause.

## Preconditions

State required authorization, recovery evidence, backups, approvals, and
whether financial/security operations must be paused.

## Diagnose

Provide ordered read-only checks from authoritative state outward. Include what
each result means.

## Contain

List the smallest reversible controls and their side effects.

## Recover

Describe supported replay, rollback, failover, or compensation. Address
idempotency and unknown external outcomes.

## Verify

Include health, metrics, durable invariants, backlog convergence, and a
production-safe user journey.

## Rollback or abort criteria

Say when to stop, who decides, and how to return to the previous safe state.

## Evidence and communication

List safe evidence, stakeholder updates, and prohibited sensitive content.

## Follow-up

Name the regression test, automation, monitoring, and documentation updates
required before closure.
