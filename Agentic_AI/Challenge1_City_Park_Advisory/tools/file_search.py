
import os
from typing import List, Tuple

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")

def read(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def search(query: str) -> List[Tuple[str, Tuple[int,int], str]]:
    """
    Naive search across data files.
    Returns: [(path, (start_line,end_line), snippet)]
    """
    results = []
    for fname in sorted(os.listdir(DATA_DIR)):
        if not fname.endswith(".txt"):
            continue
        p = os.path.join(DATA_DIR, fname)
        with open(p, "r", encoding="utf-8") as f:
            lines = f.readlines()
        joined = "".join(lines)
        if query.lower() in joined.lower():
            # crude line span (first match)
            for i, line in enumerate(lines, start=1):
                if query.lower() in line.lower():
                    start = max(1, i-1)
                    end = min(len(lines), i+1)
                    snippet = "".join(lines[start-1:end])
                    results.append((p, (start, end), snippet.strip()))
                    break
    return results
