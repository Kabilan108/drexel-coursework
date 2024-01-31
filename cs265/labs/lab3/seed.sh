#!/bin/bash

# Function to create a directory with a given number of files and directories
create_dir() {
        dir_name=$1
            num_files=$2
                num_dirs=$3

                    # Create the directory
                        mkdir -p "$dir_name"

                            # Change to directory
                                pushd "$dir_name" > /dev/null

                                    # Create files with random lines of text
                                        for ((i=1; i<=num_files; i++)); do
                                                    file_name="file_$i.txt"
                                                            touch "$file_name"
                                                                    num_lines=$((RANDOM % 5 + 1))
                                                                            for ((line=1; line<=num_lines; line++)); do
                                                                                            echo "This is line $line of $file_name" >> "$file_name"
                                                                                                    done
                                                                                                        done

                                                                                                            # Create subdirectories and files within them
                                                                                                                for ((i=1; i<=num_dirs; i++)); do
                                                                                                                            sub_dir="dir_$i"
                                                                                                                                    mkdir -p "$sub_dir"
                                                                                                                                            num_sub_files=$((RANDOM % 2 + 2))
                                                                                                                                                    for ((j=1; j<=num_sub_files; j++)); do
                                                                                                                                                                    sub_file_name="$sub_dir/file_$j.txt"
                                                                                                                                                                                touch "$sub_file_name"
                                                                                                                                                                                            num_lines=$((RANDOM % 5 + 1))
                                                                                                                                                                                                        for ((line=1; line<=num_lines; line++)); do
                                                                                                                                                                                                                            echo "This is line $line of $sub_file_name" >> "$sub_file_name"
                                                                                                                                                                                                                                        done
                                                                                                                                                                                                                                                done
                                                                                                                                                                                                                                                    done

                                                                                                                                                                                                                                                        # Return to the original directory
                                                                                                                                                                                                                                                            popd > /dev/null
                                                                                                                                                                                                                                                        }

                                                                                                                                                                                                                                                        # Main script
                                                                                                                                                                                                                                                        for i in {1..3}; do
                                                                                                                                                                                                                                                                num_files=$((RANDOM % 4 + 3)) # 3-6 files
                                                                                                                                                                                                                                                                    num_dirs=$((RANDOM % 3 + 2))  # 2-4 directories
                                                                                                                                                                                                                                                                        create_dir "testdir_$i" $num_files $num_dirs
                                                                                                                                                                                                                                                                    done

