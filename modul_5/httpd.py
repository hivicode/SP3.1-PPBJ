import socket
import os

SERVER_HOST = 'localhost'
SERVER_PORT = 8530

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen()	
print('Listening on host & port : http://%s:%s'%(SERVER_HOST, SERVER_PORT))
print('Press ctrl+c to exit')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

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
        request = client_connection.recv(1024).decode() 
        print(request)
        
        request_line = request.split('\n')[0]
        request_path = request_line.split()[1]
        
        if request_path == '/':
            request_path = '/index.html'
        
        file_path = request_path.lstrip('/')
        full_path = os.path.join(BASE_DIR, file_path)
        
        if os.path.exists(full_path) and os.path.isfile(full_path):
            _, ext = os.path.splitext(file_path)
            content_type = MIME_TYPES.get(ext, 'text/plain')
            
            if ext in ['.png', '.jpg', '.jpeg', '.gif', '.ico']:
                with open(full_path, 'rb') as file:
                    body = file.read()
            else:
                with open(full_path, 'r', encoding='utf-8') as file:
                    body = file.read().encode('utf-8')
            
            response_line = 'HTTP/1.1 200 OK'.encode()
            entity_header = f'Content-Type: {content_type}'.encode()
        else:
            response_line = 'HTTP/1.1 404 Not Found'.encode()
            entity_header = 'Content-Type: text/html; charset=utf-8'.encode()
            body = '<h1>404 Not Found</h1><p>File tidak ditemukan.</p>'.encode('utf-8')
        
        enter = '\r\n'.encode()
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

server_socket.close()