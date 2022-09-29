# CS 171 - Homework 2 (How Efficient us Your Car?)
# Purpose: This program calculates the fuel efficiency of a car, and the total
#          number of consumed gallons of gasoline as well as the cost of gasoline
#          for a given trip.
# Author:  Tony Kabilan Okeke (tko35)
# Date:    01.17.2022

# Import necessary modules
from math import e

# Define Functions
def fuelEfficiency( speed ):
	"""
	This function calculates the fuel efficiency (MPG) of a car
	given its speed.
	"""

	# Compute fuel efficiency
	fe = 71.7 * speed * ( 2 + 0.0192*speed )**(-4.5) + e**( -5.1*speed ) - 1

	return fe

if __name__ == '__main__':
	# Welcome message
	print("Welcome to the fuel efficiency calculator\n")

	# Get user input
	speed = float( input("Enter the average speed driven (in miles per hour): ") )
	dist = float( input("Enter the distance traveled (in miles): ") )
	cost_per_gal = float( input("Enter the cost of gasoline (in dollars per gallon): ") )

	# Calculations
	fe = fuelEfficiency(speed)
	gas = dist / fe
	total_cost = cost_per_gal * gas

	# Display results
	print( f"\nThe fuel efficiency of your vehicle is {round(fe, 2)} miles per gallon." )
	print( f"{round(gas, 2)} gallons of gasoline were consumed during this trip." )
	print( f"The total cost of the consumed gasoline was {round(total_cost, 2)} dollars." )