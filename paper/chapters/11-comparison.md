# 11. A comparison that can be tested


This paper proposes comparing environments along observable dimensions rather than ranking countries. The table below compares hypotheses, alternatives and required measurements. Documented product features remain in the source notes and preceding chapters; these rows are proposed mechanisms, not reported product scores.

| Dimension | Integrated environment hypothesis | Open-web alternative | Required measurement |
|---|---|---|---|
| Discovery | Shared catalog reduces search effort | Federated directories broaden choice | Correct provider selected |
| Identity | Fewer repeated connections | Portable credentials reduce host dependence | Setup and recovery time |
| Meaning | Common contracts reduce mismatch | Domain standards permit substitution | Semantic error rate |
| Authority | One review surface may improve clarity | Independent grants limit host power | Unauthorized effect rate |
| Evidence | Shared status paths simplify recovery | Provider-signed or authoritative records | False success declarations |
| Governance | One operator can resolve disputes | External appeal avoids unilateral control | Resolution time and fairness |

Every row contains a tradeoff. Shared identity can simplify use and increase the consequences of compromise. A common catalog can improve relevance and create incentives to privilege the host's own services. Portable credentials can lower switching costs but create coordination and revocation challenges.

The cleanest experiment uses the same planner and task distribution in both environments. A second experiment varies the planner while holding the environment fixed. Their interaction reveals whether improved models substitute for integration or make integration more valuable.

Measure all assigned tasks, including refusals and unresolved cases. Excluding difficult workflows because one platform cannot support them converts coverage differences into misleading success rates. Report both coverage and conditional success.

This paper provides those experiment designs and sensitivity models. It does not contain a live comparative benchmark of Tencent, Alibaba, OpenAI, Google or Walify. The strongest current conclusion is architectural plausibility with explicit ways to test it.
