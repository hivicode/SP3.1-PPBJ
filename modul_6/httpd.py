import socket
import os
import mimetypes
from urllib.parse import unquote
from template import Template


SERVER_HOST = '127.0.0.5'
SERVER_PORT = 722
# Make DOCUMENT_ROOT relative to this script's location
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DOCUMENT_ROOT = os.path.join(SCRIPT_DIR, 'htdocs')


def tcp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen()

    print(f'Listen on http://{SERVER_HOST}:{SERVER_PORT}')
    print(f'Document root: {DOCUMENT_ROOT}')

    while True:
        client_connection, client_address = server_socket.accept()
        request = client_connection.recv(1024).decode()

        if request:
            print('Request:\n', request)
            response = handle_request(request)
            client_connection.sendall(response)

        client_connection.close()


def handle_request(request):
    request_message = request.split("\r\n")
    request_line = request_message[0]
    words = request_line.split()

    if len(words) < 3:
        return response_400()

    method = words[0]
    uri = words[1]
    http_version = words[2]
    
    # Remove query string and fragment if present
    uri = uri.split('?')[0].split('#')[0]
    # Remove leading slash and decode URL encoding
    uri = unquote(uri.lstrip("/"))

    if uri == "":
        uri = "index.html"

    if method == "GET":
        return handle_get(uri, http_version)

    if method == "POST":
        data = request_message[-1]
        return handle_post(uri, http_version, data)

    return response_400()


def handle_get(uri, http_version):
    filepath = os.path.join(DOCUMENT_ROOT, uri)
    # Normalize path to prevent directory traversal and handle path separators
    filepath = os.path.normpath(filepath)
    
    # Security: Ensure the resolved path is still within DOCUMENT_ROOT
    if not filepath.startswith(os.path.normpath(DOCUMENT_ROOT)):
        message_body = b"<h1>403 Forbidden</h1>"
        response_line = f"{http_version} 403 Forbidden".encode()
        entity_header = b"Content-Type: text/html"
        crlf = b"\r\n"
        return b"".join([response_line, crlf, entity_header, crlf, crlf, message_body])

    if os.path.exists(filepath) and not os.path.isdir(filepath):
        with open(filepath, 'rb') as file:
            message_body = file.read()

        content_type = mimetypes.guess_type(filepath)[0] or 'text/html'
        response_line = f"{http_version} 200 OK".encode()
        entity_header = f"Content-Type: {content_type}".encode()
    else:
        message_body = b"<h1>404 Not Found</h1>"
        response_line = f"{http_version} 404 Not Found".encode()
        entity_header = b"Content-Type: text/html"

    crlf = b"\r\n"
    response = b"".join([
        response_line, crlf,
        entity_header, crlf,
        crlf,
        message_body
    ])
    return response


def handle_post(uri, http_version, data):
    filepath = os.path.join(DOCUMENT_ROOT, uri)
    # Normalize path to prevent directory traversal and handle path separators
    filepath = os.path.normpath(filepath)
    
    # Security: Ensure the resolved path is still within DOCUMENT_ROOT
    if not filepath.startswith(os.path.normpath(DOCUMENT_ROOT)):
        message_body = b"<h1>403 Forbidden</h1>"
        response_line = f"{http_version} 403 Forbidden".encode()
        entity_header = b"Content-Type: text/html"
        crlf = b"\r\n"
        return b"".join([response_line, crlf, entity_header, crlf, crlf, message_body])

    if os.path.exists(filepath) and not os.path.isdir(filepath):
        with open(filepath, 'r') as file:
            html = file.read()

        _POST = {}
        for item in data.split("&"):
            if "=" in item:
                key, value = item.split("=", 1)
                _POST[key] = value

        context = {
            "_POST": _POST
        }

        t = Template(html)
        message_body = t.render(context).encode()

        content_type = mimetypes.guess_type(filepath)[0] or 'text/html'
        response_line = f"{http_version} 200 OK".encode()
        entity_header = f"Content-Type: {content_type}".encode()
    else:
        message_body = b"<h1>404 Not Found</h1>"
        response_line = f"{http_version} 404 Not Found".encode()
        entity_header = b"Content-Type: text/html"

    crlf = b"\r\n"
    response = b"".join([
        response_line, crlf,
        entity_header, crlf,
        crlf,
        message_body
    ])
    return response


def response_400():
    body = b"<h1>400 Bad Request</h1>"
    return b"HTTP/1.1 400 Bad Request\r\nContent-Type: text/html\r\n\r\n" + body


if __name__ == "__main__":
    tcp_server()
