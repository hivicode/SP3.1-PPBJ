# Modul 6 - Web Server with Template Engine

## Deskripsi
Web server HTTP dengan template engine untuk dynamic content rendering menggunakan Python code embedded di HTML (`{% %}`).

## Fitur
- ✅ HTTP Server dengan TCP Socket
- ✅ **Template Engine** dengan syntax `{% %}`
- ✅ Server-side validation (Python)
- ✅ POST method support
- ✅ User authentication system
- ✅ Persistent data storage (JSON)
- ✅ Login/Signup functionality
- ✅ Dynamic HTML rendering
- ✅ Form validation (client + server side)
- ✅ Real-time password feedback

## Struktur File
```
modul_6/
├── httpd.py              # Web server dengan POST handler
├── template.py           # Template engine class
├── users_db.json         # User database (persistent)
└── htdocs/
    ├── index.html        # Landing page
    ├── login.html        # Login form (POST)
    ├── signup.html       # Signup form (POST + validation)
    ├── auth-process.html # Auth handler (template engine)
    ├── dashboard.html    # Dashboard dengan user info
    ├── about.html        # About page
    ├── services.html     # Services page
    ├── subscribe.html    # Subscribe form
    ├── header.js         # Navigation component
    └── style.css         # Stylesheet
```

## Quick Start

### 1. Jalankan Server
```bash
cd modul_6
python httpd.py
```

Server akan jalan di: `http://127.0.0.5:722`

### 2. Test Authentication

**Default User:**
- Email: `722@dor.com`
- Password: `banheesoo`

**Flow:**
1. Buka `http://127.0.0.5:722/signup.html`
2. Daftar user baru
3. Data tersimpan di `users_db.json`
4. Login di `http://127.0.0.5:722/login.html`
5. Redirect ke dashboard dengan user info

## Template Engine

### Syntax
```html
{% 
# Python code here
from urllib.parse import unquote

if '_POST' in dir() and _POST:
    username = unquote(_POST.get('username', ''))
    emit('<h1>Hello, ', username, '!</h1>')
else:
    emit('<h1>No data</h1>')
%}
```

### Built-in Functions
- `emit(*args)`: Output HTML
- `fmt_emit(format, *args)`: Format output
- `_POST`: Dictionary berisi POST data

### Contoh Template (`auth-process.html`)
```python
{% 
def authenticate(username, password):
    if username in users_db:
        if users_db[username]['password'] == password:
            return True, users_db[username]
    return False, None

is_valid, user_data = authenticate(username, password)
if is_valid:
    emit('<h1>Login Successful!</h1>')
    emit('<p>Welcome, ', user_data['nama'], '!</p>')
else:
    emit('<h1>Login Failed</h1>')
%}
```

## Form Validation

### Client-Side Validation (JavaScript)

**onsubmit validation:**
```javascript
function validateForm() {
  const username = document.getElementById('username').value;
  const email = document.getElementById('email').value;
  const password = document.getElementById('password').value;
  
  // Username validation
  if (username.trim().length < 1) {
    alert('⚠️ Username cannot be empty!');
    return false;
  }
  
  // Email format validation
  const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
  if (!emailPattern.test(email)) {
    alert('⚠️ Please enter a valid email address!');
    return false;
  }
  
  // Password length validation
  if (password.length < 3) {
    alert('⚠️ Password must be at least 3 characters!');
    return false;
  }
  
  return true;
}
```

**Real-time feedback:**
```javascript
passwordInput.addEventListener('input', function() {
  const length = this.value.length;
  const small = this.parentElement.querySelector('small');
  
  if (length === 0) {
    small.style.color = '#666';
    small.textContent = 'Password must be at least 3 characters long';
  } else if (length < 3) {
    small.style.color = '#f44336';
    small.textContent = `⚠️ ${length}/3 characters - ${3 - length} more needed`;
  } else {
    small.style.color = '#4CAF50';
    small.textContent = `✓ Password length OK (${length} characters)`;
  }
});
```

### Server-Side Validation (Python Template)
```python
{% 
def validate_email(email):
    """Validasi format email dengan regex"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def register_user(username, email, password):
    # Validasi username sudah digunakan
    if username in users_db:
        return False, "Username sudah digunakan"
    
    # Validasi email format
    if not validate_email(email):
        return False, "Format email tidak valid"
    
    # Validasi password length
    if len(password) < 3:
        return False, "Password minimal 3 karakter"
    
    # Simpan user baru
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
  "722@dor.com": {
    "password": "banheesoo",
    "nama": "Ban Heesoo",
    "email": "722@dor.com"
  },
  "username123": {
    "password": "password",
    "nama": "User Name",
    "email": "user@example.com"
  }
}
```

### Operations
- **Load**: `load_users()` - Baca dari file
- **Save**: `save_users(users_db)` - Simpan ke file
- **Authenticate**: Check username/password
- **Register**: Add new user

## HTTP Methods

### GET Request
```http
GET /dashboard.html?user=admin&name=Administrator HTTP/1.1
```
→ Server kirim file static

### POST Request
```http
POST /auth-process.html HTTP/1.1
Content-Type: application/x-www-form-urlencoded

action=login&username=admin&password=123
```
→ Server proses dengan template engine

## Konfigurasi

### Server Settings
```python
SERVER_HOST = '127.0.0.5'
SERVER_PORT = 722
DOCUMENT_ROOT = 'htdocs/'
```

### Encoding
- File dibaca dengan `encoding='utf-8'`
- Support Unicode characters dan emoji

## Features Detail

### 1. Login System
- Login dengan username atau email
- Server-side authentication
- Dynamic redirect dengan user info
- Error handling untuk invalid credentials

### 2. Signup System
- **Client-side validation:**
  - HTML5 validation (required, minlength)
  - JavaScript validation (username, email format, password)
  - Real-time password feedback
  - Alert untuk setiap error
  - Form submission blocking jika invalid
  
- **Server-side validation:**
  - Username uniqueness check
  - Email format validation (regex)
  - Password length check (min 3)
  - Data persistent ke JSON file
  - Error messages untuk setiap validation failure

### 3. Dashboard
- Display user info dari URL parameter
- Avatar initials auto-generate
- Logout functionality
- Protected pages (basic)

## Security Notes
⚠️ **Ini untuk pembelajaran saja!**

**Tidak ada:**
- Session management
- Password hashing
- HTTPS/SSL
- CSRF protection
- SQL injection protection (karena pakai JSON)

**Untuk production, butuh:**
- bcrypt/argon2 untuk password
- JWT atau session cookies
- HTTPS
- Input sanitization
- Rate limiting

## Perbedaan dengan Modul 5

| Feature | Modul 5 | Modul 6 |
|---------|---------|---------|
| Static Files | ✅ | ✅ |
| Template Engine | ❌ | ✅ |
| POST Method | ❌ | ✅ |
| Server-side Logic | ❌ | ✅ |
| Database | ❌ | ✅ (JSON) |
| Authentication | Client-side | Server-side |
| Form Validation | ❌ | Client + Server |
| Real-time Feedback | ❌ | ✅ |
| Dynamic Rendering | ❌ | ✅ |

## Learning Objectives
1. Understand template engine concept
2. Learn server-side validation
3. Handle POST requests
4. Implement persistent storage
5. Dynamic HTML generation with Python

## Next Step
Lihat folder **Dzaky** untuk implementasi yang lebih polished dengan styling yang lebih baik!

