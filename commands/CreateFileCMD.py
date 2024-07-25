from pathlib import Path


def run(args):
    if not len(args) == 2:
        print("usage: createfile [path//file]")
        return

    path = Path(args[1])

    if path.exists():
        print(f"Error: {args[1]} exists already.")
        return

    path.touch()
    print(path.__str__() + " created")

