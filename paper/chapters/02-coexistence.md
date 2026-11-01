# 2. Coexistence means shared state and bounded agency


Humans and agents will often inhabit the same workflow rather than alternate between separate worlds. A person may start a plan, an agent may collect offers, another person may change a constraint, and a service may report a delayed result. The design problem is maintaining a common understanding across those transitions.

Define coexistence operationally through four properties. **Legibility:** a person can inspect the current commitment. **Intervention:** they can pause or change future action. **Continuity:** another interface can resume the task without losing its meaning. **Accountability:** records identify the principal, delegated authority, provider and observed outcome. None requires an agent to imitate a person.

An assistant should make its role visible to counterparties where that matters. A service should distinguish a user's instruction from an agent's inference about that instruction. An affected person who never used the assistant should still have a route to dispute an incorrect invitation or transaction. A system that optimizes the principal's convenience while imposing unexplained costs on everyone else has not solved coexistence.

The broader assistant-ethics literature treats privacy, manipulation, cooperation and relationships as connected design questions. This paper narrows that agenda to observable software properties rather than assuming a conversational interface creates trust. [S26: The Ethics of Advanced AI Assistants](https://arxiv.org/abs/2404.16244v2)

The practical unit is a *jointly recoverable task*. If an agent cannot complete a request, a person should receive enough state to continue: attempted actions, confirmed effects, unresolved uncertainty and remaining permissions. A transcript alone is insufficient because it mixes intentions, speculation and facts.

This leads to a different optimization target from maximum autonomy. Minimize the total burden of obtaining a satisfactory outcome, including supervision, mistakes and recovery. Sometimes the best assistant takes the next step; sometimes it supplies a clear form; sometimes it asks a precise question. The division of work should depend on evidence about the task, not an aesthetic preference for removing every button.
