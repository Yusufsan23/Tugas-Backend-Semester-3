# Dokumentasi Alur Arsitektur API Mahasiswa

1. **Client (Postman/cURL)**: Bertugas mengirimkan HTTP Request (seperti GET, PUT, DELETE) ke URL endpoint aplikasi beserta datanya (payload).
2. **Route / Controller (Blueprint)**: Menerima request dari Client melalui rute `/api/v1/students`. Layer ini mengekstrak data parameter/JSON dari request, lalu memanggil Service terkait tanpa mengolah logika datanya.
3. **Service (Business Logic)**: Menerima instruksi dari Controller dan memproses logika atau aturan bisnis. Di sini terdapat validasi apakah **IPK berada di rentang 0.00 - 4.00** dan apakah **NIM bersifat unik**.
4. **Repository (Data Access Layer)**: Dipanggil oleh Service untuk berinteraksi langsung dengan mock dataset (atau database di masa depan) guna melakukan proses baca, ubah, dan hapus data. Hasilnya dikembalikan ke Service untuk dikirimkan kembali ke Client melalui Route.