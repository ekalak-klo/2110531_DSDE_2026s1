---
title: Train test stratification
tags:
  - concept
  - data-prep
  - dsde
  - split
aliases:
  - stratify
  - train_test_split
related:
  - "[[Week02 Titanic Data Prep]]"
---

# Train / test + stratification

> [!note] ทำไมต้องแยก
> ทดสอบโมเดลด้วยข้อมูลที่ไม่เคยเห็นตอนเรียน

## พารามิเตอร์โจทย์ Week 2

- สัดส่วน **70% train / 30% test** → `test_size=0.3`
- `random_state=123` ให้สุ่มซ้ำได้
- `stratify=y` ให้สัดส่วนคลาสใกล้ของเดิม

## ภาพ Titanic

| ชุด | n | สัดส่วน `Survived==1` |
|-----|---|------------------------|
| all | 445 | ~0.40 |
| train | 311 | **0.41** |
| test | 134 | ~0.40 |

> [!tip]
> ถ้าไม่ stratify อาจบังเอิญยัดคนรอดไป train หมด → คะแนนบน test หลอกตัวเอง
