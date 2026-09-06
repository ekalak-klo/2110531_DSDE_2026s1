---
title: Logistic Regression
tags:
  - concept
  - dsde
  - ml
  - classification
aliases:
  - logit
  - sigmoid
---

# Logistic Regression

Classification — ทำนาย **class 0/1** โดยใช้ **linear บน logit** ไม่ใช่บน probability โดยตรง

\[
\text{logit}(p) = \ln\frac{p}{1-p} = w_0 + w_1 x_1 + \cdots
\qquad
p = \frac{1}{1 + e^{-\text{logit}}}
\]

Train ด้วย **MLE** (maximize log-likelihood)

```python
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(
    random_state=2025,
    class_weight='balanced',  # class ไม่สมดุล
    max_iter=500,
)
```

| พารามิเตอร์ | ใช้เมื่อ |
|-------------|----------|
| `class_weight='balanced'` | minority class สำคัญ (bank marketing) |
| `max_iter` | solver ยังไม่ converge |

ประเมินด้วย [[Macro-F1]] มากกว่า accuracy อย่างเดียวเมื่อ class skew

ดูเพิ่ม: [[Lecture 03-04 Regression]] · [[Week04 Logistic Regression and Random Forest]]
