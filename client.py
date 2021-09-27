import socket
import os
import sys
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(("127.0.0.1", 65432))

message_to_send = input("Eithel govannen, mellon!\nWhat message would you like to send?\n")

client_socket.sendall(message_to_send.encode('utf-8'))

received_message = client_socket.recv(1024)

print(received_message.decode('utf-8'))

client_socket.close()