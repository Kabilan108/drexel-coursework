# CS 171 - Midterm Question 3 (12.8)
# Purpose: Function Implementation
# Author:  Tony Kabilan Okeke (tko35)
# Date:    02.07.2022

# Import necessary modules

# Define Functions
def functionA(x):
    # Compute result
    out = 3*x + 2

    return out

def functionB(myString):
    # Test if the string starts and ends with the same character
    if myString[0] == myString[-1]:
        out = True
    else:
        out = False
    
    return out

def functionC(luminance, threshold):
    # Return white if luminance >= threshold, black otherwise
    if luminance >= threshold:
        out = 'white'
    else:
        out = 'black'

    return out

def functionD(time):
    # Define Constant
    GRAVITY = 9.8
    # Compute result
    out = GRAVITY * time**2 / 2

    return out