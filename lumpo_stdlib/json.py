# lumpo_stdlib/json.py
import json as _json

def parse(s):
    return _json.loads(s)

def stringify(obj, indent=None):
    return _json.dumps(obj, indent=indent)
