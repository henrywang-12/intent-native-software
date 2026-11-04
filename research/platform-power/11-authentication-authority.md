# Identity and authority are separate resources

*Platform power companion · 4 November 2026 · AI-assisted analytical working note.*

A person can be correctly authenticated while an action remains unauthorized. A signed-in agent may know whose account it represents without having permission to spend money, share a document or change a booking.

OpenID Connect supplies identity assertions. Rich Authorization Requests provides a way to express fine-grained authorization data. Neither standard implies that every authenticated client may exercise every account privilege.

**Proposed grant.** A user delegates an operation on a named resource to a named agent, with a spending limit, expiry and revocation mechanism. The execution service checks those restrictions immediately before the side effect. A stale chat message is not the source of authority.

The hard case is a task that changes during execution. A requested train ticket becomes unavailable, or the provider changes the price. The system should determine whether the new offer still fits the existing grant. If it does not, the user approves a new request. This is a product interaction, not just a token-validation detail.

**Tests.** Attempt the correct operation after expiry, with another provider, with a larger amount and after revocation. All should be rejected according to the declared policy. Also verify that a harmless read remains available when a spending grant is revoked.

**Open question.** More frequent approval can reduce usability. Research should compare comprehension and error rates under explicit per-action approval and narrowly scoped standing grants rather than assume either extreme is optimal.

## Evidence boundary

- [OpenID Connect Core 1.0, errata set 2](https://openid.net/specs/openid-connect-core-1_0.html)
- [RFC 9396: Rich Authorization Requests](https://www.rfc-editor.org/rfc/rfc9396.html)

Source-backed observations are identified in the text. Mechanisms, designs and proposed tests are the author's analysis; none is an empirical result. Sources were accessed on 4 November 2026.
