# SP3.1 PPBJ - Socket Programming Project

## Deskripsi
Proyek pembelajaran socket programming menggunakan Python dengan berbagai implementasi dari UDP basic hingga Web Server dengan Template Engine.

## Struktur Project

### Modul 1 - UDP Socket Programming
Implementasi dasar UDP socket communication dengan pesan otomatis dan multi-threading.

### Modul 2 - UDP Multi-Threading Server  
Server UDP dengan multi-threading untuk menangani multiple client dan username system.

### Modul 3 - TCP Socket Programming
Implementasi TCP socket communication dengan fitur progresif dari basic hingga bidirectional chat.

### Modul 4 - Advanced TCP Chat Implementation
Chat TCP advanced dengan multi-client support dan broadcast messaging.

### Modul 5 - Static Web Server 🆕
HTTP web server sederhana untuk melayani file statis (HTML, CSS, JS, images).

### Modul 6 - Web Server with Template Engine 🆕
HTTP web server dengan template engine untuk dynamic content rendering menggunakan Python code embedded di HTML.

### Dzaky - Web Application (Production-Ready) 🆕
Web aplikasi lengkap "Dzaky Wallet" dengan authentication system, template engine, dan modern UI.

## Progres Fitur

| Fitur | Modul 1 | Modul 2 | Modul 3 | Modul 4 | Modul 5 | Modul 6 | Dzaky |
|-------|---------|---------|---------|---------|---------|---------|-------|
| **Protocol** | UDP | UDP | TCP | TCP | HTTP/TCP | HTTP/TCP | HTTP/TCP |
| **Basic Socket** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Multi-Client** | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ |
| **Threading** | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ |
| **Static Files** | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ |
| **Template Engine** | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |
| **POST Method** | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |
| **Authentication** | ❌ | ❌ | ❌ | ❌ | Client | Server | Server |
| **Database** | ❌ | ❌ | ❌ | ❌ | ❌ | JSON | JSON |
| **Form Validation** | ❌ | ❌ | ❌ | ❌ | ❌ | Client | Client+Server |
| **Dynamic Rendering** | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |

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
cd modul_3/5.soal_e
python3 server.py    # Terminal 1
python3 client.py    # Terminal 2
```

### Modul 4 - TCP Chat Server
```bash
cd modul_4/1.contoh
python3 server.py    # Terminal 1
python3 client.py    # Terminal 2 (multiple instances)
```

### Modul 5 - Static Web Server 🆕
```bash
cd modul_5
python httpd.py
# Browser: http://localhost:8530
```

### Modul 6 - Web Server with Template Engine 🆕
```bash
cd modul_6
python httpd.py
# Browser: http://127.0.0.5:722
# Login: 722@dor.com / banheesoo
```

### Dzaky - Full Web Application 🆕
```bash
cd Dzaky
python httpd.py
# Browser: http://127.0.0.1:8080
# Login: admin / 123
```

## Requirements
- Python 3.x
- Built-in modules: socket, threading, datetime, sys, os, mimetypes, json, re

## Port Configuration
- **Modul 1**: 5000 (server)
- **Modul 2**: 5002 (server)
- **Modul 3**: 12345 / 5001
- **Modul 4**: 55555
- **Modul 5**: 8530 🆕
- **Modul 6**: 722 🆕
- **Dzaky**: 8080 🆕

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

### HTTP Web Server Implementations (Modul 5-6, Dzaky) 🆕
- **Modul 5**: Static file serving, MIME types
- **Modul 6**: Template engine, POST handling, server-side logic
- **Dzaky**: Full auth system, validation, modern UI, clean code

## Template Engine Syntax (Modul 6 & Dzaky)

### Basic Usage
```html
<!DOCTYPE html>
<html>
<body>
  {% 
  # Python code here
  if condition:
      emit('<h1>True</h1>')
  else:
      emit('<h1>False</h1>')
  %}
</body>
</html>
```

### With POST Data
```html
{% 
from urllib.parse import unquote

if '_POST' in dir() and _POST:
    username = unquote(_POST.get('username', ''))
    emit('Welcome, ', username, '!')
%}
```

## Authentication System (Modul 6 & Dzaky)

### Features
- ✅ User registration (signup)
- ✅ User login (username or email)
- ✅ Server-side validation
- ✅ Client-side real-time feedback
- ✅ Persistent JSON database
- ✅ Dynamic dashboard with user info

### Flow
```
Signup → Validation → Save to JSON
Login → Verify → Generate Session → Redirect Dashboard
```

## Database (JSON)

### Location
- **Modul 6**: `modul_6/users_db.json`
- **Dzaky**: `Dzaky/users_db.json`

### Format
```json
{
  "username": {
    "password": "plain_text_password",
    "nama": "Display Name",
    "email": "user@example.com"
  }
}
```

## Learning Path

### Beginner (Socket Basics)
1. **Modul 1**: UDP socket programming
2. **Modul 2**: Multi-threading with UDP
3. **Modul 3**: TCP socket programming
4. **Modul 4**: Advanced TCP chat

### Intermediate (Web Development)
5. **Modul 5**: HTTP server & static files
6. **Modul 6**: Template engine & POST handling

### Advanced (Full Application)
7. **Dzaky**: Complete web app with auth

## Project Highlights

### Technical Skills Learned
- Socket programming (UDP/TCP)
- HTTP protocol implementation
- Template engine development
- Form processing (GET/POST)
- Client-server architecture
- Multi-threading
- Data persistence (JSON)
- Authentication systems
- Input validation (client & server)

### Best Practices Applied
- Clean code structure
- Modular functions
- Error handling
- Security considerations
- User experience (UX)
- Code documentation (README)

## Security Notes

⚠️ **Educational Purpose Only - Not for Production!**

**Missing for Production:**
- Password hashing (use bcrypt/argon2)
- Session management (JWT/cookies)
- HTTPS/SSL encryption
- CSRF protection
- Rate limiting
- SQL injection prevention
- XSS prevention
- Input sanitization

## Comparison Table

| Aspect | Modul 5 | Modul 6 | Dzaky |
|--------|---------|---------|-------|
| **Purpose** | Static web | Dynamic web | Full web app |
| **Lines of Code** | ~97 | ~156 | ~149 |
| **Template Engine** | ❌ | ✅ | ✅ |
| **Authentication** | Client-only | Server-side | Server-side |
| **Validation** | ❌ | Client | Client+Server |
| **Real-time Feedback** | ❌ | ❌ | ✅ |
| **UI Quality** | Basic | Good | Modern |
| **Code Quality** | OK | Good | Clean |
| **Login Methods** | 1 | 1 | 2 (user/email) |

## Documentation

Each module has detailed README:
- `modul_1/README.md` - UDP basics
- `modul_2/README.md` - UDP multi-threading
- `modul_3/README.md` - TCP progressive
- `modul_4/README.md` - TCP chat
- `modul_5/README.md` 🆕 - Static web server
- `modul_6/README.md` 🆕 - Template engine
- `Dzaky/README.md` 🆕 - Full web application

## Testing

### Socket Programs (Modul 1-4)
```bash
# Start server first, then client(s)
python server.py
python client.py
```

### Web Servers (Modul 5-6, Dzaky)
```bash
# Start server, then open browser
python httpd.py
# Navigate to URL in browser
```

## Troubleshooting

### Port Already in Use
```bash
# Windows
netstat -ano | findstr :PORT_NUMBER

# Linux/Mac
lsof -i :PORT_NUMBER

# Solution: Change port in code or kill process
```

### Import Errors
```bash
# Make sure you're in the correct directory
cd modul_X
python httpd.py
```

### Template Engine Errors
- Check `{% %}` syntax
- Verify indentation in Python code
- Use `encoding='utf-8'` for file reading

## Future Enhancements

Potential additions:
- [ ] Session management (cookies/JWT)
- [ ] Password hashing (bcrypt)
- [ ] Database integration (SQLite/PostgreSQL)
- [ ] HTTPS support
- [ ] File upload functionality
- [ ] REST API endpoints
- [ ] WebSocket support
- [ ] Rate limiting
- [ ] Logging system
- [ ] Unit tests

## Credits

**Course**: SP3.1 PPBJ  
**Topic**: Socket Programming & Web Development  
**Language**: Python 3.x  
**Modules**: 1-6 + Dzaky  

## License

Educational purpose only. Not for production use without proper security implementations.

---

**Last Updated**: December 2024  
**Total Modules**: 7 (Modul 1-6 + Dzaky)  
**Total Lines**: ~10,000+ lines of code  
**Skills**: Socket Programming, HTTP, Template Engine, Authentication, Web Development
