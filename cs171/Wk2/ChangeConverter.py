#Program:     ChangeConverter.py
#Purpose:     Given an amount of pennies, calculate the corresponding
#             number of quarters, dimes, nickels and pennies
#Author:      Adelaida Medlock
#Date:        September 27, 2021

# intro and instructions for the user
print('Change Converter')
print('For a given amount of pennies, this program calculates the corresponding number of')
print('quarters, dimes, nickels, and pennies.')

# get input from the user
change = int(input('Enter the amount of cents to convert: '))

# create conversion variables
CENTS_PER_QUARTER = 25
CENTS_PER_DIME = 10
CENTS_PER_NICKEL = 5

# calculate coin denominations
# start with quarters and leftover cents
quarters = change // CENTS_PER_QUARTER
change = change % CENTS_PER_QUARTER

# calculate the number of dimes and leftover change
dimes = change // CENTS_PER_DIME
change = change % CENTS_PER_DIME

# calculate the number of nickels and leftover pennies
nickels = change // CENTS_PER_NICKEL
pennies = change % CENTS_PER_NICKEL

# display the results
print('Here is your change:')
print(quarters, 'quarter(s),', end = ' ')
print(dimes, 'dime(s),', end = ' ')
print(nickels, 'nickel(s),', end = ' ')
print('and', pennies, ' pennnies.')
print()