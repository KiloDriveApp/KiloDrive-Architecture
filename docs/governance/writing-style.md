# Writing Clearly About Complex Systems

Architecture prose often becomes robotic when it tries too hard to sound
authoritative. Long noun chains, repeated bullets, and vague adjectives make a
document look formal while hiding the actual decision.

This guide keeps KiloDrive's documentation technical and human.

## Explain the reason beside the mechanism

Weak:

> Valkey is used for geospatial processing.

Better:

> Driver positions change too frequently to make every GPS sample a contested
> MySQL update. Valkey keeps the latest, expiring position close to the matching
> path, while MySQL receives selected breadcrumbs for durable evidence.

The second version tells a new engineer what problem the component solves and
why both stores exist.

## Name the tradeoff

Avoid presenting choices as universally correct. UUIDv7 improves index locality
and decentralized creation, but its timestamp portion reveals approximate
creation order. Country cells improve isolation, but cross-country reporting
requires explicit aggregation. A useful document gives both sides.

## Prefer concrete verbs

Use “locks,” “validates,” “commits,” “publishes,” “expires,” and “reconciles.”
Avoid “facilitates,” “leverages,” and “enables” when a specific verb exists.

## Let paragraphs do some work

Bullets are excellent for checks, alternatives, and symptoms. They are poor at
carrying an argument. Use a short paragraph when one idea causes another. The
reader should not have to infer the logic between eight isolated bullets.

## Use “we” carefully

“We chose country cells because…” is honest historical voice. “We guarantee
complete security” is an unsupported assurance. Describe controls and evidence,
not absolute safety.

## Tell the useful failure story

A public-safe lesson makes a design memorable:

> The API once had an outbox event type with no registered handler. The
> transaction was durable, but the worker could only retry an impossible job.
> Producer/handler contract tests now prevent that release mismatch.

Remove private identifiers, payloads, and blame. Keep the causal chain and the
preventive control.

## Define unfamiliar terms once

Link to the [glossary](../../GLOSSARY.md), but still give the reader enough
context to continue. “The outbox (a table committed with business state)…” is
more helpful than forcing a detour for every term.

## Avoid marketing language

Words such as “seamless,” “world-class,” “extreme security,” “unbreakable,” and
“infinitely scalable” do not belong in an engineering guide. Replace them with
the control, limit, test, or measured behavior.

## Be precise about status

Use **Implemented**, **Configurable**, **Operational policy**, and **Planned**.
An adapter in source code does not prove credentials, provider approval,
network reachability, or production canaries are active.

## Edit in three passes

1. **Truth pass:** verify claims, versions, ownership, and status.
2. **Teaching pass:** add why, a small example, tradeoffs, and pitfalls.
3. **Language pass:** remove repetition, vague adjectives, unexplained jargon,
   and sentences that need two readings.

Finally, read the rendered page aloud. If it sounds like a procurement brochure
or a generated checklist, rewrite it as an explanation you would give a
colleague at a whiteboard.
