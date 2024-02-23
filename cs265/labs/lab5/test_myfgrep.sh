#!/bin/bash

# Function to run a test case
run_test() {
    pattern=$1
    file=$2

    echo "Testing pattern '$pattern' in file '$file'"

    # Run fgrep
    if [ "$file" == "stdin" ]; then
        fgrep_output=$(echo -e "$3" | fgrep "$pattern")
    else
        fgrep_output=$(fgrep "$pattern" "$file")
    fi
    fgrep_status=$?

    # Run myfgrep
    if [ "$file" == "stdin" ]; then
        myfgrep_output=$(echo -e "$3" | ./myfgrep "$pattern")
    else
        myfgrep_output=$(./myfgrep "$pattern" "$file")
    fi
    myfgrep_status=$?

    # Compare outputs
    if [ "$fgrep_output" == "$myfgrep_output" ]; then
        echo "PASS: Outputs match."
    else
        echo "FAIL: Outputs do not match."
        echo "fgrep output:"
        echo "$fgrep_output"
        echo "myfgrep output:"
        echo "$myfgrep_output"
    fi

    # Compare exit statuses
    if [ $fgrep_status -eq $myfgrep_status ]; then
        echo "PASS: Exit statuses match."
    else
        echo "FAIL: Exit statuses do not match. fgrep: $fgrep_status, myfgrep: $myfgrep_status"
    fi

    echo "--------------------------------"
}

# Test cases
run_test "fgrep" "test1.txt"
run_test "line" "test2.txt"
run_test "notfoundpattern" "test1.txt"
run_test "fgrep" "nonexistentfile.txt"  # This should test error handling
# Adding a test case for stdin input
run_test "pattern" "stdin" "This is a test string.\nThis string contains the pattern."
