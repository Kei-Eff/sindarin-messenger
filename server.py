import socket
import sys
import time

host = socket.gethostname()
s = socket.socket()
print("Server will start on host:", host)

port = 8080

s.bind((host, port))
print("")
print("Server done binding to host and port successfully")
print("")
print("Server is waiting for incoming connections...")

s.listen(1)

conn, addr = s.accept()
print(addr, "has connected to the server and is now online...")
print("")