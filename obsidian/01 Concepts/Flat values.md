---
title: Flat values
tags:
  - concept
  - data-prep
  - dsde
aliases:
  - constant column
  - low variance categorical
related:
  - "[[Missing values]]"
  - "[[Week02 Titanic Data Prep]]"
---

# Flat values

> [!note] คืออะไร
> คอลัมน์ที่**ค่าใดค่าหนึ่ง occupying ตารางเกือบทั้งหมด** → แทบแยก observation ไม่ได้ → โมเดล underfit

## เกณฑ์ในโจทย์ Week 2

- flat **> 70%** → ตัดคอลัมน์
- **ยกเว้น** `Age`, `Fare` (ไม่ตรวจ)
- ต้องนับ missing ด้วย: `value_counts(normalize=True, dropna=False)`

## ตัวอย่าง Titanic

```text
Parch
  0 → 76.2%   ← เกิน 70% → ตัด
  1 → 12.8%
  2 →  9.7%

Sex
  male   → 64.7%  ← ไม่เกิน 70% → เก็บ
  female → 35.3%
```

## โค้ด (expanded)

```python
top_share = df[col].value_counts(normalize=True, dropna=False).max()
if top_share > 0.7:
    # drop this column
```

ดูการใช้จริงใน [[Week02 Titanic Data Prep#Q2]]
