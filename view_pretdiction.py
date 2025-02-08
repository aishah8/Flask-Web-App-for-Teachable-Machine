import sqlite3


conn = sqlite3.connect('detections.db')


cursor = conn.cursor()


data = [
    ('iPhone', 0.99),  
    ('Laptop', 0.99)   
]


cursor.executemany("INSERT INTO predictions (label, probability) VALUES (?, ?)", data)


conn.commit()


conn.close()

print("تم إضافة البيانات بنجاح: iPhone و Laptop مع التنبؤ 99% لكل منهما")