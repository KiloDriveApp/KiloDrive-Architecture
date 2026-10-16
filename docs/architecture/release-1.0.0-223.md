# Consumer 1.0.0+223: delivery, profile and account clarity

Reviewed 16 October 2026 against the committed product version authorities
recorded in [source-derived facts](source-versions.generated.md). This chapter
describes source behavior. Store publication, enabled country policy and
physical-device outcomes require separate evidence.

## Public experience

Build 223 combines the public build-222 notes with the newer delivery and
profile work. Delivery booking has Simple and Advanced paths. Simple asks for
the locations, a description, optional media/documents, instructions and
timing; Advanced retains additional service choices. Parcel weight and
dimensions are optional. The person's unit preferences default to pounds and
inches for input while the API continues to own normalized values. Contact
details remain optional for booking, but supplied phone numbers are validated.
The wizard preserves a draft across Back/Next and swipe navigation and still
requires authoritative quote and booking confirmation.

Profile details expose gender, pronouns and birth date separately from
name-correction review. For legacy identities missing optional gender or
pronouns, the API read projection returns safe display values without changing
the stored identity. The new two-tab Profile Edit screen and its client parser
are **working-tree changes after the committed build-223 source**; they must not
be attributed to the published binary until a later consumer build includes
them. This distinction is important when reading the current manuals.

Rental customers may browse the catalog without driver qualification. Wallet
money and reward points remain different ledgers; only a server-confirmed,
eligible conversion creates wallet value. Membership presentation makes the
beneficiary, plan and term clearer, while native-store purchase verification
and uncertain-result reconciliation remain API/provider responsibilities.

## Ownership and recovery

- The consumer client collects a draft, formats local display units and
  presents the authoritative result. It does not choose monetary or trip
  outcomes from an optimistic local state.
- The API validates the booking, identity, membership and conversion policy.
  Unknown mutation outcomes retain their original operation identity until
  reconciliation completes.
- The country cell owns trips, deliveries, rentals, wallet and points events;
  central identity owns credentials and profile source fields. The profile
  compatibility projection is read-only.
- Original build-222 wording and its earlier release-history cards remain
  dated historical evidence when the public notes are consolidated under 223.
  Consolidation does not revise app entitlements or schema.

## Evidence boundary

The public manual edition 3.6 uses an earlier genuine iPhone route capture,
an earlier physical Android verification capture and a build-223 widget
fixture. Their captions state their exact scope. None is proof that a
build-223 signed iOS or Android journey was completed. The curated public API
export is older and is not relabelled by this chapter.
