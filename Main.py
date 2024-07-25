from datetime import datetime

import commands.MoveFileCMD
import commands.WriteFileCommand
import commands.CreateFileCMD
import commands.ReadFileCMD
import commands.EditFileCMD
print(datetime.now())

def say_hi(args):
    print("Hallo!")
    print(args)


def say_bye(args):
    print("Auf Wiedersehen!")


def unknown_command(args):
    print("Unbekannter Befehl.")


cmds = {
    "hi": say_hi,
    "bye": say_bye,
    "movefile": commands.MoveFileCMD.run,
    "createfile": commands.CreateFileCMD.run,
    "writefile": commands.WriteFileCommand.run,
    "readfile": commands.ReadFileCMD.run,
    "editfile": commands.EditFileCMD.run
}



while True:
    user_input = input(">> ")

    if user_input == 'quit':
        break

    args = user_input.split(" ")
    command = cmds.get(args[0], unknown_command)

    command(args)
