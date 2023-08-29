#!/usr/bin/env python3

import argparse


# Read the csv file and return its content as a string
def read_csv_file(file_name, num_columns):
    with open(file_name, "r") as f:
        for y, line in enumerate(f):
            x = 0
            while x < num_columns:
                cells = line.strip().split(",")
                yield (cells[x], x, y)
                x += 1


def create_occurrences_dictionary(file_name, error_string, num_columns):
    occurrences = {}
    iterate = read_csv_file(file_name, num_columns)
    for cell in iterate:
        string = cell[0]
        if string == error_string:
            print(f"Found broken cell in row {cell[2]}, column {cell[1]}.")
        elif string in occurrences:
            occurrences[string] += 1
        else:
            occurrences[string] = 1
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
