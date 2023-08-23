#!/usr/bin/env python3

import os
import argparse


def main():
    parser = argparse.ArgumentParser(
        description=(
            "This script creates a 'tmp' directory with 5 subdirectories in"
            " the home directory, and creates two text files within each"
            " subdirectory."
        )
    )

    parser.parse_args()

    for i in range(1, 5):
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
