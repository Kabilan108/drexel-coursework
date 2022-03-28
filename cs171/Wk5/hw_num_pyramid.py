# CS 171 - Homework 5 (Number Pyramid)
# Purpose: This program prints a pyramid of numbers based on user input.
# Author:  Tony Kabilan Okeke (tko35)
# Date:    02.04.2022

# Define Functions
def input_validation():
    """
    This function collects and validates user input.
    """
    stop = False
    while not stop:
        try:
            rows = int(input("Enter the number of lines (1 - 9): "))
            if not (1 <= rows <= 9):
                print('Error: you must enter a value between 1 and 9. Try again.')
            else:
                stop = True
        except:
            print("Invalid input. A integer value was expected. Try again.")

    return rows

if __name__ == '__main__':
    # Collect user input
    nrow = input_validation()

    # Skip 2 lines before printing pyramid
    print('\n\n', end='')

    # Loop through each row of the pyramid
    for r in range(0, nrow):

        # Print Initial spaces
        for space in range(0, nrow-r-1):
            print(' ', end='')
        
        # Define starting number for row
        num = r + 1
        # Define number counter
        count = r

        # Loop through  entries in each row
        # (Each row contains 2*r + 1 numbers)
        for i in range(0, 2*r+1):
            print(num, end='')
            if count < 1:
                # If count drops below 1, increment the number
                num += 1
            else:
                num -= 1
            # Decrement the counter
            count -= 1
        # Jump to the next line
        print()