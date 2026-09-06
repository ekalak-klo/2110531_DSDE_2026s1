---
title: Neural network layer
tags:
  - concept
  - dsde
  - deep-learning
  - linear-algebra
aliases:
  - neural layer
  - dense layer
  - fully connected
  - Wx+b
---

# Neural network layer

> [!note] Definition
> 1 layer = **affine map แล้วบีบด้วย nonlinearity**
> `h = f(W x + b)` — W = weight matrix, b = bias, f = activation (ReLU / sigmoid …)

`W x + b` คือ [[Eigenvalues eigenvectors|linear map]] เดิมที่สร้างมาทั้ง arc — DL แค่เอามัน **ซ้อนกันหลายชั้น** คั่นด้วย f

## ทำไมต้องมี nonlinearity

> [!tip] ไม่มี f → ทั้งเครือข่ายยุบเป็น matrix เดียว
> `W₂(W₁x) = (W₂W₁)x` — ซ้อน linear map = linear map เดียว (composition ของ matrix). ต่อให้ 100 ชั้นก็เท่า [[Linear Regression|regression]] ชั้นเดียว. **f ที่โค้ง** คือสิ่งที่ทำให้ net เรียน function ที่ไม่เป็นเส้นได้

## มิติ (dimension bookkeeping)

- input `x`: (n,) → layer มี W: (m×n), b: (m,) → output `h`: (m,)
- batch: X (B×n) → `H = f(X Wᵀ + b)` = (B×m)
- ชั้นถัดไปกิน m เป็น input ต่อ

```python
import numpy as np
def layer(X, W, b, f=lambda z: np.maximum(0, z)):  # ReLU
    return f(X @ W.T + b)          # (B,n)@(n,m) -> (B,m)
```

## Training = ปรับ W, b

- **Forward** = ส่ง x ผ่านทุกชั้น → prediction → loss
- **Backprop** = [[Eigenvalues eigenvectors|chain rule]] ไล่ gradient ของ loss กลับผ่าน matrix แต่ละชั้น → อัปเดต W, b ด้วย gradient descent
- gradient คือ derivative ต่อ W ทุกตัว (matrix calculus)

## เชื่อมของเดิม

| ชั้นเดียว + activation | = โมเดลที่รู้จัก |
|----------------------|------------------|
| f = sigmoid, 1 output | [[Logistic Regression]] เป๊ะ |
| f = identity | [[Linear Regression]] |
| หลายชั้น + ReLU | MLP (เรียน nonlinear) |

**CNN** = layer พิเศษที่ W ไม่ full แต่ **share weight เป็น filter เลื่อนบนภาพ** (ลดพารามิเตอร์, จับ pattern เฉพาะที่)

**Lab:** `code/Week04_DL/1_Image_classification_CIFAR10_CNN_(lightning).ipynb` (CNN บน CIFAR10, PyTorch Lightning)

> [!example] โยง NightOwl
> Net เรียน **การผสม signal แบบ nonlinear** ได้ แต่บน edge บางๆ = overfit ง่าย (พารามิเตอร์เยอะ, ข้อมูล crypto สั้น+noisy). NightOwl จึงยังใช้ rule/rank เชิงเส้น ([[PCA]]/[[SVD]] factor) ไม่ใช่ deep net — DL คุ้มเมื่อมี data เยอะ+โครงสร้างชัด (ภาพ/ข้อความ), ไม่ใช่สัญญาณราคาบาง

Related: [[Eigenvalues eigenvectors]], [[SVD]], [[Logistic Regression]], [[Linear Regression]], [[Projection least squares]]
