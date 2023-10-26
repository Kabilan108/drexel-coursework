#!/bin/bash

# Push latest version of course repository to Google Drive
rclone sync \
    /mnt/sietch/courses/bmes477 \
    gdrive:/Drexel/Academic/05\ -\ Senior/01\ -\ Fall\ Quarter/BMES\ 477/labs 

echo "Pushed to Google Drive"

