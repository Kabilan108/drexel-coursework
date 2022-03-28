# Author: Tony Kabilan Okeke (tko35)
# Last Modified: 01/06/22
# Description: This program takes user input and concatenates
#              it into a sentence.

# Collect user input
print("Please provide the following:")
color = input("A color: ")
animal = input("An animal: ")
car = input("A vehicle: ")
city = input("A city: ")

# Concatenate input
print("The {} {} drove the {} to {}.".format(color, animal, car, city))