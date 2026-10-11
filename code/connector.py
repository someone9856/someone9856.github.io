import socket

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Connecting to listener...")
client.connect((HOST, PORT))
client.send("Hello from reverse connector".encode())
reply = client.recv(1024).decode()
print("Listener replied:", reply)
client.close()
