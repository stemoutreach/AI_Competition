
import os, re
from typing import List, Tuple

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "faqs")

def read(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def search_files(query: str, k: int = 3) -> List[Tuple[str, Tuple[int,int], str]]:
    """Naive keyword search over FAQ text files."""
    hits = []
    for fname in sorted(os.listdir(DATA_DIR)):
        if not fname.endswith(".txt"):
            continue
        p = os.path.join(DATA_DIR, fname)
        text = read(p)
        # Find first matching line
        for line in text.splitlines():
            if query.lower() in line.lower():
                m = re.match(r"(\d+):\s*(.*)", line)
                if m:
                    ln = int(m.group(1))
                    start, end = max(1, ln-1), ln+1
                else:
                    start, end = 1, 1
                snippet = "\n".join(text.splitlines()[start-1:end])
                hits.append((p, (start, end), snippet))
                break
        if len(hits) >= k:
            break
    return hits
