# S07 · RFC 9396: OAuth 2.0 Rich Authorization Requests

**Source:** Lodderstedt, Richer and Campbell · 2023-05
**Evidence type:** IETF standard
**Accessed:** 2026-11-01 · [Original source](https://www.rfc-editor.org/rfc/rfc9396.html)

## What the source supports

The authorization_details parameter supports structured fine-grained authorization. Common fields and API-specific types express more detail than a broad scope string.

## Boundary of the evidence

Field combinations can expand requested rights. The standard does not supply every domain's consent semantics or prove that a person understood an approval screen.

## Use in this study

Bind grants to concrete actions, resources and limits. Protocol P03 tests parameter drift; P04 tests revocation after approval. Neither is solved by placing an approval button in chat.

This note is an editorial evidence assessment, not an independent replication or an endorsement by the cited authors.
