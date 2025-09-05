
# Challenge 2 — TDD Software Build: Task Triage & Scheduler Agent

**Goal:** Use **TDD** to implement a small, useful program that reads `data/sample_tasks.csv` and outputs `schedule.json` (ordered with start times, short breaks, and flags for infeasible items).

## Quickstart
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest -q  # expect FAIL at first (red)
# Implement minimal code to pass, then refactor (green -> refactor)
```

## Deliverables
- Passing tests (include a screenshot or report)
- `schedule.json`
- `TDD_NOTES.md` (red->green->refactor steps)

## Optional
- `cli.py` to run: `python cli.py data/sample_tasks.csv`
