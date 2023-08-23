#!/usr/bin/env python3

import os
import sys


def usage():
    print("Description:\n")
    print(
        "\tThis script creates a 'tmp' directory with 5 subdirectories in the "
        + "home directory, and creates two text files within each subdirectory"
        + "}\n"
    )
    print("\tand creates two text files within each subdirectory.\n")
    print("Usage:\n")
    print("\ttask1a.py [-h]\n")
    print("Options:\n")
    print("\t-h: Displays this help message and exits.")
    sys.exit(0)


def main():
    for arg in sys.argv[1:]:
        if arg == "-h":
            usage()
        else:
            print("Invalid option:", arg, file=sys.stderr)
            sys.exit(1)

    for i in range(1, 6):
        dir_path = os.path.expanduser(f"~/tmp/training_project{i}")
        os.makedirs(dir_path, exist_ok=True)
        os.chdir(dir_path)

        with open(f"module_{i}_a.txt", "w") as f:
            f.write(f"Hello Basil Mari welcome to file {i}.A\n")

        with open(f"module_{i}_b.txt", "w") as f:
            f.write(f"Hello Basil Mari welcome to file {i}.B\n")

        os.chdir("..")


if __name__ == "__main__":
    main()
