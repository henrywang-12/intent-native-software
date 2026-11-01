# P12 · Does commercial ranking change user outcomes?

**Status: proposed protocol; not run.** The local analytical models are separate artifacts.

## Estimand

Measure how commission-aware routing affects satisfaction and provider access.

## Design and control

Use a synthetic marketplace with known prices, quality and commission. Compare user-utility ranking, disclosed commercial ranking and undisclosed commission ranking.

## Outcomes

Record utility regret against the feasible best option, concentration of exposure, completion and provider revenue.

## Confounds and boundaries

Keep provider eligibility and supply constant. Avoid defining utility entirely through the same proxy optimized by the ranker.

## Decision and reporting rule

Reject claims of better matching when gains depend on hidden user costs. Report the tradeoff surface rather than a single platform-revenue score.

Record assignment, exclusions, all attempts, versions and budgets. Choose sample size and a stopping rule before confirmatory data collection; publish null and adverse results. Live-service or participant studies require an appropriate separate study setup.

**Methodological context:** [S21: Platform Competition in Two-Sided Markets](https://academic.oup.com/jeea/article-abstract/1/4/990/2280902); [S26: The Ethics of Advanced AI Assistants](https://arxiv.org/abs/2404.16244v2). These sources motivate the design; they did not run this proposed study.
