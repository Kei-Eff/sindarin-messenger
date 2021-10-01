import socket


class TranslationClient:
    """Client that communicates with a translation server.
    """
    def __init__(self):
        """Initialises client socket and connects to server.
        """
        self.client_socket = None
        self.connect_to_server()

    def connect_to_server(self):
        """Creates socket and connects to the server."""

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.client_socket.connect(("127.0.0.1", 65432))

        print("Eithel govannen, mellon! Well met, friend!")
        print("Enter the message you want translated. Type '/quit' to quit.")

    def get_input(self):
        """Function that returns the user's input. Takes in no arguments.

        Returns:
            str: The user's input.
        """

        message_to_send = input("\n>> ")
        return message_to_send

    def send_message_to_translate(self, message):
        """Function that sends a message via the client socket.

        Args:
            message (str): The message to be sent.
        """
        self.client_socket.sendall(str(message).encode('utf-8'))

    def receive_translation(self):
        """Function that receives translated message via the client socket.

        Returns:
            str: The translated text.
        """
        received_message = self.client_socket.recv(1024)

        return received_message.decode('utf-8')

    def disconnect(self):
        """Function closes client socket."""
        self.client_socket.close()


def main():
    """Function starts the program.
    Loop will run until the user inputs '/quit' or reaches API request limit.
    """

    translation_client = TranslationClient()

    while True:
        user_input = translation_client.get_input()
        translation_client.send_message_to_translate(user_input)

        if user_input == "/quit":
            break

        translated_output = translation_client.receive_translation()

        print(translated_output)
        if translated_output.startswith("Too Many Requests"):
            break

    translation_client.disconnect()

main()
