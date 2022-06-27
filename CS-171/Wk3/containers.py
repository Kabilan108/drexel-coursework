#File Name: containers.py
#Purpose:   Demo how to create and use lists, dictionaries, sets, tuples
#Author:    Adelaida A. Medlock
#Date:      4/12/19

# using lists: find the min and max numbers from a list of values
# entered by the user
# creating a basic empty list an appending values to it
print('Enter 3 numbers on each line')
numbers = []  #empty list - no items

# input: ask user to enter each number
numbers.append(int(input('Enter the first number: ')))
numbers.append(int(input('Enter the second number: ')))
numbers.append(int(input('Enter the third number: ')))

# display some stats on the numbers in the list
print('The minimum number was', min(numbers))
print('The maximum number was', max(numbers))
print()


# using lists: calculate quiz averages of a list of values
# entered by the user
quizzes = [float(input("Enter Quiz %d Grade: " %(x + 1))) for x in range (0, 4)]
average = sum(quizzes)/len(quizzes)
print("Quiz Average: %.2f" %average)
print()


# dictionaries: using a dictionary to perform conversions between units
fluid = {"cups" :    1,
         "pints" :   2 ,
         "quarts" :  4 ,
         "gallons" : 16
         }

print("Fluid Conversion")
cups = float(input("Enter a number of cups: "))
print("Units: cups, pints, quarts, or gallons")
units = input ("Enter target units: ")
result = cups / fluid[units]
print(cups, "cups is", result , units)
print()


# using sets: using a set to keep a grocery check-list
myGroceries = {"milk", "bananas", "eggs", "bread", "coffee"}
print('Initial grocery check-list:')
print(myGroceries)
myGroceries.add("butter")
myGroceries.add("sugar")
print('Updated grocery check-list')
print(myGroceries)
print('You have', len(myGroceries), 'items in your grocery check-list.')
print()


# using tuples: this tuple represents the primary colors
primaryColors = ('red', 'blue', 'yellow')
print('There are', len(primaryColors), 'primary colors: ')
print('Primary Color #1: ', primaryColors[0])
print('Primary Color #2: ', primaryColors[1])
print('Primary Color #3: ', primaryColors[2])
print()
