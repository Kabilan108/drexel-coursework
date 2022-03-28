#Program:     PriceCalculator_V2.py
#Purpose:     Add tax and discount to an item's price - with functions
#Author:      Adelaida Medlock
#Date:        January 5, 2020

# function that calculates final price of an item
def calculateFinalPrice(price, tax, discount):
    # apply price deduction
    deduction = price * discount
    price = price - deduction

    # apply sales tax
    increase = price * tax
    price = price + increase

    # return final price
    return(price)

# declare variables to hold known values
tax =  0.08   #8% sales tax
discount = 0.1  #item is 10% off

# get input from the user
price = float(input("Enter item's price: "))

# call function
finalPrice = calculateFinalPrice(price, tax, discount)

# display final price
print("Final Price for the item:" , finalPrice)
