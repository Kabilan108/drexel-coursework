#Program:   bmiCalculator.py
#Purpose:   This program computes you BMI. The user will enter their height (in ft, in) 
#           and weight in pounds. The formula used needs height and weight in 
#           the metric system. 
#Author:    Adelaida Medlock
#Date:      October 16, 2021


# Conversion factors
POUNDS_TO_KG = 0.453592
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
    
# Here is the main script
if __name__ == "__main__" :
    # intro
    print("Let's calculate your BMI and see if it's in the healthy range")
    print('-------------------------------------------------------------')

    # Get input from user and validate it
    validData = True
    try:
        weight =  int(input ("Enter your weight (in pounds): " ))
        height1 = int(input ("Enter your height (feet): " ))
        height2 = int(input ("Enter your height (inches): " ))
    except ValueError as e:
        print('Value entered was not an integer.')
        validData = False

    # does the data meet the criteria? are values greater than zero?
    if validData and (weight <= 0  or height1 <= 0 or height2 <= 0) :
        print('Invalid data: weight and/or height is too low.')
        validData = False  

    # decide if we should exit the program
    if not validData :  
        print('Invalid data. Your BMI cannot be calculated')
    else:
        # data is valid, calculate BMI
        result = bmi(weight, height1, height2)
        print("Your BMI is", round(result, 2))

        #Determine status of person
        print("Your status is:", weightStatus(result))
    
    
    

