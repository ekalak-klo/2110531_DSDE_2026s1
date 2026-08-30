---
title: "Lab Week03 Decision Trees"
tags:
  - source
  - dsde
  - week3
---

# Lab — Decision Trees & Random Forests

| | |
|--|--|
| Notebook | `code/Week03_ML/1_Decision_Trees_Random_Forests_v4.ipynb` |
| Dataset | `datasets/diabetes.csv` (via GitHub raw URL) |
| Target | `diabetes` (0=absent, 1=present) |
| Split | `test_size=0.30`, `random_state=30`, `stratify=y` |

Baseline model:

```python
DecisionTreeClassifier(min_samples_leaf=10, max_depth=3, criterion='entropy')
```

Assignment extension: [[Week03 Decision Tree Ensembles]]
