# Workflow reliability and common-mode failure

**Synthetic analytical model; no empirical measurements.**

For n required steps with conditional success p and a workflow-wide outage probability q, success is (1-q)p^n. The n=0 convention is one: no action is required. The model assumes conditional independence, no recovery and a common event that blocks the whole workflow. It does not estimate p or q from data.

At p=0.98, twenty independent required steps yield about 0.668 completion. Reducing the required steps to five gives about 0.904 under the same assumption. This demonstrates a mechanism by which integration could help; it is not a measured superapp advantage. Common failures can offset the benefit.

Run `python3 research/experiments/reliability.py`. Vary p, n and q through the importable function. Compare with protocol P01 before making real-world claims.
