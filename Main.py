from datetime import datetime
import commands.MoveFileCMD

print(datetime.now())

def say_hi(args):
    print("Hallo!")
    print(args)


def say_bye(args):
    print("Auf Wiedersehen!")


def unknown_command(args):
    print("Unbekannter Befehl.")


commands = {
    "hi": say_hi,
    "bye": say_bye,
    "movefile": commands.MoveFileCMD.run
}



while True:
    user_input = input(">> ")

    if user_input == 'quit':
        break

    args = user_input.split(" ")
    command = commands.get(args[0], unknown_command)

    command(args)
