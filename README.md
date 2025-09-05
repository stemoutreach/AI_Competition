
# AI_Competition — High‑School AI Mini‑Challenges
Short, hands‑on **Agentic AI** and **Machine Learning** challenges designed for high‑school teams to complete in **1–3 hours**. Perfect for a 3–4 hour mini‑competition day or in‑class labs.

- **Agentic AI Track** → small agent systems (plan→act→observe→revise), safe refusals, transparent citations/logs, and one **Test‑Driven Development (TDD)** build.
- **Machine Learning Track** → notebook‑based modules focused on data literacy, curation & bias, simple baselines, and clear communication.

> Internet/LLM use is optional and must be disclosed. All work follows a DoD‑aligned AI Ethics checklist (Responsible, Equitable, Traceable, Reliable, Governable).

---

## Contents
- [Tracks & Folders](#tracks--folders)
- [Quick Start](#quick-start)
- [Ethics & LLM Policy](#ethics--llm-policy)
- [Judging & Scoring](#judging--scoring)
- [Event Day Flow](#event-day-flow)
- [Submission Checklist](#submission-checklist)
- [Contributing](#contributing)
- [License](#license)

---

## Tracks & Folders

### Agentic AI
**Folder:** [`Agentic_AI/`](./Agentic_AI/README.md)

| ID | Challenge | Duration | Focus | Primary Deliverables |
|---|---|---:|---|---|
| A1 | **[Challenge1_City_Park_Advisory](./Agentic_AI/Challenge1_City_Park_Advisory/)** | 1.5–2h | PAOR agent over local files; evidence‑based memo | `memo.md`, `decision_checklist.md`, `trace.json` |
| A2 | **[Challenge2_TDD_Scheduler](./Agentic_AI/Challenge2_TDD_Scheduler/)** | 2–3h | **TDD** + useful day scheduler; optional agentic replanning | Passing tests, `schedule.json`, `TDD_NOTES.md` |
| A3 | **[Challenge3_Civic_FAQ_Agent](./Agentic_AI/Challenge3_Civic_FAQ_Agent/)** | 1–2h | Retrieval Q&A with **verbatim citations** & **refusal policy** | `answers.md`, `refusal_policy.md`, `risks.md` |

See the track landing page: [`Agentic_AI/README.md`](./Agentic_AI/README.md).

---

### Machine Learning
**Folder:** [`Machine_Learning/`](./Machine_Learning/README.md)

**Notebooks included:**
- [`Machine_Learning/Getting_Started_DS101_Intro_Notebook.ipynb`](./Machine_Learning/Getting_Started_DS101_Intro_Notebook.ipynb) — Jupyter basics, CSVs, simple charts.
- [`Machine_Learning/Bias_Buster_Challenge_Solution.ipynb`](./Machine_Learning/Bias_Buster_Challenge_Solution.ipynb) — Data curation, imbalance, bias notes.
- [`Machine_Learning/Sentiment_Switch_Challenge_Solution.ipynb`](./Machine_Learning/Sentiment_Switch_Challenge_Solution.ipynb) — Lightweight text classification workflow.
- [`Machine_Learning/Emotion_Translator_Challenge_Solution.ipynb`](./Machine_Learning/Emotion_Translator_Challenge_Solution.ipynb) — Simple NLP feature engineering & evaluation.

See the track landing page: [`Machine_Learning/README.md`](./Machine_Learning/README.md).

---

## Quick Start

> **Python 3.10+** recommended.

### Agentic AI (examples)
```bash
# A1 — City Park Advisory
cd Agentic_AI/Challenge1_City_Park_Advisory
python3 main.py   # creates trace.json
# Then write memo.md and decision_checklist.md using cited evidence

# A2 — TDD Scheduler
cd Agentic_AI/Challenge2_TDD_Scheduler
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest -q  # expect FAIL first (RED) → implement → pass (GREEN) → refactor
python cli.py data/sample_tasks.csv  # creates schedule.json

# A3 — Civic FAQ Agent
cd Agentic_AI/Challenge3_Civic_FAQ_Agent
python3 app.py
```

### Machine Learning (examples)
```bash
cd Machine_Learning
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt  # if present
jupyter notebook  # or jupyter lab
# open any of the notebooks listed above and follow the cells
```

**Deliverables (all entries)**
- Required files listed in the specific challenge/track README
- A short **README** with run steps & assumptions
- **Ethics checklist** (see below)
- If LLMs used: `prompts.md` with exact prompts and a note on edited outputs

---

## Ethics & LLM Policy

### DoD‑Aligned Ethics
All submissions should demonstrate:
- **Responsible** — State assumptions & uncertainties; avoid unsupported claims.
- **Equitable** — Consider diverse users; inclusive language; note fairness impacts.
- **Traceable** — Use citations (file+lines), tests/logs, or run traces; disclose prompts.
- **Reliable** — Deterministic where possible; handle edge cases; note limits.
- **Governable** — Provide safe‑fail behavior (refuse/redirect) and rollback/stop criteria.

### LLM Usage Policy
- LLMs may be used for brainstorming or generation **only if** you include `prompts.md` and clearly mark any edited outputs.
- **No web scraping** or external datasets unless the folder’s README explicitly allows it.
- Cite any sources used.

---

## Judging & Scoring

Standard **100‑point** rubric:

| Category | Points | What judges look for |
|---|---:|---|
| Correctness / Accuracy | 25 | Output matches task & data; reasoning is sound |
| Traceability (citations/tests/logs) | 20 | Evidence links; tests/logs; transparent prompts |
| Safety & Ethics | 20 | DoD alignment; refusals/rollback; bias mitigation |
| Tool Use / TDD Discipline | 15 | Purposeful tool use; **TDD** steps for A2 |
| Usefulness & Clarity | 20 | Clear writing/UI; actionable outputs |
| **Total** | **100** |  |

**Tie‑breakers:** (1) stronger ethics; (2) better traceability; (3) higher human usefulness.

---

## Event Day Flow (3–4 hours suggested)
1. **Kickoff (10–15 min)**: rules, ethics, deliverables, scoring.  
2. **Work time (90–140 min)**: teams build and document.  
3. **Submission (10–15 min)**: zip or push following the track’s checklist.  
4. **Judging (30–60 min, parallel)**: apply rubric; verify ethics & traceability.  
5. **Demos & Awards (15–30 min)**: 2‑minute pitches + Q&A.

---

## Submission Checklist
- Required files present and named correctly  
- Repro steps work with provided data  
- Ethics checklist complete  
- `prompts.md` included if LLMs used

---

## Contributing
PRs welcome! To add a new challenge/module:
1. Propose a brief (goals, outcomes, deliverables, rubric, ethics).  
2. Include **starter code/data** and a one‑page `README.md`.  
3. Add tests where applicable (especially TDD‑style challenges).

**Code of Conduct:** Be kind, constructive, inclusive.

---

## License
TBD by repo owner (MIT/Apache‑2.0/CC‑BY‑SA, etc.). Add a `LICENSE` file and reference it here.

---

### Repo Map (for reference)
```
AI_Competition/
├─ README.md  ← (this file)
├─ Agentic_AI/
│  ├─ Challenge1_City_Park_Advisory/
│  ├─ Challenge2_TDD_Scheduler/
│  ├─ Challenge3_Civic_FAQ_Agent/
│  └─ README.md
└─ Machine_Learning/
   ├─ Bias_Buster_Challenge_Solution.ipynb
   ├─ Emotion_Translator_Challenge_Solution.ipynb
   ├─ Getting_Started_DS101_Intro_Notebook.ipynb
   ├─ Sentiment_Switch_Challenge_Solution.ipynb
   └─ README.md
```
