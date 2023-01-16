# File Name:   main-hangman.py
# Purpose:     Implements the Hangman game
# Author:      Tony Kabilan Okeke
# Date:        January 16, 2023

# Rules for Playing against the Computer
# 1. The computer will choose a secret random word from a list of words stored in a 
#    data file.
# 2. The player will try to guess the secret word by entering one letter in each turn.
# 3. The computer will give feedback to the player by indicating whether:
#    - The letter entered by the player does not exist in the secret word, or
#    - The letter entered by the player exists in the secret word. In this case the 
#      program will show the user the position of the letter within the word.
# 4. The player has unlimited number of turns until they have guessed the word. At that 
#    point program tell the user how many turns it took to guess the secret word.

# Set random seed
import random
random.seed(15)


def getFile() -> str:
    """
    This function prompts the user to provide a file name and checks whether the
    file is valid.

    Returns
    -------
    str
        Name (and path) of the file
    """

    while True:
        try:
            filename = input("Enter name of the data file: ")
            f = open(filename, 'r').close()
        except FileNotFoundError:
            print("Error: that file does not exist. Try again.")
            continue
        break

    return filename

def findMatches(word: str, letter: str) -> str:
    """
    This function will find where `letter` appears in word.

    Parameters
    ----------
    word : str
        The secret word
    letter : str
        The letter to search for

    Returns
    -------
    str
        String indicating where the letter appears
    """

    return ''.join([letter if letter == l else '-' for l in word])


def merge(word1: str, word2: str) -> str:
    """
    This function will parse two strings and produce a string that combines the
    letters and `-` from both

    Parameters
    ----------
    word1, word2 : str
        Strings to parse

    Returns
    -------
    str
        Merged string
    """

    return ''.join([w1 if w1 != '-' else w2 for w1, w2 in zip(word1, word2)])

       
if __name__ == "__main__":
    # Prompt user for the data file
    filename = getFile()

    # Select a random word from the data file
    with open(filename, 'r') as f:
        words = [word.strip() for word in f.readlines()]
    SECRETWORD = random.choice(words)

    # Tell user the word length
    print(
        f"I have a {len(SECRETWORD)} letter word, try to guess it.\n"
        "You will enter one letter at the time."
    )

    # Define turn counter
    turns = 1

    # Define an tracker for the guessed word
    found = ''.join(['-' for _ in SECRETWORD])

    # Prompt user for input
    while True:
        # Prompt for a letter
        letter = input("Enter a letter to see if it's in the word: ")

        # Check letter
        if letter in SECRETWORD:
            print(f"{letter} is part of my secret word.")

            # Show where the letter matches in the word
            match = findMatches(SECRETWORD, letter)
            found = merge(found, match)
            print(found)
        else:
            print(
                f"{letter} is not in my secret word."
                "Guess another letter."
            )

        # Exit loop when all words are guessed
        if '-' not in found:
            print("Congratulations, you guessed my secret word!")
            print(f"It took you {turns} turns to guess my secret word.")
            break
        else:
            turns += 1
