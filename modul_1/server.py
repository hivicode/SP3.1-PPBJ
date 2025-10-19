import socket

myp = socket.SOCK_DGRAM 
afn = socket.AF_INET
socketServer = socket.socket(afn, myp)

socketServer.bind(("0.0.0.0", 5000))
print("Server mendengarkan...")

while True:
    clientData = socketServer.recvfrom(1024)
    addrs = clientData[1][0]
    msg = clientData[0].decode()
    print(addrs + " : " + msg)