##File Name:  car.py
#Purpose:     Class to represent a car
#Author:      Adelaida Medlock
#Date:        January 20, 2020

class Car:
    # constructor
    def __init__ (self, make, model, year, color = '', mileage = 0):  
        self.__make = make
        self.__model = model
        self.__color = color
        self.__year = year
        self.__mileage = mileage
    
    # getters
    def getMake(self):
        return self.__make
    
    def getModel(self):
        return self.__model

    def getColor(self):
        return self.__color
    
    def getYear(self):
        return self.__year
    
    def getMileage(self):
        return self.__mileage
    
    # setters
    def setColor(self, color):
        self.__color = color
    
    def increaseMileage(self):
        self.__mileage = self.__mileage + 1
        
    # Overloaded operators
    def __str__(self):
        mystr = ''
        mystr += 'Make:     ' + self.__make + '\n'
        mystr += 'Model:    ' + self.__model + '\n'
        mystr += 'Color:    ' + self.__color + '\n'
        mystr += 'Year:     ' + str(self.__year) + '\n'     
        mystr += 'Mileage:  ' + str(self.__mileage) + '\n'
        return mystr


    def __eq__(self, other):
        make = self.__make == other.getMake()
        model = self.__model == other.getModel()
        color = self.__color == other.getColor()
        year = self.__year == other.getYear()
        miles = self.__mileage == other.getMileage()
    
        return (make and model and color and year and miles)

    def __ne__(self, other):
        make = self.__make != other.getMake()
        model = self.__model != other.getModel()
        color = self.__color != other.getColor()
        year = self.__year != other.getYear()
        miles = self.__mileage != other.getMileage()
    
        return (make or model or color or year or miles)
    
    # Questions
    # 1) does it make sense to overload the arithmetic operators? + - * / etc.
    # 2) does it make sense to overlaod other comparison operators? < <= > >= 
