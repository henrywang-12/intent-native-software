# 22. A transition path that does not require replacing the web


An intent-native internet need not arrive as a replacement for existing applications. A plausible transition is incremental: services expose reliable actions, agents use them alongside conventional interfaces, and reusable contracts gradually lower the cost of composition.

The first stage is assisted work. The agent gathers information and drafts an action; a person completes it through an existing interface. The second stage adds bounded execution for specific capabilities. The third adds reliable recovery across several services. The fourth supports broader discovery and provider substitution. These are capability milestones, not calendar predictions.

Each stage has an exit criterion. Drafting must save total effort. Bounded execution must preserve authorization and evidence. Cross-service work must handle partial completion. Discovery must select genuinely compatible providers. Skipping an exit criterion can produce a compelling demonstration without a sustainable product.

Legacy interfaces will remain important. Some services lack usable APIs; others require interaction designed around human judgment. GUI agents can bridge part of this gap, while typed contracts can make selected operations more reliable. OSWorld's original execution-based benchmark and its later long-workflow extension motivate testing both routes under realistic state and interruptions. [S13: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://arxiv.org/abs/2404.07972v2) [S14: OSWorld 2.0: Benchmarking Computer Use Agents on Long-Horizon Real-World Tasks](https://arxiv.org/abs/2606.29537v2)

Migration should preserve a manual path. If an agent fails, the task state should still be inspectable and actionable. An ecosystem that requires its own assistant for every operation increases dependence and makes outages more damaging.

The transition also needs provider incentives. A contract is maintained when the resulting demand or operating savings justify the work. Standards that ignore support burden can accumulate abandoned integrations. The research protocols therefore include integration drift and supplier maintenance as first-class measurements.

The likely outcome is a hybrid internet: documents, applications, APIs and agents coexist. The new layer coordinates them. Its success depends on reducing the user's burden without obscuring the obligations that existing systems already carry.
