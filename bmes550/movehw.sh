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
oldnames=()
newnames=()

for file in $1/hw_*; do
    oldfilename=$(basename $file)
    newfile="$2/${oldfilename#hw_}"
    newfilename=$(basename $newfile)
    
    if grep -q 'bmes550.TonyOkeke.tko35' <<< $(realpath $newfile); then
        # Copy file to dropbox
        cp $file $newfile
        
        # Check if file was copied
        if [ $? -ne 0 ]; then
            echo "Error: could not copy $file to $newfile"
            exit 1
        fi
    else
        echo "$2 is not a subfolder of bmes550.TonyOkeke.tko35"
        exit 1
    fi

    oldnames+=($oldfilename)
    newnames+=($newfilename)
done;

# Fix file paths
for i in "${!oldnames[@]}"; do
    for file in $2/*; do
        "sed -i 's/${oldnames[$i]}/${newnames[$i]}/g' "
    done
done

# export oldnames=$oldnames
# export newnames=$newnames


echo "Moved files from $1 to $(realpath $2)"
