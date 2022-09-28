# CS 171 - Midterm Question 1 (12.6)
# Purpose: This program asks the user to enter an integer value that satisfies
#          given criteria.
# Author:  Tony Kabilan Okeke (tko35)
# Date:    02.07.2022

if __name__ == '__main__':

    # collect and validate User Input
    try:
        num = int(input("Enter an integer that is multiple of 4 and 14: "))
        if (num % 4 == 0) and (num % 14 == 0):
            print('Good Choice')
        else:
            print(f"Invalid Input: {num} is not a multiple of both, 4 and 14.")
    except:
        print('Invalid Input: Not an integer!')

    print('All Done!')