# imports

# get the argument from the cmd
if server
    translator = Translator()
    translator.wait_for_connections()

    while True
        message = translator.receive()