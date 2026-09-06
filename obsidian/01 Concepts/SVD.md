---
title: SVD (Singular Value Decomposition)
tags:
  - concept
  - dsde
  - linear-algebra
  - dimensionality-reduction
aliases:
  - SVD
  - singular value decomposition
  - low-rank
---

# SVD (Singular Value Decomposition)

> [!note] Definition
> แยก **matrix ใดก็ได้** (m×n, ไม่ต้องจัตุรัส) เป็น 3 ชิ้น:
> `A = U Σ Vᵀ` — U, V ตั้งฉาก (แกนหมุน); Σ ทแยงมุม = **singular values** σ₁≥σ₂≥… ≥0 (อัตราการยืดแต่ละแกน)

[[Eigenvalues eigenvectors|Eigen]] ทำได้เฉพาะ matrix จัตุรัส. **SVD = generalization** ใช้กับ matrix รูปไหนก็ได้ (ข้อมูลจริง = m แถว × n feature, ไม่จัตุรัส)

## เชื่อมกับ eigen

- คอลัมน์ **V** = eigenvector ของ `AᵀA`; คอลัมน์ **U** = eigenvector ของ `AAᵀ`
- `σᵢ = √λᵢ` (singular value = รากของ eigenvalue)
- ถ้า A symmetric → SVD กับ eigen ตรงกัน

$$ A = \sum_{i} \sigma_i\, u_i v_i^\top \qquad (\text{ผลรวมชั้น rank-1}) $$

```python
import numpy as np
U, s, Vt = np.linalg.svd(A, full_matrices=False)
# rank-k approximation (เก็บ k singular value แรก)
Ak = U[:, :k] @ np.diag(s[:k]) @ Vt[:k]
```

> [!tip] Low-rank = projection ที่ดีสุด (Eckart–Young)
> เก็บ top-k σ = matrix rank-k ที่**ใกล้ A สุด** (error น้อยสุด) = [[Projection least squares|ฉาย]]ลง subspace k มิติ. ธีมเดิม: เก็บทิศ σ ใหญ่ (สัญญาณ), ทิ้ง σ เล็ก ([[Orthogonal complement]], มัก noise)

## SVD ↔ [[PCA]]

PCA เชิงเลขจริง = **SVD ของข้อมูล centered** (ไม่ใช่ eig ของ covariance — sklearn `PCA` ใช้ SVD เพราะเสถียร+เร็วกว่า, ไม่ต้องสร้าง covariance ชัดๆ)

- center X (ลบ mean) → `X = UΣVᵀ`
- **V** = principal components; **σ²/(n−1)** = variance แต่ละ PC
- `U Σ` = พิกัดข้อมูลบนแกนใหม่ (= transform ของ PCA)

## ทำไม DS ต้องรู้

- **ลดมิติ / บีบข้อมูล** — เก็บ k แกน (รูป, สัญญาณ, embedding)
- **Latent factors** — recommender (SVD ของ user×item), LSA (term×document) → หา "หัวข้อ" แฝง
- **Pseudo-inverse / least-squares** เสถียร — `np.linalg.lstsq` ข้างในใช้ SVD
- **ตัด noise** — ทิ้ง singular value เล็ก = denoise

> [!example] โยง NightOwl
> **SVD ของ panel ผลตอบแทน** (เหรียญ×เวลา) = หา statistical factor โดยตรง: σ ใหญ่สุด = factor ตลาด. เอาชั้น rank-1 นั้นออก = residualize ([[Orthogonal complement|ฉายลง H⊥]]) → เหลือ `xsec_resid`. เป็นวิธีเดียวกับ [[PCA]] factor model แต่ทำบน matrix ตรงๆ

Related: [[PCA]], [[Eigenvalues eigenvectors]], [[Projection least squares]], [[Orthogonal complement]]
