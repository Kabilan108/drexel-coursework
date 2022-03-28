# CS 171 - Homework 8 (Converting to Binary)
# Purpose: Display the binary representation of a user-provided number using recursion.
# Author:  Tony Kabilan Okeke (tko35)
# Date:    03.04.2022

# Define Functions
def decimalToBinary(number):
    """
    A recursive function that takes a positive integer number (in decimal) and returns
    a string with it's binary representation.
    @param number
        Positive integer (in decimal)
    @return
        String with binary representation of argument
    """
    if number < 0:
        raise ValueError("Only positive integers allowed.")
    elif number < 2:
        # Base case: For 0,1, return number only #//remainder only
        #//return str(number % 2)
        return str(number)

    # Recursive call: Join remainder of smaller problems to remainder of larger one
    return decimalToBinary(number // 2) + str(number % 2)

def validateInput():
    """
    Validate user input
    @param   None
    @retrun  user input
    """
    while True:
        try:
            value = int(input("Enter a positive integer or 0 to end: "))
            if value > 0:
                print("Error: you entered a negative value. Try again")
            else:
                break
        except:
            print("Error: An integer value was expected. Try again")

    return value

def main():
    """Run program"""
    while True:
        # Prompt user for number
        number = validateInput()
        if number != 0:
            # Convert to binary, print result
            binary = decimalToBinary(number)
            print(f"The equivalent of {number} in Binary is {binary}\n")
        else:
            break  # Exit loop if number == 0


if __name__ == '__main__':
    main()