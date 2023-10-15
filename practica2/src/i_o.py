import os
import sys

def read_file(path_to_file: str) -> str:

    if not os.path.isfile(path_to_file):
        print("Not an existing file\nTry again")
        sys.exit(1)

    raw_str = ""
    try:
        raw_str = open(path_to_file, 'r').read()
    except IOError:
        print("Error reading input file")
        sys.exit(1)

    return raw_str

def write_file(target_path:str, content: str) -> None:
    try:
        with open(target_path, 'w') as file:
            file.write(content)
    except IOError:
        print("Error while writing file")
        sys.exit(1)
