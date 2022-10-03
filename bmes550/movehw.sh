#!/bin/bash

# Bash script to move files from git directory to dropbox directory
# this assumes that the homework files begin with the prefix 'hw_'
# Args
#   $1 - directory to move files from
#   $2 - directory to move files to (subfolder of dropbox)

# Check for arguments
if [ $# -ne 2 ]; then
    echo "Usage: $0 <code directory> <directory in bmes550.TonyOkeke.tko35>"
    exit 1
fi

# Move files
if grep -q 'bmes550.TonyOkeke.tko35' <<< $(realpath $2); then\
    ptns=""

    for file in $1/hw_*; do
        oldfilename=$(basename $file)
        newfile="$2/${oldfilename#hw_}"  # Remove prefix 'hw_'
        newfilename=$(basename $newfile)
         
        # Copy file to dropbox
        cp $file $newfile
        
        # Check if file was copied
        if [ $? -ne 0 ]; then
            echo "Error: could not copy $file to $newfile"
            exit 1
        fi

        ptns+="s/$oldfilename/$newfilename/g;"
    done;

    # Fix paths in new files
    for file in $2/*; do
        if ! file $file | grep -iq -e 'ASCII' -e 'JSON'; then
            echo "Skpping $file (Can't fix paths in non-ASCII files)"
        elif [[ -f $file ]]; then
            sed -i "$ptns" $file
        fi
    done;

    echo "Moved files from $1 to $(realpath $2)"
else
    echo "$2 is not a subfolder of bmes550.TonyOkeke.tko35"
    exit 1
fi
