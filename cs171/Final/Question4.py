# CS 171 - Final Question 4 (20.4)
# Purpose: Display the qHash for user-provided strings
# Author:  Tony Kabilan Okeke (tko35)
# Date:    03.15.2022

# Definitions
def qHash(string):
    """
    Compute the qHash value of a given string
    """
    unicode = [ord(char) for char in string]
    ones_sum = sum([x % 10 for x in unicode])
    tens_sum = sum([x // 10 % 10 for x in unicode])

    return ones_sum * tens_sum

def main():
    """
    Run program
    """
    print("To Exit type \"quit\"")
    
    while True:
        string = input("Enter Text: ")
        if string == "quit":
            break
        print(f"Hash is {qHash(string)}")


if __name__ == "__main__":
    main()