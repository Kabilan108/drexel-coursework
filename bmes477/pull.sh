#!/bin/bash

# Pull latest version of course repository from Google Drive
rclone sync \
    gdrive:/Drexel/Academic/05\ -\ Senior/01\ -\ Fall\ Quarter/BMES\ 477/labs \
    /home/muaddib/arrakis/courses/bmes477

echo "Pulled latest version of course repository from Google Drive"

