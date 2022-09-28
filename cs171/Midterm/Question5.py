# CS 171 - Midterm Question 5 (12.10)
# Purpose: This program computes the distance from Earth to the Sun on
#          any given day.
# Author:  Tony Kabilan Okeke (tko35)
# Date:    02.07.2022

# Import modules
from math import pi, cos

if __name__ == '__main__':

    # Collect and validate user input (number of days)
    valid = True
    try:
        days = int(input("Enter the number of days from perihelion: "))
    except:
        valid = False
        print('Invalid Input')
    if valid and not 0 <= days <= 365:
        valid = False
        print('Invalid Input')

    # If valid inputs were provided
    if valid:

        # Define equation parameters
        a = 149600000
        e = 0.01672
        theta = 2*pi*days / 365.256

        # Compute and print result (in km)
        r_km = a * (1 - e**2) / (1 + e*cos(theta))
        print(f"On this day the distance from the Earth to the Sun is {r_km:.2f} km.")
        
        # Compute and print result in miles
        r_mile = r_km *0.6215
        print(f"That is {r_mile:.2f} miles.")