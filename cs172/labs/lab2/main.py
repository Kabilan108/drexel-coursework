# CS 172 - Lab 1
#
# Description: This script allows the user to create a receipt and add items to it.
#
# Author: Tony Kabilan Okeke <tko35@drexel.edu>
# Date: 01.19.2023

# Imports
from receipt import Receipt
from item import Item


# Main Program
if __name__=="__main__":
	# Welcome message
    print("Welcome to Receipt Creator")

    # Instantiate a receipt
    reciept = Receipt()

    # Collect user input
    while True:
        # Prompt for item information
        name = input("Enter Item name: ")
        price = float(input("Enter Item Price: "))
        taxable = input("Is the item taxable (yes/no): ").lower() == "yes"

        # Add the item to the reciept
        reciept.addItem(Item(name, price, taxable))

        # Check if user wants to add another item
        if input("Add another item (yes/no): ").lower() != "yes":
            break

    # Print the reciept
    print(reciept.receiptToString())

