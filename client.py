import socket
import os


class TranslationClient:
    """Creates socket and gets IP address of the server.

    Args:


    Returns:
        Function returns the translated text.
    """
    def __init__(self):
        self.client_socket = None
        self.connect_to_server()

    def connect_to_server(self):
        """Client that connects to the server and sends a message for translation.

        Args:
            message: The message to be sent to the server.

        Returns:
            The translated message from the server.
        """

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.client_socket.connect(("127.0.0.1", 65432))

        print("Eithel govannen, mellon!")
        print("Enter the message you want translated.")

    def get_input(self):
        """Function that returns the user's input. Takes in no arguments.

        Returns:
            message_to_send: The user's input.
        """

        message_to_send = input(">> ")
        return message_to_send

    def send_message_to_translate(self, message_to_send):
        """Client socket sends a message to the server socket.

        Args:
            message_to_send (string): Sends the encoded message to the server.
        """
        self.client_socket.sendall(str(message_to_send).encode('utf-8'))

    def receive_translation(self):
        """Client connects to the server. Sends a message and waits for a response.

        Returns:
            received_message: The translated text
        """
        received_message = self.client_socket.recv(1024)

        return received_message.decode('utf-8')

    def disconnect(self):
        """Function closes client socket.

        """
        self.client_socket.close()

# Create a TranslationClient object.
translation_client = TranslationClient()

while True:
    """Main program loop that asks for user input, sends input to the server.
    Receives and prints translated message from the server.
    Loop will run until the user inputs '/exit' or reaches API request limit.

    Args:
        user_input: The text that the user wants to translate.

    Returns:
        The translated message.
    """
    user_input = translation_client.get_input()
    translation_client.send_message_to_translate(user_input)

    if user_input == "/exit":
        break

    translated_output = translation_client.receive_translation()

    print(translated_output)
    if translated_output.startswith("Too Many Requests"):
        break

translation_client.disconnect()
