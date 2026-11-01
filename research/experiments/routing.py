"""Hypothetical cost-quality arithmetic, not a model benchmark."""
import json
import math

def evaluate(cheap_success,strong_success,false_accept,false_reject,
             cheap_cost=1.,strong_cost=8.,check_cost=.5):
    ps=(cheap_success,strong_success,false_accept,false_reject)
    costs=(cheap_cost,strong_cost,check_cost)
    if any(isinstance(v,bool) or not math.isfinite(v) or not 0<=v<=1 for v in ps):
        raise ValueError("invalid probability")
    if any(isinstance(v,bool) or not math.isfinite(v) or v<0 for v in costs):
        raise ValueError("invalid cost")
    accepted_correct=cheap_success*(1-false_reject)
    accepted_wrong=(1-cheap_success)*false_accept
    escalated=1-accepted_correct-accepted_wrong
    return {"correct_probability":accepted_correct+escalated*strong_success,
            "accepted_wrong_without_escalation":accepted_wrong,
            "escalation_probability":escalated,
            "expected_cost":cheap_cost+check_cost+escalated*strong_cost}

def report():
    return {"scope":"hypothetical routing sensitivity", "cost_unit":"arbitrary units",
        "assumptions":["Fallback success is conditional on the escalated subset.",
        "Verifier is applied to cheap outputs; strong outputs are final.",
        "No external actions occur; costs omit human recovery and service fees."],
        "rows":[{"cheap_success":p,"false_accept":fa,
                 **evaluate(p,.95,fa,.05)}
                for p in (.4,.6,.8,.9) for fa in (0.,.05,.2)],
        "strong_only":{"cost":8.,"correct_probability":.95}}

if __name__ == "__main__":
    print(json.dumps(report(),indent=2,allow_nan=False))
