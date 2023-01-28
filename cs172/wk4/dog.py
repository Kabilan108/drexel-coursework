#File Name:  dog.py
#Purpose:    The Dog class represents a dog, which is a kind of a pet
#Author:     Adelaida A. Medlock
#Date:       April 11, 2022

from pets import Pet

class Dog(Pet):
    # constructor
    def __init__(self, breed, age = 0):
        super().__init__('dog', age)   # calling constructor from parent class
        self.__breed = breed   #additional attribute
    
    # getters and setters
    def getBreed(self):
        return self.__breed
 
    # additional behavior
    def playCatch(self) :
        print('Running and catching the stick. Good doggie!')
    
    # override makeSound
    def makeSound(self):
        print('Woof! Woof!')
        
    # override __str__
    def __str__(self):
        myStr = super().__str__() +  ', ' + self.__breed
        return myStr

    # override the __eq__ operator
    def __eq__(self, other) :
        return (self.__breed == other.getBreed() and super().__eq__(other))

