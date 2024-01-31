#!/bin/bash

# Author: Tony K. Okeke
# Date:   01-30-2024

if [[ -v 1 ]]; then
    dir="$1"
    if [[ ! -d "$dir" ]]; then
        echo "sorry, that folder doesn't exist."
        exit 1
    fi
else
    dir=$(pwd)
fi

find "$dir" -type f | while read file; do
    name=$(basename "$file")
    lines=$(wc -l "$file" | grep -o '^[0-9]*')
    words=$(wc -w "$file" | grep -o '^[0-9]*')

    echo "$name $lines $words"
done

