---
title: "Week05 K-Means Clustering"
course: "2110531 DSDE"
week: 5
status: done
tags:
  - assignment
  - dsde
  - week5
  - kmeans
  - clustering
aliases:
  - สรุปการบ้าน week5
  - Clustering mushroom assignment
created: 2026-09-06
sources:
  - "homework/attachment_week5/problems/03_ml_03_2026s1.pdf"
  - "code/Week03_ML/8_K_Means_Clustering_v2.ipynb"
answers:
  q1: [2104, 2]
  q2: [2.51, 2.3]
  q3: [1.01, 1.0]
---

# Week 5 — K-Means on Edible Mushrooms

> [!abstract] งาน
> Cluster **edible** mushrooms ด้วย 2 features → รายงาน max centroid (scaled) และ min centroid (original scale)

**โจทย์:** `homework/attachment_week5/problems/`  
**ส่ง:** `homework/attachment_week5/student.py`  
**Notebook สอน:** `homework/attachment_week5/walkthrough_week5.ipynb`

---

## Pipeline

| ขั้น | ทำอะไร |
|------|--------|
| 1–2 | โหลด `ModifiedEdibleMushroom.csv` → `label == 'e'` (2104 แถว) |
| 3 | เหลือ `cap-color-rate`, `stalk-color-above-ring-rate` |
| 4 | `fillna(mean)` → `StandardScaler` |
| 5–6 | `KMeans(n_clusters=5, random_state=0, n_init='auto')` → **max** ต่อ feature |
| 7 | `scaler.inverse_transform(centroids)` → **min** ต่อ feature |

> [!tip] ทำไมต้อง inverse?
> KMeans รันบน **standardized** space — centroid ที่อ่าน “ค่าจริง” ต้องแปลงกลับด้วย `inverse_transform`

---

## คำตอบ

| Q | คำตอบ |
|---|--------|
| **Q1** | `(2104, 2)` |
| **Q2** | `[2.51 2.3 ]` |
| **Q3** | `[1.01 1.  ]` |

---

## รัน

```bash
cd homework/attachment_week5
python3 main_v2.py   # พิมพ์ Q1 / Q2 / Q3
```

## ลิงก์

- Lab: `code/Week03_ML/8_K_Means_Clustering_v2.ipynb`
- Concept: [[K-Means]]
