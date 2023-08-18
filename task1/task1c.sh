#!/bin/sh

usage() {
    printf "Description:\n"
    printf "\tThis script creates a \"tmp\" with 5 directories in it in the home directory, and creates two text files within each subdirectory. The text files contain the first name and last name of the user which are read as arguments.\n\n"
    printf "Usage:\n"
    printf "\ttask1a.sh [-h] [-cap] --first-name FIRST_NAME --last-name LAST_NAME\n"
    printf "Options:\n"
    printf "\t-h: Displays this help message and exits.\n"
    exit 0
}

while getopts ":h-:" opt; do
    case $opt in
        h)
            usage
            ;;
		-)
            case "${OPTARG}" in
                first-name)
                    eval arg_first_name=\"\$$OPTIND\"; OPTIND=$(( $OPTIND + 1 ))
                    ;;
                last-name)
                    eval arg_last_name=\"\$$OPTIND\"; OPTIND=$(( $OPTIND + 1 ))
                    ;;
				:)
            		echo "Option -$OPTARG requires an argument." >&2
					exit 1
					;;
                *)
                    echo "Invalid option: --${OPTARG}" >&2
                    exit 1
                    ;;
            esac
            ;;
        ?)
            printf "Invalid option: -$OPTARG\n" >&2
            exit 1
            ;;
    esac
done

if [ -z "${arg_first_name}" ] || [ -z "${arg_last_name}" ]; then
	echo "Missing required arguments" >&2
	exit 1
fi

rm -r ~/tmp


i=1
while [ "${i}" -le 5 ]; do

    mkdir -p ~/tmp/training_project${i}
	cd ~/tmp/training_project${i} || exit
	touch module_${i}_a.txt module_${i}_b.txt
	echo "Hello ${arg_first_name} ${arg_last_name} welcome to file ${i}.A" > module_${i}_a.txt
	echo "Hello ${arg_first_name} ${arg_last_name} welcome to file ${i}.B" > module_${i}_b.txt

    i=$((i+1))
done

exit 0
