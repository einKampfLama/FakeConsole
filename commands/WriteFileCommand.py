from pathlib import Path

def run(args):
    if len(args) < 2:
        print("usage: writefile [file]")
        return

    path = Path(args[1])

    if not path.is_file():
        print(f"Error: {args[1]} isn't a file.")
        return

    if not path.exists():
        print(f"Error: {args[1]} doesn't exist.")
        return

    lines = []
    print("You can now write (FINISH to finish :D): \n")
    while True:
        line = input()
        if line == "FINISH":
            break
        lines.append(line)

    text = "\n".join(lines)

    with open(path, "w") as f:
        f.write(text)
