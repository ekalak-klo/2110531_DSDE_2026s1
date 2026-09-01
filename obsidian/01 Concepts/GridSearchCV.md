---
title: GridSearchCV
tags:
  - concept
  - dsde
  - ml
  - hyperparameter
aliases:
  - grid search
---

# GridSearchCV

ลอง **ทุกชุด** hyperparameter ใน `param_grid` แล้วเลือกชุดที่ให้คะแนน CV ดีที่สุด

```python
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier

param_grid = {
    'criterion': ['gini', 'entropy'],
    'max_depth': [2, 3],
    'min_samples_leaf': [2, 5],
    'n_estimators': [100],
    'random_state': [2020],
}

gs = GridSearchCV(
    RandomForestClassifier(),
    param_grid,
    cv=5,
    scoring='f1_weighted',
)
gs.fit(X_train, y_train)
gs.best_params_
```

| | GridSearchCV | RandomizedSearchCV |
|--|-------------|-------------------|
| วิธี | ลองครบทุกชุดใน grid | สุ่ม subset |
| การันตี best ใน grid | ใช่ | ไม่เสมอ |

ใช้ใน [[Week04 Logistic Regression and Random Forest]] (Mushroom 4.1)
