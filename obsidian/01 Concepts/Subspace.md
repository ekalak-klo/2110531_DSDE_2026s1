---
title: Subspace
tags:
  - concept
  - dsde
  - linear-algebra
aliases:
  - subspace
  - ปริภูมิย่อย
---

# Subspace

> [!note] Definition
> **Subspace** = subset ของปริภูมิ ที่ **ปิดใต้การบวก + การคูณสเกลาร์** และมีเวกเตอร์ศูนย์ (0) เสมอ

ผ่าน 3 เงื่อนไข → เป็น subspace:
1. มี **0**
2. `u, v ∈ H` → `u + v ∈ H` (ปิดใต้บวก)
3. `u ∈ H`, สเกลาร์ `c` → `cu ∈ H` (ปิดใต้คูณ)

ใน R² subspace = {0}, เส้นผ่านจุดกำเนิด, หรือ R² ทั้งอัน (เส้นที่**ไม่**ผ่าน 0 ไม่ใช่ subspace — ไม่มี 0)

## เขียน subspace เดียวได้ 2 แบบ

ใช้ **Example 4.2**: `H = { x ∈ R² : x₁ = 2x₂ }` (เส้นผ่านจุดกำเนิด ความชัน ½)

| แบบ | เขียน | ชื่อ |
|-----|-------|------|
| **ข้อจำกัด** | `x₁ − 2x₂ = 0` = `A·x = 0`, A = (1 −2) | H = [[Null space\|null(A)]] |
| **พาราเมตริก** | `x = uB`, B = (2, 1)ᵀ → (2u, u) | H = range(B) = span{B} |

เช็ก: `A·(2u, u) = 2u − 2u = 0` ✓ → สองแบบคือเส้นเดียวกัน

## ทำไม DS ต้องรู้

- **Column space** ของ design matrix = subspace ที่ least-squares ฉาย y ลงไป
- **Feature space** ที่โมเดลทำงาน = subspace
- ทุก subspace มีคู่ตั้งฉาก → [[Orthogonal complement]]

Related: [[Null space]], [[Orthogonal complement]], [[Linear Regression]]
