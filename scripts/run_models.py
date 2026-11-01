"""Print all analytical results; no network, credentials or real actions."""
from pathlib import Path
import sys, json, importlib
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'research/experiments'))

def results():
    return {'edition':'2026-11-01','scope':'synthetic analytical results; no empirical estimates',
            'models':{name:importlib.import_module(name).report() for name in
                      ('reliability','marketplace','routing','verification','retry')}}

if __name__=='__main__':print(json.dumps(results(),indent=2,allow_nan=False))
