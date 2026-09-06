---
title: PCA
tags:
  - concept
  - dsde
  - linear-algebra
  - dimensionality-reduction
  - unsupervised
aliases:
  - PCA
  - principal component analysis
  - ลดมิติ
---

# PCA (Principal Component Analysis)

> [!note] Definition
> หา **แกนใหม่** (principal components) = ทิศที่ข้อมูล**กระจายมากสุด** และ**ตั้งฉากกัน**
> แล้วเก็บแค่ไม่กี่แกนแรก → ลดมิติ โดยเสีย variance น้อยสุด

## กลไก = [[Eigenvalues eigenvectors|eigen]] ของ covariance

1. **standardize** feature (mean 0, ต้อง scale ก่อน — ไม่งั้นหน่วยใหญ่ครอบ)
2. คำนวณ covariance matrix `C` (symmetric)
3. **eigenvectors ของ C** = principal components; **eigenvalue** = variance ตามแกนนั้น
4. เรียง eigenvalue มาก→น้อย, เก็บ top-k
5. **project** ข้อมูลลง top-k PC → มิติ k

$$ \text{explained variance ratio}_i = \frac{\lambda_i}{\sum_j \lambda_j} $$

```python
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

Xs = StandardScaler().fit_transform(X)     # ต้อง scale ก่อน
pca = PCA(n_components=2)
Z = pca.fit_transform(Xs)
pca.explained_variance_ratio_              # แต่ละ PC เก็บ variance กี่ %
```

> [!tip] PCA = projection ที่ดีที่สุด
> เก็บ top-k PC = [[Projection least squares|ฉาย]]ข้อมูลลง subspace k มิติที่**เก็บ variance สูงสุด** (เสีย reconstruction error ต่ำสุด). ส่วนที่ทิ้ง = [[Orthogonal complement]] ของ subspace นั้น = variance น้อย (มัก noise)

## ทำไม/เมื่อไหร่ใช้

- **ลดมิติ** ก่อนเข้าโมเดล → เร็วขึ้น, ลด overfit
- **กำจัด collinearity** — PC ตั้งฉากกัน = ไม่ซ้ำซ้อน ([[Null space]] หาย)
- **visualize** ข้อมูลมิติสูงบน 2D
- ⚠️ PC ตีความยาก (ผสม feature เดิม); unsupervised (ไม่ดู target)

> [!example] โยง NightOwl
> **Factor model** = PC ของ panel ผลตอบแทน: PC1 มัก = "ตลาด" (ทุกเหรียญขึ้นลงพร้อมกัน). เอา factor นั้นออก = residualize ([[Orthogonal complement|ฉายลง H⊥]]) → เหลือ signal เฉพาะตัว = `xsec_resid`

Related: [[SVD]], [[Eigenvalues eigenvectors]], [[Projection least squares]], [[Orthogonal complement]], [[Subspace]]
