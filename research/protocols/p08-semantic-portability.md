# P08 · Do matching schemas preserve meaning?

**Status: proposed protocol; not run.** The local analytical models are separate artifacts.

## Estimand

Measure provider substitution errors that structural type checking misses.

## Design and control

Replace one provider with another using superficially similar fields but different units, timezone conventions, availability semantics and status vocabularies.

## Outcomes

Count semantic mismatches caught before effect, incorrect successful outcomes and manual adapter work.

## Confounds and boundaries

Use an independent domain oracle and equivalent user goals. Include version negotiation and explicit unsupported cases.

## Decision and reporting rule

Accept substitution only when postconditions remain equivalent within declared tolerances. Record integration effort rather than calling every schema-compatible case portable.

Record assignment, exclusions, all attempts, versions and budgets. Choose sample size and a stopping rule before confirmatory data collection; publish null and adverse results. Live-service or participant studies require an appropriate separate study setup.

**Methodological context:** [S06: MCP architecture, 2025-06-18 specification](https://modelcontextprotocol.io/specification/2025-06-18/architecture); [S05: Announcing the Agent2Agent Protocol](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/). These sources motivate the design; they did not run this proposed study.
