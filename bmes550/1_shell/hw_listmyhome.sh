#!/bin/bash

# List the name, file size, and access permissions for non-empy files in 
# the home directory.

old_dir=$(pwd)
cd ~
ls -lhA | \
    awk -v FS=' ' -v OFS='\t' '
        BEGIN{ print "PERMISSIONS \t SIZE \t FILENAME" } 
        NR>1{ printf "%-11s \t %-5s \t %-10s\n", $1, $5, $9 }
    '
cd $old_dir
