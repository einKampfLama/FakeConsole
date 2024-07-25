from datetime import datetime

print(datetime.now())

def say_hi():
    print("Hallo!")


def say_bye():
    print("Auf Wiedersehen!")


def unknown_command():
    print("Unbekannter Befehl.")


commands = {
    "hi": say_hi,
    "bye": say_bye
}

while True:
    user_input = input(">> ")

    if user_input == 'quit':
        break

    command = commands.get(user_input, unknown_command)
    command()
