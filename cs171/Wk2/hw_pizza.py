# CS 171 - Homework 2 (Pizza for Everyone!)
# Purpose: This program calculates the number of slices a pizza can be divided into,
#          and the number of pizzas that should be ordered for a party given
#          the diameter of the pizza and the size of the party.
# Author:  Tony Kabilan Okeke (tko35)
# Date:    01.17.2022

# Import necessary modules
from math import pi, ceil, floor

# Define functions
def slicesPerPizza( diameter ):
	"""
	This function returns the number of slices in a pizza
	of a specific size.
	Assume each slice has an area of 14.125
	"""

	# Compute the area of the pizza
	area = pi * (diameter / 2)**2
	
	# Compute the number of slices
	slices = area / 14.125

	# Return the rounded down value of slices as an integer
	return int( floor(slices) )

def pizzasPerParty( party_size, diameter ):
	"""
	This function returns the number of pizzas a party of
	a specific size should order.
	Assume that each person eats 3 pizzas.
	"""
	# Compute the number of slices for a party
	party_slices = party_size * 3

	# Determine the number of pizzas
	pizzas = party_slices / slicesPerPizza(diameter)

	# Return the rounded up value of pizzas as an integer
	return int( ceil(pizzas) )

# Main script
if __name__ == "__main__":
	# Welcome message
	print("Welcome to Mario and Luigi's Pizzeria\n")

	# Get user input
	diameter = int(input("Enter the diameter of the pizzas you want to order (in inches): "))
	party_size = int(input("Enter the number of people in your party: "))

	# Calculations
	slices = slicesPerPizza(diameter)
	pizzas = pizzasPerParty(party_size, diameter)

	# Display results
	print( f"For a party of {party_size} people you need to order {pizzas} pizza(s)." )
	print( f"A {diameter} inch pizza will yield {slices} slices." )