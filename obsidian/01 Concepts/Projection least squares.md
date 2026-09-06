---
title: Projection (least squares)
tags:
  - concept
  - dsde
  - linear-algebra
  - projection
  - regression
aliases:
  - projection
  - least squares
  - orthogonal projection
  - normal equation
  - การฉาย
---

# Projection (least squares)

> [!note] Definition
> **ฉาย (project)** เวกเตอร์ b ลง subspace = หาจุดใน subspace ที่**ใกล้ b ที่สุด**
> จุดนั้น = เงาของ b; เส้นจาก b ไปหาเงา (**residual**) **ตั้งฉาก** subspace

นี่คือหัวใจของ **least squares**: ระบบ `Ax = b` ที่ไม่มีคำตอบเป๊ะ (สมการมากกว่าตัวแปร) → หา x ที่ทำให้ `Ax` ใกล้ b สุด

## สูตร — ฉายลง column space ของ A

$$ \hat{x} = (A^\top A)^{-1} A^\top b \qquad p = A\hat{x} = \underbrace{A(A^\top A)^{-1}A^\top}_{P}\, b $$

- `P` = **projection matrix** (P² = P, Pᵀ = P)
- **Normal equation:** `AᵀA x̂ = Aᵀb`
- **Residual** `r = b − Ax̂` → `Aᵀr = 0` → **r ตั้งฉาก column space** = r อยู่ใน [[Orthogonal complement|H⊥]]

```python
import numpy as np
# least squares: min ||b - A x||
x_hat, *_ = np.linalg.lstsq(A, b, rcond=None)   # ไม่ต้อง invert เอง (เสถียรกว่า)
residual = b - A @ x_hat
# A.T @ residual ≈ 0  → residual ตั้งฉาก col(A)
```

> [!tip] ทำไม residual ต้องตั้งฉาก
> ถ้า residual ยังมีส่วนขนานกับ subspace → ขยับเงาตามนั้นได้อีก แล้ว error สั้นลง → แปลว่ายังไม่ใช่จุดใกล้สุด. จุดใกล้สุด = residual ตั้งฉากล้วน. (Pythagoras)

## ทำไม DS ต้องรู้

- **[[Linear Regression]]** = ฉาย y ลง column space ของ feature → ค่า fit; residual = ส่วนที่โมเดลอธิบายไม่ได้
- **R²** = สัดส่วน variance ที่เงา (fit) เก็บได้ เทียบทั้งหมด
- **Feature ตั้งฉากกัน** (orthogonal) → coefficient อิสระต่อกัน, ตีความง่าย; ถ้าไม่ตั้งฉาก (collinear) → [[Null space]] ≠ {0}, coefficient สั่น
- **Residualization / market-neutral:** ฉาย signal ลง H⊥ ของ common factor = เก็บเฉพาะส่วนที่ตั้งฉากกับตัวร่วม (เช่น ตลาด) → ตัดอิทธิพล factor ออกก่อน rank

Related: [[Orthogonal complement]], [[Subspace]], [[Null space]], [[Linear Regression]]
