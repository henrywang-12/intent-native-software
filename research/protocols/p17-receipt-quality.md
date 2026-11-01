# P17 · Can receipts distinguish claims from facts?

**Status: proposed protocol; not run.** The local analytical models are separate artifacts.

## Estimand

Evaluate whether a receipt verifier accepts only evidence matching the authorized action.

## Design and control

Generate stale, mismatched, replayed, missing and internally inconsistent records alongside valid records. Use a separate provider-state oracle.

## Outcomes

Count false verified outcomes, false rejections and correctly retained unknowns. Include cases where a valid record proves booking but not service delivery.

## Confounds and boundaries

Do not treat a signature as proof of the underlying business fact. State the trust assumptions for provider identity and read freshness.

## Decision and reporting rule

Any unsupported success claim fails the declared evidence contract. Report coverage limits instead of broadening the word verified.

Record assignment, exclusions, all attempts, versions and budgets. Choose sample size and a stopping rule before confirmatory data collection; publish null and adverse results. Live-service or participant studies require an appropriate separate study setup.

**Methodological context:** [S08: RFC 9110 section 9.2.2: Idempotent methods](https://www.rfc-editor.org/rfc/rfc9110.html#section-9.2.2); [S27: Model Cards for Model Reporting](https://arxiv.org/abs/1810.03993v2). These sources motivate the design; they did not run this proposed study.
