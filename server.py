import socket
import requests
import json

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(("127.0.0.1", 65432))
server_socket.listen()
print("Listening for incoming connection...")

connection, address = server_socket.accept()
print("Connection established. Suilad!")

while True:
    data = connection.recv(1024)

    if not data:
        break

    original_message = data.decode('utf-8')
    
    print(original_message)

    # translate to target language
    url = "https://api.funtranslations.com/translate/sindarin.json"

    querystring = {
        "text": original_message
        }

    response = requests.request("POST", url, data=querystring)

    response_json = response.json()
    contents = response_json["contents"]
    message = contents["translated"]

    # end

    print(message)

    connection.sendall(message.encode('utf-8'))

server_socket.close()