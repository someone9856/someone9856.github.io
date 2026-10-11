import socket

HOST = "127.0.0.1"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)
print("Waiting for reverse connection...")
conn, addr = server.accept()
print("Connected from:", addr)
message = conn.recv(1024).decode()
print("Received:", message)
conn.send("Hello from listener".encode())
conn.close()
server.close()
