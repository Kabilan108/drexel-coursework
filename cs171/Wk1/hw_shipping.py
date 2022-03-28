# CS 171 - Homework 1
# Purpose: This program calculates and displays the shipping charges for a parcel
#          given its weight in pounds and the shipping rate per pound.
# Author: Tony Kabilan Okeke (tko35)
# Date: 01.06.2022

# Define function for rounding floating point numbers
# to the nearest hundredth
def roundFloat(num):
  return int((num + 0.005) * 100) / 100

# Instructions to the user:
#   Once this program is run, it will prompt you to provide 2 values.
#   Please enter the values into the console.
#   The shipping cost will then be displayed in the console
print("Shipping Charges Calculator\n\n")

# Get user input
wt = float( input("Enter the weight of your parcel in pounds: ") ) # weight
ppp = float( input("Enter the shipping price per pound: ") ) # price per pound

# Calculate shipping charges
charge = wt * ppp

# Round the result to the nearest hundredth
charge = roundFloat(charge)

# Display the results
print("The weight of your parcel is", wt, "pounds")
print("The shipping price per pound is", ppp, "dollars")
print("The shipping charges for your parcel is", charge, "dollars")