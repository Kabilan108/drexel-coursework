#File Name:  pets.py
#Purpose:    The Pet class represents a generic pet
#Author:     Adelaida A. Medlock
#Date:       January 29, 2021

class Pet:
    def __init__(self, species, age = 0):
        self.__species = species
        self.__age = age

    # getters
    def getSpecies(self):
        return self.__species
    
    def getAge(self):
        return self.__age
    
    # setters
    def haveBirthday(self):
        self.__age = self.__age + 1   

    # The make_sound method is the pet's way of making a generic sound
    def makeSound(self):
        print('Grrrrr')
       
    # overloading the print operator
    def __str__(self):
        myStr = 'A ' + str(self.__age) + '-year old ' + self.__species
        return myStr


