#!/usr/bin/env python3

import sys
import os


def usage():
    print("Description:")
    print(
        "\tThis script creates a 'tmp' directory with 5 subdirectories in the"
        + "home directory, and creates two text files within each subdirectory"
        + ".The text files contain the first name and last name of the user"
        + "which are read as arguments.\n"
    )
    print("Usage:")
    print(
        "\ttask1c.py [OPTION]... --first-name FIRST_NAME --last-name LAST_NAME"
    )
    print("Options:")
    print("\t-h, --help\t\tDisplays this help message and exits.")
    print(
        "\t-c, --capitalize\tCapitalizes the first letter of the first and"
        + "last names."
    )
    sys.exit(0)


def main():
    cap = False
    i = 1

    while i < len(sys.argv):
        arg = sys.argv[i]

        if arg == "-h" or arg == "--help":
            usage()
        elif arg == "-c" or arg == "--capitalize":
            cap = True
        elif arg == "--first-name":
            if i + 1 < len(sys.argv):
                i += 1
                arg_first_name = sys.argv[i]
            else:
                print(
                    "Option --first-name requires an argument.",
                    file=sys.stderr,
                )
                sys.exit(1)
        elif arg == "--last-name":
            if i + 1 < len(sys.argv):
                i += 1
                arg_last_name = sys.argv[i]
            else:
                print(
                    "Option --last-name requires an argument.", file=sys.stderr
                )
                sys.exit(1)
        else:
            print("Invalid option:", arg, file=sys.stderr)
            sys.exit(1)

        i += 1

    if not ("arg_first_name" in locals() and "arg_last_name" in locals()):
        print("Missing required arguments", file=sys.stderr)
        sys.exit(1)

    if cap:
        arg_first_name = arg_first_name.capitalize()
        arg_last_name = arg_last_name.capitalize()

    i = 1
    while i <= 5:
        try:
            os.makedirs(
                os.path.expanduser(f"~/tmp/training_project{i}"), exist_ok=True
            )
        except OSError:
            print("Creation of the directory failed")
            sys.exit(1)

        os.chdir(os.path.expanduser(f"~/tmp/training_project{i}"))

        with open(f"module_{i}_a.txt", "w") as f:
            f.write(
                f"Hello {arg_first_name} {arg_last_name}"
                + f" welcome to file {i}.A\n"
            )

        with open(f"module_{i}_b.txt", "w") as f:
            f.write(
                f"Hello {arg_first_name} {arg_last_name}"
                + f" welcome to file {i}.B\n"
            )

        os.chdir("..")
        i += 1


if __name__ == "__main__":
    main()
