#!/bin/bash

while read f; do
    mv "$f" "$(echo $f | sed -E 's/(.*)_(.*).txt/\2_\1.txt/g')"
done < <(ls *_*.txt)
