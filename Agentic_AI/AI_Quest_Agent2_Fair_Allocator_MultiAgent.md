
# AI Quest — Agentic AI Problem 2  
**Title:** Multi‑Agent Fair Scholarship Allocator (Game‑Theoretic Negotiation)

## Scenario
You must award a limited number of scholarships. Build a **multi‑agent system**:
- **Selector Agent** proposes an allocation based on a composite merit score.
- **Auditor Agent** checks **budget and fairness** constraints and explains disparities.
- **Negotiator Agent** iteratively adjusts thresholds to improve utility **and** fairness.

## Objectives
- Implement a negotiation loop (best‑response or heuristic search)
- Respect **budget** and maintain **fairness**: group allocation rates within ±15% of overall rate
- Log every proposal/critique/change (transparency)
- Provide final allocation + explanation for trade‑offs (accountability & human agency)

## Deliverables
- Working notebook with 3 agents, logs, final allocation vector
- Markdown summary of ethics: transparency, fairness, explainability, override policy

## Scoring (auto-checked in notebook)
- Meets budget exactly (20 pts)
- Overall utility score ≥ baseline greedy (20 pts)
- Group allocation rate gap ≤ 0.15 (20 pts)
- ≥ 8 negotiation turns logged (20 pts)
- Markdown ethics summary present (20 pts)

**Total:** 100 pts
