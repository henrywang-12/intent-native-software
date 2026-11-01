# P18 · When is extra reasoning worth its cost?

**Status: proposed protocol; not run.** The local analytical models are separate artifacts.

## Estimand

Estimate outcome improvement from adaptive reasoning budgets relative to fixed budgets.

## Design and control

Use a held-out task set stratified by independently assigned difficulty. Compare equal-budget routing, cheap-first escalation and a fixed strong model.

## Outcomes

Measure verified completion, full inference and verification cost, latency tails and unnecessary escalation.

## Confounds and boundaries

Account for unsuccessful attempts and verifier errors. Do not choose escalation thresholds using held-out answers or equate longer traces with better reasoning.

## Decision and reporting rule

Choose a policy on the cost-quality frontier under the product latency constraint. Publish sensitivity to fallback frequency and correlated errors.

Record assignment, exclusions, all attempts, versions and budgets. Choose sample size and a stopping rule before confirmatory data collection; publish null and adverse results. Live-service or participant studies require an appropriate separate study setup.

**Methodological context:** [S18: Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556); [S19: Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters](https://arxiv.org/html/2408.03314v1). These sources motivate the design; they did not run this proposed study.
