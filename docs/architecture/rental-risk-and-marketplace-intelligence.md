# Rental Risk Exchange and marketplace intelligence

These two programmes help a rental provider make a documented human decision
and help operators understand marketplace conditions. Neither is a shortcut to
an automatic denial, a new fare, an account penalty, or a financial posting.
They have different data, legal and activation boundaries. This chapter
describes reviewed source design, not a claim of country activation or measured
commercial performance. See the [current baseline](../current-baseline.md).

## Rental Risk Exchange

The Exchange is a restricted, country-scoped workflow for participating rental
organizations. It separates a private report from any later shareable,
reviewed derivative. A provider may record an incident tied to an actual
rental or an independently verified external relationship. Evidence, claimed
amounts, identity and relationship assertions remain private during intake.
An authorized reviewer checks provenance, reason, contradictory information
and the subject's rights before approving any limited publication. A report
being filed is not a finding of guilt.

| Step | Meaning | Boundary |
| --- | --- | --- |
| Participate | An organization accepts the applicable country agreement and is independently reviewed. | A company account alone does not enable sharing. |
| Report | A scoped incident and original evidence are submitted. | Drafts and raw attachments are private; a booking reference alone does not prove a relationship. |
| Review | A permitted operator assesses identity, relationship, evidence, reason and response. | The reporter cannot approve their own publication. |
| Publish | An immutable, redacted version becomes shareable under the active policy. | Original documents, contact data and unrelated facts do not become a public blacklist. |
| Screen | An eligible provider checks a particular rental, purpose, subject and allowance. | A tracking or person identifier alone does not authorize a read; a no-report result is not proof of safety. |
| Decide | The provider records a human rental decision. | The Exchange does not cancel a booking, block all rentals or change price on its own. |
| Correct or appeal | A subject can access, dispute and seek a corrected outcome. | Revocation of the old version precedes correction notices; delivery and acknowledgement are separate facts. |

The system retains immutable provenance for the reviewed derivative, exact
publication version and authorized disclosures. Current permission and policy
are rechecked when a previously issued result is opened. Correction and
retention workflows account for open disputes, holds, outstanding disclosures
and other retained references. Private evidence has its own protected viewer
and erasure path. An unsuccessful notification cannot restore a revoked
publication. Cross-border sharing is unsupported by this design.

Exchange access is **not** a Service Provider Silver or Gold benefit. Its
separate commercial design is a fixed-period, organization-benefiting wallet
purchase paid from the rental owner's personal wallet. The offer and country
terms are versioned. The quote states beneficiary, payer, currency, minor-unit
price, period and allowances. A purchase must atomically record the debit,
payment, entitlement and ledger evidence; an interrupted response is resolved
through the original receipt and independent current-state read. It is not a
recurring native-store subscription. New wallet sales are disabled by default
and still require approved country terms, prices and channel policy. No public
page should imply that they are active merely because checkout code exists.

The source programme explicitly retains activation dependencies: approved
country policy and processing basis, published agreement, retention/dispute
rules, precise channel authorization, and real provider/device verification.
The Exchange must not be described as an active universal background-check
service or a definitive statement about a person's safety. The subject's
rights and applicable law govern any launch decision.

## Marketplace and product intelligence

Committed trips, deliveries, rentals, payments and membership periods remain
the source of truth for completed work. Optional product-interaction
observations describe **attempts**: a tap or form step does not create a trip,
charge, entitlement or approval. Central identity owns the person's current
analytics-consent decision; a country cell keeps allowed, subject-bound
observations. Logout and account switch discard another person's queued
device observations. Withdrawal stops new optional ingestion without deleting
financial or safety evidence that must be retained for a separate purpose.

The reporting layer uses bounded, replayable projections with explicit source
watermarks, metric definitions, population provenance and quality status.
Presentations must distinguish observed, estimated, forecast, recommendation
and confirmed outcome. They must also distinguish a measured zero from
unavailable, stale, incomplete, privacy-suppressed and insufficient evidence.
Missing provider cost cannot become zero contribution cost. Synthetic or
unclassified accounts cannot silently become organic growth.

The current source includes diagnostic marketplace metrics, service-funnel
foundations, an internal event calendar, heuristic quote guidance and
shadow-only forecasting work. A recommendation cannot write a wallet entry,
alter an entitlement, change a booking allocation, suspend a provider or
increase a fare without the ordinary authorized domain workflow. External
weather, flight, cruise or other feeds need reviewed provenance, licence,
coverage, cost and fallback before activation. Forecast code and a historical
backtest alone do not prove live predictive accuracy or marketplace uplift.

Privacy suppression happens before a result leaves the API. Flexible
filtering, adjacent-window differencing, precise location and small cohorts
need particular care. Ordinary product analytics excludes passwords, codes,
tokens, private documents, chat/call content and payment details. A coarse
marketplace view cannot infer a person's presence at a sensitive venue.
Security traces are not a growth-data source.

## Administrative and operational view

The separate [System Admin app](system-admin-mobile-app.md) presents scoped
Exchange review, rights, policy, commercial administration and operational
queues. Its intelligence views show metric definitions, provenance and
freshness so an operator can tell a missing source from a real zero. Both
families require their own current country, tenant and capability checks.
Administrative access to a private incident is not an ordinary provider's
permission to screen, and visibility into a metric is not authority to mutate
the underlying marketplace.

Bounded queries, projection checkpoints, outbox recovery and provider health
matter under load. The existence of these controls does not establish a
50,000-active-user capacity envelope. That needs sustained, representative
traffic with measured latency, queue lag, saturation, privacy suppression and
recovery. See [scaling and capacity](scaling-and-capacity.md) and
[testing and verification](../quality/testing-and-verification.md).
