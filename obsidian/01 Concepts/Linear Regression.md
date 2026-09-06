---
title: Linear Regression
tags:
  - concept
  - dsde
  - ml
  - regression
aliases:
  - OLS
  - R-squared
---

# Linear Regression

ทำนาย **ตัวเลขต่อเนื่อง** (regression) ด้วยเส้นตรง (หรือ hyperplane)

\[
y = \beta_0 + \beta_1 x_1 + \cdots + \beta_n x_n
\]

**OLS** — หา \(\beta\) ที่ทำให้ผลรวม residual กำลังสองน้อยที่สุด

```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
model.predict(X_test)
```

| Metric | ความหมาย |
|--------|----------|
| \(R^2\) | variance ที่ model อธิบายได้ (train/test แยกกัน) |
| RMSE | ขนาด error หน่วยเดียวกับ y |

ดูเพิ่ม: [[Lecture 03-04 Regression]] · lab `2_Linear_Regression_v2.ipynb`
