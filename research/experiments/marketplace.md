# Two-sided participation and portability sensitivity

**Synthetic analytical model; no empirical measurements.**

This toy model uses u(t+1) = 0.5u(t) + 0.5 sigmoid(-4 + b(1-m)s(t)), with a symmetric equation for suppliers. Participation is normalized to [0,1]. b is cross-side feedback; m is a hypothetical portability parameter reducing dependence on this host. Neither is estimated.

At b=8 and m=0, low and high initial participation approach different fixed points. This shows how feedback can preserve an initial advantage under selected assumptions. It does not establish that actual agent markets tip, that the first entrant wins, or that one stable point is socially preferable.

Increasing m in this model weakens host participation because outside value is held fixed and only the feedback term changes. Do not interpret that as evidence that portability reduces total market welfare. A model with adoption benefits from portability could give a different result. Run `python3 research/experiments/marketplace.py`; the residual reports closeness to a fixed point.
