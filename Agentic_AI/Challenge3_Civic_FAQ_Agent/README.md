
# Challenge 3 — Safety‑Aware FAQ “Civic Helper” Agent

**Goal:** Build a retrieval Q&A agent over `data/faqs/*.txt` with **verbatim citations** (file + line span). Implement clear **refusals** or **redirects** when the answer is out of scope or risky. Include `refusal_policy.md` and `risks.md`.

## Quickstart
```bash
python3 app.py
# Then follow the prompts in terminal, or adapt to a simple web/CLI as you like.
```

## Deliverables
- `answers.md` with 6–10 Q&As (each: 2+ citations **or** a clear refusal)
- `refusal_policy.md` (what triggers refusal + redirect steps)
- `risks.md` (3–5 risks + mitigations)
