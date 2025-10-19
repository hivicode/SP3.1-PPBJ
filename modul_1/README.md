# Modul 1 - UDP Socket Programming

## Deskripsi
Implementasi komunikasi socket menggunakan protokol UDP (User Datagram Protocol) dengan client yang mengirim pesan berulang dan server yang menerima pesan.

## Fitur
- **UDP Protocol**: Menggunakan socket UDP untuk komunikasi
- **Automatic Message Sending**: Client mengirim pesan otomatis setiap detik
- **Dynamic Server Configuration**: User dapat memasukkan IP dan port server
- **Threading**: Menggunakan threading untuk mengirim pesan dan mengontrol stop
- **Message Counter**: Pesan dikirim dengan counter yang bertambah otomatis

## File Structure
- `server.py`: Server UDP yang menerima dan menampilkan pesan
- `client.py`: Client UDP yang mengirim pesan berulang

## Cara Menjalankan

### 1. Jalankan Server
```bash
python3 server.py
```
Server akan:
- Bind ke alamat 0.0.0.0:5000
- Menampilkan "Server mendengarkan..."
- Menerima dan menampilkan pesan dari client

### 2. Jalankan Client
```bash
python3 client.py
```
Client akan meminta:
- IP Address Server
- Port Server
- Kemudian mulai mengirim pesan otomatis

## Keterangan Teknis
- **Protocol**: UDP (SOCK_DGRAM)
- **Server Port**: 5000 (hardcoded di server)
- **Client Behavior**: Mengirim pesan "Data ke: {counter}" setiap detik
- **Stop Mechanism**: Tekan Enter untuk menghentikan pengiriman
- **Threading**: 2 thread - satu untuk mengirim, satu untuk kontrol stop

## Contoh Output

### Server:
```
Server mendengarkan...
192.168.1.100 : Data ke: 1
192.168.1.100 : Data ke: 2
192.168.1.100 : Data ke: 3
```

### Client:
```
Masukkan IP Address Server: 192.168.1.6
Masukkan Port Server: 5000
Ter kirim: Data ke: 1
Ter kirim: Data ke: 2
Ter kirim: Data ke: 3
```

## Catatan
- UDP adalah protokol connectionless, jadi tidak ada handshake
- Pesan mungkin hilang atau tidak terurut (karakteristik UDP)
- Cocok untuk aplikasi real-time yang toleran terhadap packet loss
