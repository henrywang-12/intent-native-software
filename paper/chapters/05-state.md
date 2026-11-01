# 5. A timeout is a state of knowledge


Suppose an agent submits a booking and the connection closes. The absence of a response says something about the coordinator's knowledge, not necessarily about the provider's state. The provider may have committed the action. Blindly submitting again can create a duplicate.

Use an explicit lifecycle: proposed, authorized, executing, verified, rejected, cancelled or indeterminate. These names are less important than the invariants. A verified result requires matching evidence; cancellation before dispatch differs from compensation after an effect; uncertainty must remain visible until resolved.

HTTP idempotence provides relevant vocabulary, but it does not guarantee exactly-once business execution. Repeated requests are safe only under the operation's actual semantics and the provider's deduplication contract. [S08: RFC 9110 section 9.2.2: Idempotent methods](https://www.rfc-editor.org/rfc/rfc9110.html#section-9.2.2)

An execution coordinator should persist intent before dispatch and retain the provider's reference afterward. Recovery first asks what happened. If the evidence is missing, stale or contradictory, another attempt may require waiting, human intervention or a fresh authorization. The correct action can be to stop with an honest unknown.

Multi-service work adds partial completion. If transport is reserved and a hotel fails, “undo” may involve cancellation fees and lost availability. Saga-style compensation is a precedent for organizing such recovery, but a compensating transaction is not time travel. [S09: Sagas](https://sigmodrecord.org/1987/12/09/sagas/)

The public demonstration uses a simulated provider with permanent deduplication and direct state inspection. Real providers can have shorter deduplication windows, delayed reads and different refund rules. The paper's evaluation protocols deliberately remove those conveniences.

This has a market consequence. A platform with reliable status APIs and clear recovery procedures can create value even without the best planner. Conversely, a platform with excellent reasoning and poor evidence can make users pay for its uncertainty. Reliability is partly an institutional property of the environment, not merely a characteristic of the model.
