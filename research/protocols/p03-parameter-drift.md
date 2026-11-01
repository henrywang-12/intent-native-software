# P03 · Does approval bind to the actual action?

**Status: proposed protocol; not run.** The local analytical models are separate artifacts.

## Estimand

Test whether changing an approved parameter prevents dispatch under the old grant.

## Design and control

Generate cases that change recipient, amount, currency, resource, date, timezone or provider after approval. Include harmless formatting changes with identical canonical meaning.

## Outcomes

Count prohibited dispatches and unnecessary reapprovals. The oracle compares domain meaning and grant scope, not raw string identity alone.

## Confounds and boundaries

Exercise version changes and alternate encodings. A test that uses the implementation canonicalizer as its oracle risks reproducing the same bug.

## Decision and reporting rule

Any unauthorized material change is a failing invariant. Report false rejections independently rather than weakening the rule to raise completion.

Record assignment, exclusions, all attempts, versions and budgets. Choose sample size and a stopping rule before confirmatory data collection; publish null and adverse results. Live-service or participant studies require an appropriate separate study setup.

**Methodological context:** [S07: RFC 9396: OAuth 2.0 Rich Authorization Requests](https://www.rfc-editor.org/rfc/rfc9396.html); [S08: RFC 9110 section 9.2.2: Idempotent methods](https://www.rfc-editor.org/rfc/rfc9110.html#section-9.2.2). These sources motivate the design; they did not run this proposed study.
