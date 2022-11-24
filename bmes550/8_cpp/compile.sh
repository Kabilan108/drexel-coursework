#!/bin/bash
# This script will compile a cpp file which depends on the Armadillo library

# An input file must be provided
if [[ $# -eq 0 ]]; then
    echo "You must provide an input file"
    exit 1
elif [ ! -f "$1" ]; then
    echo "$1 does not exist"
    exit 1
fi

# If no output file is provided, use the input file name
if [[ $# -eq 1 ]]; then
    file=$(basename -- "$1")
    file="${file%.*}"
else
    file="$2"
fi

# Compile the file
if grep -q '#include <armadillo>' "$1"; then
    g++ $1 -o "$file" -DARMA_DONT_USE_WRAPPER -lopenblas -llapack
else
    g++ $1 -o "$file"
fi
