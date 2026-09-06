---
title: Eigenvalues & eigenvectors
tags:
  - concept
  - dsde
  - linear-algebra
aliases:
  - eigenvalue
  - eigenvector
  - eigen
  - ค่าลักษณะเฉพาะ
---

# Eigenvalues & eigenvectors

> [!note] Definition
> **Eigenvector** ของ A = เวกเตอร์ที่ A **แค่ยืด/หด ไม่หมุน**
> `A·v = λ·v` — λ (**eigenvalue**) = อัตราการยืด (ทิศเดิม)

A ทำกับเวกเตอร์ทั่วไป = ยืด + หมุน. eigenvector = ทิศพิเศษที่โดนแค่ยืด → บอก "แกนธรรมชาติ" ของ A

## หายังไง

$$ A v = \lambda v \;\Rightarrow\; (A - \lambda I)v = 0 \;\Rightarrow\; \det(A - \lambda I) = 0 $$

- แก้ `det(A − λI) = 0` (characteristic equation) → ได้ λ
- แทน λ กลับ → หา v จาก [[Null space|null(A − λI)]]

```python
import numpy as np
vals, vecs = np.linalg.eig(A)      # ทั่วไป
vals, vecs = np.linalg.eigh(A)     # symmetric: λ จริง, eigenvector ตั้งฉาก (เร็ว+เสถียร)
```

> [!tip] Symmetric matrix สำคัญกับ DS
> ถ้า A **symmetric** (เช่น covariance): eigenvalue เป็นจำนวนจริง และ **eigenvector ตั้งฉากกันทั้งหมด** → ใช้เป็นแกนใหม่ที่ [[Orthogonal complement|ตั้งฉาก]]ได้เลย. นี่คือฐานของ [[PCA]]

## ทำไม DS ต้องรู้

- **[[PCA]]** = eigenvector ของ covariance matrix = แกน variance สูงสุด
- eigenvalue ใหญ่ = ทิศที่ข้อมูลกระจายมาก (สัญญาณ); เล็ก = ทิศแบน (noise)
- ใช้ใน spectral clustering, PageRank (graph), ความเสถียรของระบบ

Related: [[PCA]], [[Orthogonal complement]], [[Projection least squares]], [[Null space]]
