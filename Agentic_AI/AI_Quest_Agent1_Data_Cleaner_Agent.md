
# AI Quest — Agentic AI Problem 1  
**Title:** Single‑Agent Data Cleaner & Modeler (with Human‑in‑the‑Loop)

## Scenario
Design a **single agent** that chooses from available **tools** to clean data, engineer features, train a model, and meet **accuracy and fairness** targets. The agent must log actions (transparency) and request **human approval** before executing its plan.

## Tools (provided as Python functions)
- `preview_data()`, `impute_numeric()`, `encode_categorical()`, `scale_numeric()`
- `train(algorithm)`, `evaluate()`, `check_fairness()`
- `set_thresholds(th_A, th_B)` (group-aware mitigation)

## Objectives
- Implement an agent loop: **plan → (human approve) → act → evaluate → iterate**
- Achieve target metrics; keep a **transparent action log**
- Include a **stop condition** and **fallback policy**

## Deliverables
- Working notebook with agent class, action log, final metrics, and fairness
- Short Markdown: explain **why** the final plan is acceptable (accountability + human agency)

## Scoring (auto-checked in notebook)
- Accuracy ≥ 0.78 and F1 ≥ 0.78 (30 pts)
- Equal Opportunity |Δ| ≤ 0.15 after mitigation (30 pts)
- Action log contains ≥ 6 steps incl. human approval checkpoint (20 pts)
- Markdown rationale provided (20 pts)

**Total:** 100 pts

## Ethics
- **Transparency:** action log
- **Explainability:** report feature importance
- **Fairness:** parity/opportunity checks + mitigation
- **Human Agency:** explicit approval gate to proceed
