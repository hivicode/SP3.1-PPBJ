# Modul 4 - Advanced TCP Chat Implementation

## Deskripsi
Implementasi chat TCP yang lebih advanced dengan multi-threading dan fitur chat room yang lengkap.

## Struktur Folder

### 1. `1.contoh/` - Multi-Threading Chat
Implementasi chat TCP dengan server multi-threading yang dapat menangani multiple client secara bersamaan.

## Fitur
- **Multi-Client Support**: Server dapat menangani multiple client secara bersamaan
- **Threading Architecture**: Menggunakan threading untuk setiap client connection
- **Nickname System**: Client dapat menggunakan username untuk identifikasi
- **Real-time Communication**: Komunikasi real-time antara client dan server
- **Broadcast Messaging**: Server dapat mengirim pesan ke semua client yang terhubung
- **Error Handling**: Proper error handling untuk koneksi yang terputus

## Cara Menjalankan

### 1. Jalankan Server
```bash
python3 server.py
```
Server akan:
- Bind ke alamat 127.0.0.1:55555 (default)
- Menampilkan "Server menunggu koneksi..."
- Menerima koneksi dari multiple client

### 2. Jalankan Client (dapat multiple client)
```bash
python3 client.py
```
Client akan meminta:
- Username untuk identifikasi
- Kemudian dapat mengirim dan menerima pesan

## Keterangan Teknis
- **Protocol**: TCP (SOCK_STREAM)
- **Server Port**: 55555 (default)
- **Threading**: Server menggunakan thread terpisah untuk setiap client
- **Message Format**: "{username}: {message}"
- **Nickname Handling**: Server menangani nickname request dari client

## Contoh Output

### Server:
```
Server menunggu koneksi...
Client 192.168.1.100 terhubung dengan nickname: user1
Client 192.168.1.101 terhubung dengan nickname: user2
user1: Hello everyone!
user2: Hi there!
```

### Client:
```
Masukkan username: user1
>> Hello everyone!
user2: Hi there!
>> 
```

## Perbedaan dengan Modul 3
- **Modul 3**: Client-server 1:1 communication
- **Modul 4**: Multi-client support dengan broadcast messaging
- **Modul 3**: Simple threading untuk bidirectional chat
- **Modul 4**: Advanced threading untuk multiple client handling
- **Modul 4**: Nickname system dan broadcast functionality

## Catatan
- Server dapat menangani unlimited client (dalam batas sistem)
- Setiap client connection diproses dalam thread terpisah
- Cocok untuk implementasi chat room sederhana
- Menggunakan TCP untuk reliable communication
