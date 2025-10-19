# Modul 3 - Socket Programming dengan Python

## Deskripsi
Koleksi implementasi client-server socket communication menggunakan Python, dari contoh dasar hingga chat bidirectional dengan fitur lengkap.

## Struktur Folder

### 1. `1.contoh/` - Contoh Dasar
Implementasi client-server socket paling sederhana dengan hardcoded IP dan port.

### 2. `2.soal_a/` - Auto IP Detection
Menambahkan fitur deteksi IP client otomatis menggunakan koneksi ke server eksternal.

### 3. `3.soal_b/` - Dynamic Configuration
Menambahkan konfigurasi IP dan port server yang dinamis (user input).

### 4. `4.soal_c/` - Date & Time Display
Menambahkan fitur tampilan tanggal dan timestamp untuk semua pesan yang masuk.

### 5. `5.soal_e/` - Bidirectional Chat
Implementasi chat bidirectional lengkap dengan threading dan fitur timestamp.

## Progres Fitur

| Fitur | Contoh | Soal A | Soal B | Soal C | Soal E |
|-------|--------|--------|--------|--------|--------|
| Basic Socket | ✅ | ✅ | ✅ | ✅ | ✅ |
| Auto IP Detection | ❌ | ✅ | ✅ | ✅ | ✅ |
| Dynamic Server IP | ❌ | ❌ | ✅ | ✅ | ✅ |
| Dynamic Server Port | ❌ | ❌ | ✅ | ✅ | ✅ |
| Date Display | ❌ | ❌ | ❌ | ✅ | ✅ |
| Message Timestamps | ❌ | ❌ | ❌ | ✅ | ✅ |
| Bidirectional Chat | ❌ | ❌ | ❌ | ❌ | ✅ |
| Threading | ❌ | ❌ | ❌ | ❌ | ✅ |
| Input Clearing | ❌ | ❌ | ❌ | ❌ | ✅ |

## Cara Menjalankan

### Untuk semua implementasi:
1. Jalankan server terlebih dahulu
2. Jalankan client
3. Ikuti petunjuk di terminal

### Port yang digunakan:
- Contoh, Soal A, B, C: Port 12345
- Soal E: Port 5001 (dapat berubah jika port sudah digunakan)

## Requirements
- Python 3.x
- Socket module (built-in)
- Threading module (built-in)
- Datetime module (built-in)

## Catatan
- Pastikan tidak ada aplikasi lain yang menggunakan port yang sama
- Untuk testing di komputer yang sama, gunakan IP 127.0.0.1
- Untuk testing di komputer berbeda, gunakan IP address komputer server
