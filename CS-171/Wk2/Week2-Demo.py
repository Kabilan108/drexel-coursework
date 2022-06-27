# Week 2 - Demo

## variables
#itemName = 'Chocolate bar'  #string
#numberOfItems = 2           #int
#itemPrice = 3.54            #float
#change = 0.0
#
## basic output
#print("item's name", itemName)
#print("Price:", itemPrice)
#print()
#
##input
#itemName = input('Enter the name of the item: ')
#print('Item:', itemName)
#
#numberOfItems = int(input('How many items do you want to buy? '))
#itemPrice = float(input('Enter the price per unit: '))
#
## basic calculations:  + - * /
#total = numberOfItems * itemPrice
#print('The total price is $', total)
#
## features of variables
## value: get it with print(variable)
## type: get it with type(variable)
## id: get it with id(variable)
#print("the total variable")
#print("value is", total)
#print('type of total is', type(total))
#print('id of total is', id(total))
#print()
#
##Arithmetic operators: + - * /
## Other arithmetic operators:
## //  floor division or integer division
## %    modulus operator
## **   power operator

# arithmetic expressions: + - * / // ** %
# PEMDAS  left to right
#a = 2
#b = 7
#x = 3.5
#y = 5.0
#
#result = a + b * x / y
#print(result)
#
#result = (a + b) * x / y
#print(result)
#
#result = (a + (b * x)) / y
#print(result)
#

#calculate the area of a circle
#radius = float(input('Enter the radius of a circle: '))
#PI = 3.14159
#area = PI * radius ** 2.0
#print('The area of the circle is:', area)
#print()
#
## modules
#import math
#r = math.sqrt(25.0)
#print(r)

import math
radius = float(input('Enter the radius: '))
area = math.pi * math.pow(radius, 2.0)
print('The area of the circle is:', area)

# volume of a sphere
volume = (4 / 3) * math.pi * (radius ** 3)
print('Volume = ', volume)
