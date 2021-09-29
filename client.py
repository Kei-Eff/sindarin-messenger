import socket
import os

class TranslationClient:
    def __init__(self):
        self.client_socket = None
        self.connect_to_server()

    def connect_to_server(self):

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.client_socket.connect(("127.0.0.1", 65432))

        print("Eithel govannen, mellon!")
        print("Enter the message you want translated.")

    def get_input(self):

        message_to_send = input(">> ")
        return message_to_send

    def send_message_to_translate(self, message_to_send):
        self.client_socket.sendall(str(message_to_send).encode('utf-8'))

    def receive_translation(self):
        received_message = self.client_socket.recv(1024)

        return received_message.decode('utf-8')

    def disconnect(self):
        self.client_socket.close()


translation_client = TranslationClient()

while True:
    user_input = translation_client.get_input()
    translation_client.send_message_to_translate(user_input)

    if user_input == "/exit":
        break

    translated_output = translation_client.receive_translation()

    print(translated_output)
    
    if translated_output.startswith("Too Many Requests"):
        break


translation_client.disconnect()