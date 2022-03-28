# CS 171 - Homework 5 (A Penny a Day)
# Purpose: This program prints the number of times each letter occurs in
#          a sentence.
# Author:  Tony Kabilan Okeke (tko35)
# Date:    02.04.2022

# Define Functions
def uniqueChars(string):
	"""
	This function returns a sorted list containing the unique 
	characters in a string.
	"""

	# Keep unique characters (string -> set -> list)
	chars = list( set(string) )
	# Sort list alphabetically
	chars.sort()

	return chars


if __name__ == '__main__':
	
	# Get user input and convert it to lower case
	myString = input('Enter a sentence: ')
	myString = myString.lower()

	# Identify unique characters in string
	chars = uniqueChars(myString)

	# Print count for each alphabetic character
	for char in chars:
		if 'a' <= char <= 'z':
			print( f"{char}: {myString.count(char)} times" )