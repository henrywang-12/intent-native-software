# Research companion

Read the position paper together with its evidence boundaries. The materials below support independent inspection; protocols and forecasts are not completed studies.

- [Methods and limitations](METHODS.md)
- [Machine-readable source register](sources.json)

## Evidence notes

- [S01 · Situational Awareness: The Decade Ahead](evidence/s01-situational-awareness.md)
- [S02 · Weixin Mini Programs](evidence/s02-weixin-mini-programs.md)
- [S03 · Qwen App advances agentic AI strategy through ecosystem services](evidence/s03-qwen-ecosystem.md)
- [S04 · Introducing apps in ChatGPT and the new Apps SDK](evidence/s04-chatgpt-apps.md)
- [S05 · Announcing the Agent2Agent Protocol](evidence/s05-a2a.md)
- [S06 · MCP architecture, 2025-06-18 specification](evidence/s06-mcp.md)
- [S07 · RFC 9396: OAuth 2.0 Rich Authorization Requests](evidence/s07-rich-authorization.md)
- [S08 · RFC 9110 section 9.2.2: Idempotent methods](evidence/s08-http-idempotence.md)
- [S09 · Sagas](evidence/s09-sagas.md)
- [S10 · Measuring AI Ability to Complete Long Software Tasks](evidence/s10-metr-horizons.md)
- [S11 · Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity](evidence/s11-developer-rct.md)
- [S12 · We are Changing our Developer Productivity Experiment Design](evidence/s12-productivity-update.md)
- [S13 · OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](evidence/s13-osworld.md)
- [S14 · OSWorld 2.0: Benchmarking Computer Use Agents on Long-Horizon Real-World Tasks](evidence/s14-osworld-long-horizon.md)
- [S15 · tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains](evidence/s15-tau-bench.md)
- [S16 · DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](evidence/s16-deepseek-r1.md)
- [S17 · Qwen3 Technical Report](evidence/s17-qwen3.md)
- [S18 · Training Compute-Optimal Large Language Models](evidence/s18-compute-optimal.md)
- [S19 · Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters](evidence/s19-test-time-compute.md)
- [S20 · The Open Source AI Definition 1.0](evidence/s20-open-source-definition.md)
- [S21 · Platform Competition in Two-Sided Markets](evidence/s21-two-sided-markets.md)
- [S22 · Peter Thiel's Quest for One-of-a-Kind Ideas](evidence/s22-zero-to-one.md)
- [S23 · Guidelines for Human-AI Interaction](evidence/s23-human-ai-interaction.md)
- [S24 · AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents](evidence/s24-agentdojo.md)
- [S25 · Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](evidence/s25-indirect-injection.md)
- [S26 · The Ethics of Advanced AI Assistants](evidence/s26-assistant-ethics.md)
- [S27 · Model Cards for Model Reporting](evidence/s27-model-cards.md)
- [S28 · Intent-Native Software: public execution demo](evidence/s28-public-execution-demo.md)
- [S29 · About the Digital Markets Act](evidence/s29-contestability.md)
- [S30 · AI Index 2026: Technical Performance](evidence/s30-ai-index.md)

## Proposed evaluation protocols

- [P01 · Does integration improve authorized completion?](protocols/p01-integration.md)
- [P02 · Can users understand delegated commitments?](protocols/p02-comprehension.md)
- [P03 · Does approval bind to the actual action?](protocols/p03-parameter-drift.md)
- [P04 · Is revocation respected at the dispatch boundary?](protocols/p04-revocation-race.md)
- [P05 · Can recovery avoid duplicate effects?](protocols/p05-ambiguous-timeout.md)
- [P06 · Does compensation preserve its own authority?](protocols/p06-compensation.md)
- [P07 · Can the system retain utility under hostile content?](protocols/p07-injection.md)
- [P08 · Do matching schemas preserve meaning?](protocols/p08-semantic-portability.md)
- [P09 · Can planners change without changing authority?](protocols/p09-model-substitution.md)
- [P10 · Do contracts reduce maintenance cost?](protocols/p10-integration-maintenance.md)
- [P11 · How costly is joining a second host?](protocols/p11-multihoming.md)
- [P12 · Does commercial ranking change user outcomes?](protocols/p12-ranking-incentives.md)
- [P13 · Does catalog growth improve effective liquidity?](protocols/p13-provider-quality.md)
- [P14 · Can users leave with usable task state?](protocols/p14-task-export.md)
- [P15 · Does assistance preserve recovery competence?](protocols/p15-human-recovery.md)
- [P16 · Does integration concentrate failure?](protocols/p16-shared-outage.md)
- [P17 · Can receipts distinguish claims from facts?](protocols/p17-receipt-quality.md)
- [P18 · When is extra reasoning worth its cost?](protocols/p18-compute-allocation.md)
- [P19 · Can different users exercise the same control?](protocols/p19-accessibility.md)
- [P20 · Does repeat use reflect durable value?](protocols/p20-longitudinal-value.md)

## Dated working forecasts

- [F01 · Planner substitution becomes a product feature](forecasts/f01-portable-planners.md)
- [F02 · Task portability moves beyond chat export](forecasts/f02-portable-tasks.md)
- [F03 · Typed capabilities beat GUI automation on bounded tasks](forecasts/f03-capability-advantage.md)
- [F04 · Verification remains a material operating cost](forecasts/f04-verification-cost.md)
- [F05 · Interoperability lowers second-host integration effort](forecasts/f05-multihoming.md)
- [F06 · Open weights support more than prototype deployments](forecasts/f06-open-models.md)
- [F07 · Agent products preserve conventional task controls](forecasts/f07-human-controls.md)
- [F08 · Interoperability does not eliminate gateways](forecasts/f08-concentration.md)
- [F09 · Completion reporting includes unauthorized effects](forecasts/f09-reliability-reporting.md)
- [F10 · The monopoly claim remains unproven without participation data](forecasts/f10-marketplace-thesis.md)

## Executable analytical models

- [Two-sided participation and portability sensitivity](experiments/marketplace.md)
- [Workflow reliability and common-mode failure](experiments/reliability.md)
- [Duplicate-effect risk after ambiguous responses](experiments/retry.md)
- [Cost and quality of cheap-first model routing](experiments/routing.md)
- [The expected-loss tradeoff of verification](experiments/verification.md)

Run model tests with `python3 -m unittest discover -s research/experiments -v` from the repository root. Each model script prints hypothetical results and assumptions as JSON. These are mechanism demonstrations, not measured company or agent performance.
