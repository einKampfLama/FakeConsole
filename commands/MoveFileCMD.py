import shutil
from pathlib import Path


def run(args):
    if not len(args) == 3:
        print("usage: movefile [file] [dir]")
        return

    path = Path(args[1])
    to_path = Path(args[2])

    if not path.is_file():
        print(f"Error: {args[1]} is not a valid file.")
        return

    if not to_path.is_dir():
        print(f"Error: {args[2]} is not a valid directory.")
        return

    try:
        shutil.move(str(path), str(to_path))
        print(f"File moved to {to_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
