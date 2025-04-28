from flask import Flask, render_template_string 
import mysql.connector 

app = Flask(__name__)

# Koneksi ke Database
def get_db_connection():
    connection = mysql.connector.connect(
        host='34.116.104.154',    # Ganti ini sama IP Public Cloud SQL kamu
        user='root',                   # Atau username lain kalau sudah dibuat
        password='utsuts', # Password DB kamu
        database='products_db'           # Nama database
    )
    return connection

# Route utama
@app.route('/')
def home():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT name, price FROM products')  # Pastikan tabelnya `products`
    products = cursor.fetchall()
    cursor.close()
    connection.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
