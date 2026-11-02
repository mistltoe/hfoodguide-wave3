import json, re, sys
from pathlib import Path
P = Path(sys.argv[1]); d = json.loads(P.read_text())
used = set()
def scan(o):
    if isinstance(o, str): used.update(int(x) for x in re.findall(r"\[(\d+)\]", o))
    elif isinstance(o, list): [scan(x) for x in o]
    elif isinstance(o, dict):
        for k, v in o.items():
            if k == "sources": continue
            if k == "source" and isinstance(v, list): used.update(v)
            else: scan(v)
scan(d)
old = [s["n"] for s in d["sources"] if s["n"] in used]
m = {o: i+1 for i, o in enumerate(old)}
def fix(o):
    if isinstance(o, str): return re.sub(r"\[(\d+)\]", lambda x: f"[{m[int(x.group(1))]}]", o)
    if isinstance(o, list): return [fix(x) for x in o]
    if isinstance(o, dict):
        r = {}
        for k, v in o.items():
            if k == "sources": r[k] = v
            elif k == "source" and isinstance(v, list): r[k] = [m[x] for x in v]
            else: r[k] = fix(v)
        return r
    return o
nd = fix(d)
nd["sources"] = [dict(s, n=m[s["n"]]) for s in d["sources"] if s["n"] in m]
P.write_text(json.dumps(nd, ensure_ascii=False, indent=1))
print({k: v for k, v in m.items() if k != v})
