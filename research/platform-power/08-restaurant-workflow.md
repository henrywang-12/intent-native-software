# Restaurant software as a transaction-state example

*Platform power companion · 4 November 2026 · AI-assisted analytical working note.*

Consider a hypothetical restaurant reservation service. The user asks for a table for four at 19:00 within a budget. The agent must discover availability, obtain a current offer, explain any deposit or cancellation policy, request approval and return a confirmed booking reference.

This is a small interface over a consequential state machine. The proposed states are requested, offered, approved, submitted, confirmed, canceled and unresolved. A timeout after submission must enter unresolved until reconciliation establishes whether the provider created a booking. Blindly repeating a write may create duplicate reservations.

**Architecture proposal.** Bind approval to the exact provider, party size, time, maximum charge and expiry. Revalidate if the offer changes. Store a durable operation identifier and obtain provider-side status before retrying. Cancellation must be a separate authorized operation with its own receipt.

RFC 9396 provides a standard mechanism for carrying fine-grained authorization details. The restaurant-specific fields and state machine here are proposed application semantics, not requirements imposed by that RFC.

**Evaluation.** Inject sold-out offers, changed deposits, delayed confirmations and cancellation failures. Success means both the user's intended reservation and a verifiable final state. A persuasive conversational response alone is insufficient.

The example is deliberately generic. Restaurants illustrate low-frequency service software and real-world fulfillment; this note makes no statement about Walify being a restaurant or loyalty product.

## Evidence boundary

- [RFC 9396: Rich Authorization Requests](https://www.rfc-editor.org/rfc/rfc9396.html)

Source-backed observations are identified in the text. Mechanisms, designs and proposed tests are the author's analysis; none is an empirical result. Sources were accessed on 4 November 2026.
