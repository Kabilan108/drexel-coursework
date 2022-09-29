#!/bin/bash

# Write a script wctop10lines.sh that prints the name of the file, followed by 
# the number of words on the first 10 lines of each file in the current 
# directory. (Hint: head, pipe, wc).

for file in $(ls); do
    if [ -f $file ]; then
        echo -e "$file \t $(head -n 10 $file | wc -w) words"
    fi
done
