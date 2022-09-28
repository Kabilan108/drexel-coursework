#!/bin/bash

# Write a bash script that goes into the home directory, lists files 
# in that directory, with file sizes and access permissions, then
# go back to the original directory you started with.


old_dir=$(pwd)
cd ~
ls -lha
cd $old_dir
