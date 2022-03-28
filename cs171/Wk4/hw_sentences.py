# CS 171 - Homework 4 (Sentences)
# Purpose: This program reads a one-line sentence as input from the user
# 		   then displays a response based on the criteria satisfied by the sentence.
# Author:  Tony Kabilan Okeke (tko35)
# Date:    01.30.2022

# Define Functions
def evenCharacters(myString):
	"""
	This functions returns True if the string provided
	contains an even number of characters and False otherwise.
	"""
	is_even = len(myString) % 2 == 0

	return is_even


if __name__ == '__main__':

	# Collect user input
	myString = input("Enter a sentence: ")

	# Display response
	if myString[-1] == '?': 
		# If sentence ends with '?'
		if evenCharacters(myString):
			# Check if sentence has even length
			print('Yes')
		else: 
			# Check if sentence has odd length
			print('No')

	elif myString[-1] == '!': 
		# Sentence ends with '!'
		print('Wow')

	else: 
		# Otherwise
		print( f'You always say "{myString}"' )