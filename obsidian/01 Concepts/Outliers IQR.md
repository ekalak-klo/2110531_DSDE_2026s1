---
title: Outliers IQR
tags:
  - concept
  - data-prep
  - dsde
  - outliers
aliases:
  - IQR
  - winsorize
related:
  - "[[Week02 Titanic Data Prep]]"
---

# Outliers (IQR)

> [!note] คืออะไร
> ค่าสุดโต่งที่ดึงสถิติ (เช่น mean) และโมเดลเชิงเส้นได้ง่าย

## สูตร

$$
IQR = Q3 - Q1
$$

$$
\text{lower} = Q1 - 1.5 \times IQR,\quad
\text{upper} = Q3 + 1.5 \times IQR
$$

## วิธีในโจทย์ Week 2

**clip / winsorize** — ไม่ลบแถว แค่ดึงค่ากลับขอบ

```python
fare = fare.clip(lower=lower, upper=upper)
```

## Titanic Fare

| | ค่า |
|--|-----|
| Q1 | 7.925 |
| Q3 | 34.375 |
| IQR | 26.45 |
| upper | **74.05** |
| mean ก่อน | 34.24 |
| mean หลัง | **26.27** |

> [!example] Mr. Fortune
> Fare `263` → clip เป็น `74.05`
