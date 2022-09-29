#!/bin/bash

# Write a bash script findrecentdocx.sh that lists all of the recently 
# modified *.docx files (recursively) in a specified folder. Let recently 
# mean in the last week. If the target folder is not specified, use the current 
# user's home directory.

dir=${1:-$HOME}  # if no argument, use $HOME

find $dir -mtime -7 -type f -name '*.docx'
