#Program:     bmiWithFunctions.py
#Purpose:     BMI calculator using functions
#Author:      Adelaida Medlock
#Date:        May 9, 2020

''' Purpose: converts measurements from the English system to the metrict system
    Parameters:
       height: an integer that represents the height in inches
       weight: an integer that represents the weight in pounds
    Return value:a tuple with the values in the metric system
    Usage example: w, h = get_int_in_range (100, 60)  
'''  
def convert_to_metric(height, weight):
    POUNDS_TO_KG = 2.205
    INCHES_TO_METERS = 39.37
    weight = weight / POUNDS_TO_KG
    height = height / INCHES_TO_METERS
    return (weight, height)

''' Purpose: calculates the body mass index based on the weight and height (metric system)
    Parameters:
       weight: an integer value representing a person's weight in kilograms
       height: an integer value representing a person's height in meters
    Return value:an integer number greater than zero
    Usage example:  bmi = bmi_calculator(65, 1.73)  
'''  
def bmi_calculator(weight, height) :
    bmi = (weight) / (height ** 2)
    return bmi

''' Purpose: displays BMI feedback based on the BMI of a person
    Parameters:
       bmi: an positive integer reprenseting the body mass index
    Return value:none
    Usage example: bmi_feedback(22.55)
'''  
def bmi_feedback(bmi) :
    if bmi < 18.5 :
        print("You are underweight.")
    elif bmi < 25 :
        print("You have a normal weight.")
    elif bmi < 30 :
        print("You are overweight.")
    else :
        print("You are obese.")

''' Purpose: validates input from the user to be an integer greater than zero
    Parameters:none
    Return value:an integer number greater than zero
    Usage example:  num = validate_input()  
'''  
def validate_input() :
    stop = False
    while (not stop):
        try:
            number = int(input())
            while (number <= 0):
                  print('Invalid data. Value entered is too low. Try again:', end = ' ')
                  number = int(input())
            stop = True
        except Exception as e:
            print('Invalid input: an integer value was expected. Try again:', end = ' ')
    return number


# typically you will have a main or driver function that organizes and calls the other functions
def main():
    again = True
    
    while again:
        #intro
        print("Let's calculate your BMI and see if it's in the healthy range")
        print('-------------------------------------------------------------')

        # Data input and validation
        print('Enter your weight (lbs):', end = ' ')
        weight = validate_input()
    
        print('Enter your height (inches):', end = ' ')
        height = validate_input()    
    
        # Convert o the metric system
        weight, height = convert_to_metric(height, weight)
        
        # Compute and display BMI  
        bmi = bmi_calculator(weight, height)
        print("Your BMI is", round(bmi, 2))

        # Determine status of person
        bmi_feedback(bmi)
        
        # another user?
        print('\nAnother user? (y/n): ', end = ' ')
        answer = input()
        if answer[0].lower() != 'y':
            again = False
        print()
    
    print('Good-bye!')
    
    

