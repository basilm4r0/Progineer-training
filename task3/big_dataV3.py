#!/usr/bin/env python3

import argparse


# Read the csv file and return its content as a string
def read_csv_file(file_name, num_columns):
    with open(file_name, "r") as f:
        cells = f.read().replace("\n", ",").split(",")[0:-1]
        x = 0
        y = 0
        for cell in cells:
            yield (cell, x, y)
            x += 1
            if x == num_columns:
                x = 0
                y += 1
        yield (None, 0, 0)


def create_occurrences_dictionary(file_name, error_string, num_columns):
    occurrences = {}
    gen = read_csv_file(file_name, num_columns)
    while True:
        cell, x, y = next(gen)
        if cell is None:
            break
        if str(cell) == error_string:
            print(f"Found broken cell in row {y}, column {x}.")
            continue
        if cell in occurrences:
            occurrences[cell] += 1
        else:
            occurrences[cell] = 1
    return occurrences


def main():
    parser = argparse.ArgumentParser(
        description=(
            "\t This script reads a CSV file and counts the number of times"
            " each element in the file is repeated. It also has error checking"
            " which checks the cell contents against a specified error"
            " value.\n"
        )
    )

    parser.add_argument(
        "-e",
        "--error",
        type=str,
        help="The error value to check against.",
    )

    parser.add_argument(
        "-f",
        "--file",
        type=str,
        help="The CSV file to read.",
    )

    parser.add_argument(
        "-c",
        "--columns",
        type=int,
        help="The number of columns in the CSV file.",
    )

    error_string = parser.parse_args().error

    print("Reading CSV file...")
    try:
        dictionary = create_occurrences_dictionary(
            parser.parse_args().file, error_string, parser.parse_args().columns
        )
    except FileNotFoundError:
        print("Error reading the input file.")
        exit(1)

    for i in dictionary:
        print(i, ":", dictionary[i])


if __name__ == "__main__":
    main()
