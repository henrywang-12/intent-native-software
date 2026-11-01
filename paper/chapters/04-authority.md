# 4. Authority must survive model substitution


A capable model is not an identity system. A persuasive explanation is not a delegation grant. If replacing the planner changes what the application is permitted to do, authorization is embedded in the wrong place.

Let a grant bind a principal, actor, capability, resource set, parameter limits, expiry and revocation state. At dispatch, the runtime evaluates the concrete action against that grant and the current service state. The model can propose a different action, but the proposal does not expand the grant. Child delegation should only attenuate authority: its permitted actions are a subset of the parent's.

Structured authorization already has a standards foundation. RFC 9396 provides a way to carry fine-grained authorization details in OAuth, including API-specific semantics. It does not remove the need to define and enforce the meaning of those details. [S07: RFC 9396: OAuth 2.0 Rich Authorization Requests](https://www.rfc-editor.org/rfc/rfc9396.html)

There are two separate races. The user may revoke permission between planning and dispatch. The provider state may change between inspection and commitment. Handling the first requires a declared commitment boundary: the service must define when a grant is consumed and how revocation is ordered against dispatch. A coordinator-side check alone leaves a race before provider commitment. Revocation after the declared boundary may require provider cancellation or compensation. Handling state drift may require a version condition, reservation or renewed quote. A single initial approval cannot make both races disappear.

Human approval is useful when it reveals the actual decision. Show the recipient, amount, lasting effect and uncertainty. Avoid asking a person to approve a vague plan and later interpreting that as approval of materially different parameters. Repeated low-information confirmations train users to stop reading.

Our proposal allows previously authorized low-risk actions to proceed without another prompt when the grant remains applicable. The criterion is bounded authority, not constant interruption. Consequential deviations require a new decision.

This boundary makes open and proprietary planners easier to compare. Both receive the same capabilities and are judged under the same rules. The system's authority should remain intelligible even if the model is wrong, unavailable or replaced by a conventional algorithm.
