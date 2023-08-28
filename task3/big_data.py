#!/usr/bin/env python3

import argparse


# Read the csv file and return its content as a string
def read_csv_file(file_name):
    with open(file_name, "r") as f:
        return f.read()


# Crete an list from the csv string
def create_list(csv_string):
    return [x.split(",") for x in csv_string.split("\n")[0:-1]]


def create_occurrences_dictionary(list_list, error_string):
    occurrences = {}
    for y, string_list in enumerate(list_list):
        for x, string in enumerate(string_list):
            if string == error_string:
                print(f"Found broken cell in row {y}, column {x}.")
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
            " which checks the cell concents against a specified error"
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

    error_string = parser.parse_args().error

    print("Reading CSV file...")
    try:
        dictionary = create_occurrences_dictionary(
            create_list(read_csv_file(parser.parse_args().file)), error_string
        )
    except FileNotFoundError:
        print("Error reading the input file.")
        exit(1)

    for i in dictionary:
        print(i, ":", dictionary[i])


if __name__ == "__main__":
    main()
