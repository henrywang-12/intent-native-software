# Cost and quality of cheap-first model routing

**Synthetic analytical model; no empirical measurements.**

A cheap model succeeds with probability p. Its checker falsely rejects correct answers with probability r and falsely accepts wrong answers with probability a. The escalation fraction is e = 1 - p(1-r) - (1-p)a. If fallback success on that escalated subset is q, final correctness is p(1-r)+eq; expected cost is c_cheap+c_check+e c_strong.

The distinction between overall strong-model quality and quality on difficult escalated cases matters. The function's q is explicitly conditional. Treating an aggregate benchmark score as q can overstate routing quality. False acceptance can make a cheap pipeline look economical by silently keeping wrong answers.

Costs are arbitrary units, not provider prices. The script compares a hypothetical strong-only baseline but does not include real verification, support or tool costs. Run `python3 research/experiments/routing.py`; use protocol P18 for a measured comparison.
