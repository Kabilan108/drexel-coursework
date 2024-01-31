#!/bin/bash

# Step 1: Create base directory `sample/`
mkdir -p sample/foo/baaz/a_different_directory
mkdir -p sample/bar
mkdir -p sample/foo

# Step 2: Create `_special` and `_blacklist` files
echo -e "x\na_different_directory\ny\nz" > sample/foo/baaz/_special
echo -e "yet another file\nabc" > sample/foo/baaz/_blacklist

# Step 3: Create regular files and `some_directory`
touch sample/foo/baaz/"another file"
touch sample/foo/baaz/file1
touch sample/foo/baaz/this_file
touch sample/foo/baaz/x
touch sample/foo/baaz/y
touch sample/foo/baaz/z

# Create `some_directory` inside `foo/baaz/`
mkdir sample/foo/baaz/some_directory

# Step 4: Create placeholder files in `a_different_directory`
touch sample/foo/baaz/a_different_directory/file_in_different_directory

# Step 5: Create placeholder content in other directories
touch sample/foo/file_in_foo
touch sample/bar/file_in_bar

echo "Sample directory structure created."

