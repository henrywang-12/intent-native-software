# 20. Trust is an operating property


A trustworthy agent environment should remain understandable when a component behaves unexpectedly. This is stronger than a promise that the model normally follows instructions.

Retrieved service descriptions, messages and documents can contain text that tries to redirect an agent. Indirect prompt-injection research establishes why treating all encountered language as equally authoritative is dangerous. AgentDojo's evaluation design further separates legitimate task utility from attacker objectives. [S25: Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/abs/2302.12173) [S24: AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents](https://arxiv.org/html/2406.13352v3)

Our architectural response is to constrain effects outside the planner. Untrusted content can inform a proposal but cannot mint a grant, redefine an approved recipient or turn a provider's assertion into verified state. This does not solve every attack: compromised credentials, misleading evidence and incorrect policy remain possible. It narrows specific paths from data to unintended effects.

Trust also requires operations after failure. A person needs to know whether an action occurred, which authority was used and how to seek correction. Logs should distinguish observations from claims. A receipt should identify its evidence scope rather than imply certainty about facts it cannot establish.

For example, a provider record may prove that a reservation exists but not that the service was delivered satisfactorily. A cryptographic signature proves something about the signer and message integrity, not the truth of every statement. More elaborate evidence formats do not remove this distinction.

The paper's verification model makes the economic tradeoff explicit: checking adds cost and may introduce false rejections, but can reduce costly false acceptance. Its parameters are hypothetical. Real deployments need measured detector behavior under distribution shift and adaptive pressure.

Trust is also earned through incentives. A host paid to promote a provider has a conflict that should be visible. Security, transparency and commercial governance are related, but success in one does not certify the others.
