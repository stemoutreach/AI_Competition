
import csv, os
from scheduler.triage import plan_day

SAMPLE = os.path.join(os.path.dirname(__file__), "..", "data", "sample_tasks.csv")

def load_rows():
    with open(SAMPLE, newline="", encoding="utf-8") as f:
        return [r for r in csv.DictReader(f)]

def test_plan_day_structure():
    rows = load_rows()
    plan = plan_day(rows, day_minutes=120)
    assert isinstance(plan, list)
    assert all(set(["task","start","duration","notes"]).issubset(p.keys()) for p in plan)

def test_plan_day_time_budget():
    rows = load_rows()
    plan = plan_day(rows, day_minutes=120)
    total = sum(int(p.get("duration",0)) for p in plan if p.get("duration"))
    assert total <= 120
