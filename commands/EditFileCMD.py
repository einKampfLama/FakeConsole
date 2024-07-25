from pathlib import Path

def run(args):
    if len(args) < 4:
        print("usage: writefile [file] [line] [content]1")
        return

    path = Path(args[1])
    line_num = int(args[2]) - 1
    content = " ".join(args[3:])

    if not path.is_file():
        print(f"Error: {args[1]} isn't a file.")
        return

    if not path.exists():
        print(f"Error: {args[1]} doesn't exist.")
        return

    if not isinstance(line_num, int):
        print("usage: writefile [file] [line] [content]2")
        return

    with open(path, 'r') as file:
        lines = file.readlines()

    # Überprüfen, ob die Zeilennummer gültig ist
    if line_num < 0 or line_num >= len(lines):
        print("Line not exists.")
        return

    # Die gewünschte Zeile ändern
    lines[line_num] = content + '\n'

    # Datei mit den neuen Inhalten überschreiben
    with open(path, 'w') as file:
        file.writelines(lines)


