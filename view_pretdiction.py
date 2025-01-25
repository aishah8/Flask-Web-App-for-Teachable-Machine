import sqlite3

# الاتصال بقاعدة البيانات
conn = sqlite3.connect('detections.db')

# إنشاء مؤشر للتعامل مع البيانات
cursor = conn.cursor()

# إضافة بيانات جديدة
data = [
    ('iPhone', 0.99),  # iPhone مع الاحتمال 99%
    ('Laptop', 0.99)   # Laptop مع الاحتمال 99%
]

# إضافة البيانات إلى الجدول
cursor.executemany("INSERT INTO predictions (label, probability) VALUES (?, ?)", data)

# حفظ التغييرات في قاعدة البيانات
conn.commit()

# غلق الاتصال بقاعدة البيانات
conn.close()

print("تم إضافة البيانات بنجاح: iPhone و Laptop مع التنبؤ 99% لكل منهما")