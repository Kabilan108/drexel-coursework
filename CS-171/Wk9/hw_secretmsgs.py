# CS 171 - Homework 7 (Secret Messages)
# Purpose: Perform a simple encryption and decryption of a originalMsg message.
# Author:  Tony Kabilan Okeke (tko35)
# Date:    02.24.2022

# Import necessary modules
import os

# Define Functions
def encode(originalMsg, code):
    """
    Encrypt originalMsg using code
    @param originalMsg
        Raw message to encode
    @param code
        code used for encryption
    @return
        Encrypted message
    """
    # Define original alphabet
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # Encrypt original message
    codedMsg = [code[alphabet.index(c)] if c in alphabet else c for c in originalMsg]

    # Return encrypted string
    return ''.join(codedMsg)

def decode(codedMsg, code):
    """
    Decrypt originalMsg using code
    @param codedlMsg
        Encrypted message
    @param code
        code used for encryption
    @return
        Decrypted message
    """
    # Define original alphabet
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # Decrypt original message
    originalMsg = [alphabet[code.index(c)] if c in alphabet else c for c in codedMsg]

    # Return decrypted string
    return ''.join(originalMsg)

def file_prompt(prompt=''):
    """
    Prompt user for file containing code and read file contents.
    @param prompt
        The text for the prompt
    @return
        file name
    """
    while True:
        file_name = input(prompt)
        if os.path.isfile(file_name):
            with open(file_name, 'r') as file:
                # Read file and remove whitespace characters from the ends.
                code = file.read().strip()
            break
        else:
            print("Error: that file does not exist")

    return code

def main():
    """
    Run program.
    """

    # Prompt user to select menu option
    print("Enter E to encode a message.\nEnter D to decode a message.")
    while True:
        mode = input("Enter your choice: ")
        if mode.upper() in ['E', 'D']:
            break
        else:
            print("Error: You must enter E or D")

    # Prompt for code file
    code = file_prompt("Enter name of the file that has the code: ")

    if mode.upper() == 'E': # Encode mode
        # Ask user for message
        originalMsg = input("Enter the message you want to encode: ")
        
        # Encrypt message
        codedMsg = encode(originalMsg, code)
        
        # Write message to file
        with open('secret.txt', 'w') as file:
            file.write(codedMsg)
        
        # Print results
        print(f"\nEncoded message: {codedMsg}")
        print("Encoded message has been saved in secret.txt")
    else: # Decode mode
        # Ask user for file containing encoded message
        codedMsg = file_prompt("Enter name of the file that has the message to decode: ")
        
        # Decrypt message
        originalMsg = decode(codedMsg, code)
        
        # Print results
        print(f"\nEncoded message: {codedMsg}\nDecoded message: {originalMsg}")
        

if __name__ == '__main__':
    main()