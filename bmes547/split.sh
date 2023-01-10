#!/bin/bash

# This script will split the given file and input each line as a cell in a
# Jupter notebook

tr '^\n' '\n\n\n' < homework.md | while read -r line; do
    
    if [[ "$line" =~ ^#\ .* ]]; then
        # Add author and date to cell with top header
        line=$(cat <<EOF
$line\n
**Author:** [Tony Kabilan Okeke](mailto:tko35@drexel.edu)\n
**Date:** $(date '+%B %d, %Y')
EOF
)
    else
        # Remove the leading '- ' from each line
        line=$(echo $line | sed 's/^- //')
    fi

    # Create the new cell
    cell=$(cat <<EOF
{
  "cell_type": "markdown",
  "execution_count": null,
  "metadata": {},
  "outputs": [],
  "source": [
    "$line"
  ]
}
EOF
)

    # Add the cell to the cells array in a json file using jq
    jq --argjson cell "$cell" '.cells += [$cell]' hwtemplate.ipynb > $2
done
