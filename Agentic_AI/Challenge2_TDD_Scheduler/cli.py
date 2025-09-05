
import sys, csv, json
from scheduler.triage import plan_day

def main():
    if len(sys.argv) < 2:
        print("Usage: python cli.py data/sample_tasks.csv [day_minutes]")
        sys.exit(1)
    path = sys.argv[1]
    day_minutes = int(sys.argv[2]) if len(sys.argv) > 2 else 180
    with open(path, newline="", encoding="utf-8") as f:
        rows = [r for r in csv.DictReader(f)]
    plan = plan_day(rows, day_minutes=day_minutes)
    with open("schedule.json", "w", encoding="utf-8") as out:
        json.dump(plan, out, indent=2)
    print("Wrote schedule.json")

if __name__ == "__main__":
    main()
