import socket

server_socket = socket.socket(AF_INET, socket.SOCK_STREAM)
server_socket.bind("127.0.0.1", 65432)
server_socket.listen()

print("Listening... test, test, test...")

server_socket.close()