# Modul 3 - Soal A: Auto IP Detection

## Deskripsi
Implementasi client-server dengan deteksi IP client otomatis.

## Fitur
- **Auto IP Detection**: Client secara otomatis mendeteksi dan menampilkan IP address-nya
- Koneksi sederhana antara client dan server
- Pertukaran pesan dasar

## Cara Menjalankan
1. Jalankan server terlebih dahulu:
   ```bash
   python3 server.py
   ```

2. Jalankan client:
   ```bash
   python3 client.py
   ```

## Keterangan
- Client otomatis mendeteksi IP address menggunakan koneksi ke server eksternal
- Fallback ke 127.0.0.1 jika deteksi gagal
- Server berjalan di IP: 127.0.0.1, Port: 12345
- Komunikasi satu arah dari client ke server
