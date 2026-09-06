---
title: "Week04 Logistic Regression and Random Forest"
course: "2110531 DSDE"
week: 4
status: done
tags:
  - assignment
  - dsde
  - week4
  - logistic-regression
  - random-forest
  - gridsearch
aliases:
  - สรุปการบ้าน week4
  - Bank Logistic assignment
  - Mushroom RF assignment
created: 2026-08-31
sources:
  - "homework/attachment_week4/"
answers:
  mushroom_q1: 121
  mushroom_q2: [5764, 12]
  mushroom_q3: [3660, 2104]
  mushroom_q4: [4611, 1153]
  mushroom_q5:
    criterion: gini
    max_depth: 3
    min_samples_leaf: 2
    n_estimators: 100
    random_state: 2020
  mushroom_q6: 0.98
  bank_q1: 41158
  bank_q3: [0.887, 0.113]
  bank_q4: [41146, 21]
  bank_q5_train_test: [[28802, 19], [12344, 19]]
  bank_q6_shape: [28802, 49]
  bank_q7_macro_f1: 0.75
---

# Week 4 — Mushroom RF (4.1) + Bank Logistic (4.2)

> [!abstract] งาน
> สองชิ้นใน `attachment_week4/` — **4.2 อิง [[Lecture 03-04 Regression]]** (Logistic + Non-numeric) — **4.1** Random Forest + GridSearch บน mushroom, **4.2** Logistic Regression บน bank marketing

**โจทย์:** `homework/attachment_week4/problems/` (PDF + template)  
**ส่ง:** `4.1/student.py` + `4.2/student.py`  
**Notebook สอน:** `homework/attachment_week4/walkthrough_week4.ipynb`

---

## 4.1 — Mushroom (`MushroomClassifier`)

| ขั้น | ทำอะไร |
|------|--------|
| 1 | โหลด `mushroom2020_dataset.csv` (5824×24) |
| 2 | ลบแถวที่ `label` หาย → เหลือ 5764 แถว |
| 3 | ลบ 12 คอลัมน์ที่โจทย์ระบุ (รวม `gill-size`) |
| 5–6 | [[Imputation mean mode]] ทั้งชุด → map `p→0`, `e→1` |
| 7–8 | `pd.get_dummies(drop_first=True)` → split 80/20, `random_state=2020`, stratify |
| 9 | `GridSearchCV` RF, 5-fold, `scoring='f1_weighted'` |
| 10 | ประเมินบน test → [[Macro-F1]] |

### คำตอบ

| Q | คำตอบ |
|---|--------|
| **Q1** | `121` — ค่า missing ใน `gill-size` ก่อน prep |
| **Q2** | `(5764, 12)` — แถว × ตัวแปรหลังลบ label หาย + drop cols |
| **Q3** | `(3660, 2104)` — poisonous : edible |
| **Q4** | `(4611, 1153)` — train : test |
| **Q5** | `criterion='gini', max_depth=3, min_samples_leaf=2, n_estimators=100, random_state=2020` |
| **Q6** | **0.98** Macro-F1 (2 ทศนิยม) |

> [!tip] หมายเหตุ imputation
> Mushroom impute บน **ทั้ง dataset ก่อน split** (ตามขั้นในโจทย์) — ต่างจาก Bank 4.2 ที่ impute จาก train เท่านั้นเพื่อกัน leakage

---

## 4.2 — Bank Marketing (`BankLogistic`)

> [!tip] ทบทวนก่อนทำ
> Slide: Logistic §58–80, Non-numeric §88–93 → [[Logistic Regression]] · [[Non-numeric variables]]

| ขั้น | ทำอะไร |
|------|--------|
| 1–4 | โหลด → นับแถว / ชนิดตัวแปร / class ratio / dedupe |
| 5 | `unknown→NaN` → ลบ flat >99% → split 70/30, `random_state=0`, stratify |
| 6 | impute mean/mode จาก **train** → ordinal `education` + [[One-hot encoding]] |
| 7 | `LogisticRegression(random_state=2025, class_weight='balanced', max_iter=500)` |

### คำตอบ

| Q | คำตอบ |
|---|--------|
| **Q1** | `41158` |
| **Q2** | numeric 10 ตัว + categorical 11 ตัว (รวม `y`) |
| **Q3** | `(0.887, 0.113)` — no : yes |
| **Q4** | `(41146, 21)` หลัง dedupe |
| **Q5** | `((28802, 20), (12344, 20))` |
| **Q6** | `(28802, 51)` หลัง encode |
| **Q7** | **0.749** Macro-F1 |

> [!note] flat column
> ไม่มีคอลัมน์ไหน >99% flat (`pdays` ที่ 999 อยู่ที่ ~96%) — ใช้กฎ `> 0.99` ตามโจทย์

---

## รัน grader

```bash
# 4.1 Mushroom
cd homework/attachment_week4/4.1
jupyter notebook student.ipynb   # รัน cell ท้าย

# 4.2 Bank
cd homework/attachment_week4/4.2
python3 main.py   # พิมพ์ Q1 … Q7
```

## ลิงก์หลักการ

- [[Macro-F1]]
- [[Imputation mean mode]]
- [[One-hot encoding]]
- [[Train test stratification]]
- [[Flat values]]
