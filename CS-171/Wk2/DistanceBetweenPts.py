#Program:     DistanceBetweenPts.py
#Purpose:     Given to points at coordinates (x1, y2) and (x2, y2), 
#             this program calculates the distance between the points
#Author:      Adelaida Medlock
#Date:        September 27, 2021

# import math module to use sqrt() and pow() functions
import math

# define the function
def calculateDistance(x1, y1, x2, y2) :
    distance = math.sqrt( math.pow(x2 - x1, 2.0) + math.pow(y2 - y1, 2.0) )
    return distance

# main script below this line
if __name__ == "__main__" :
    
    # intro to the user
    print('This program calculates the distacen between 2 points')
    
    # get data from the user
    x1 = int(input('Enter point 1, x coordinate: '))
    y1 = int(input('Enter point 1, y coordinate: '))
    x2 = int(input('Enter point 2, x coordinate: '))
    y2 = int(input('Enter point 2, y coordinate: '))
    
    # invoke function that calculates distance between points
    dist = calculateDistance(x1, y1, x2, y2)
    
    # display the results
    print('The distance between the 2 points is:', round(dist, 2))
    print()