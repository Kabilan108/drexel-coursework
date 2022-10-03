#!/bin/bash

# Compare the number of a's and b's in a file

# Check that input file was provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 filename"
    exit 1
fi

# Check that input file exists
if [ ! -f $1 ]; then
    echo "$1 is not a file"
    exit 1
fi

# Count number of a's and b's
a_count=$(grep -o 'a' $1 | wc -l)
b_count=$(grep -oi 'b' $1 | wc -l)

# Print results
if [ $a_count -gt $b_count ]; then
    echo "There are more a's than b's."
elif [ $a_count -lt $b_count ]; then
    echo "There are more b's than a's."
else
    echo "There are the same number of a's and b's."
fi
