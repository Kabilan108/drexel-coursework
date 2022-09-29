# Author: Tony Kabilan Okeke
# Date: 01.27.2022

"""
Question 20
"""
# Get variable values
testA = int(input('Enter value for testA: '))
num1 = int(input('Enter value for num1: '))

# Decison Structure:
if testA == 25:
	num1 += 5
else:
	num1 -= 5


"""
Question 21
"""
# Collect input
word = input('Please provide a word: ')

# Return Output
if ('apple' < word) and ('pear' > word):
	print(f'"{word}" is valid.')
else:
	print(f'"{word}" is out of range.')


"""
Question 22
"""
# Collect inputs
item1 = float(input( "Enter the price of the first item: " ))
item2 = float(input( "Enter the price of the second item: " ))
payment = float(input( "How much did you pay? " ))

# Compute total cost
total_cost = item1 + item2

# Print output
if ( payment < total_cost ):
	balance = total_cost - payment
	print (f"You still owe ${balance:.2f}")
else:
	change = payment - total_cost
	print (f"Your change is ${change:.2f}.\nThank you!")


"""
Question 23
"""
# Collect input
num = int(input("Please Enter a Multiple of 5 Between 1 and 100: "))

# Print Output
if (num % 5 == 0) and (num >= 1) and (num <= 100):
	print(f"{num} is valid.")
else:
	print(f"{num} is invalid.")
