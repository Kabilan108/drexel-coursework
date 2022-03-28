#Program:   bmiCalculator-V2.py
#Purpose:   This program computes you BMI. The user will enter their height (in ft, in) 
#           and weight in pounds. The formula used needs height and weight in 
#           the metric system. 
#Author:    Adelaida Medlock
#Date:      October 24, 2021


# Conversion factors
POUNDS_TO_KG = 0.453592 # Constants written in uppercase
INCHES_PER_FEET = 12
INCHES_TO_METERS = 0.0254

# Functions needed -- defined below this line
# We need to convert lbs to kgs
def poundsToKg(weight):
    return weight * POUNDS_TO_KG

# We need to convert feet/inches to meters
def heightToMeters(feet, inches):
    totalInches = feet * INCHES_PER_FEET + inches
    return totalInches * INCHES_TO_METERS

# Compute a person's BMI
# Formula:
# BMI = (weight in Kg) / (height in meters) ^ 2
def bmi(weight, feet, inches):
    kg = poundsToKg(weight)
    meters = heightToMeters(feet, inches)
    myBmi = kg / (meters ** 2)
    return myBmi

# Describe of the person's weight
def weightStatus(bmiValue):
    if bmiValue < 18.5:
        return "Underweight"
    elif bmiValue <= 24.5:
        return "Normal Weight"
    elif bmiValue <= 29.9:
        return "Overweight"
    else:
        return "Obese"
    
# Get input from the user and validate it    
def validate_input() :
    stop = False # flag - check value to trigger loop or decision
    while (not stop):
        try:
            # Code that could raise error
            number = int(input())
            if (number <= 0):
                print('Invalid data. Value entered is too low. Try again:', end = ' ')
            else :
                stop = True
        except Exception as e:
            print('Invalid input: an integer value was expected. Try again:', end = ' ')
    return number


# Here is the main script
if __name__ == "__main__" :
    
    # Repeat as many times as the user wants
    more = 'Y'
    while more == 'Y' :
        
        # intro
        print("Let's calculate your BMI and see if it's in the healthy range")
        print('-------------------------------------------------------------')

        # Get input from user
        print("Enter your weight (in pounds):", end = ' ')
        weight =  validate_input()
        print("Enter your height (feet):", end = ' ')
        height1 = validate_input()
        print("Enter your height (inches):", end = ' ')
        height2 = validate_input()
 
        # Calculate BMI
        result = bmi(weight, height1, height2)
        print("Your BMI is", round(result, 2))

        # Determine status of person
        print("Your status is:", weightStatus(result))
    
        # ask user if she/he wants to go again
        print()
        more = input('Do you want to calculate another BMI? (Y/N): ')
        more = more[0].upper()
        print()

    

if __name__ = '__main__':

    # Input validation
    validData = True
    try: #code that could cause error
        weight = int(input('Enter the weight in pounds: '))
        height1 = int(input('Enter your height in feet: '))
        height2 = int(input('Enter your height in inches: '))

    except: # what to do
        print('Error: value entered was not an integer')
        validData = False

    # does the data meet the criteria? values greater than zero
    if validData and (weight <= 0 or height1 <= 0 or height2 <=0):
        print('Error you bastard! How can your height / weight be negative?')
        validData = False

    # Calculations
    if validData:
        BMI = bmi(weight, height1, height2)
        print(f'BMI = {bmi}')
        print(f'You are {weightStatus(BMI)}')
    else:
        print('Invalid Data: Your BMI cannot be calculated.')


# Use while loops and try except for input validation