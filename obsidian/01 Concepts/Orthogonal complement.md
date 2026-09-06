---
title: Orthogonal complement
tags:
  - concept
  - dsde
  - linear-algebra
  - projection
aliases:
  - orthogonal complement
  - H perp
  - ส่วนเติมเต็มตั้งฉาก
---

# Orthogonal complement

> [!note] Definition
> **Orthogonal complement** ของ subspace H = เวกเตอร์ทุกตัวที่ **ตั้งฉากกับทุกตัวใน H**
> เขียน `H⊥` = `{ v : v · h = 0 ทุก h ∈ H }` — เป็น [[Subspace]] เสมอ

## Example 4.2

| | subspace | basis | ทิศ |
|--|----------|-------|-----|
| **H** | `x₁ = 2x₂` | (2, 1)ᵀ | เส้นความชัน ½ |
| **H⊥** | `x = (1, −2)ᵀ u` | (1, −2)ᵀ | ตั้งฉาก H |

เช็กตั้งฉาก: `(2, 1) · (1, −2) = 2 − 2 = 0` ✓

> [!abstract] Fundamental Theorem of Linear Algebra
> `null(A) ⊥ row(A)` และรวมกันเต็มปริภูมิ: `R² = H ⊕ H⊥`
> ทุกเวกเตอร์ x แตกได้แบบเดียว = (ส่วนใน H) + (ส่วนใน H⊥)

## ทำไม DS ต้องรู้ — projection

- **Least-squares regression** = ฉาย y ลง column space; **residual อยู่ใน H⊥** → `Aᵀ(y − Ax) = 0` (residual ตั้งฉากพื้นที่ fit) = normal equation
- **PCA** = หาแกน (subspace) ที่ตั้งฉากกัน เก็บ variance สูงสุด; ส่วนที่ทิ้ง = complement
- **Residual / market-neutral:** เอาเฉพาะส่วนของสัญญาณที่**ตั้งฉากกับ common factor** (เช่น ตลาด) = ฉายลง H⊥ ของ factor → ตัดอิทธิพลตัวร่วมออก

Related: [[Projection least squares]], [[Subspace]], [[Null space]], [[Linear Regression]]
