# System Admin accessibility and localization

Administrative work can disable an account, decide a payout or inspect private
evidence. A control that is technically present but clipped, untranslated or
unreadable at large text scale is not a safe control. This chapter defines the
review matrix for the separate System Admin app. It describes a target and
source-level conventions; it does not claim every screen has completed a
qualified linguistic or signed-device review. The consumer app's six-language
catalog is a design reference, not automatic proof of Admin-app parity.

## Shared design, separate certification

The Admin app borrows KiloDrive's Material 3 visual language, typography,
theme, dark mode, high contrast and text scaling, with its own persisted
preferences. Phones use compact navigation; wide screens may show more
context. Appearance settings must not change the underlying capability or
country scope. A user can understand where they are from the screen title,
selected navigation state and current workspace, even after a deep link or
return from detail.

The app's copy should be task-specific. “Approve” without a named object or
effect is weak in a high-risk dialog. A confirmation should name the intended
change, affected party by a safely displayed label, any irreversible or
delayed consequence, and a distinct cancel action. After submission, success,
rejection, conflict, still processing and unknown outcome need different
human-readable messages. A raw JSON body, numeric enum, stack trace or blank
spinner is not an accessible result.

## Screen-state matrix

For every listed screen, inspect initial loading, non-empty, true empty,
partial-data, denied, failed, refreshing, pending-mutation and post-action
states. Preserve the active tab, subtab, scroll and focus when returning from
an authorized detail. A permission revocation or scope switch may legitimately
close the detail, but it should explain why rather than show old data.

| Screen family | Critical presentation questions |
| --- | --- |
| Sign-in and workspace choice | Can a keyboard/screen reader identify fields, errors, current country and allowed tenant? Does a long name wrap? |
| Dashboard and My Work | Are freshness and unavailable metrics spoken and visible? Does zero differ from failed load? |
| People listing and dossier | Can search, filters, eight tabs and nested subtabs be reached in order? Are dates, currency, identifiers and readiness labelled? |
| Security actions and sessions | Does the confirmation explain disable, lock, reset and revoke separately? Is proof entry protected from shoulder surfing and logs? |
| Documents and vehicles | Is status distinguishable without color? Can a restricted or expired record explain why it cannot open? |
| Finance and bank decisions | Can large/negative amounts, minor-unit currencies, fees, current revision and unknown outcomes fit without truncation? |
| Trips and replay | Are timeline order, map alternatives, retained evidence gaps and call status available without relying only on color or animation? |
| Notifications and alerts | Does the UI distinguish queued, provider accepted, failed and read? Is private text absent from generic previews? |
| Audit and PDF | Is each event readable as labelled facts in affected-user time? Does export identify the single record and sensitivity? |
| Support and outbox | Are owner, age, current status, next action and retry consequence apparent at narrow width and large text? |

## Layout and interaction cases

Test the smallest supported phone width, a typical phone, tablet portrait,
tablet landscape and split-window width. Pair these with platform text scale,
app text preference, light/dark/high contrast, open keyboard, gesture and
button navigation, and long translated strings. Do not certify a page from a
single golden image: focus, semantics and overflow need interaction tests.

On narrow screens, a dossier tab strip may scroll but must expose the selected
tab and not trap horizontal gestures. On wider screens, a rail or more columns
must not duplicate the same action or leave a dialog detached from its target.
Lists need accessible row labels and stable pagination. Loading placeholders
should not be read as real records. Empty states explain that the query
succeeded with no matching rows; failures offer a labelled retry. A small
in-button progress indicator is acceptable while submitting one action, but
the affected control remains clearly identified and prevents duplicate taps.

Focus follows the task: opening a dialog announces its title and consequence;
validation moves to a useful error; closing returns focus to the invoking
control where possible; a completed operation announces its result. A back
gesture must not silently discard a pending financial action whose outcome
is uncertain. Screen readers should hear amount **with currency**, time **with
its zone context**, and status **with text**, not icon or color alone.

## Localization contract

The consumer app has English, Spanish, French, Japanese, Simplified Chinese
and Traditional Chinese resources. The Admin app should use the same supported
language policy only where a complete, reviewed Admin catalog exists. Its
current source includes localized copy for parts of People and finance, while
broader parity and rendered review remain incremental. An English fallback is
preferable to a misleading partial translation of a consequential action; the
release record must disclose that limitation.

For each Admin message key and locale, reviewers check:

1. meaning of the action and affected subject, not word-for-word similarity;
2. distinct verbs for request, approve, reject, revoke, retry and refresh;
3. plural, gender and ICU placeholder parity where applicable;
4. number grouping, decimal symbol, negative amount and ISO currency;
5. date/time order, twelve-hour or selected format, time-zone label and DST;
6. truncation/wrapping for long personal or organization names;
7. reading order, semantics labels and announcements for changing status; and
8. native OS permission, notification and billing text in the signed build.

The affected user's time zone governs user audit presentation; the admin's
selected zone governs general operations where specified. Stored timestamps
remain UTC and malformed values render unavailable, never an invented current
time. Money layout preferences alter presentation only, never the ledger
currency or integer minor-unit amount. An unknown API enum displays a neutral
localized state and disables unsafe actions.

## Verification and evidence

Widget tests should exercise a representative screen in each state and width,
including 2x text, keyboard, semantics and focus. Locale tests should render
actual messages and verify placeholders, amount/time examples and responsive
wrapping. Native certification repeats critical journeys on signed Android
and iOS candidates with real screen reader and OS text scaling. A human
linguistic review records locale, reviewer qualification, source revision and
scope without publishing private reviewer or fixture data.

Keep a per-workflow matrix with: screen and state; locale; size/text scale;
expected announcement; expected visible result; test evidence level; current
result; owner; and remaining limitation. An analyzer pass or ARB key count
does not prove that a translated confirmation is safe or fits the screen.

Continue with [mobile architecture](mobile.md),
[System Admin mobile app](system-admin-mobile-app.md), and
[mobile security verification](../quality/mobile-security-verification.md).
