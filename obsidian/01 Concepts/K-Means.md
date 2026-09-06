---
title: K-Means
tags:
  - concept
  - dsde
  - ml
  - clustering
aliases:
  - kmeans
  - clustering
---

# K-Means

**Unsupervised** — จัดกลุ่มข้อมูลตามความใกล้ centroid โดยไม่ใช้ label

```python
from sklearn.cluster import KMeans
km = KMeans(n_clusters=5, random_state=0, n_init='auto')
km.fit(X_scaled)
km.cluster_centers_   # shape (k, n_features)
```

| จุดสำคัญ | |
|----------|--|
| Scale ก่อน | มักใช้ `StandardScaler` — ระยะ Euclidean อ่อนไหวต่อหน่วย |
| `n_clusters` | จำนวนกลุ่ม (k) ที่กำหนดเอง |
| `random_state` | ให้ผล reproducible |
| `inverse_transform` | แปลง centroid กลับหน่วยเดิมหลัง scale |

ใช้ใน [[Week05 K-Means Clustering]]
