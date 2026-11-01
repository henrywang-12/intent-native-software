"""Decision arithmetic with explicit perfect-review assumption."""
import json
import math

def compare(success,false_accept,false_reject,loss,check_cost,review_cost):
    for v in (success,false_accept,false_reject):
        if isinstance(v,bool) or not math.isfinite(v) or not 0<=v<=1:
            raise ValueError("invalid probability")
    for v in (loss,check_cost,review_cost):
        if isinstance(v,bool) or not math.isfinite(v) or v<0:
            raise ValueError("invalid cost")
    review=success*false_reject+(1-success)*(1-false_accept)
    unchecked=(1-success)*loss
    checked=check_cost+review*review_cost+(1-success)*false_accept*loss
    return {"unchecked_expected_loss":unchecked,
            "checked_expected_cost_and_loss":checked,
            "review_fraction":review,"net_reduction":unchecked-checked}

def report():
    return {"scope":"hypothetical expected-loss analysis", "unit":"arbitrary cost units",
        "assumptions":["Rejected cases receive perfect human review.",
        "False accepts incur a fixed loss; all costs are linear.",
        "Hard prohibitions override any favorable expected value."],
        "rows":[{"loss":loss,"false_accept":fa,
                 **compare(.9,fa,.05,loss,1.,3.)}
                for loss in (1.,10.,100.,1000.) for fa in (.01,.1,.5)]}

if __name__ == "__main__":
    print(json.dumps(report(),indent=2,allow_nan=False))
