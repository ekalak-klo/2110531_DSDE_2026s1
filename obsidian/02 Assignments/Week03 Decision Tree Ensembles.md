---
title: "Week03 Decision Tree Ensembles"
course: "2110531 DSDE"
week: 3
status: done
tags:
  - assignment
  - dsde
  - week3
  - decision-tree
  - random-forest
  - gradient-boosting
aliases:
  - สรุปการบ้าน week3
  - Decision Tree RF GB assignment
created: 2026-08-23
sources:
  - "[[Lab Week03 Decision Trees]]"
  - "homework/attachment_week3/"
answers:
  baseline_macro_f1: 0.8770
  random_forest_macro_f1: 0.8848
  gradient_boosting_macro_f1: 0.8968
  best_model: Gradient Boosting
---

# Week 3 — Decision Tree → Random Forest & Gradient Boosting

> [!abstract] งาน
> จาก lab Decision Tree บน diabetes dataset → ลอง **Random Forest** และ **Gradient Boosting** โดย **manual tune hyperparameters** แล้วให้ **Macro-F1** สูงกว่า baseline

**โจทย์:** `homework/attachment_week3/problems/` (lab v4 + README)  
**Notebook ส่ง:** `homework/attachment_week3/hw_week3_decision_tree_ekalak.ipynb`  
**Notebook สอน:** `homework/attachment_week3/walkthrough_week3.ipynb`

---

## Dataset & split

| | |
|--|--|
| ไฟล์ | `diabetes.csv` (2000 rows) |
| target | `diabetes` |
| features | `age`, `hypertension`, `heart_disease`, `bmi`, `blood_glucose_level`, `gender`, `smoking_history` |
| split | 70/30, `random_state=30`, `stratify=y` |

Class ไม่สมดุล → ใช้ [[Macro-F1]] แทน accuracy อย่างเดียว

---

## Baseline — Decision Tree

```python
DecisionTreeClassifier(min_samples_leaf=10, max_depth=3, criterion='entropy')
```

| Metric | ค่า |
|--------|-----|
| **Macro-F1** | **0.8770** |
| recall `present` | 0.6275 |

---

## Random Forest (manual tune)

ลอง grid มือ (ไม่ใช้ GridSearchCV): `n_estimators` × `max_depth` × `min_samples_leaf` × `criterion`

> [!example] Best config
> `n_estimators=100, max_depth=8, min_samples_leaf=1, criterion='gini'`

| Metric | ค่า |
|--------|-----|
| **Macro-F1** | **0.8848** |
| Δ vs baseline | +0.0078 |

---

## Gradient Boosting (manual tune)

ลอง: `n_estimators` × `max_depth` × `learning_rate` × `min_samples_leaf`

> [!example] Best config
> `n_estimators=200, max_depth=4, learning_rate=0.1, min_samples_leaf=20`

| Metric | ค่า |
|--------|-----|
| **Macro-F1** | **0.8968** |
| Δ vs baseline | +0.0198 |

---

## สรุปเปรียบเทียบ

| Model | Macro-F1 |
|-------|----------|
| Decision Tree (baseline) | 0.8770 |
| Random Forest | 0.8848 |
| **Gradient Boosting** | **0.8968** ← best |

**Best Macro-F1 achieved: 0.8968** (Gradient Boosting)

---

## Textbox สำหรับส่ง (copy ได้)

```
Experiments on diabetes.csv (70/30 stratified split, random_state=30):

1. Baseline Decision Tree (min_samples_leaf=10, max_depth=3, criterion=entropy): Macro-F1 = 0.8770

2. Random Forest — manually tried combinations of n_estimators {100,200,300}, max_depth {5,8,None}, min_samples_leaf {1,5,10}, criterion {gini,entropy}. Best: n_estimators=100, max_depth=8, min_samples_leaf=1, criterion=gini → Macro-F1 = 0.8848 (+0.0078)

3. Gradient Boosting — manually tried n_estimators {100,200}, max_depth {2,3,4}, learning_rate {0.05,0.1,0.2}, min_samples_leaf {5,10,20}. Best: n_estimators=200, max_depth=4, learning_rate=0.1, min_samples_leaf=20 → Macro-F1 = 0.8968 (+0.0198)

Best overall: Gradient Boosting with Macro-F1 = 0.8968. Both ensemble models beat the baseline; GB improved recall on the minority class (present) the most.
```

---

## ทำไม ensemble ชนะ

- **Random Forest:** bagging หลาย tree ลด variance
- **Gradient Boosting:** boost ทีละ tree แก้ error ของ tree ก่อนหน้า → recall ของ minority ดีขึ้น

Related: [[Macro-F1]], [[Lab Week03 Decision Trees]]
