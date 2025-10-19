import socket
import time
import threading

server_ip = input("Masukkan IP Address Server: ")
server_port = int(input("Masukkan Port Server: "))

socketClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socketClient.connect((server_ip, server_port))

counter = 1
is_running = True

def send_messages():
    global counter, is_running
    while is_running:
        message = f"Data ke: {counter}"
        socketClient.send(message.encode())
        print(f"Ter kirim: {message}")
        counter += 1
        time.sleep(1)

def stop_sending():
    global is_running
    input("Tekan Enter untuk menghentikan pengiriman...")
    is_running = False
    print("Pengiriman dihentikan")

send_thread = threading.Thread(target=send_messages)
stop_thread = threading.Thread(target=stop_sending)

send_thread.start()
stop_thread.start()

send_thread.join()
socketClient.close()