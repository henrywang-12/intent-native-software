# P05 · Can recovery avoid duplicate effects?

**Status: proposed protocol; not run.** The local analytical models are separate artifacts.

## Estimand

Measure recovery after provider commitment with a lost response.

## Design and control

Inject loss before delivery, after commitment and during reconciliation. Compare blind retry, bounded idempotency and read-before-redispatch strategies.

## Outcomes

Count duplicate obligations, false no-effect conclusions, unresolved cases and recovery latency. Record provider deduplication retention.

## Confounds and boundaries

Vary delayed visibility and expired deduplication keys; do not grant the test coordinator perfect provider access unless labeled as a separate condition.

## Decision and reporting rule

Require zero duplicates within the declared supported envelope. Keep indeterminate outcomes visible and report their rate; an honest unknown is not verified success.

Record assignment, exclusions, all attempts, versions and budgets. Choose sample size and a stopping rule before confirmatory data collection; publish null and adverse results. Live-service or participant studies require an appropriate separate study setup.

**Methodological context:** [S08: RFC 9110 section 9.2.2: Idempotent methods](https://www.rfc-editor.org/rfc/rfc9110.html#section-9.2.2); [S09: Sagas](https://sigmodrecord.org/1987/12/09/sagas/). These sources motivate the design; they did not run this proposed study.
