# CS 171 - Homework 7 (Grade Stats)
# Purpose: Automate grade calculation for a course.
#          Load grades from a text file and compute statistics for each student.
# Author:  Tony Kabilan Okeke (tko35)
# Date:    02.24.2022

# Import necessary modules
import os

# Define Functions
def get_file_name():
    """
    Validate user input for data file
    @return
        User-provided file name
    """
    while True:
        value = input("Enter name of the data file: ")
        if os.path.isfile(value):
            break
        else:
            print("Error: that file does not exist. Try again.")

    return value

def read_data(file_name):
    """
    Read student grade data from a text file
    @param file_name
        A valid file name containing student grade data
    @retrun
        A dictionary containing student grades
    """
    with open(file_name, 'r') as file:
        # Read lines from files
        lines = file.readlines()
        
        # Read names and scores from file and store in a dictionary
        # Keys -> student names, Values -> list of scores
        grades = {name: grades.split() for (name, grades) in (line.split(' ', 1) for line in lines)}

    # Convert student grades to integers
    grades = { k: [int(i) for i in v] for (k,v) in grades.items() }

    return grades 

def compute_grade_stats(student_grades):
    """
    Compute Total Score, Number of Tests, and Average Score for each student
    @param student_grades
        A dictionary containing student grades
    @return
        A string containing desired results
    """
    data = ""
    for name, grades in student_grades.items():
        total = sum(grades)
        num_tests = len(grades)
        avg_score = total / num_tests

        # Append data to string
        data += f"{name} {total} {num_tests} {avg_score:.2f}\n"

    return data

def main():
    """
    Run program
    """

    # Prompt user for file name
    file_name = get_file_name()
    # Read data from file
    student_grades = read_data(file_name)
    # Compute results
    grade_stats = compute_grade_stats(student_grades)
    # Write results to file
    with open('stats.txt', 'w') as file:
        file.write(grade_stats)
        print("Stats have been save in the output file")

if __name__ == '__main__':
    # Load data
    main()