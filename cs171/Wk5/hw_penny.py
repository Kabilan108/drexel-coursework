# CS 171 - Homework 5 (Counting Letters)
# Purpose: This program calculates how much money one would have after a
#          certain number of days if their salary doubled every day
#          starting at 1 cent.
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
            days = int(input("Enter the number of days: "))
            if not days > 0:
                print('Error: you must enter a number greater than zero. Try again.')
            else:
                stop = True
        except:
            print("Invalid input. A integer value was expected. Try again.")

    return days

if __name__ == '__main__':
    # Collect user input
    days = input_validation()

    # Print table header
    print(f"\n{'Day':5s}Pennies")

    # Compute the daily salaries as a geometric sequence
    a = 0.01  #Day 1 = 1 cent = $0.01
    r = 2 #Doubles daily
    salaries = [a*r**n for n in range(0, days)]

    # Print the salary table
    for day in range(0, days):
        print(f"{day+1:<5d}${salaries[day]:.2f}")

    # Print total salary
    print(f"\nThe total salary for {days} days is ${sum(salaries):.2f}")