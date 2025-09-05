[
# AI_Competition — Agentic AI Challenges for High School

**Short, hands‑on AI competition kits (1–3 hours each)** focused on **agentic AI**, **responsible AI ethics**, and **practical software skills**. This repo enables organizers to run a 3–4 hour event where teams tackle one of several challenges, produce clear deliverables, and are evaluated with a transparent rubric.

> Audience: **Students (HS)**, **Organizers/Mentors**, **Judges**  
> Tech stack: Python 3.10+, basic CLI, optional LLM access with disclosure (see policy)

---

## Why this repo
- **Accessible**: time‑boxed challenges that fit a class period or half‑day event.
- **Agentic AI**: emphasizes *plan–act–observe–revise* loops, tool use, and safe refusals.
- **Ethics‑first**: aligned to DoD AI principles (Responsible, Equitable, Traceable, Reliable, Governable).
- **Real skills**: includes a **Test‑Driven Development (TDD)** challenge to grow software engineering discipline.

---

## Challenges (pick one per team)
| ID | Title | Duration | Focus | Primary Deliverables |
|---|---|---:|---|---|
| C1 | **City Park Advisory** | 1.5–2h | Agent loop over local files; evidence‑based writing | `memo.md`, `decision_checklist.md`, `trace.json` |
| C2 | **TDD Task Scheduler (Agent‑aware)** | 2–3h | **TDD** + useful planning tool; optional replanning step | Passing tests, `schedule.json`, `TDD_NOTES.md` |
| C3 | **Civic Helper FAQ Agent** | 1–2h | Retrieval with **citations** and **refusal policy** | `answers.md`, `refusal_policy.md`, `risks.md` |

> Each challenge has its own README, starter code/data, and clear outcomes.

### Repository Structure (recommended)
```
AI_Competition/
├─ challenges/
│  ├─ challenge1_city_park_advisory/
│  ├─ challenge2_tdd_scheduler/
│  └─ challenge3_civic_faq_agent/
├─ universal/
│  ├─ judge_score_sheet.md
│  └─ submission_checklist.md
├─ docs/
│  └─ Agentic_AI_Mini_Challenges.md   # overview & organizer notes (optional)
└─ README.md
```
> Adjust paths if your folder names differ. Keep challenge folders self‑contained (data, tools, app/tests).

---

## Ethics & Safety (DoD‑aligned)
All teams must include an **Ethics Checklist** in their submission. Judges verify that work is:
- **Responsible** — limits are stated; uncertainties and assumptions are called out.
- **Equitable** — considers diverse users; avoids stigmatizing or exclusionary language.
- **Traceable** — key claims are tied to citations, tests, or logs; prompts are disclosed.
- **Reliable** — outputs are consistent/deterministic where applicable; edge cases considered.
- **Governable** — includes stop/rollback criteria and safe‑fail behavior (e.g., refuse/redirect).

**LLM Usage Policy**
- Allowed to use LLMs for brainstorming and code/text generation **only if** you include `prompts.md` with the exact prompts and note where you **edited** outputs.
- **No web scraping** or external datasets unless explicitly provided by organizers.
- Cite all sources used (even if AI‑assisted).

---

## Quick Start (Students)
1. **Pick your challenge** in `/challenges/*` and read its README.  
2. **Set up Python** (3.10+ recommended):  
   ```bash
   python3 -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt  # if provided
   ```
3. **Build & run** according to the challenge README. Common patterns:
   - C1: `python3 main.py` → produces `trace.json` → write `memo.md` & `decision_checklist.md`
   - C2: `pytest -q` (RED) → implement → `pytest -q` (GREEN) → refactor → `python cli.py data/sample_tasks.csv`
   - C3: `python3 app.py` → ask questions in terminal → compile `answers.md` with citations

**Deliverables (all challenges)**
- A small **README** (how to run + assumptions)
- Required files listed in the challenge (see table above)
- **Ethics Checklist** (filled)
- If LLMs used: `prompts.md` with notes on any edits

---

## Event Day Flow (3–4 hours)
1. **Kickoff (10–15 min)**: Rules, ethics, deliverables, scoring.  
2. **Work time (90–140 min)**: Teams build and document.  
3. **Submission (10–15 min)**: Zip or push to repo following the **submission checklist**.  
4. **Judging (30–60 min, parallel)**: Use sheet below; confirm ethics & traceability.  
5. **Demos & Awards (15–30 min)**: 2‑minute pitches + judge Q&A.

**Submission Checklist** (see `/universal/submission_checklist.md`)
- Required files present and named correctly
- Repro steps work with provided data
- Ethics checklist complete
- `prompts.md` included if LLMs used

---

## Judging & Scoring
Use the standard 100‑point rubric (see `/universal/judge_score_sheet.md`).

| Category | Points | What judges look for |
|---|---:|---|
| Correctness / Accuracy | 25 | Output matches task & data; reasoning sound |
| Traceability (citations/tests/logs) | 20 | Evidence links; tests or logs; transparent prompts |
| Safety & Ethics | 20 | DoD alignment; refusals/rollback; bias mitigation |
| Tool Use / TDD Discipline | 15 | Purposeful tool use; TDD steps for C2 |
| Usefulness & Clarity | 20 | Clear writing/UI; actionable outputs |
| **Total** | **100** |  |

**Tie‑breakers**: (1) stronger ethics; (2) better traceability; (3) higher human usefulness.

---

## Organizer Guide
- Print or package each challenge’s **Info Pack** / dataset.  
- Provide **starter folders** to teams (minimal, commented).  
- Clarify Internet/LLM policy and submission method.  
- Recruit enough judges to score in parallel (2 per room is ideal).  
- Prepare a timing bell or slide with checkpoints (start / 60m / 30m / 10m / stop).

**Hardware/Software**
- Student laptops with Python 3.10+
- Optional: offline LLM access or none (competition works without it)
- Editors: VS Code/IDEs allowed

---

## Contributing
Pull requests are welcome! Please open an issue first to discuss scope. For major changes:
1. Propose a challenge outline (brief, outcomes, deliverables, rubric, ethics).  
2. Provide **starter code/data** and a 1–page README for the challenge.  
3. Add/update tests where applicable (especially for TDD‑style challenges).

**Code of Conduct**: Be kind, constructive, and inclusive. We actively encourage contributions that improve accessibility and equity.

---

## License
TBD by repo owner (e.g., MIT/Apache‑2.0/CC‑BY‑SA for docs). Add your choice in `LICENSE` and mention it here.

---

## Acknowledgments
- Community educators and students who piloted early versions of these exercises.  
- Industry guidance on agentic systems and model interoperability; and public‑sector conversations on AI ethics that inspire the DoD‑aligned checklist.

> Questions or ideas? Open an issue or start a discussion in this repo.
](https://github.com/stemoutreach/AI_Competition/blob/main/README.md)
