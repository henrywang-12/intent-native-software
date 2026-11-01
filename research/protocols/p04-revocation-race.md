# P04 · Is revocation respected at the dispatch boundary?

**Status: proposed protocol; not run.** The local analytical models are separate artifacts.

## Estimand

Identify the last point at which an unexecuted action can be stopped.

## Design and control

Inject revocation before planning, after approval, immediately before dispatch and after provider commitment. Use a controlled event scheduler and record the chosen linearization point.

## Outcomes

Measure dispatch after effective revocation, incorrect claims of cancellation and time to surface already-committed effects.

## Confounds and boundaries

Revocation cannot reverse history. Separate provider-side cancellation from blocking a future request, and model delayed revocation propagation explicitly.

## Decision and reporting rule

Reject implementations that claim cancellation when an effect is already committed or allow dispatch after their declared revocation boundary.

Record assignment, exclusions, all attempts, versions and budgets. Choose sample size and a stopping rule before confirmatory data collection; publish null and adverse results. Live-service or participant studies require an appropriate separate study setup.

**Methodological context:** [S07: RFC 9396: OAuth 2.0 Rich Authorization Requests](https://www.rfc-editor.org/rfc/rfc9396.html); [S09: Sagas](https://sigmodrecord.org/1987/12/09/sagas/). These sources motivate the design; they did not run this proposed study.
