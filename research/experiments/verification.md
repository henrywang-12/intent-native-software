# The expected-loss tradeoff of verification

**Synthetic analytical model; no empirical measurements.**

Without checking, expected loss is (1-p)L. A checker sends a fraction pr+(1-p)(1-a) to review, where p is initial success, r false rejection and a false acceptance. Checked expected cost plus loss is c_check + [pr+(1-p)(1-a)]c_review + (1-p)aL.

The model assumes perfect correction by reviewers and a fixed loss for every undetected error. Neither assumption should be carried into a deployment without evidence. It excludes correlated failures, delayed discovery and reviewer fatigue. Some actions remain prohibited even if a favorable average can be computed.

The purpose is to show why verification can be rational for high-consequence tasks and wasteful for some low-consequence tasks. Run `python3 research/experiments/verification.py`. All values are hypothetical and should not be used as financial or operational advice.
