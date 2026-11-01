# P11 · How costly is joining a second host?

**Status: proposed protocol; not run.** The local analytical models are separate artifacts.

## Estimand

Measure incremental provider effort to maintain the same capability on another host.

## Design and control

Give independent implementers one working integration and a second host with either compatible or incompatible contracts. Include billing and support configuration.

## Outcomes

Primary: total incremental engineer-hours to pass identical acceptance tests. Secondary: recurring upkeep and behavior differences.

## Confounds and boundaries

Do not count only initial code changes. Separate host-specific governance, credential setup and commercial work from transport adaptation.

## Decision and reporting rule

Evidence for interoperability requires sustained savings after a version change, not a one-time successful handshake.

Record assignment, exclusions, all attempts, versions and budgets. Choose sample size and a stopping rule before confirmatory data collection; publish null and adverse results. Live-service or participant studies require an appropriate separate study setup.

**Methodological context:** [S05: Announcing the Agent2Agent Protocol](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/); [S21: Platform Competition in Two-Sided Markets](https://academic.oup.com/jeea/article-abstract/1/4/990/2280902). These sources motivate the design; they did not run this proposed study.
