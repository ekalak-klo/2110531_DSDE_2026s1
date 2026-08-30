---
title: "Macro-F1"
tags:
  - concept
  - dsde
  - week3
  - evaluation
aliases:
  - macro f1
  - f1 macro average
---

# Macro-F1

> [!note] Definition
> **Macro-F1** = ค่าเฉลี่ยของ F1 **ทุก class แบบเท่ากัน** (ไม่ถ่วงตามจำนวนตัวอย่าง)

```python
from sklearn.metrics import f1_score
macro = f1_score(y_true, y_pred, average='macro')
```

## เมื่อไหร่ใช้

- ข้อมูล **class ไม่สมดุล** (เช่น diabetes: absent >> present)
- อยากให้ minority class มีน้ำหนักเท่า majority

## เปรียบเทียบ

| Metric | พฤติกรรม |
|--------|----------|
| **Accuracy** | ถูกหลอกได้ถ้า predict majority ทั้งหมด |
| **Weighted F1** | ถ่วงตาม support ของแต่ละ class |
| **Macro-F1** | ทุก class นับเท่ากัน |

## ใน Week 03 assignment

Baseline Decision Tree มี recall ของ class `present` ต่ำ → Macro-F1 ต่ำกว่า ensemble ที่จับ minority ได้ดีกว่า

Related: [[Week03 Decision Tree Ensembles]]
