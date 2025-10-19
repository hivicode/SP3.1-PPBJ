# Modul 3 - Soal C: Server Date & Time Display

## Deskripsi
Implementasi server dengan fitur tampilan tanggal dan waktu untuk pesan yang masuk.

## Fitur
- **Auto IP Detection**: Client otomatis mendeteksi IP address-nya
- **Dynamic Server Configuration**: IP dan port server dapat dikonfigurasi
- **Date Display**: Server menampilkan tanggal saat startup (tidak berulang)
- **Time Stamps**: Setiap pesan dari client ditampilkan dengan timestamp
- Format waktu: HH:MM:SS

## Cara Menjalankan
1. Jalankan server:
   ```bash
   python3 server.py
   ```

2. Jalankan client:
   ```bash
   python3 client.py
   ```

3. Masukkan IP dan port server

## Keterangan
- Server menampilkan tanggal saat startup: DD/MM/YYYY
- Setiap pesan client ditampilkan dengan format: [HH:MM:SS] username: message
- Komunikasi satu arah dari client ke server
- Logging yang lebih baik dengan informasi waktu
