---
title: "isna mean loc drop columns"
tags:
  - code
  - pandas
  - dsde
  - week2
aliases:
  - df.loc isna mean
  - drop columns missing 50 percent
related:
  - "[[Missing values]]"
  - "[[Week02 Titanic Data Prep]]"
---

# `df.loc[:, df.isna().mean() <= 0.5]`

> [!abstract]
> บรรทัดเดียวใน `student.py` Q2 = **เก็บคอลัมน์ที่ว่าง ≤ 50%**  
> ด้านล่างคือความหมายทีละชั้น (ใช้ใน [[Week02 Titanic Data Prep]])

## Compact (ส่ง grader)

```python
df = df.loc[:, df.isna().mean() <= 0.5]
```

## Expanded (สำหรับเรียน)

```python
# ขั้น 1 — True = ว่าง, False = มีค่า
is_missing = df.isna()

# ขั้น 2 — สัดส่วนว่างต่อคอลัมน์
missing_ratio = is_missing.mean()
# Cabin     0.739
# Age       0.191
# Embarked  0.101
# Fare      0.000

# ขั้น 3 — mask คอลัมน์ที่ผ่าน
mask = missing_ratio <= 0.5
# Cabin     False  ← ตัด
# Age       True

# ขั้น 4 — เลือกคอลัมน์ (ทุกแถว)
df = df.loc[:, mask]
# :    = ทุกแถว (ไม่ลบคน)
# mask = คอลัมน์ที่เป็น True
```

## อ่าน `loc`

```text
df.loc[ แถว , คอลัมน์ ]
df.loc[  :  ,  mask  ]
         │        │
         │        └─ boolean Series ยาวเท่าจำนวนคอลัมน์
         └─ colon = เอาทุกแถว
```

## เทียบกับ lab

```python
# ความหมายใกล้กัน: ต้องมีค่าอย่างน้อยครึ่งหนึ่งของจำนวนแถว
df = df.dropna(thresh=len(df) / 2, axis=1)
```

| | `loc` + `isna().mean()` | `dropna(thresh=…, axis=1)` |
|--|-------------------------|----------------------------|
| อ่านตรงโจทย์ “missing > 50%” | ✅ | ใกล้เคียง |
| เห็นชัดว่าเลือกคอลัมน์ | `loc[:, …]` | ต้องจำ `axis=1` |

## สิ่งที่เปลี่ยน / ไม่เปลี่ยน

| | |
|--|--|
| แถว | **ไม่เปลี่ยน** (ยัง 445) |
| คอลัมน์ | ตัดที่ว่างเกินครึ่ง (เช่น `Cabin`) |
| ค่าในช่องที่เหลือ | ไม่แก้ |

กลับไป [[Week02 Titanic Data Prep#Q2]]
