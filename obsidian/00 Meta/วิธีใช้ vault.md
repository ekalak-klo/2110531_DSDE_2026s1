---
title: "วิธีใช้ Obsidian vault นี้"
tags:
  - meta
  - dsde
---

# วิธีใช้ Obsidian vault นี้

## เปิดใน Obsidian

1. Obsidian → **Open folder as vault**
2. เลือกโฟลเดอร์:
   `2110531_DSDE_2026s1/obsidian`
3. เริ่มที่ [[MOC - DSDE]]

## ชนิดโน้ต

| โฟลเดอร์ | เก็บอะไร | ความยาว |
|---------|----------|---------|
| `01 Concepts` | หลักการ 1 เรื่องต่อไฟล์ | สั้น |
| `02 Assignments` | สรุปการบ้าน + คำตอบ + ตัวอย่างจาก CSV | ยาว |
| `03 Sources` | ชี้ไป slide/lab (ไม่ copy PDF ทั้งก้อน) | สั้น |
| `04 Code Explanations` | แกะ 1 บรรทัด/1 pattern | กลาง |

## Callouts ที่ใช้

- `[!abstract]` — สรุป pipeline / ภาพรวม
- `[!note]` — หลักการ
- `[!example]` — before/after จากข้อมูลจริง
- `[!tip]` — compact vs expanded
- `[!warning]` — ผิดบ่อย

## หลังทำ assignment ใหม่

Agent จะสร้างตาม skill `dsde-assignment-obsidian`:

1. `homework/attachment_weekN/student.py`
2. `homework/attachment_weekN/walkthrough_weekN.ipynb`
3. `obsidian/02 Assignments/WeekNN ....md`
4. concept / code-explanation ใหม่ถ้ายังไม่มี
5. อัปเดตตารางใน [[MOC - DSDE]]
