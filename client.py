import socket
import sys
import time

s = socket.socket()
host = input(str("Please enter the hostname of the server: "))
port = 8080

s.connect((host, port))
print("Eithel govannen, mellon! Welcome to Sindarin Messenger!")

while 1:
    message = input(str(">> "))
    message = message.encode()

    s.send(message)
    print("Message has been sent...")
    print("")
    
    incoming_message = s.recv(1024)
    incoming_message = incoming_message.decode()
    print("Server: ", incoming_message)
    print("")
