#!/usr/bin/env python3

import os
import sys


def usage():
    print("Description:")
    print(
        "\tThis script creates a 'tmp' directory with 5 subdirectories in the home directory, and creates two text files within each subdirectory. The text files contain the first name and last name of the user which are read as environment variables from $FIRST_NAME and $LAST_NAME.\n"
    )
    print("Usage:")
    print("\ttask1b.py [-h]")
    print("Options:")
    print("\t-h: Displays this help message and exits.")
    sys.exit(0)


def main():
    for arg in sys.argv[1:]:
        if arg == "-h":
            usage()
        else:
            print("Invalid option:", arg, file=sys.stderr)
            sys.exit(1)

    first_name = os.environ.get("FIRST_NAME")
    last_name = os.environ.get("LAST_NAME")

    if not (first_name and last_name):
        print(
            "Error: FIRST_NAME and LAST_NAME environment variables are not set."
        )
        sys.exit(1)

    for i in range(1, 6):
        os.makedirs(
            os.path.expanduser(f"~/tmp/training_project{i}"), exist_ok=True
        )
        os.chdir(os.path.expanduser(f"~/tmp/training_project{i}"))

        with open(f"module_{i}_a.txt", "w") as f:
            f.write(f"Hello {first_name} {last_name} welcome to file {i}.A\n")

        with open(f"module_{i}_b.txt", "w") as f:
            f.write(f"Hello {first_name} {last_name} welcome to file {i}.B\n")

        os.chdir("..")


if __name__ == "__main__":
    main()
