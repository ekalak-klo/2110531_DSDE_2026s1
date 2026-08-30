---
title: One-hot encoding
tags:
  - concept
  - data-prep
  - dsde
  - encoding
aliases:
  - dummy coding
  - get_dummies
  - OneHotEncoder
related:
  - "[[Imputation mean mode]]"
  - "[[Week02 Titanic Data Prep]]"
---

# One-hot encoding (dummy coding)

> [!note] ใช้เมื่อไหร่
> ตัวแปร **nominal** (ไม่มีลำดับ) เช่น ท่าเรือ, เพศ, สี  
> โมเดลบวกคำว่า `"S"` ไม่ได้ → แตกเป็นหลายคอลัมน์ 0/1

## ภาพ

| Embarked เดิม | Embarked_C | Embarked_Q | Embarked_S |
|---------------|------------|------------|------------|
| C | 1 | 0 | 0 |
| Q | 0 | 1 | 0 |
| S | 0 | 0 | 1 |

แถวหนึ่งมี `1` ได้แค่ช่องเดียว

## ทำไมไม่ใส่ S=0, C=1, Q=2?

> [!warning] Common mistake
> การใส่เลขเรียงจะบอกโมเดลว่า Q > C > S ทั้งที่ท่าเรือ**ไม่มีลำดับ**

Ordinal (เช่น size เสื้อ S < M < L) ถึงจะ enumerate ได้ — ดู slide [[DataPreparation_v10]]

## อ่าน mean ของคอลัมน์ dummy

$$
\text{mean}(\text{Embarked\_Q}) = \frac{\#\text{ คนขึ้น Q}}{n}
$$

ใน Titanic: `27/445 ≈ 0.06` → ไม่ใช่ “คะแนน”

## เครื่องมือ

| เครื่องมือ | เมื่อไหร่ |
|------------|----------|
| `pd.get_dummies` | สั้น เหมาะ EDA / โจทย์ |
| `OneHotEncoder` | pipeline จริง — fit train แล้ว transform test |

รายละเอียดขั้นตอน: [[Week02 Titanic Data Prep#Q6]]
