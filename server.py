import socket
import requests

class Server:
    def __init__(self):
        self.server_socket = None
        self.create_listening_server()
    
    #listen for incoming connection
    def create_listening_server(self):
    
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create a socket using TCP port and ipv4
        local_ip = '127.0.0.1'
        local_port = 65432

        self.server_socket.bind((local_ip, local_port))
        print("Listening for incoming messages..")
        self.server_socket.listen() #listen for incomming connections

    def receive_messages(self):
        connection, address = self.server_socket.accept()
        print("Connection to {address} established. Suilad!")

        while True:
            data = connection.recv(1024)

            if not data:
                break

            received_message = data.decode('utf-8')
            
            print(received_message)

            sindarin_translator = Translator()
            translated_message = sindarin_translator.translate(received_message)

            print(translated_message)
            return translated_message

    def send_messages(self, message):
        pass

class Translator:
    def __init__(self):
        pass

    def translate(self, text):
        # translate to target language
        url = "https://api.funtranslations.com/translate/sindarin.json"

        querystring = {
            "text": text
            }

        response = requests.request("POST", url, data=querystring)

        response_json = response.json()
        contents = response_json["contents"]
        translation = contents["translated"]
        return translation

server_socket.close()