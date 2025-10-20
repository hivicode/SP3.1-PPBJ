import socket
import threading

userName = input("Masukkan username: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5001))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(userName.encode('ascii'))
            else:
                print(message)
        except:
            print("Terjadi kesalahan!")
            client.close()
            break

def write():
    while True:
        message = '{}: {}'.format(userName, input('>> '))
        client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()