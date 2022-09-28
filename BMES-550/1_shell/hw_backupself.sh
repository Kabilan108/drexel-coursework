#!/bin/bash

# Write a bash script file that creates a backup copy of itself (append 
# .bak to whatever its own name is). e.g., backupself.sh should create
# a backup of itself called backupself.sh.bak. 
# If you run backupself.sh.bak it should create backupself.sh.bak.bak

cp $0 "$0.bak"
