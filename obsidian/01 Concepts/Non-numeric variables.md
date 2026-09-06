---
title: Non-numeric variables for regression
tags:
  - concept
  - dsde
  - encoding
aliases:
  - dummy coding
  - ordinal encoding
  - non-numeric
---

# Non-numeric variables (regression)

Model ต้องการตัวเลข → แปลง categorical ก่อน `fit`

| ชนิด | ตัวอย่าง | วิธี |
|------|----------|------|
| **Ordinal** | education level | map ลำดับ: `{'basic.4y': 2, ...}` |
| **Nominal** | job, month | `pd.get_dummies(..., drop_first=True)` → n−1 columns |

```python
# ordinal ก่อน
X['education'] = X['education'].map(EDUCATION_ORDER)

# nominal ที่เหลือ
X = pd.get_dummies(X)
X_train, X_test = X_train.align(X_test, join='left', fill_value=0)
```

> [!warning] Data leakage
> คำนวณ mode/mean และ fit encoder จาก **train เท่านั้น** แล้ว apply บน test

เชื่อม: [[One-hot encoding]] · [[Imputation mean mode]] · slide [[Lecture 03-04 Regression]] §88–93
