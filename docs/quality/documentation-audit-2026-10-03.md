# Documentation integrity review: 2026-10-03

[Current baseline](../current-baseline.md) · [Contribution guide](../../CONTRIBUTING.md)

This review improves the public Architecture repository. It does not change
the applications, production data, deployment policy or store submissions.
The inspected product revision and versions are in the current baseline.

## Corrected defects and omissions

| Finding | Correction | Regression protection |
| --- | --- | --- |
| Export sanitization deleted real DTO fields named `description` | Restored all 23 omitted fields; the subset now contains 5,012 properties | Context-aware OpenAPI filtering, nested keyword-name fixtures and independent source wire-shape comparison |
| A hypothetical `default` response could be removed as if it were a schema default value | Preserve response-map keys while removing unreviewed schema default metadata | Default-response regression test |
| A route outside the admin prefix could declare `TenantAdmin` without triggering the privileged-role guard | Reject declared tenant-administrator authority as well as other administrator roles | Role-boundary tests; no previously published route had this role |
| Response tables flattened arrays into a model name | Show arrays, maps, composition, nullability and binary response types | Array/binary rendering fixtures |
| Parameter constraints and inline-body requiredness were difficult to discover | Include their schema constraints and required markers beside the fields | Parameter-boundary rendering test |
| Shared field names produced misleading descriptions | Add model-specific explanations for HTTP problem status, registration role, push binding, membership, store products, wallet and readiness | Context-sensitive meaning tests |
| Template-generated explanations looked equivalent to individually reviewed semantics | Label explanation basis on operations and fields; publish counts and an actionable review queue | Deterministic coverage generation |
| Long reference pages lacked useful local navigation | Add per-domain operation contents, alphabetical model contents, a single operation finder and reverse model-usage data | Regeneration and fragment-link checks |
| Relative-link checks ignored heading fragments and could normalize away wrong case on Windows | Validate local anchors and lexical filename case | Broken-anchor, duplicate-heading, fence and filename-case tests |
| Documentation used several incompatible meanings of “current” | Add a central baseline and mark historical source/test checkpoints as historical | Source manifest remains the version authority |
| FX chapters required independent approval unconditionally | Describe optional domain policy and the source default; retain audit, authorization and concurrency rules | Cross-check against the reviewed approval options and example configuration |
| Admin chapter described implemented document-review features as absent | Update the source-level driver/identity review and membership-center description | Review of current repositories/workspaces; no device result inferred |
| Dependency baseline described build 144 and omitted the Admin app | Regenerate from committed metadata for both apps and .NET, retaining package owners and differing versions | Ownership, provenance and reproducible readable-inventory checks |
| Source-controlled plugin forks were labelled as upstream Pub packages and an explicit override was omitted | Give reviewed forks distinct coordinates and include explicit overrides; reject unreviewed non-hosted dependencies | Fork-identity, overlap/version and non-hosted-origin tests |
| Native-package chapter described both apps as remote-notification-only | Correct the consumer's declared background location mode and distinguish it from the Admin declaration | Inspection of both source Info.plist files; no background-device result inferred |

## What was checked

The local and GitHub documentation lanes check the public OpenAPI, policy and
artifact hashes; reproducible reference/coverage output; focused exporter and
navigation regressions; links and fragments; public-content patterns; the
source-pinned dependency baseline; Markdown structure and spelling.
The maintainer's source-backed lane also compares wire shapes with the pinned
private contract. Public CI cannot independently fetch that private contract.

Those checks do not establish the correctness of every sentence. The semantic
review queue remains visible precisely because structural generation and
correct prose are different forms of evidence. Neither a green documentation
job nor a large word count is an application certification.

## Remaining work and owners

| Work | Owner role | Required evidence or action |
| --- | --- | --- |
| Route-derived operation summaries | Owning API feature engineer | Review controller, validator, handler and tests; replace generic purpose with an operation-specific explanation |
| Type-only field meanings | Owning domain engineer | Establish units, allowed vocabulary, lifecycle and model-specific context before editing the dictionary registry |
| Untyped success responses | API contract maintainer | Add accurate canonical response annotations and verify them with contract tests; do not invent a public-only DTO |
| Stale private migration inventories | Admin release owner | Reconcile old inventories with the current exact-operation ledger and executable UI paths |
| Signed-client and provider certification | Mobile/release and operations owners | Exercise the exact candidate, policy, country and provider boundary and retain sanitized results |
| Deployed policy/configuration | Operations owner | Inspect effective runtime configuration; example defaults do not prove the deployed value |

Every remaining operation/field item is enumerated in the generated
[coverage report and queue](../api/reference/coverage.md). The public guide's
[limitations](../api/coverage-and-limitations.md) explain how to interpret them.
Private incidents, raw logs, receipts, identity documents and infrastructure
identifiers remain outside this repository.
