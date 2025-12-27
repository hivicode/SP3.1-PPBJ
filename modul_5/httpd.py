import socket
import os

SERVER_HOST = 'localhost'
SERVER_PORT = 8530

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen()	
print('Listening on host & port : http://%s:%s'%(SERVER_HOST, SERVER_PORT))
print('Press ctrl+c to exit')

# Path file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# MIME types
MIME_TYPES = {
    '.html': 'text/html; charset=utf-8',
    '.css': 'text/css; charset=utf-8',
    '.js': 'application/javascript; charset=utf-8',
    '.json': 'application/json; charset=utf-8',
    '.png': 'image/png',
    '.jpg': 'image/jpeg',
    '.jpeg': 'image/jpeg',
    '.gif': 'image/gif',
    '.svg': 'image/svg+xml',
    '.ico': 'image/x-icon'
}

while True:	
    client_connection, client_address = server_socket.accept() 
    
    try:
        # Request
        request = client_connection.recv(1024).decode() 
        print(request)
        
        # Parse request untuk mendapatkan path
        request_line = request.split('\n')[0]
        request_path = request_line.split()[1]
        
        # Default ke index.html jika path adalah /
        if request_path == '/':
            request_path = '/index.html'
        
        # Hilangkan leading slash
        file_path = request_path.lstrip('/')
        
        # Full path
        full_path = os.path.join(BASE_DIR, file_path)
        
        # Cek apakah file ada
        if os.path.exists(full_path) and os.path.isfile(full_path):
            # Tentukan MIME type berdasarkan ekstensi
            _, ext = os.path.splitext(file_path)
            content_type = MIME_TYPES.get(ext, 'text/plain')
            
            # Baca file
            if ext in ['.png', '.jpg', '.jpeg', '.gif', '.ico']:
                # Binary mode untuk gambar
                with open(full_path, 'rb') as file:
                    body = file.read()
            else:
                # Text mode untuk HTML, CSS, JS
                with open(full_path, 'r', encoding='utf-8') as file:
                    body = file.read().encode('utf-8')
            
            response_line = 'HTTP/1.1 200 OK'.encode()
            entity_header = f'Content-Type: {content_type}'.encode()
        else:
            # File tidak ditemukan - 404
            response_line = 'HTTP/1.1 404 Not Found'.encode()
            entity_header = 'Content-Type: text/html; charset=utf-8'.encode()
            body = '<h1>404 Not Found</h1><p>File tidak ditemukan.</p>'.encode('utf-8')
        
        enter = '\r\n'.encode()
        
        # Response
        response = b''.join([response_line, enter, entity_header, enter, enter, body])
        client_connection.send(response)
        
    except Exception as e:
        print(f'Error: {e}')
        response_line = 'HTTP/1.1 500 Internal Server Error'.encode()
        entity_header = 'Content-Type: text/html; charset=utf-8'.encode()
        body = f'<h1>500 Internal Server Error</h1><p>{str(e)}</p>'.encode('utf-8')
        enter = '\r\n'.encode()
        response = b''.join([response_line, enter, entity_header, enter, enter, body])
        client_connection.send(response)
    
    finally:
        client_connection.close()
        
#End while
server_socket.close()