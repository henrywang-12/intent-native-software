# 19. Human work moves toward specification and responsibility


When software can propose and execute more steps, some human work shifts toward specifying goals, choosing tradeoffs, reviewing uncertain cases and accepting responsibility. This is a scenario about task composition, not a numerical prediction of job losses.

The size of the shift depends on verification. A generated artifact that is cheap to check can support extensive delegation. A decision whose consequences emerge months later is harder to supervise. In the latter case, fluent output may increase the demand for expertise rather than remove it.

Time-horizon research gives one way to describe progress on software tasks, but a 50% success threshold is not a service-level promise. Deployment needs to account for the distribution of failures, their detectability and their recovery cost. [S10: Measuring AI Ability to Complete Long Software Tasks](https://arxiv.org/abs/2503.14499v4)

A useful division of labor preserves a person's ability to understand the work. If automation removes practice in ordinary cases but expects expert intervention in rare failures, competence may become difficult to maintain. The study proposes measuring recovery performance after repeated assisted use, rather than assuming a human fallback remains effective indefinitely.

There is also a distributional question. An organization may benefit from faster throughput while workers experience more monitoring or less autonomy. A consumer may save time while a provider handles a flood of low-quality requests. Counting only the principal's saved minutes misses those burdens.

The proposed evaluation includes user comprehension, provider workload and unresolved disputes alongside completion. A coexistence architecture should make responsibility legible: which choices were made by a person, which were delegated, and which were imposed by the platform's rules.

The most credible near-term prediction is uneven change. Tasks with stable contracts and immediate evidence are easier to delegate than tasks with contested goals and delayed outcomes. Progress in general reasoning can change that boundary, but it does not eliminate the need to define whose outcome is being optimized.
