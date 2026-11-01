# P01 · Does integration improve authorized completion?

**Status: proposed protocol; not run.** The local analytical models are separate artifacts.

## Estimand

Estimate the effect of a typed service environment on verified task completion, holding the planner constant.

## Design and control

Randomize matched task instances between a conventional human interface, a GUI agent and a capability agent. Use the same initial provider state and completion oracle. Stratify by task length.

## Outcomes

Primary: authorized and verified completion per assigned task. Secondary: human minutes, false success, duplicate effects and total cost.

## Confounds and boundaries

Count unsupported tasks as coverage failures in the overall denominator; also report conditional completion. Freeze model, prompts and budgets before the held-out run.

## Decision and reporting rule

Favor capability investment only if completion improves without worsening prohibited effects and total task cost. Report paired confidence intervals; do not select the best seed.

Record assignment, exclusions, all attempts, versions and budgets. Choose sample size and a stopping rule before confirmatory data collection; publish null and adverse results. Live-service or participant studies require an appropriate separate study setup.

**Methodological context:** [S13: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://arxiv.org/abs/2404.07972v2); [S15: tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains](https://arxiv.org/abs/2406.12045). These sources motivate the design; they did not run this proposed study.
