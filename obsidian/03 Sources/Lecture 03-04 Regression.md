---
title: "Lecture 03-04 Regression"
tags:
  - source
  - dsde
  - week3
  - week4
  - lecture
  - linear-regression
  - logistic-regression
aliases:
  - Regression slide
  - Linear Logistic lecture
---

# Lecture 03–04 — Regression (`Regression_v2_compressed.pdf`)

> [!abstract] โฟกัส
> **Linear Regression** (ตัวเลขต่อเนื่อง) → **Logistic Regression** (classification) → **Non-numeric variables** (encode ก่อน fit)

**ไฟล์:** `slide/Week03,04_ML/Regression_v2_compressed.pdf` (93 หน้า)

---

## 1. Linear Regression

| แนวคิด | สูตร / จุดจำ |
|--------|----------------|
| Simple | \(y = \beta_0 + \beta_1 x\) |
| Multiple | \(y = \beta_0 + \beta_1 x_1 + \cdots + \beta_n x_n\) |
| OLS | หาเส้นที่ **residual รวมน้อยที่สุด** |
| Matrix form | \(\mathbf{Y} = \mathbf{X}\boldsymbol{\beta}\), \(\boldsymbol{\beta} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{Y}\) |
| \(R^2\) | \(1 - SS_E/SS_T\) — สัดส่วน variance ที่ model อธิบายได้ |
| Adjusted \(R^2\) | ลงโทษเมื่อเพิ่ม feature มากเกินไป |

**สมมติฐาน 4 ข้อ:** linear relationship, normality, ไม่ multicollinear, homoscedasticity

**Lab:** `code/Week03_ML/2_Linear_Regression_v2.ipynb` (USA Housing → `LinearRegression`)

---

## 2. Feature Selection (slide §32–57)

Greedy ลด dimension ก่อน regression:

- **Forward** — เริ่มว่าง แล้วเพิ่ทีละตัว
- **Backward** — เริ่มครบ แล้วลบทีละตัว
- **Stepwise / SFFS / SBFS** — ลอยขึ้นลงได้

sklearn: `SequentialFeatureSelector`

---

## 3. Logistic Regression

Classification แต่ใช้ **linear model บน logit** (ไม่ใช่ linear บน probability โดยตรง)

```
logit(p) = ln(p / (1-p)) = w0 + w1*x1 + w2*x2 + ...
p = 1 / (1 + e^(-logit))
```

| หัวข้อ | รายละเอียด |
|--------|-------------|
| Sigmoid | แปลง logit score → ความน่าจะเป็น 0–1 |
| Training | **MLE** — maximize log-likelihood (หรือ minimize -2LL) |
| สมมติฐาน | linear บน **logit** กับ X (ไม่ใช่บน p) |

**Interpret odds ratio:** \(e^{w}\) — เช่น \(w=0.2\) → OR=1.22 (+22% odds)

**Lab:** `code/Week03_ML/3_Logistic_Regression_v3.ipynb` (Titanic)

**Homework 4.2:** [[Week04 Logistic Regression and Random Forest]] — `class_weight='balanced'`, [[Macro-F1]]

---

## 4. Non-numeric variables (slide §88–93)

Regression ต้องการตัวเลข → encode ก่อน fit

| ชนิด | วิธี |
|------|------|
| **Ordinal** | map ลำดับเป็นตัวเลข (เช่น education 1–7) |
| **Nominal** | **dummy coding** = n−1 columns (`pd.get_dummies`, `drop_first=True`) |

เชื่อมกับ [[One-hot encoding]], [[Imputation mean mode]] (week 4.2 pipeline)

---

## 5. Evaluation (classification)

| Metric | ใช้เมื่อ |
|--------|----------|
| Confusion matrix | TP/TN/FP/FN |
| Precision / Recall / F1 | imbalance |
| **Macro F1** | ทุก class น้ำหนักเท่ากัน → ใช้ในการบ้าน |
| Pseudo \(R^2\) | คุณภาพ fit logistic (ไม่ใช่ \(R^2\) แบบ linear) |

---

## แผนทบทวน (สั้น)

1. อ่าน Linear §2–17 → รัน lab `2_Linear_Regression_v2`
2. อ่าน Logistic §58–80 → รัน lab `3_Logistic_Regression_v3`
3. อ่าน Non-numeric §88–93 → ทำ [[Week04 Logistic Regression and Random Forest]] Q5–Q7
4. ML อื่น (Tree, RF) → `ML1_v9_compressed.pdf` + [[Week03 Decision Tree Ensembles]]
