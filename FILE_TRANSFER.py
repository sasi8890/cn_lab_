import socket

s = socket.socket()
s.bind(('localhost', 9999))
s.listen(1)

conn, addr = s.accept()

file = open("received.txt", "wb")
data = conn.recv(1024)

while data:
    file.write(data)
    data = conn.recv(1024)

file.close()
conn.close()
