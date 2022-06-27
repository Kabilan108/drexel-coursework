#Program:   InputValidation.py
#Purpose:   Demo input validation
#            1) is the value entered the right type?
#            2) does the value meet the criteria?
#Author:    Adelaida Medlock
#Date:      October 9, 2020

# import module needed for calculations
import math

# use try/except and if/else for input validation
try:
    number = int(input("Enter an integer value greater than zero: "))
    if number > 0 :  
       print('The square root of', number, 'is', math.sqrt(number))
    else :  
      print("Error: Value entered is not positive.")

except Exception as e:
    print('Error: Value entered is not an integer.')

