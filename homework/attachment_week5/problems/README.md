# Week 5 — โจทย์ (Clustering / K-Means)

| ไฟล์ | คืออะไร |
|------|--------|
| `03_ml_03_2026s1.pdf` | โจทย์ Q1–Q3 + Expected Results |
| `To_student.ipynb` | template notebook (อ้างอิง) |

## ส่ง grader

โฟลเดอร์บน: `student.py` (+ data `ModifiedEdibleMushroom.csv`, รันด้วย `main_v2.py`)

ส่ง **เฉพาะ** libraries + class `Clustering`

## Pipeline สั้น ๆ

1. โหลด CSV → เลือก `label == 'e'` (edible)
2. เหลือ 2 features: `cap-color-rate`, `stalk-color-above-ring-rate`
3. fillna mean → `StandardScaler`
4. `KMeans(n_clusters=5, random_state=0, n_init='auto')`
5. Q2: max centroid (scaled) 2 ทศนิยม
6. Q3: inverse_transform → min centroid (original) 2 ทศนิยม

## Expected

| Q | Output |
|---|--------|
| Q1 | `(2104, 2)` |
| Q2 | `[2.51 2.3 ]` |
| Q3 | `[1.01 1.  ]` |
