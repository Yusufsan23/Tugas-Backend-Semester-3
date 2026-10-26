# Backend RESTful API - Products

Proyek praktikum **Dasar Pemrograman Backend** menggunakan Flask, menerapkan arsitektur berlapis, *Response Envelope* (JSend), dan *API Versioning*.

## Endpoint API (v1)
* **GET** `/api/v1/products` - Menampilkan seluruh data produk
* **POST** `/api/v1/products` - Menambahkan produk baru (dengan validasi)
* **PUT** `/api/v1/products/<id>` - Memperbarui data produk berdasarkan ID
* **DELETE** `/api/v1/products/<id>` - Menghapus produk berdasarkan ID

## Cara Menjalankan
1. Pastikan Flask sudah terpasang:
   ```bash
   python -m pip install Flask

2. Jalankan Terminal:
   ```bash
   python run.py

3. Akses server di: 
   ```bash
   http://127.0.0.1:5000

