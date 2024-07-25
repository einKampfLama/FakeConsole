from pathlib import Path

def run(args):
    if len(args) < 2:
        print("usage: readfile [file]")
        return

    path = Path(args[1])

    if not path.is_file():
        print(f"Error: {args[1]} isn't a file.")
        return

    if not path.exists():
        print(f"Error: {args[1]} doesn't exist.")
        return

    with open(path, "r") as f:
        lines = f.readlines()
        i = 1
        for line in lines:
            print(i.__str__() + ". " + line)
            i = i+1
