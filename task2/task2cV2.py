#!/usr/bin/env python3

import sys
import os
import argparse


def main():
    parser = argparse.ArgumentParser(
        description=(
            "\tThis script creates a 'tmp' directory with 5 subdirectories in"
            " the home directory, and creates two text files within each"
            " subdirectory.The text files contain the first name and last name"
            " of the user which are read as arguments.\n"
        )
    )

    parser.add_argument(
        "-c",
        "--capitalize",
        action="store_true",
        help="Capitalize the first and last name.",
    )
    parser.add_argument(
        "--first-name",
        type=str,
        help="The first name of the user.",
        required=True,
    )
    parser.add_argument(
        "--last-name",
        type=str,
        help="The last name of the user.",
        required=True,
    )

    cap = parser.parse_args().capitalize
    arg_first_name = parser.parse_args().first_name
    arg_last_name = parser.parse_args().last_name
    i = 1

    if cap:
        arg_first_name = arg_first_name.capitalize()
        arg_last_name = arg_last_name.capitalize()

    for i in range(1, 6):
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


if __name__ == "__main__":
    main()
