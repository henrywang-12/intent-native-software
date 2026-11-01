# P07 · Can the system retain utility under hostile content?

**Status: proposed protocol; not run.** The local analytical models are separate artifacts.

## Estimand

Measure legitimate completion and prohibited effects when retrieved data attempts to redirect the planner.

## Design and control

Pair clean and adversarial versions of the same synthetic task. Place controlled hostile text in provider descriptions, receipts and messages; vary placement and phrasing.

## Outcomes

Report the joint table of task success/failure and attacker success/failure, not attack success alone.

## Confounds and boundaries

Hold attacker budget and defender versions fixed, then run adaptive held-out attacks. Do not test against third-party production systems.

## Decision and reporting rule

A defense that blocks all tasks is not a successful assistant. Require the stated effect invariants and disclose utility loss with uncertainty.

Record assignment, exclusions, all attempts, versions and budgets. Choose sample size and a stopping rule before confirmatory data collection; publish null and adverse results. Live-service or participant studies require an appropriate separate study setup.

**Methodological context:** [S24: AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents](https://arxiv.org/html/2406.13352v3); [S25: Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/abs/2302.12173). These sources motivate the design; they did not run this proposed study.
