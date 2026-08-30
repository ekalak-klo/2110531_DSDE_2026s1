---
title: Missing values
tags:
  - concept
  - data-prep
  - dsde
aliases:
  - NaN
  - missing data
related:
  - "[[Imputation mean mode]]"
  - "[[Flat values]]"
  - "[[Week02 Titanic Data Prep]]"
---

# Missing values

> [!note] คืออะไร
> ช่องว่างในตาราง (`NaN` / `None`) — ไม่มีค่าให้โมเดลใช้

## จาก slide [[DataPreparation_v10]]

| ชนิด missing | ทำอย่างไร |
|--------------|-----------|
| **Target** ว่าง | **ลบแถว** — ห้ามเดาคำตอบ |
| **Input ตัวเลข** ว่าง | [[Imputation mean mode\|impute mean/median]] |
| **Input หมวดหมู่** ว่าง | [[Imputation mean mode\|impute mode]] |
| **คอลัมน์ว่าง > 50%** | **ตัดทั้งคอลัมน์** |

## ใน Titanic (Week 2)

| คอลัมน์ | % ว่าง | การตัดสินใจ |
|---------|--------|-------------|
| Cabin | 73.9% | ตัดคอลัมน์ (Q2) |
| Age | 19.1% | เติม mean (Q5) |
| Embarked | 10.1% | เติม mode ก่อน one-hot (Q6) |
| Survived | 2.9% | ลบแถว (Q3) |

## โค้ดที่เกี่ยวข้อง

- ตัดคอลัมน์ missing มาก: [[isna mean loc drop columns]]
- ลบแถว target: `df.dropna(subset=["Survived"])`
