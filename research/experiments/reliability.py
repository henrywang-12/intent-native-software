"""Illustrative probabilities, not empirical agent measurements."""
import json
import math

def probability(value):
    if isinstance(value, bool) or not math.isfinite(value) or not 0 <= value <= 1:
        raise ValueError("probability must be finite and between zero and one")
    return value

def completion(step_success, steps, common_failure=0.0):
    probability(step_success)
    probability(common_failure)
    if isinstance(steps, bool) or not isinstance(steps, int) or steps < 0:
        raise ValueError("steps must be a nonnegative integer")
    if steps == 0:
        return 1.0
    return (1-common_failure) * step_success ** steps

def report():
    return {"scope":"hypothetical sensitivity analysis", "assumptions":[
        "All steps are required; no retries or recovery.",
        "Steps are independent conditional on no common-mode failure.",
        "Common-mode failure blocks every nonempty workflow."],
        "rows":[{"steps":n,"step_success":p,"common_failure":q,
                 "completion":completion(p,n,q)}
                for p in (0.95,0.98,0.995) for n in (1,5,10,20)
                for q in (0.0,0.02)]}

if __name__ == "__main__":
    print(json.dumps(report(), indent=2, allow_nan=False))
