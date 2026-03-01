import os
import psycopg2
from flask import Flask

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST'),
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD')
    )
    return conn

# Инициализация базы: создаем таблицу при старте
def init_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS hits (id serial PRIMARY KEY, count integer);')
    cur.execute('INSERT INTO hits (id, count) SELECT 1, 0 WHERE NOT EXISTS (SELECT 1 FROM hits WHERE id = 1);')
    conn.commit()
    cur.close()
    conn.close()

@app.route('/')
def hello():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('UPDATE hits SET count = count + 1 WHERE id = 1 RETURNING count;')
    count = cur.fetchone()[0]
    conn.commit()
    cur.execute('SELECT version();')
    db_version = cur.fetchone()
    cur.close()
    conn.close()
    return f"Я построил этот CI/CD пайплайн! Визит №{count}.  База говорит: {db_version}"

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
