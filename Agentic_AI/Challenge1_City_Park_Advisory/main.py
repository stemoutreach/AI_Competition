
import json
from tools.file_search import search

TRACE = []

def log(step, detail):
    TRACE.append({"step": step, "detail": detail})

def plan(query:str):
    log("plan", f"Initial plan to investigate: {query}")
    return [
        {"act": "search", "args": {"query": "access"}},
        {"act": "search", "args": {"query": "lighting"}},
        {"act": "search", "args": {"query": "budget"}},
    ]

def act(action):
    if action["act"] == "search":
        q = action["args"]["query"]
        res = search(q)
        log("observe", {"query": q, "results": [{"path": p, "lines":ls, "snippet": sn[:120]} for p,ls,sn in res]})
        return res
    return []

def revise(evidence):
    log("revise", "Choose top 3 pieces of evidence and draft memo (TODO: student writes memo.md & checklist).")
    # TODO(student): Generate memo.md and decision_checklist.md using evidence + additional searches.

def save_trace():
    with open("trace.json", "w", encoding="utf-8") as f:
        json.dump(TRACE, f, indent=2)

def main():
    actions = plan("Should the city expand the park with attention to cost, environment, and accessibility?")
    evidence = []
    for a in actions:
        evidence.extend(act(a))
    revise(evidence)
    save_trace()
    print("Trace saved to trace.json. Now write memo.md and decision_checklist.md using your findings.")

if __name__ == "__main__":
    main()
