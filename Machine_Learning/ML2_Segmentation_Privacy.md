
# ML Model Development Problem 2  
**Title:** Segments & Sensitivity: Clustering with a Privacy Twist (Unsupervised)

## Scenario
You must segment users for personalized messaging. Clustering should be **useful** yet **respect privacy** and **avoid disparate impact** on a protected group.

## Objectives
- Data cleaning & scaling
- Compare **KMeans** and **Gaussian Mixture** (or DBSCAN)
- Model selection: choose K via **elbow & silhouette**
- Validation: **stability via bootstrapping**
- **Ethics:** evaluate whether clusters disproportionately isolate a protected group; implement a simple **differential-privacy-like noise** mechanism and discuss the utility trade‑off.

## Deliverables
1. Notebook that fits ≥2 clustering methods, chooses K, and compares solutions
2. Stability analysis over bootstraps (e.g., Adjusted Rand Index)
3. Fairness analysis across clusters (distribution by protected attribute)
4. A small **Data Sheet** Markdown cell describing privacy choices and limitations

## Scoring (auto-checked in notebook)
- Silhouette ≥ 0.35 **without** privacy noise (20 pts)
- Stability ARI median ≥ 0.40 (20 pts)
- After adding noise, silhouette drop ≤ 0.15 absolute (utility preserved) (20 pts)
- Fairness check reported + no cluster with >70% from one group unless justified (20 pts)
- Data Sheet provided (20 pts)

**Total:** 100 pts

## Ethics Notes
- **Fairness:** check protected group representation per cluster
- **Transparency & Explainability:** document K choice, method selection, and noise parameter
- **Privacy:** add Gaussian noise to features; discuss trade-offs
- **Human Agency:** recommend human override when segment-driven actions affect individuals

---

**How to run**
Open `AI_Quest_ML2_Segmentation_Privacy.ipynb` and follow TODOs.
