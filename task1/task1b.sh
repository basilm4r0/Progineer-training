#!/bin/sh

usage() {
        printf "Description:\n"
        printf "\tThis script creates a \"tmp\" with 5 directories in it in the home directory, and creates two text files within each subdirectory. The text files contain the first name and last name of the user which are read as environment variables from \$FIRST_NAME and \$LAST_NAME.\n\n"
        printf "Usage:\n"
        printf "\ttask1b.sh [-h]\n"
        printf "Options:\n"
        printf "\t-h: Displays this help message and exits.\n"
        exit 0
    }

while [ $# -gt 0 ]; do
    case $1 in
        -h)
            usage
            ;;
        *)
            echo "Invalid option: $1" >&2
            exit 1
            ;;
    esac
done

if [ -z "$FIRST_NAME" ] && [ -z "$LAST_NAME" ]; then
    echo "Error: FIRST_NAME and LAST_NAME environment variables are not set."
    exit 1
fi

rm -r ~/tmp

for i in 1 2 3 4 5
do

    mkdir -p ~/tmp/training_project${i}
	cd ~/tmp/training_project${i} || exit
	touch module_${i}_a.txt module_${i}_b.txt
	echo "Hello ${FIRST_NAME} ${LAST_NAME} welcome to file ${i}.A" > module_${i}_a.txt
	echo "Hello ${FIRST_NAME} ${LAST_NAME} welcome to file ${i}.B" > module_${i}_b.txt

done

exit 0
