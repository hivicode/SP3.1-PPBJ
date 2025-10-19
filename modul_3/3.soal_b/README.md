# Modul 3 - Soal B: Dynamic IP & Port Configuration

## Deskripsi
Implementasi client-server dengan konfigurasi IP dan port server yang dinamis.

## Fitur
- **Auto IP Detection**: Client otomatis mendeteksi IP address-nya
- **Dynamic Server IP**: User dapat memasukkan IP server secara manual
- **Dynamic Server Port**: User dapat memasukkan port server secara manual
- Koneksi fleksibel ke berbagai server

## Cara Menjalankan
1. Jalankan server di komputer pertama:
   ```bash
   python3 server.py
   ```

2. Jalankan client di komputer lain:
   ```bash
   python3 client.py
   ```

3. Masukkan IP dan port server sesuai dengan server yang berjalan

## Keterangan
- Client dapat terhubung ke server di IP dan port manapun
- Fleksibilitas tinggi untuk testing di berbagai environment
- Server default berjalan di IP: 127.0.0.1, Port: 12345
- Komunikasi satu arah dari client ke server
