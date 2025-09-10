
# ML Model Development Problem 1  
**Title:** Bias Buster: Fair Loan Approval Classifier (Supervised Learning)

## Scenario
You’re building a binary classifier to **predict loan approvals**. The historical data has **embedded bias** across a protected attribute (`group` ∈ {A, B}).

## Objectives
- Data cleaning & feature engineering
- Model selection: try at least **2 algorithms** (e.g., Logistic Regression, Random Forest)
- Hyperparameter tuning (Grid/Random search ok)
- Validation: **cross-validation**
- Evaluation: **accuracy, precision, recall, F1**
- **Ethics:** compute **Demographic Parity Difference** and **Equal Opportunity Difference**; propose a mitigation (thresholding, reweighting, or feature handling) and document trade-offs (transparency, fairness, accountability, human agency).

## Deliverables
1. Working notebook that:
   - Trains ≥2 models and selects one final model with CV
   - Reports metrics listed above
   - Computes fairness metrics and applies a mitigation
   - Provides **Permutation Feature Importance** (XAI)
   - Produces a short **Model Card** (Markdown cell)
2. Export the final metrics summary as a printed Python dict.

## Scoring (auto-checked in notebook)
- Accuracy ≥ 0.78 and F1 ≥ 0.78 (20 pts)
- Equal Opportunity |Δ| ≤ 0.15 after mitigation (20 pts)
- Demographic Parity |Δ| ≤ 0.15 after mitigation (20 pts)
- Used CV + tuning + feature importance (20 pts)
- Model Card covering transparency/fairness/accountability/human-in-loop (20 pts)

**Total:** 100 pts

## Ethics Notes
- **Transparency**: log data cleaning steps and model choices
- **Explainability**: include feature importance + error analysis
- **Fairness**: measure parity and opportunity; mitigate and justify
- **Accountability & Human Agency**: define a manual review policy for borderline cases

---

**How to run**
- Open `AI_Quest_ML1_Bias_Buster.ipynb` and follow the numbered TODOs.
- Python 3.9+ recommended. Packages: `pandas`, `numpy`, `scikit-learn`, `matplotlib`.
- If needed, run the optional `pip install` cell inside the notebook.
