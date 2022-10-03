#!/bin/bash

# Print the name of each file in the current directory and the word count 
# in the first 10 lines.

printf "%-25s\t%-10s\n" 'FILE' 'WORD COUNT'

for file in $(ls); do
    if [ -f $file ]; then
        printf "%-25s\t%-10s\n" $file $(head -n 10 $file | wc -w)
    fi
done
