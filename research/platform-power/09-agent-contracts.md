# From app screens to callable service contracts

*Platform power companion · 4 November 2026 · AI-assisted analytical working note.*

An interface helps a person navigate. A callable contract must also specify what an action means, who may perform it, when it takes effect and how uncertainty is resolved.

**Proposed capability record.** Include a stable identifier, operation version, typed input, preconditions, price and availability rules, side effects, authorization requirements, retry semantics, status lookup and support owner. Classify operations as read-only, reversible writes or writes with potentially irreversible effects.

A platform should not derive authority from a tool's natural-language description. The execution boundary checks the approved operation and resource against a machine-readable policy. It must reject a broader action even if a model proposes it confidently.

RFC 9396 supports structured authorization information. It does not by itself supply provider correctness, idempotency or rollback. Those must be defined and tested in the service contract.

**Compatibility problem.** An updated field can preserve JSON validity while changing meaning. A booking date interpreted in a different timezone is syntactically acceptable and operationally wrong. Version policy must cover semantics, not only schemas.

**Proposed acceptance test.** Run contract examples against a provider sandbox, then inject stale offers, revoked authority and ambiguous outcomes. Publish which assertions were tested and which depend on the provider's guarantees.

**Counterexample.** A trivial read-only lookup may not need the same governance as a payment operation. The contract burden should scale with consequence rather than force every capability into the most expensive review path.

## Evidence boundary

- [RFC 9396: Rich Authorization Requests](https://www.rfc-editor.org/rfc/rfc9396.html)

Source-backed observations are identified in the text. Mechanisms, designs and proposed tests are the author's analysis; none is an empirical result. Sources were accessed on 4 November 2026.
