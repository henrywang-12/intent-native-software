# P13 · Does catalog growth improve effective liquidity?

**Status: proposed protocol; not run.** The local analytical models are separate artifacts.

## Estimand

Estimate the marginal effect of adding providers with varied reliability.

## Design and control

Expand a synthetic catalog while varying duplication, stale availability and true coverage. Compare raw relevance search with reliability-aware selection.

## Outcomes

Measure probability of a feasible verified match, search latency, stale selections and supplier concentration.

## Confounds and boundaries

Keep task demand fixed for the primary analysis; separately vary its distribution. Added providers must not all be selected for unusually high quality.

## Decision and reporting rule

A larger catalog supports the network-effect claim only when effective liquidity improves after accounting for search and verification cost.

Record assignment, exclusions, all attempts, versions and budgets. Choose sample size and a stopping rule before confirmatory data collection; publish null and adverse results. Live-service or participant studies require an appropriate separate study setup.

**Methodological context:** [S02: Weixin Mini Programs](https://www.tencent.com/products/weixin-mini-programs/); [S21: Platform Competition in Two-Sided Markets](https://academic.oup.com/jeea/article-abstract/1/4/990/2280902). These sources motivate the design; they did not run this proposed study.
