#File Name: PaintCost.py
#Purpose:   This program calculates the cost of painting a wall, based on the wall area
#           and the price of the paint color. Assume a gallon of paint covers 350 square feet.
#           One can hold one gallon of paint
#Author:    Adelaida A. Medlock
#Date:      10/5/20

# Import math module needed for rounding values up
import math

# Create a dictionary to store paint colors and cost per gallon
# and a constant to hold the square feet per gallon
paintColors = { 'red': 35, 'blue': 25, 'green': 23  }
SQ_FEET_PER_GALLON = 350

# Prompt user to input wall's dimensions and desired paint color
height = int(input('Enter wall height (feet): '))
width = int(input('Enter wall width (feet): '))
color = input('Choose a color to paint the wall: ')

# Calculate wall area
area = height * width
   
# Calculate the amount of paint in gallons needed to paint the wall   
gallons = area / SQ_FEET_PER_GALLON

# Calculate number of cans needed
cans = math.ceil(gallons)

# Calculate the total cost of paint can needed depending on color
cost = paintColors[color] * cans

# Display the results
print()
print('Wall area: %d square feet' %(area))
print('Paint needed: %.2f gallons' %(gallons))
print('Cans needed: %d can(s)' %(cans))
print('Cost of purchasing %s paint: $%.2f' %(color, cost))