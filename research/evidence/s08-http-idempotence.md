# S08 · RFC 9110 section 9.2.2: Idempotent methods

**Source:** Fielding, Nottingham and Reschke · 2022-06
**Evidence type:** IETF standard
**Accessed:** 2026-11-01 · [Original source](https://www.rfc-editor.org/rfc/rfc9110.html#section-9.2.2)

## What the source supports

Idempotence concerns the intended effect of repeated requests. The specification cautions against automatic retries of non-idempotent requests without additional knowledge.

## Boundary of the evidence

An HTTP success response is not proof of a business outcome, and an operation ID is not a universal exactly-once guarantee. Provider deduplication scope and expiry matter.

## Use in this study

After an ambiguous timeout, reconciliation must precede another consequential action. This motivates the existing SQLite demo and the new retry-risk sensitivity model.

This note is an editorial evidence assessment, not an independent replication or an endorsement by the cited authors.
