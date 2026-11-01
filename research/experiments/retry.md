# Duplicate-effect risk after ambiguous responses

**Synthetic analytical model; no empirical measurements.**

Condition on an ambiguous response. Let p be the probability the original effect committed, d the probability deduplication is effective and v the probability a read reveals a committed effect. One blind retry has duplicate probability p(1-d). Reading first but retrying after missing evidence gives p(1-v)(1-d), under the stated conditional-independence assumption.

A read-only policy produces no new duplicates but leaves probability 1-pv unresolved after that observation. This includes truly absent effects because a missing read cannot establish absence in the assumed interface. Availability is traded for restraint; zero duplicates is not full task success.

Run `python3 research/experiments/retry.py`. The model does not implement network calls or validate any provider. Its purpose is to expose the assumptions behind a retry policy, especially deduplication expiry and delayed visibility.
