import socket
import requests

class MessageServer:
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
        self.server_socket.listen() #listen for incoming connections

        self.connection, address = self.server_socket.accept()
        print(f"Connection to {address} established. Suilad!")

    def receive_messages(self):
        data = self.connection.recv(1024)

        if not data:
            return

        received_message = data.decode('utf-8')
        
        print(received_message)
        return received_message

    def send_message(self, message):
        self.connection.sendall(str(message).encode('utf-8'))

    def close_server(self):
        self.server_socket.close()


class Translator:
    def __init__(self, url):
        self.url = url

    def translate(self, text):
        # translate to target language
        querystring = {
            "text": text
            }

        response = requests.request("POST", self.url, data=querystring)

        response_json = response.json()
        print(response_json)

        if "error" in response_json:
            return (response_json["error"]["message"], True)
        else:
            contents = response_json["contents"]
            translation = contents["translated"]
            return (translation, False)

class SindarinTranslator(Translator):
     def __init__(self):
        Translator.__init__(self, "https://api.funtranslations.com/translate/sindarin.json")


# main program

translation_server = MessageServer()
translator = SindarinTranslator()

while True:
    message = translation_server.receive_messages()

    if not message:
        continue

    if message == "/exit":
        break

    translation, is_error = translator.translate(message)
    translation_server.send_message(translation)

    if is_error:
        break

translation_server.close_server()