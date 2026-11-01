"""One-retry probability model, not a distributed transaction guarantee."""
import json
import math

def risk(committed_given_unknown,dedup_effective,visibility):
    for v in (committed_given_unknown,dedup_effective,visibility):
        if isinstance(v,bool) or not math.isfinite(v) or not 0<=v<=1:
            raise ValueError("invalid probability")
    p,d,v=committed_given_unknown,dedup_effective,visibility
    return {"blind_retry_duplicate_probability":p*(1-d),
            "read_then_retry_on_missing_duplicate_probability":p*(1-v)*(1-d),
            "read_only_duplicate_probability":0.,
            "read_only_unresolved_probability":1-p*v}

def report():
    return {"scope":"hypothetical ambiguous-response analysis", "assumptions":[
        "A retry commits unless deduplication recognizes an existing effect.",
        "A positive read is authoritative; a missing read is not proof of absence.",
        "Visibility and deduplication are conditionally independent given commitment.",
        "Read-only policy waits on missing evidence, including truly absent effects."],
        "rows":[{"committed_given_unknown":p,"dedup_effective":d,"visibility":v,
                 **risk(p,d,v)} for p in (.1,.5,.9) for d in (0.,.9,1.)
                for v in (.5,.9,1.)]}

if __name__ == "__main__":
    print(json.dumps(report(),indent=2,allow_nan=False))
