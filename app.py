from flask import Flask, jsonify, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_predictions', methods=['GET'])
def get_predictions():
    # الاتصال بقاعدة البيانات
    conn = sqlite3.connect('detections.db')
    cursor = conn.cursor()
    
    # استرجاع البيانات من الجدول
    cursor.execute('SELECT * FROM predictions')
    predictions = cursor.fetchall()
    
    # غلق الاتصال
    conn.close()

    # إرسال البيانات بشكل منسق للواجهة
    return render_template('predictions.html', predictions=predictions)

if __name__  == '__main__':
    app.run(debug=True)
