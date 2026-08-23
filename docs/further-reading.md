# Further Reading from Primary Sources

KiloDrive's documentation explains how this particular platform joins several
technologies into one operating model. It should not replace the standards and
vendor documentation that define those technologies. Use this page when a term
or design choice is new to you, and return to the KiloDrive chapter afterward
to see how the general rule applies here.

Links on this page intentionally favor standards bodies and official project or
vendor documentation. Blog posts can be useful, but they may omit constraints,
describe an older release, or present one team's preference as a universal
rule.

## Identifiers and data

- [RFC 9562: UUIDs](https://www.rfc-editor.org/info/rfc9562/) defines the UUID
  layouts, including UUIDv7. Read sections 5.7 and 6 before reasoning about
  ordering, monotonicity, or database locality. A UUIDv7 timestamp is useful
  for index behavior; it is not authorization evidence and should not be used
  as the authoritative business creation time.
- [MySQL 8 spatial data types](https://dev.mysql.com/doc/refman/8.0/en/spatial-types.html)
  introduces geometry types, spatial reference systems, spatial functions, and
  indexes. Pay attention to SRID, axis order, validity, and which predicates can
  use an index. A spatial column alone does not make a query spatially correct
  or fast.
- [MySQL 8 reference manual](https://dev.mysql.com/doc/refman/8.0/en/) is the
  primary reference for transaction isolation, InnoDB locking, indexes,
  collations, generated columns, JSON, and `INFORMATION_SCHEMA`. Confirm the
  documentation for the deployed server family before copying syntax from a
  newer release.

## Observability and operations

- [OpenTelemetry documentation](https://opentelemetry.io/docs/) explains the
  APIs, SDKs, semantic conventions, collector, and signals. OpenTelemetry
  transports and describes telemetry; it is not itself the long-term
  observability backend.
- [OpenTelemetry concepts](https://opentelemetry.io/docs/concepts/) is a good
  starting point for traces, spans, metrics, logs, baggage, resources, and
  context propagation. In KiloDrive, correlation IDs are safe operational
  handles, while baggage is kept deliberately small and free of personal data.
- [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html)
  provides a structured way to examine operational excellence, security,
  reliability, performance efficiency, cost optimization, and sustainability.
  Use it as a review conversation, not as a badge or substitute for workload
  tests and recovery exercises.

## Mobile quality and accessibility

- [Flutter accessibility guidance](https://docs.flutter.dev/ui/accessibility)
  covers semantics, text scaling, contrast, focus, and minimum interaction
  sizes. Test these behaviors on physical devices with TalkBack and VoiceOver;
  a static widget tree cannot prove the complete experience.
- [Flutter DevTools performance view](https://docs.flutter.dev/tools/devtools/performance)
  explains frame analysis, rebuild/layout/paint events, and profile-mode
  measurement. Debug-mode timing is not a release-performance baseline.

## Supply-chain evidence

- [CycloneDX specification overview](https://cyclonedx.org/specification/overview/)
  describes machine-readable bills of materials and their media types. A valid
  SBOM is an inventory, not proof that every component is safe, licensed for a
  particular use, or present in the exact signed artifact.
- The public
  [KiloDrive CycloneDX baseline](third-party/kilodrive-public-direct.cdx.json)
  demonstrates a deliberately limited direct-dependency inventory. Release
  evidence must add resolved transitive and native components and bind them to
  signed artifact hashes.

## A useful way to study

For each source, answer four questions in your own words:

1. What guarantee does the standard or service actually provide?
2. What does it explicitly leave to the application?
3. What new failure mode appears when the dependency is slow, unavailable, or
   returns an unknown outcome?
4. Which KiloDrive invariant, metric, test, or runbook detects that failure?

This habit is more valuable than memorizing API names. Mature engineering
comes from knowing where a guarantee begins, where it ends, and what evidence
would show that an assumption is wrong.
