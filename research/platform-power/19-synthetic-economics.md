# Synthetic economics: the shared-runtime crossover

This model is a sensitivity tool, not a forecast or estimate of any company.

[Executable model and nine invariant tests](../experiments/test_platform_power.py) run under the existing research CI.

## A worked example

Assume 100 monthly tasks, contribution of 10 units per task before the listed costs, and support cost of 1 per task. A standalone service has fixed cost 600 and no platform fee. A shared runtime has fixed cost 100 and fee 2 per task.

| Architecture | Calculation | Net contribution |
|---|---|---:|
| Standalone | 100 × (10 − 0 − 1) − 600 | 300 |
| Shared runtime | 100 × (10 − 2 − 1) − 100 | 600 |
| Shared runtime, fee 8 | 100 × (10 − 8 − 1) − 100 | 0 |

The first shared-runtime scenario saves 300. It is not inherently better: at fee 8 it loses to the standalone implementation. At fee 2, the fixed-cost saving of 500 is exhausted at 250 tasks; above that volume the standalone service wins under these assumptions.

This comparison holds demand, quality and support costs constant. Real platforms can change all three. Acquisition costs, taxes, migration, outages and refunds are omitted unless explicitly included in inputs. Never label these numbers as measured merchant savings.

## Distribution and execution

The module also computes normalized-share HHI and a chain of conditional completion probabilities. HHI describes concentration in the supplied shares; it cannot establish the relevant market or a legal monopoly. For four equal shares it is 0.25; for a single share it is 1.

Completion uses the probability of each stage succeeding **conditional on all previous stages succeeding**. The chain rule then applies without an independence assumption. Substituting marginal stage probabilities would require an additional assumption and may misestimate correlated failures.

## Reproduce

```sh
python3 research/experiments/test_platform_power.py
```

Tests cover break-even rounding, nonviable margins, cost crossover, both favorable and unfavorable shared-runtime cases, concentration endpoints, conditional completion and invalid inputs. All inputs are synthetic; no accounts, network connections or credentials are used.
