# P14 · Can users leave with usable task state?

**Status: proposed protocol; not run.** The local analytical models are separate artifacts.

## Estimand

Test whether an unresolved workflow can move to an independent host without losing meaning or leaking unrelated data.

## Design and control

Export synthetic completed, pending, cancelled and indeterminate tasks. Import them into an independently implemented reader and recovery tool.

## Outcomes

Measure preserved commitments, correct uncertainty labels, rejected expired grants and unnecessary fields disclosed.

## Confounds and boundaries

Exported history must not silently recreate live credentials or permissions. Validate references whose providers are offline.

## Decision and reporting rule

Pass only when the receiving system can explain and safely continue supported work. A valid JSON file alone is not successful portability.

Record assignment, exclusions, all attempts, versions and budgets. Choose sample size and a stopping rule before confirmatory data collection; publish null and adverse results. Live-service or participant studies require an appropriate separate study setup.

**Methodological context:** [S07: RFC 9396: OAuth 2.0 Rich Authorization Requests](https://www.rfc-editor.org/rfc/rfc9396.html); [S27: Model Cards for Model Reporting](https://arxiv.org/abs/1810.03993v2). These sources motivate the design; they did not run this proposed study.
