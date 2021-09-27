import socket
import requests

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
    url = "https://elvish.p.rapidapi.com/sindarin.json"

    querystring = {"text": "{original_message}"}

    headers = {
        'x-rapidapi-host': "elvish.p.rapidapi.com",
        'x-rapidapi-key': "cd788f8a40msh8521eb366d07abdp16c66fjsn5ab319342906"
    }

    response = requests.request("POST", url, headers=headers, params=querystring)

    message = response.text
    # end

    print(message)

    connection.sendall(message.encode('utf-8'))

server_socket.close()