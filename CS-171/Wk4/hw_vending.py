# CS 171 - Homework 4 (Sentences)
# Purpose: This program simulates a vending machine that contains six snacks
#          labelled 1 through 6.
# Author:  Tony Kabilan Okeke (tko35)
# Date:    01.30.2022

# Define functions
def printMenu():
	"""
	This function prints the vending machine menu and
	returns (parallel) lists of items and their prices
	"""
	# Create lists of items and their prices
	items = ["Roasted Almonds", "Pretzels", "Chewing Gum", "Mints", "Chocolate bar", "Cookies"]
	prices = [1.25, 1.75, 0.90, 0.75, 1.50, 2.00]

	# Display menu
	print("Vending Machine\n",
		  f"1. {items[0]:15} --> ${prices[0]:.2f}",
		  f"2. {items[1]:15} --> ${prices[1]:.2f}",
		  f"3. {items[2]:15} --> ${prices[2]:.2f}",
		  f"4. {items[3]:15} --> ${prices[3]:.2f}",
		  f"5. {items[4]:15} --> ${prices[4]:.2f}",
		  f"6. {items[5]:15} --> ${prices[5]:.2f}\n",
		  sep = '\n')

	return items, prices

if __name__ == '__main__':

	# Print menu
	items, prices = printMenu()

	# Get and validate user input
	validData = True
	try:
		# Get user selection
		item = int(input("Enter your choice of item: "))

		# Determine if selection is valid
		if not (0 < item < 7):
			validData = False
			print("Invalid item choice.")
		else:
			# Ask user for paymet
			payment = float(input("Enter money to purchase item: "))

			# Validate payment
			if payment < 0:
				validData = False
				print("Amount of money cannot be a negative value.")
	except:
		validData = False
		print("Value entered was not a number.")

	# If user provided valid data
	if validData:
		# Calculate change and display appropriate message
		if payment < prices[item-1]:
			amount_owed = prices[item-1] - payment
			print( f"You are ${amount_owed:.2f} short." )
		else:
			change = payment - prices[item-1]
			print( f"Thanks for buying {items[item-1]}.\nYour change is ${change:.2f}." )