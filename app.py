import os
from os.path import join, dirname
from dotenv import load_dotenv

from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MONGODB_URI = os.environ.get("MONGODB_URI")
DB_NAME =  os.environ.get("DB_NAME")

client = MongoClient(MONGODB_URI)

db = client[DB_NAME]

app = Flask(__name__)

# Route untuk halaman utama
@app.route('/')
def index():
    return render_template('index.html')

# Route untuk meng-handle form submission dari halaman kontak
@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        # Mengambil data dari form
        nama = request.form['nama']
        email = request.form['email']
        pesan = request.form['pesan']
        
        # Menyimpan data ke dalam collection "messages"
        messages_collection = db['messages']
        new_message = {
            'nama': nama,
            'email': email,
            'pesan': pesan
        }
        db.portfolio.insert_one(new_message)
        
        # Menanggapi dengan pesan sukses
        return 'Form submitted successfully!'

if __name__ == '__main__':
    app.run(debug=True)
