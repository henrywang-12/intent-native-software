# P16 · Does integration concentrate failure?

**Status: proposed protocol; not run.** The local analytical models are separate artifacts.

## Estimand

Estimate the effect of shared infrastructure failures on end-to-end task availability.

## Design and control

Inject identity, catalog, policy and evidence-store outages in a local simulator. Compare centralized dependencies with independently available alternatives.

## Outcomes

Measure fraction of tasks blocked, unsafe fallback attempts, recovery time and inconsistent state.

## Confounds and boundaries

Independent components can still share hidden infrastructure. Make assumed dependency graphs explicit and vary common-mode failure probabilities.

## Decision and reporting rule

Prefer redundancy only when it improves supported recovery without bypassing authority. Report availability and integrity separately.

Record assignment, exclusions, all attempts, versions and budgets. Choose sample size and a stopping rule before confirmatory data collection; publish null and adverse results. Live-service or participant studies require an appropriate separate study setup.

**Methodological context:** [S06: MCP architecture, 2025-06-18 specification](https://modelcontextprotocol.io/specification/2025-06-18/architecture); [S08: RFC 9110 section 9.2.2: Idempotent methods](https://www.rfc-editor.org/rfc/rfc9110.html#section-9.2.2). These sources motivate the design; they did not run this proposed study.
