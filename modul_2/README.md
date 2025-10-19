# Modul 2 - UDP Multi-Threading Server

## Deskripsi
Implementasi server UDP dengan multi-threading untuk menangani multiple client secara bersamaan, dan client yang mengirim pesan dengan username.

## Fitur
- **UDP Protocol**: Menggunakan socket UDP untuk komunikasi
- **Multi-Threading Server**: Server menggunakan threading untuk menangani setiap pesan
- **Username Support**: Client dapat memasukkan username untuk identifikasi
- **Automatic Message Sending**: Client mengirim pesan dengan username dan counter
- **Thread per Message**: Setiap pesan diterima dalam thread terpisah

## File Structure
- `server.py`: Server UDP multi-threading yang menerima pesan dari multiple client
- `client.py`: Client UDP yang mengirim pesan dengan username

## Cara Menjalankan

### 1. Jalankan Server
```bash
python3 server.py
```
Server akan:
- Bind ke alamat 0.0.0.0:5002
- Menampilkan "Server menunggu..."
- Menerima pesan dan menampilkannya dalam thread terpisah

### 2. Jalankan Client (dapat multiple client)
```bash
python3 client.py
```
Client akan meminta:
- Username
- Kemudian mulai mengirim pesan otomatis dengan format: "{username}: pesan ke-{counter}"

## Keterangan Teknis
- **Protocol**: UDP (SOCK_DGRAM)
- **Server Port**: 5002
- **Client IP**: 192.168.1.6 (hardcoded di client)
- **Threading**: Server membuat thread baru untuk setiap pesan yang diterima
- **Message Format**: "{username}: pesan ke-{counter}"
- **Auto Send**: Pesan dikirim setiap detik

## Contoh Output

### Server:
```
Server menunggu...
[192.168.1.100] user1: pesan ke-1
[192.168.1.101] user2: pesan ke-1
[192.168.1.100] user1: pesan ke-2
[192.168.1.101] user2: pesan ke-2
```

### Client:
```
Masukkan username: user1
Ter kirim: user1: pesan ke-1
Ter kirim: user1: pesan ke-2
Ter kirim: user1: pesan ke-3
```

## Perbedaan dengan Modul 1
- **Modul 1**: Server single-threaded, client dengan counter tanpa username
- **Modul 2**: Server multi-threaded, client dengan username dan counter
- **Modul 1**: Port 5000
- **Modul 2**: Port 5002

## Catatan
- Server dapat menangani multiple client secara bersamaan
- Setiap pesan diproses dalam thread terpisah
- Cocok untuk simulasi chat room sederhana dengan UDP
- Client IP hardcoded, perlu diubah sesuai environment
