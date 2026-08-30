---
title: Imputation mean mode
tags:
  - concept
  - data-prep
  - dsde
  - impute
aliases:
  - impute
  - fillna
related:
  - "[[Missing values]]"
  - "[[One-hot encoding]]"
---

# Imputation (mean / mode)

> [!note] จาก [[DataPreparation_v10]]
> - **Numerical** → mean หรือ median
> - **Categorical** → **mode** (ค่าที่พบบ่อยสุด)
> - **Target** → ไม่ impute — ลบแถว

## ตัวเลข (Week 2 Q5)

```python
num_means = df.select_dtypes(include="number").mean()
df = df.fillna(num_means)
# Age NaN → 29.14; mean หลังเติมยัง ≈ 29.14
```

## หมวดหมู่ (Week 2 Q6 — ก่อน one-hot)

```python
mode_emb = df["Embarked"].mode()[0]  # "S"
df["Embarked"] = df["Embarked"].fillna(mode_emb)
```

> [!warning]
> อย่า one-hot ตอนยังมี NaN ถ้าทำตามสูตร slide — ต้อง mode ก่อน
> (แม้ `get_dummies` จะกลายเป็นแถว 0 ทั้งแถวได้ แต่ pipeline ที่ถูกคือ impute ก่อน)
