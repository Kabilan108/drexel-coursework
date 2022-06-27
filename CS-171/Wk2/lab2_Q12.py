# Author: Tony Kabilan Okeke
# Date: 01.13.2022
# Title: Lab 2 Question 12

# Execute if file is called as a script
if __name__ == "__main__":
	# Welcome message
	print("Hi! Welcome to the Python's Belly!\n\nI'm here to take your order.")

	# Collect user input
	burgers = int( input("How many Hamburgers would you like? ") )
	fries = int( input("How many fries would you like? ") )
	drinks = int( input("How many drinks do you want? ") )

	# Compute total price
	price = 2.0*burgers + 1.5*fries + 1.0*drinks

	# Output results to user
	print( "\nYour total will be $", format(price, ".2f") , sep="" )
	print( "Have a great day!\n" )