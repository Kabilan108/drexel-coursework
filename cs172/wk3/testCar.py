#Program:     testCar.py
#Purpose:     Test the Car class
#Author:      Adelaida Medlock
#Date:        January 20, 2020

# import the car module so we can use the Car class
from car import Car

# create an object from the Car class
JoesCar = Car('Tesla', 'Model 3', 2019)

# using setters to add information about the car
JoesCar.setColor('Gray')
JoesCar.increaseMileage()

# create another car
JanesCar = Car('Audi', 'A8', 2019, 'Black', 500)

# compare the cars
if JanesCar == JoesCar :
    print('Jane and Joe have two identical cars!\n')
    print (JanesCar)
    
else :
    print('Jane and Joe have different cars\n')
    print ("Jane's car:")
    print(JanesCar)
    print ("Joe's car:")
    print(JoesCar)


