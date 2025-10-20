# SP3.1 PPBJ - Socket Programming Project

## Deskripsi
Proyek pembelajaran socket programming menggunakan Python dengan berbagai implementasi dari UDP hingga TCP multi-threading chat server.

## Struktur Project

### Modul 1 - UDP Socket Programming
Implementasi dasar UDP socket communication dengan pesan otomatis dan multi-threading.

### Modul 2 - UDP Multi-Threading Server  
Server UDP dengan multi-threading untuk menangani multiple client dan username system.

### Modul 3 - TCP Socket Programming
Implementasi TCP socket communication dengan fitur progresif dari basic hingga bidirectional chat.

### Modul 4 - Advanced TCP Chat Implementation
Chat TCP advanced dengan multi-client support dan broadcast messaging.

## Progres Fitur

| Fitur | Modul 1 | Modul 2 | Modul 3 | Modul 4 |
|-------|---------|---------|---------|---------|
| **Protocol** | UDP | UDP | TCP | TCP |
| **Basic Socket** | ✅ | ✅ | ✅ | ✅ |
| **Auto IP Detection** | ❌ | ❌ | ✅ | ❌ |
| **Dynamic Configuration** | ✅ | ❌ | ✅ | ❌ |
| **Multi-Client Support** | ❌ | ✅ | ❌ | ✅ |
| **Threading** | ✅ | ✅ | ✅ | ✅ |
| **Username System** | ❌ | ✅ | ❌ | ✅ |
| **Date/Time Display** | ❌ | ❌ | ✅ | ❌ |
| **Bidirectional Chat** | ❌ | ❌ | ✅ | ✅ |
| **Broadcast Messaging** | ❌ | ❌ | ❌ | ✅ |

## Quick Start

### Modul 1 - UDP Basic
```bash
cd modul_1
python3 server.py    # Terminal 1
python3 client.py    # Terminal 2
```

### Modul 2 - UDP Multi-Threading
```bash
cd modul_2
python3 server.py    # Terminal 1
python3 client.py    # Terminal 2 (multiple instances)
```

### Modul 3 - TCP Progressive
```bash
cd modul_3/5.soal_e  # Latest TCP implementation
python3 server.py    # Terminal 1
python3 client.py    # Terminal 2
```

### Modul 4 - TCP Chat Server
```bash
cd modul_4/1.contoh
python3 server.py    # Terminal 1
python3 client.py    # Terminal 2 (multiple instances)
```

## Requirements
- Python 3.x
- Built-in modules: socket, threading, datetime, sys

## Port Configuration
- **Modul 1**: Port 5000 (server), dynamic (client)
- **Modul 2**: Port 5002 (server), 192.168.1.6:5002 (client)
- **Modul 3**: Port 12345 (default), 5001 (latest)
- **Modul 4**: Port 55555 (default)

## Features Summary

### UDP Implementations (Modul 1-2)
- Connectionless communication
- Fast but unreliable
- Suitable for real-time applications
- Multi-client support with threading

### TCP Implementations (Modul 3-4)
- Reliable connection-oriented communication
- Auto IP detection with hostname resolution
- Progressive feature development
- Advanced chat functionality
- Input clearing and proper message handling

## Learning Path
1. **Start with Modul 1**: Learn basic UDP socket programming
2. **Progress to Modul 2**: Understand multi-threading with UDP
3. **Move to Modul 3**: Learn TCP socket programming progressively
4. **Finish with Modul 4**: Master advanced TCP chat implementation

## Notes
- Each module builds upon previous concepts
- README files provide detailed documentation for each implementation
- Code includes proper error handling and threading
- Suitable for learning socket programming fundamentals
