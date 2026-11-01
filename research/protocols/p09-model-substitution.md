# P09 · Can planners change without changing authority?

**Status: proposed protocol; not run.** The local analytical models are separate artifacts.

## Estimand

Test planner portability while preserving runtime rules and task quality.

## Design and control

Evaluate at least two independently developed models and a deterministic baseline against the same capability contracts, grants and task distribution.

## Outcomes

Report authorized completion, policy violations, latency, inference cost and adapter changes by task stratum.

## Confounds and boundaries

Match total budgets rather than token counts alone. Do not tune each model on held-out tasks or let one bypass the policy layer.

## Decision and reporting rule

Policy invariants must hold for every planner. A quality decline is a portability cost even when the API remains compatible.

Record assignment, exclusions, all attempts, versions and budgets. Choose sample size and a stopping rule before confirmatory data collection; publish null and adverse results. Live-service or participant studies require an appropriate separate study setup.

**Methodological context:** [S17: Qwen3 Technical Report](https://arxiv.org/abs/2505.09388); [S20: The Open Source AI Definition 1.0](https://opensource.org/ai/open-source-ai-definition). These sources motivate the design; they did not run this proposed study.
