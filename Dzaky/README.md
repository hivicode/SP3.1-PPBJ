# Dzaky - Web Application with Template Engine

## Deskripsi
Web aplikasi lengkap "Dzaky Wallet" dengan template engine, authentication system, dan modern UI. Implementasi production-ready untuk pembelajaran web development dengan Python socket programming.

## Fitur
- ✅ HTTP Server dengan TCP Socket
- ✅ Template Engine (`{% %}` syntax)
- ✅ Server-side validation & processing
- ✅ User authentication (login/signup)
- ✅ Persistent JSON database
- ✅ Login dengan username atau email
- ✅ Real-time form validation
- ✅ Modern & responsive UI
- ✅ Dashboard dengan user info
- ✅ Clean code (no unnecessary comments)

## Struktur File
```
Dzaky/
├── httpd.py              # Web server (149 lines)
├── template.py           # Template engine (69 lines)
├── users_db.json         # User database
└── htdocs/
    ├── index.html        # Landing page (Dzaky Wallet)
    ├── login.html        # Login form
    ├── signup.html       # Signup form + validation
    ├── auth-process.html # Authentication handler
    ├── dashboard.html    # User dashboard
    └── style.css         # Modern styling
```

## Quick Start

### 1. Jalankan Server
```bash
cd Dzaky
python httpd.py
```

Server akan jalan di: `http://127.0.0.1:8080`

### 2. Test Authentication

**Default User:**
- Username: `admin`
- Password: `123`

**Test Flow:**
1. **Signup**: `http://127.0.0.1:8080/signup.html`
   - Username: `dzaky`
   - Email: `dzaky@mail.com`
   - Password: `test123`

2. **Login**: `http://127.0.0.1:8080/login.html`
   - Gunakan username `dzaky` atau email `dzaky@mail.com`
   - Password: `test123`

3. **Dashboard**: Auto-redirect dengan user info

## Template Engine

### Cara Kerja
File HTML dengan embedded Python code:

```html
<!DOCTYPE html>
<html>
<body>
  {% 
  from urllib.parse import unquote
  
  if '_POST' in dir() and _POST:
      username = unquote(_POST.get('username', ''))
      emit('<h1>Welcome, ', username, '!</h1>')
  %}
</body>
</html>
```

### Built-in Functions
- `emit(*args)`: Output HTML/text
- `_POST`: Dictionary dengan POST data
- Import Python modules as needed

### Example: Auth Processing

```python
{% 
def authenticate(username_or_email, password):
    if username_or_email in users_db:
        if users_db[username_or_email]['password'] == password:
            return True, users_db[username_or_email]
    
    for username, user_data in users_db.items():
        if user_data.get('email', '').lower() == username_or_email.lower():
            if user_data['password'] == password:
                return True, user_data
    
    return False, None

is_valid, user_data = authenticate(username, password)

if is_valid:
    nama_encoded = user_data['nama'].replace(' ', '+')
    redirect_url = f'dashboard.html?user={username}&name={nama_encoded}'
    emit('<h1>Login Berhasil!</h1>')
    emit('<meta http-equiv="refresh" content="2;url=', redirect_url, '">')
else:
    emit('<h1>Login Gagal!</h1>')
    emit('<p>Username atau password salah</p>')
%}
```

## Form Validation

### Client-Side (Real-time)
```javascript
// Password validation dengan feedback
passwordInput.addEventListener('input', function() {
  const length = this.value.length;
  const small = this.parentElement.querySelector('small');
  
  if (length === 0) {
    small.style.color = '#666';
    small.textContent = 'Password minimal 3 karakter';
  } else if (length < 3) {
    small.style.color = '#f44336';
    small.textContent = `⚠️ ${length}/3 karakter - butuh ${3 - length} lagi`;
  } else {
    small.style.color = '#4CAF50';
    small.textContent = `✓ Password OK (${length} karakter)`;
  }
});
```

### Server-Side (Python)
```python
{% 
def register_user(username, email, password):
    if username in users_db:
        return False, "Username sudah digunakan"
    if not validate_email(email):
        return False, "Format email tidak valid"
    if len(password) < 3:
        return False, "Password minimal 3 karakter"
    
    users_db[username] = {
        'password': password,
        'nama': username.title(),
        'email': email
    }
    
    if save_users(users_db):
        return True, "Registrasi berhasil"
    return False, "Gagal menyimpan data"
%}
```

## Database (users_db.json)

### Format
```json
{
  "admin": {
    "password": "123",
    "nama": "Administrator",
    "email": "admin@dzaky.com"
  },
  "dzaky": {
    "password": "test123",
    "nama": "Dzaky",
    "email": "dzaky@mail.com"
  }
}
```

### Functions
```python
def load_users():
    """Load dari JSON file"""
    try:
        if os.path.exists(DB_FILE):
            with open(DB_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        return default_users
    except:
        return default_users

def save_users(users_data):
    """Save ke JSON file"""
    try:
        with open(DB_FILE, 'w', encoding='utf-8') as f:
            json.dump(users_data, f, indent=2, ensure_ascii=False)
        return True
    except:
        return False
```

## HTTP Flow

### GET Request
```
Browser → GET /index.html → Server
Server → Read file → Send response → Browser
```

### POST Request (Login/Signup)
```
Browser → POST /auth-process.html + data
Server → Parse POST data
      → Execute Python code in template
      → Render dynamic HTML
      → Send response
Browser → Display result / redirect
```

## Validation Flow

### Signup Validation
1. **Client-side (JavaScript)**:
   - Username tidak kosong
   - Email format valid (regex)
   - Password ≥ 3 karakter
   - Alert jika gagal, block submit

2. **Server-side (Python)**:
   - Username belum digunakan
   - Email format valid
   - Password length check
   - Save to database

### Login Validation
1. **Client-side**: Basic field validation
2. **Server-side**:
   - Check username/email di database
   - Verify password
   - Generate redirect URL dengan user info

## Konfigurasi

### Server
```python
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8080
DOCUMENT_ROOT = 'htdocs/'
DB_FILE = 'Dzaky/users_db.json'
```

### Encoding
- UTF-8 untuk semua file
- Support emoji dan special characters

## UI/UX Features

### Landing Page (index.html)
- Hero section dengan CTA
- Fitur showcase
- Modern gradient design
- Responsive layout

### Login/Signup Forms
- Clean & minimal design
- Input validation feedback
- Error messages
- Loading states
- Smooth transitions

### Dashboard
- Welcome message dengan nama user
- User stats cards
- Summary grid
- Chart placeholders
- Logout functionality

## Code Quality

### Clean Code
- ✅ No unnecessary comments
- ✅ Self-explanatory variable names
- ✅ Modular functions
- ✅ Consistent formatting
- ✅ Error handling

### File Sizes
- `httpd.py`: 149 lines (compact)
- `template.py`: 69 lines (efficient)
- Total backend: ~6.3 KB

## Security Considerations

⚠️ **For Learning Purposes Only!**

**Current Implementation:**
- Plain text passwords (❌ Production)
- No session management
- No HTTPS
- Basic validation only

**For Production, Add:**
- Password hashing (bcrypt/argon2)
- Session tokens (JWT/cookies)
- HTTPS/SSL encryption
- CSRF protection
- Rate limiting
- SQL injection protection (if using DB)
- Input sanitization
- XSS prevention

## Comparison with Other Modules

| Feature | Modul 5 | Modul 6 | Dzaky |
|---------|---------|---------|-------|
| Static Files | ✅ | ✅ | ✅ |
| Template Engine | ❌ | ✅ | ✅ |
| POST Handler | ❌ | ✅ | ✅ |
| Authentication | Client-only | Server-side | Server-side |
| Database | ❌ | JSON | JSON |
| Login Method | Basic | Username | Username/Email |
| Form Validation | ❌ | Client | Client + Server |
| UI Quality | Basic | Good | Modern |
| Code Quality | OK | Good | Clean |
| Real-time Feedback | ❌ | ❌ | ✅ |

## Learning Objectives

### Technical Skills
1. **Socket Programming**: HTTP server implementation
2. **Template Engine**: Dynamic content rendering
3. **Form Processing**: POST request handling
4. **Data Persistence**: JSON file operations
5. **Validation**: Client & server-side
6. **Authentication**: User login system

### Best Practices
1. Clean code without cluttered comments
2. Modular function design
3. Error handling
4. User experience (UX)
5. Code organization

## Testing Checklist

- [ ] Server starts without errors
- [ ] Landing page loads correctly
- [ ] Signup with valid data works
- [ ] Signup validation blocks invalid input
- [ ] Alert shows for password < 3 chars
- [ ] Real-time feedback updates
- [ ] Data saves to users_db.json
- [ ] Login with username works
- [ ] Login with email works
- [ ] Wrong password shows error
- [ ] Dashboard shows correct user info
- [ ] Logout redirects to login

## Troubleshooting

### Server tidak start
```bash
# Check port sudah dipakai
netstat -an | findstr :8080

# Ganti port di httpd.py jika perlu
SERVER_PORT = 8081
```

### File tidak ditemukan
```bash
# Pastikan working directory benar
cd d:/Repo/hivicode/SP3.1-PPBJ/Dzaky
python httpd.py
```

### Database tidak tersimpan
```bash
# Check file permissions
# Pastikan folder writable
# Check error messages di terminal
```

## Deployment Notes

Untuk production deployment:
1. Use proper web framework (Flask/Django)
2. Implement proper authentication (OAuth, JWT)
3. Use real database (PostgreSQL/MySQL)
4. Add HTTPS certificate
5. Implement session management
6. Add logging and monitoring
7. Use environment variables
8. Add unit tests
9. Implement CI/CD pipeline

## Credits

**Developer**: Dzaky  
**Purpose**: Learning Project - Socket Programming & Web Development  
**Course**: SP3.1 PPBJ  
**Tech Stack**: Python Socket, Custom Template Engine, HTML/CSS/JavaScript

## License

Educational purpose only. Not for production use.


