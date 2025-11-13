# Modul 4 - Advanced TCP Chat Implementation

## Deskripsi
Implementasi chat TCP yang lebih advanced dengan multi-threading dan fitur chat room yang lengkap. Modul ini memperkenalkan konsep multi-client support dimana satu server dapat menangani multiple client secara bersamaan, berbeda dengan modul 3 yang hanya mendukung komunikasi 1:1.

## Struktur Folder

### 1. `1.contoh/` - Multi-Threading Chat Server
Implementasi chat TCP dengan server multi-threading yang dapat menangani multiple client secara bersamaan. Server menggunakan thread terpisah untuk setiap koneksi client dan mengimplementasikan sistem broadcast untuk mengirim pesan ke semua client yang terhubung.

## Fitur
- **Multi-Client Support**: Server dapat menangani multiple client secara bersamaan dalam satu waktu
- **Threading Architecture**: Menggunakan threading untuk setiap client connection, memungkinkan server melayani banyak client secara paralel
- **Nickname System**: Setiap client harus memasukkan username untuk identifikasi dalam chat room
- **Real-time Communication**: Komunikasi real-time antara semua client melalui server
- **Broadcast Messaging**: Server mengirim pesan dari satu client ke semua client yang terhubung
- **Join/Leave Notifications**: Server mengirim notifikasi otomatis ketika client bergabung atau keluar dari chat room
- **Error Handling**: Proper error handling untuk menangani koneksi yang terputus secara tiba-tiba
- **Dual Threading on Client**: Client menggunakan dua thread terpisah untuk receiving dan sending messages

## Cara Menjalankan

### 1. Jalankan Server
```bash
cd 1.contoh
python3 server.py
```
Server akan:
- Bind ke alamat 127.0.0.1:5001
- Menunggu koneksi dari client
- Menampilkan informasi setiap client yang terhubung
- Menerima dan mem-broadcast pesan dari semua client

### 2. Jalankan Client (dapat multiple client)
Buka terminal baru untuk setiap client:
```bash
cd 1.contoh
python3 client.py
```
Client akan:
- Meminta username untuk identifikasi
- Menampilkan pesan "Terkoneksi dengan Server!" setelah berhasil terhubung
- Dapat mengirim pesan dengan format ">> {pesan}"
- Menerima pesan dari client lain secara real-time
- Menampilkan notifikasi ketika client lain bergabung atau keluar

## Keterangan Teknis
- **Protocol**: TCP (SOCK_STREAM)
- **Server Host**: 127.0.0.1 (localhost)
- **Server Port**: 5001
- **Encoding**: ASCII
- **Buffer Size**: 1024 bytes
- **Threading**: 
  - Server: Satu thread untuk setiap client connection (handle function)
  - Client: Dua thread terpisah (receive thread dan write thread)
- **Message Format**: "{username}: {message}"
- **Nickname Protocol**: Server mengirim 'NICK' untuk meminta username dari client
- **Broadcast Function**: Server memiliki fungsi broadcast() untuk mengirim pesan ke semua client
- **Client Management**: Server menyimpan list clients dan nicknames untuk manajemen koneksi

## Alur Kerja

### Server Side:
1. Server bind ke 127.0.0.1:5001 dan mulai listen
2. Ketika client terhubung, server mengirim 'NICK' untuk meminta username
3. Server menerima username dan menambahkan client ke list
4. Server mengirim notifikasi "Terkoneksi dengan Server!" ke client baru
5. Server mem-broadcast "{username} Bergabung!" ke semua client
6. Server membuat thread baru untuk handle client tersebut
7. Thread handle menerima pesan dari client dan mem-broadcast ke semua client
8. Ketika client disconnect, server mem-broadcast "{username} keluar!" dan remove client dari list

### Client Side:
1. Client meminta username dari user
2. Client connect ke server di 127.0.0.1:5001
3. Client membuat receive thread untuk menerima pesan dari server
4. Client membuat write thread untuk mengirim pesan ke server
5. Ketika menerima 'NICK', client mengirim username
6. Client menampilkan semua pesan yang diterima (baik dari server maupun client lain)
7. Client mengirim pesan dengan format "{username}: {message}"

## Contoh Output

### Server:
```
Terhubung dengan ('127.0.0.1', 54321)
Username alice
Terhubung dengan ('127.0.0.1', 54322)
Username bob
```

### Client 1 (alice):
```
Masukkan username: alice
Terkoneksi dengan Server!
alice Bergabung!
>> Hello everyone!
alice: Hello everyone!
bob Bergabung!
bob: Hi alice!
bob keluar!
```

### Client 2 (bob):
```
Masukkan username: bob
Terkoneksi dengan Server!
alice Bergabung!
alice: Hello everyone!
bob Bergabung!
>> Hi alice!
bob: Hi alice!
```

## Perbedaan dengan Modul 3

| Aspek | Modul 3 | Modul 4 |
|-------|---------|---------|
| **Komunikasi** | 1:1 (satu server, satu client) | 1:N (satu server, banyak client) |
| **Threading** | Simple threading untuk bidirectional chat | Advanced threading untuk multi-client handling |
| **Broadcast** | Tidak ada | Ada (pesan dikirim ke semua client) |
| **Nickname System** | Sederhana (hanya untuk identifikasi) | Dengan protokol NICK request |
| **Join/Leave** | Tidak ada notifikasi | Ada notifikasi ketika client join/leave |
| **Client Management** | Tidak perlu (hanya satu client) | Perlu manage list clients dan nicknames |
| **Use Case** | Private chat | Chat room / group chat |

## Catatan Penting
- Server dapat menangani unlimited client (dalam batas resource sistem)
- Setiap client connection diproses dalam thread terpisah untuk menghindari blocking
- Cocok untuk implementasi chat room sederhana atau group chat
- Menggunakan TCP untuk reliable communication dengan jaminan pengiriman data
- Client menggunakan dual threading untuk non-blocking communication (dapat kirim dan terima secara bersamaan)
- Encoding menggunakan ASCII, sehingga karakter non-ASCII mungkin tidak didukung dengan baik
- Pastikan tidak ada aplikasi lain yang menggunakan port 5001
- Untuk testing di komputer yang sama, gunakan IP 127.0.0.1
- Untuk testing di komputer berbeda, ubah host di client.py menjadi IP address komputer server

## Requirements
- Python 3.x
- Socket module (built-in)
- Threading module (built-in)

## Troubleshooting
- **Port already in use**: Pastikan tidak ada server lain yang menggunakan port 5001
- **Connection refused**: Pastikan server sudah berjalan sebelum menjalankan client
- **Client tidak menerima pesan**: Pastikan receive thread berjalan dengan baik
- **Encoding error**: Pastikan menggunakan karakter ASCII saja (hindari karakter khusus)
