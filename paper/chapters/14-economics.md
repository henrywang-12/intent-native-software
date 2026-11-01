# 14. The cost of a verified outcome


Token price is an input price. A person or business buys an outcome. Confusing the two can make an apparently inexpensive assistant costly to operate.

Define expected task cost as C = C_model + C_integration + C_review + C_recovery + C_service. The terms include inference, amortized integration, human oversight, failures and the underlying provider's service. Compare alternatives only at a matched level of outcome quality and acceptable risk. Dividing cost by the number of attempted tasks rewards systems that fail cheaply.

A more useful operational measure is cost per verified execution, with unsuccessful attempts and their consequences retained in the numerator. Report user satisfaction and delayed service quality separately: a booking record does not establish satisfactory delivery. Keep pending outcomes separate, and report total cost with an undefined cost-per-success ratio when there are zero verified successes. Report latency separately: averaging it into money can hide an unacceptable tail. For irreversible effects, expected loss alone may also be insufficient; hard constraints can prohibit certain actions regardless of average benefit.

Software production has a similar distinction. Generating an interface is not the full cost of operating a service. Testing, migration, support, dependency changes and incidents remain. METR's 2025 randomized study is a concrete warning against equating perceived ease with measured productivity in every setting. Its 2026 update also warns against treating that historical estimate as timeless. [S11: Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity](https://metr.org/Early_2025_AI_Experienced_OS_Devs_Study-paper.pdf) [S12: We are Changing our Developer Productivity Experiment Design](https://metr.org/blog/2026-02-24-uplift-update/)

This yields a falsifiable economic thesis: if generation costs decline while maintenance and coordination costs remain significant, value can shift toward reusable service infrastructure. If models also remove most integration and recovery costs, that shift may be weaker than we expect.

The routing model accompanying this paper uses hypothetical prices and success probabilities. It shows how fallback and verification costs can erase nominal savings. Those numbers are illustrative inputs, not current provider prices or estimates of Walify margins.

Value creation does not establish value capture. A platform earns an attractive margin only if willingness to pay survives competitive alternatives and provider bargaining, while acquisition, support, subsidies and losses remain affordable. A reduction in total task cost can accrue entirely to users or suppliers. Proposed protocols P11, P12 and P20 test parts of this commercial bridge; no profitable margin is inferred here.

The strategic question is therefore not “How cheaply can we generate software?” It is “Which repeated costs disappear for a user or provider when they join this system?” A platform earns its place by answering the second question with evidence.
