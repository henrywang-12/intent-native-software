"""An unestimated dynamical model; it predicts no actual market shares."""
import json
import math

def sigmoid(x):
    if x >= 0:
        z=math.exp(-x)
        return 1/(1+z)
    z=math.exp(x)
    return z/(1+z)

def evolve(start, feedback=8.0, portability=0.0, steps=400):
    values=(start,feedback,portability)
    if any(isinstance(v,bool) or not math.isfinite(v) for v in values):
        raise ValueError("finite numeric inputs required")
    if not 0<=start<=1 or not 0<=portability<=1 or feedback<0:
        raise ValueError("invalid participation, feedback or portability")
    if isinstance(steps,bool) or not isinstance(steps,int) or steps<0:
        raise ValueError("steps must be a nonnegative integer")
    u=s=start
    effective=feedback*(1-portability)
    for _ in range(steps):
        # Intrinsic value minus outside option is fixed at -4.
        next_u=sigmoid(-4+effective*s)
        next_s=sigmoid(-4+effective*u)
        u,s=.5*u+.5*next_u,.5*s+.5*next_s
    residual=max(abs(u-sigmoid(-4+effective*s)),
                 abs(s-sigmoid(-4+effective*u)))
    return {"users":u,"suppliers":s,"fixed_point_residual":residual}

def report():
    return {"scope":"unestimated mechanism model", "assumptions":[
        "Symmetric populations, logistic response, fixed outside option.",
        "Portability only reduces host-specific cross-side feedback.",
        "No prices, strategic entrants, heterogeneous preferences or regulation.",
        "Portability's participation level effect is not a welfare estimate."],
        "rows":[{"start":start,"feedback":f,"portability":p,
                 **evolve(start,f,p)}
                for f in (2.,5.,8.,10.) for p in (0.,.25,.5,.75)
                for start in (.05,.95)]}

if __name__ == "__main__":
    print(json.dumps(report(),indent=2,allow_nan=False))
