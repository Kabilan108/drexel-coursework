# CS 172 - Lab 1
#
# Description: This script will read in a text file and print out any word that 
#              is not found in the spelling dictionary.
# Author: Tony Kabilan Okeke <tko35@drexel.edu>
# Date: 01.12.2023

from spellchecker import spellchecker


def get_file() -> str:
    """
    This function prompts the user to provide a file name and checks whether the 
    file is valid.
    """

    while True:
        try:
            filename = input("Enter the name of the file to read:\n")
            f = open(filename, 'r')
            f.close();
        except Exception as E:
            print("Could not open file.")
            continue;
        break;

    return filename


def main() -> None:
    """
    Main Script for the Program
    """
    
    # Welcome text
    print("Welcome to Text File Spellchecker.")

    # Instatiate the Spell Checker
    SP = spellchecker("english_words.txt")

    # Ask user for file to spell check
    filename = get_file()

    with open(filename, 'r') as file:
        # Define counters
        passed, failed, lc = 0, 0, 1

        # Check words
        for line in file:
            for word in line.split():
                if not SP.check(word):
                    print(f"Possible Spelling Error on line {lc}: {word}")
                    failed += 1
                else:
                    passed += 1
            lc += 1

    # Print summary
    print(f"{passed:,} words passed spell checker.")
    print(f"{failed:,} words failed spell checker.")
    print(f"{passed / (passed + failed) * 100:.2f}% of the words passed.")

if __name__ == '__main__':
    main()
