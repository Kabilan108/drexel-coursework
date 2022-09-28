# CS 171 - Homework 3 (Phone Number Converter)
# Purpose: This program takes a 10-character phone number in the format XXX-XXX-XXXX and 
#          displays the number with any alphabetic characters that in the original string
#          translated to their numeric equivalent.
# Author:  Tony Kabilan Okeke (tko35)
# Date:    01.27.2022

# Create dictionary for mapping letters to numbers
letter2num = {'A': '2', 'B': '2', 'C': '2', 'D': '3', 'E': '3', 'F': '3',
              'G': '4', 'H': '4', 'I': '4', 'J': '5', 'K': '5', 'L': '5',
              'M': '6', 'N': '6', 'O': '6', 'P': '7', 'Q': '7', 'R': '7',
              'S': '7', 'T': '8', 'U': '8', 'V': '8', 'W': '9', 'X': '9',
              'Y': '9', 'Z': '9'}

if __name__ == '__main__':
  # Print welcome statement
  print("Phone Number Translator")

  # Get user input
  phone_num = input("Enter a phone number in the format XXX-XXX-XXXX: ")

  # Split string on '-' into a list of 3 strings
  phone_num = phone_num.split("-")

  # Use list comprehension to convert each string into the appropriate number
  phone_num = [''.join([ letter2num.get(char,char) for char in phone_num[0] ]),
               ''.join([ letter2num.get(char,char) for char in phone_num[1] ]),
               ''.join([ letter2num.get(char,char) for char in phone_num[2] ])]

  # Combine list into string and print the results
  phone_num = '-'.join(phone_num)
  
  print( f"Dial: {phone_num}" )