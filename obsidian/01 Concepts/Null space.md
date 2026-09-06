---
title: Null space
tags:
  - concept
  - dsde
  - linear-algebra
aliases:
  - null space
  - kernel
  - ปริภูมิว่าง
---

# Null space

> [!note] Definition
> **Null space** ของ A = เซตของ x ทุกตัวที่ `A·x = 0`
> เขียน `null(A)` หรือ `ker(A)` — เป็น [[Subspace]] เสมอ

```python
# null(A) = คำตอบของระบบ homogeneous
import numpy as np
from scipy.linalg import null_space
A = np.array([[1, -2]])
null_space(A)   # คอลัมน์ = basis ของ null(A) → ทิศ (2, 1) (normalize)
```

## Example 4.2

`A = (1 −2)` → `A·x = 0` คือ `x₁ − 2x₂ = 0` → `x₁ = 2x₂`

นั่นคือเส้น `H = { x₁ = 2x₂ } = span{(2, 1)ᵀ}` → **H = null(A)**

> [!tip] คู่สลับบทบาท
> B = (2 1) → null(B) คือ `2x₁ + x₂ = 0` → `x = (1, −2)ᵀ u` = [[Orthogonal complement|H⊥]]
> สรุป: `H = null(A) = range(B)` · `H⊥ = null(B) = range(A)`

## ทำไม DS ต้องรู้

- **null(A) ≠ {0}** = คอลัมน์ (feature) พึ่งพากันเชิงเส้น → **multicollinearity** → coefficient ไม่ identifiable (มีหลายคำตอบ)
- ยิ่ง null space ใหญ่ = feature ซ้ำซ้อนมาก → ตัด/รวม feature หรือใช้ regularization
- **Rank-nullity:** `rank(A) + dim(null(A)) = จำนวนคอลัมน์`

Related: [[Subspace]], [[Orthogonal complement]], [[Linear Regression]], [[Non-numeric variables]]
