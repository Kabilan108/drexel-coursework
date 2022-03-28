# CS 171 - Homework 8 (Reversing Text)
# Purpose: Reverse string provided by the user
# Author:  Tony Kabilan Okeke (tko35)
# Date:    03.04.2022

# Define Functions
def reverseString(string):
    """
    A recursive function that reverses a string.
    @param string
        String to be reversed
    @return
        Reversed string
    """
    
    #// Base case: reverse a two character string
    #//if len(string) <= 2:
    #//    return string[1] + string[0]
    # Base case: a single character
    if len(string) == 1:
        return string
    
    # Join reversed strings to first character
    return reverseString(string[1:]) + string[0]

def main():
    """Run program"""
    
    # Prompt for string
    string = input("Enter a string you wish to reverse: ")

    # Reverse string and pring result
    reverse = reverseString(string)
    print(f"Here is the reversed string: {reverse}")


if __name__ == '__main__':
    main()