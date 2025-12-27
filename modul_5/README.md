# Modul 5 - Static Web Server

## Deskripsi
Web server HTTP sederhana yang melayani file statis (HTML, CSS, JavaScript, gambar) menggunakan socket TCP.

## Fitur
- ✅ HTTP Server menggunakan TCP Socket
- ✅ MIME Type detection untuk berbagai format file
- ✅ Static file serving (HTML, CSS, JS, Images)
- ✅ Error handling (404, 500)
- ✅ Automatic index.html serving
- ✅ UTF-8 encoding support

## Struktur File
```
modul_5/
├── httpd.py          # Web server
├── index.html        # Landing page
├── login.html        # Login page
└── style.css         # Stylesheet
```

## Quick Start

### 1. Jalankan Server
```bash
cd modul_5
python httpd.py
```

Server akan jalan di: `http://localhost:8530`

### 2. Akses via Browser
- Homepage: `http://localhost:8530/`
- Login: `http://localhost:8530/login.html`

## Konfigurasi

### Port & Host
```python
SERVER_HOST = 'localhost'
SERVER_PORT = 8530
```

### MIME Types Support
- **Text**: `.html`, `.css`, `.js`, `.json`
- **Images**: `.png`, `.jpg`, `.jpeg`, `.gif`, `.svg`, `.ico`

## Cara Kerja

1. **Server Listen**: Server mendengarkan koneksi di port 8530
2. **Client Request**: Browser mengirim HTTP request
3. **Parse Request**: Server parse request untuk mendapat path file
4. **Serve File**: 
   - Jika file ada → kirim dengan MIME type yang sesuai
   - Jika tidak ada → kirim 404 Not Found
5. **Close Connection**: Tutup koneksi setelah response dikirim

## Response Codes
- **200 OK**: File ditemukan dan berhasil dikirim
- **404 Not Found**: File tidak ditemukan
- **500 Internal Server Error**: Error saat memproses request

## Contoh Request & Response

### Request
```http
GET /index.html HTTP/1.1
Host: localhost:8530
```

### Response
```http
HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8

<!DOCTYPE html>
<html>
...
</html>
```

## Catatan
- Server ini hanya untuk pembelajaran
- Tidak ada security features
- Single-threaded (satu request per waktu)
- Tidak ada caching
- Client-side authentication menggunakan localStorage

## Teknologi
- **Backend**: Python Socket Programming
- **Protocol**: HTTP/1.1 over TCP
- **Frontend**: HTML5, CSS3, JavaScript

## Next Step
Lihat **Modul 6** untuk implementasi dengan template engine dan server-side processing.

