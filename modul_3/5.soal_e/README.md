# Modul 3 - Soal E: Bidirectional Chat with Timestamps

## Deskripsi
Implementasi chat bidirectional antara client dan server dengan fitur timestamp lengkap.

## Fitur
- **Auto IP Detection**: Client otomatis mendeteksi IP address menggunakan hostname resolution
- **Dynamic Server Configuration**: IP dan port server dapat dikonfigurasi
- **Date Display**: Server menampilkan tanggal saat startup (tidak berulang)
- **Bidirectional Communication**: Server dan client dapat saling mengirim pesan
- **Time Stamps**: Semua pesan ditampilkan dengan timestamp
- **Input Clearing**: Input prompt dibersihkan saat menerima pesan
- **Threading**: Menggunakan threading untuk komunikasi non-blocking

## Cara Menjalankan
1. Jalankan server:
   ```bash
   python3 server.py
   ```

2. Jalankan client:
   ```bash
   python3 client.py
   ```

3. Masukkan IP dan port server (default: 127.0.0.1:5001)

## Keterangan
- Server berjalan di port 5001 (dapat diubah jika port sudah digunakan)
- Format pesan server: [HH:MM:SS] username: message
- Format pesan client: [HH:MM:SS] username: message
- Komunikasi real-time bidirectional
- Input prompt otomatis dibersihkan saat menerima pesan
- Threading memungkinkan pengiriman dan penerimaan pesan secara bersamaan

## Catatan Teknis
- Menggunakan threading untuk menangani komunikasi non-blocking
- Implementasi proper output synchronization
- Error handling untuk koneksi yang terputus
