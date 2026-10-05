# Quality engineering

Quality in KiloDrive means proving the promises that matter: one assignment has
one winner, money reconciles, private data stays private, clients converge after
disconnects, and operators can recover without inventing state.

- [Testing and verification](testing-and-verification.md) defines the test
  taxonomy, risk-based expectations, invariant traceability, authorization and
  lifecycle matrices, concurrency/failure testing, mobile pyramid, and release
  evidence policy.
- [Documentation integrity review](documentation-audit-2026-10-03.md) records
  corrected publication defects, regression checks and remaining explanation debt.
- [Public quality assurance and concurrency guarantees](public-assurance-and-concurrency.md)
  publishes the public-safe test inventory, outcome-oriented coverage model,
  concurrency guarantees, and the boundary between architecture and measured
  capacity.
- [Capability status](../architecture/capability-status.md) records which
  evidence families support each public architecture claim.
- [Mobile security verification](mobile-security-verification.md) maps the
  consumer and separate Admin app to source, API, signed-device and provider
  evidence levels without treating a mock as native certification.
- [Native platform certification matrix](native-platform-certification-matrix.md)
  records applicable iOS/Android lifecycle/provider scenarios for the latest
  source observation, while leaving unexecuted signed-artifact rows untested.
- [Runbooks](../runbooks/README.md) explain how approved releases and recovery
  exercises turn those tests into operational confidence.

Public documents describe the philosophy and safe evidence categories. Exact
private test revisions, raw results, fixture credentials, provider destinations, and
security-sensitive test details remain in restricted release evidence.
