import socket

sock = socket.socket()
host = "private ip"
port = 6969

sock.bind((host, port))
sock.listen(5)

client, address = sock.accept()
print("Connection from ", address)

while True:
    client.send(str.encode(input()))
