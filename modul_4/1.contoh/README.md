# Modul 4 - Contoh: Multi-Threading Chat Server

## Deskripsi
Implementasi chat TCP dengan server multi-threading yang dapat menangani multiple client secara bersamaan.

## Fitur
- **Multi-Client Support**: Server dapat menangani multiple client secara bersamaan
- **Threading Architecture**: Menggunakan threading untuk setiap client connection
- **Nickname System**: Client dapat menggunakan username untuk identifikasi
- **Real-time Communication**: Komunikasi real-time antara client dan server
- **Broadcast Messaging**: Server dapat mengirim pesan ke semua client yang terhubung
- **Error Handling**: Proper error handling untuk koneksi yang terputus

## File Structure
- `server.py`: Server TCP multi-threading yang menangani multiple client
- `client.py`: Client TCP dengan threading untuk send dan receive

## Cara Menjalankan

### 1. Jalankan Server
```bash
python3 server.py
```
Server akan:
- Bind ke alamat 127.0.0.1:55555
- Menampilkan "Server menunggu koneksi..."
- Menerima koneksi dari multiple client

### 2. Jalankan Client (dapat multiple client)
```bash
python3 client.py
```
Client akan meminta:
- Username untuk identifikasi
- Kemudian dapat mengirim dan menerima pesan secara real-time

## Keterangan Teknis
- **Protocol**: TCP (SOCK_STREAM)
- **Server Port**: 55555
- **Threading**: 
  - Server: Thread terpisah untuk setiap client connection
  - Client: Thread terpisah untuk receiving dan sending messages
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

## Catatan
- Server dapat menangani unlimited client (dalam batas sistem)
- Setiap client connection diproses dalam thread terpisah
- Cocok untuk implementasi chat room sederhana
- Menggunakan TCP untuk reliable communication
- Client menggunakan threading untuk non-blocking communication
